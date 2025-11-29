"""
RLVR Training Loop

Rollout → execute code → reward → gradient descent (via ART).
"""

import os
import asyncio
from typing import Dict

from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

# ART imports (optional for dry-run)
try:
    import art
    from art.serverless.backend import ServerlessBackend
    HAS_ART = True
except ImportError:
    art = None
    HAS_ART = False

from .eval import compute_reward

# System prompt for generating pretty_midi code
SYSTEM_PROMPT = """You are a jazz composer. Generate Python code using pretty_midi to create a 4-bar jazz composition.

Your code must:
1. Import pretty_midi
2. Create a PrettyMIDI object
3. Add instruments and notes
4. Assign the final PrettyMIDI object to a variable called `midi`

Example:
```python
import pretty_midi

midi = pretty_midi.PrettyMIDI()
piano = pretty_midi.Instrument(program=0)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
midi.instruments.append(piano)
```

Only output Python code. No explanations."""


class JazzScenario(BaseModel):
    """Scenario for a single rollout."""
    step: int
    key: str = "C"
    tempo: int = 120


def execute_midi_code(code: str):
    """Execute LLM-generated code and return PrettyMIDI object."""
    import pretty_midi

    # Clean code (remove markdown fences if present)
    if "```python" in code:
        code = code.split("```python")[1].split("```")[0]
    elif "```" in code:
        code = code.split("```")[1].split("```")[0]

    # Execute in isolated namespace
    namespace = {"pretty_midi": pretty_midi}
    try:
        exec(code, namespace)
        return namespace.get("midi", None)
    except Exception as e:
        print(f"Code execution failed: {e}")
        return None


async def rollout(model, scenario: JazzScenario) -> "art.Trajectory":
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

    # Call LLM
    try:
        completion = await client.chat.completions.create(
            model=model.get_inference_name(),
            messages=trajectory.messages(),
            max_completion_tokens=1000,
            temperature=0.7,
        )
        choice = completion.choices[0]
        trajectory.messages_and_choices.append(choice)

        # Execute code
        code = choice.message.content
        midi = execute_midi_code(code)

        # Compute reward
        trajectory.reward = compute_reward(midi)

    except Exception as e:
        print(f"Rollout failed: {e}")
        trajectory.reward = -1.0

    return trajectory


async def train(
    num_steps: int = 20,
    rollouts_per_step: int = 8,
    dry_run: bool = False,
    project: str = "jazz-band-rlvr",
    model_name: str = "composer-001",
    base_model: str = "OpenPipe/Qwen3-14B-Instruct",
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

    # Initialize model
    print(f"Initializing model: {model_name} (base: {base_model})")
    model = art.TrainableModel(
        name=model_name,
        project=project,
        base_model=base_model,
    )

    backend = ServerlessBackend()
    await model.register(backend)
    print("Model registered with ServerlessBackend")

    # Training loop
    best_reward = float("-inf")

    for step in range(await model.get_step(), num_steps):
        print(f"\nStep {step}/{num_steps}")

        train_groups = await art.gather_trajectory_groups(
            (
                art.TrajectoryGroup(
                    rollout(model, JazzScenario(step=step))
                    for _ in range(rollouts_per_step)
                )
                for _ in range(1)
            ),
            pbar_desc=f"Step {step}",
            max_exceptions=rollouts_per_step,
        )

        # Compute stats
        all_rewards = []
        for group in train_groups:
            for traj in group.trajectories:
                all_rewards.append(traj.reward)

        if all_rewards:
            avg_reward = sum(all_rewards) / len(all_rewards)
            if avg_reward > best_reward:
                best_reward = avg_reward
            print(f"  avg_reward={avg_reward:.3f}, best={best_reward:.3f}")

        # Train
        await model.delete_checkpoints()
        await model.train(train_groups, config=art.TrainConfig(learning_rate=1e-5))

    return {"num_steps": num_steps, "best_reward": best_reward}


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="RLVR Training")
    parser.add_argument("--steps", type=int, default=20, help="Training steps")
    parser.add_argument("--rollouts", type=int, default=8, help="Rollouts per step")
    parser.add_argument("--dry-run", action="store_true", help="Use mock rewards")
    parser.add_argument("--project", default="jazz-band-rlvr", help="W&B project")
    parser.add_argument("--model-name", default="composer-001", help="Model name")
    parser.add_argument("--base-model", default="Qwen/Qwen2.5-Coder-7B-Instruct", help="Base model")
    args = parser.parse_args()

    summary = asyncio.run(train(
        num_steps=args.steps,
        rollouts_per_step=args.rollouts,
        dry_run=args.dry_run,
        project=args.project,
        model_name=args.model_name,
        base_model=args.base_model,
    ))
    print(f"Done: {summary}")
