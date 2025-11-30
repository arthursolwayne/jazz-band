"""
RLVR Training Loop

Rollout → execute code → reward → gradient descent (via ART).
"""

import os
import json
import asyncio
import logging
import subprocess
from pathlib import Path
from typing import Dict
from datetime import datetime

from dotenv import load_dotenv
from pydantic import BaseModel
import weave

load_dotenv()

# Suppress weave info logs (keep errors)
logging.getLogger("weave").setLevel(logging.ERROR)

# ART imports (optional for dry-run)
try:
    import art
    from art.serverless.backend import ServerlessBackend
    HAS_ART = True
except ImportError:
    art = None
    HAS_ART = False

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jazz_band.symbol_engine import SYSTEM_PROMPT, execute_midi_code, compute_reward

# Artifacts directory
ARTIFACTS_DIR = Path(__file__).parent.parent / "artifacts" / "rollouts"


class JazzScenario(BaseModel):
    """Scenario for a single rollout."""
    step: int
    key: str = "C"
    tempo: int = 120
    rollout_id: int = 0


def save_rollout(scenario: JazzScenario, code: str, midi, reward: float, run_id: str, error: str = None):
    """Save rollout artifacts: code, MIDI, metadata."""
    rollout_dir = ARTIFACTS_DIR / run_id / f"step_{scenario.step:03d}" / f"rollout_{scenario.rollout_id:03d}"
    rollout_dir.mkdir(parents=True, exist_ok=True)

    # Save code
    (rollout_dir / "code.py").write_text(code)

    # Save MIDI if valid
    if midi is not None:
        midi_path = rollout_dir / "output.mid"
        midi.write(str(midi_path))

    # Save metadata
    meta = {
        "step": scenario.step,
        "rollout_id": scenario.rollout_id,
        "key": scenario.key,
        "tempo": scenario.tempo,
        "reward": reward,
        "has_midi": midi is not None,
        "error": error,
        "timestamp": datetime.now().isoformat(),
    }
    (rollout_dir / "meta.json").write_text(json.dumps(meta, indent=2))

    return rollout_dir


def open_midi_in_garageband(midi_path: Path):
    """Open MIDI file in GarageBand (macOS)."""
    subprocess.run(["open", "-a", "GarageBand", str(midi_path)])


@weave.op
async def rollout(model, scenario: JazzScenario, run_id: str) -> "art.Trajectory":
    """
    Single rollout: prompt LLM → execute code → compute reward.
    """
    from openai import AsyncOpenAI

    client = AsyncOpenAI(
        base_url=model.inference_base_url,
        api_key=model.inference_api_key,
    )

    # Build trajectory
    trajectory = art.Trajectory(
        messages_and_choices=[
            {"role": "system", "content": SYSTEM_PROMPT}
        ],
        metadata={"step": scenario.step, "key": scenario.key, "tempo": scenario.tempo},
        reward=0.0,
    )

    # User prompt
    user_prompt = f"Compose a 4-bar jazz piece in {scenario.key} at {scenario.tempo} BPM."
    trajectory.messages_and_choices.append({"role": "user", "content": user_prompt})

    code = ""
    midi = None
    error = None

    # Call LLM
    try:
        completion = await client.chat.completions.create(
            model=model.get_inference_name(),
            messages=trajectory.messages(),
            max_completion_tokens=12000,
            temperature=0.75,
        )
        choice = completion.choices[0]
        trajectory.messages_and_choices.append(choice)

        # Execute code
        code = choice.message.content
        midi, cleaned_code, error = execute_midi_code(code)
        code = cleaned_code

        # Compute reward
        reward = compute_reward(midi)
        trajectory.reward = reward

        # Track metrics for W&B
        note_count = sum(len(inst.notes) for inst in midi.instruments) if midi else 0
        trajectory.metrics["note_count"] = note_count
        trajectory.metrics["reward"] = reward
        trajectory.metrics["valid_midi"] = 1.0 if midi else 0.0

    except Exception as e:
        error = str(e)
        trajectory.reward = 0.0  # Floor at 0, not negative (for GRPO)
        trajectory.metrics["reward"] = 0.0
        trajectory.metrics["valid_midi"] = 0.0

    # Save artifacts
    save_rollout(scenario, code, midi, trajectory.reward, run_id, error)

    return trajectory


async def train(
    num_steps: int = 20,
    rollouts_per_step: int = 24,
    dry_run: bool = False,
    project: str = "jazz-band-rlvr",
    model_name: str = "composer-001",
    base_model: str = "OpenPipe/Qwen3-14B-Instruct",
    resume: str = None,  # Pass run_id to resume
) -> Dict:
    """
    Main training loop.
    """
    if dry_run:
        # Dry-run: mock rewards
        import random
        best_reward = float("-inf")
        for step in range(num_steps):
            rewards = [random.choice([-1.0, 1.0]) for _ in range(rollouts_per_step)]
            avg_reward = sum(rewards) / len(rewards)
            if avg_reward > best_reward:
                best_reward = avg_reward
            print(f"Step {step}: avg_reward={avg_reward:.3f}")
        return {"num_steps": num_steps, "best_reward": best_reward}

    # Real training with ART
    if not HAS_ART:
        raise ImportError("openpipe-art required. Install with: pip install openpipe-art")

    # Set API key
    api_key = os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY")
    if not api_key:
        raise ValueError("WANDB_API_KEY or WANDBAPIKEY required")
    os.environ["WANDB_API_KEY"] = api_key

    # Initialize weave for logging
    weave.init(project)

    # Resume existing run or create new one
    if resume:
        run_id = resume
        run_name = resume
    else:
        run_id = f"{model_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        run_name = run_id

    # Print header
    artifacts_path = ARTIFACTS_DIR / run_id
    artifacts_rel = f"artifacts/rollouts/{run_id}"

    print()
    print("=" * 60)
    print(f"RLVR Training Run: {run_name}")
    print("=" * 60)
    print(f"  Base model:  {base_model}")
    print(f"  Steps:       {num_steps}")
    print(f"  Rollouts:    {rollouts_per_step} per step")
    print(f"  Artifacts:   {artifacts_rel}")
    print("=" * 60)
    print()

    model = art.TrainableModel(
        name=run_name,
        project=project,
        base_model=base_model,
    )

    backend = ServerlessBackend()
    await model.register(backend)

    # Training loop stats
    total_valid = 0
    total_rollouts = 0
    best_single_reward = float("-inf")
    step_summaries = []

    start_step = await model.get_step()

    for step in range(start_step, num_steps):
        train_groups = await art.gather_trajectory_groups(
            (
                art.TrajectoryGroup(
                    rollout(model, JazzScenario(step=step, rollout_id=i), run_id)
                    for i in range(rollouts_per_step)
                )
                for _ in range(1)
            ),
            pbar_desc=f"Step {step}/{num_steps}",
            max_exceptions=rollouts_per_step,
        )

        # Compute stats
        step_rewards = []
        step_valid = 0
        step_errors = []
        for group in train_groups:
            for traj in group.trajectories:
                step_rewards.append(traj.reward)
                if traj.reward > best_single_reward:
                    best_single_reward = traj.reward
                if traj.metrics.get("valid_midi", 0) > 0:
                    step_valid += 1

        total_valid += step_valid
        total_rollouts += len(step_rewards)

        avg_reward = sum(step_rewards) / len(step_rewards) if step_rewards else 0
        step_summaries.append({
            "step": step,
            "avg_reward": avg_reward,
            "valid": step_valid,
            "total": len(step_rewards),
        })

        # Print step summary (clean, single line)
        print(f"  Step {step}: reward={avg_reward:+.2f}  valid={step_valid}/{len(step_rewards)}")

        # Train
        await model.delete_checkpoints()
        await model.train(
            train_groups,
            config=art.TrainConfig(learning_rate=5e-6),
            _config={"advantage_balance": 0.3},
        )

    # Find best MIDI and open in GarageBand
    best_midi_path = None
    for step_dir in sorted(artifacts_path.glob("step_*")):
        for rollout_dir in sorted(step_dir.glob("rollout_*")):
            midi_file = rollout_dir / "output.mid"
            if midi_file.exists():
                best_midi_path = midi_file

    # Print final summary
    print()
    print("=" * 60)
    print("Training Complete")
    print("=" * 60)
    print(f"  Steps completed:    {num_steps}")
    print(f"  Total rollouts:     {total_rollouts}")
    print(f"  Valid MIDIs:        {total_valid}/{total_rollouts} ({100*total_valid/total_rollouts:.0f}%)")
    print(f"  Best single reward: {best_single_reward:+.2f}")
    print(f"  Artifacts:          {artifacts_rel}")
    print("=" * 60)

    if best_midi_path:
        print(f"\nOpening best MIDI in GarageBand...")
        open_midi_in_garageband(best_midi_path)
    print()

    return {
        "num_steps": num_steps,
        "total_rollouts": total_rollouts,
        "total_valid": total_valid,
        "best_reward": best_single_reward,
        "run_id": run_id,
    }


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="RLVR Training")
    parser.add_argument("--steps", type=int, default=20, help="Training steps")
    parser.add_argument("--rollouts", type=int, default=24, help="Rollouts per step")
    parser.add_argument("--dry-run", action="store_true", help="Use mock rewards")
    parser.add_argument("--project", default="jazz-band-rlvr", help="W&B project")
    parser.add_argument("--model-name", default="composer-001", help="Model name")
    parser.add_argument("--base-model", default="OpenPipe/Qwen3-14B-Instruct", help="Base model")
    parser.add_argument("--resume", type=str, default=None, help="Run ID to resume")
    args = parser.parse_args()

    summary = asyncio.run(train(
        num_steps=args.steps,
        rollouts_per_step=args.rollouts,
        dry_run=args.dry_run,
        project=args.project,
        model_name=args.model_name,
        base_model=args.base_model,
        resume=args.resume,
    ))
