"""
RLVR Training Loop

Implements ART-based reinforcement learning loop for Jazz Band Composer.
Follows the 2048.py pattern with rollout function, trajectory collection,
and training steps.

Features:
- Rollout function generates 8-bar JamJSON and computes reward
- Early stopping based on Judge score plateau
- Mid-course correction if Judge score < 6.0 at step 10
- Checkpoint management with best-so-far tracking
- MIDI artifact export per checkpoint
- Weave logging for metrics, rewards, and outputs
"""

import os
import sys
import json
import logging
import asyncio
from pathlib import Path
from typing import Dict, Optional, List
from dataclasses import dataclass
from collections import deque

import requests
import weave
import wandb
from pydantic import BaseModel

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jazz_band.agents import compose_bars, critique_parallel
from jazz_band.agents.llm import init_model, load_prompt, extract_json_from_response
from jazz_band.agents.composer import _build_composer_user_prompt
from jazz_band.agents.judge import _build_judge_user_prompt, _validate_critique_structure
from jazz_band.memory import ChemistryMemory
from jazz_band.score_builder import ScoreBuilder
from jazz_band.schema import validate_jam_json

from .metrics import compute_all_metrics
from .reward import calculate_reward, reset_exploration_bonuses

# Suppress weave logs (following 2048.py pattern)
logging.getLogger("weave").setLevel(logging.CRITICAL)

# Import ART only when not in dry-run mode
try:
    import art
except ImportError:
    art = None


class JazzScenario(BaseModel):
    """Scenario for a single jazz jam rollout."""
    step: int
    key: str = "C"
    tempo: int = 120
    session_id: str = "default"


@dataclass
class CheckpointMetrics:
    """Metrics tracked per checkpoint for early stopping."""
    step: int
    avg_reward: float
    avg_judge_score: float
    best_reward: float
    best_judge_score: float


# ============================================================================
# ROLLOUT FUNCTION (Following 2048.py pattern)
# ============================================================================

@weave.op
@art.retry(exceptions=(requests.ReadTimeout,)) if art else lambda f: f
async def rollout(
    model,  # art.Model or None for dry-run
    scenario: JazzScenario,
) -> "art.Trajectory":
    """
    Single rollout: Generate 8-bar JamJSON and compute reward.

    This function mirrors the 2048.py rollout pattern:
    - Takes model and scenario
    - Populates trajectory.messages_and_choices with conversation history
    - Computes reward based on verifiable metrics
    - Returns art.Trajectory with messages, choices, reward, and metrics

    Args:
        model: ART model (or None for dry-run)
        scenario: JazzScenario with step, key, tempo

    Returns:
        art.Trajectory with reward and metrics
    """
    if art is None and model is not None:
        raise ImportError("openpipe-art required for LLM mode")

    # Load prompts
    composer_system_prompt = load_prompt("composer")
    judge_system_prompt = load_prompt("judge")

    # Initialize jam state
    jam_state = {
        "key": scenario.key,
        "tempo": scenario.tempo,
        "time_sig": "4/4",
        "last_n_bars": [],  # Fresh start for each rollout
        "form_position": "intro",
    }

    # Initialize memory
    memory = ChemistryMemory()

    # Create trajectory with Composer system message (following 2048.py pattern)
    if model is not None:
        trajectory = art.Trajectory(
            messages_and_choices=[
                {"role": "system", "content": composer_system_prompt}  # ← CRITICAL: Add system message
            ],
            metadata={
                "step": scenario.step,
                "key": scenario.key,
                "tempo": scenario.tempo,
                "session_id": scenario.session_id,
            },
            reward=0.0,
        )
    else:
        # Dry-run mode: create mock trajectory and use existing agents
        trajectory = type('Trajectory', (), {
            'messages_and_choices': [],
            'metadata': {
                "step": scenario.step,
                "key": scenario.key,
                "tempo": scenario.tempo,
                "session_id": scenario.session_id,
            },
            'reward': 0.0,
            'metrics': {},
        })()

    try:
        # ===== DRY-RUN MODE: Use existing agent functions =====
        if model is None:
            jam_json = await compose_bars(model=None, jam_state=jam_state, memory=memory, bars_per_call=8)
            is_valid, error_msg, cleaned_jam = validate_jam_json(jam_json)
            if not is_valid:
                logging.warning(f"Dry-run: Invalid JamJSON: {error_msg}")
                trajectory.reward = -1.0
                # Don't store error message - ART API only accepts numeric metrics
                return trajectory
            jam_json = cleaned_jam

            critique_result = await critique_parallel(model=None, jam_json=jam_json, summary=f"RLVR step {scenario.step}")
            judge_score = critique_result.get("overall_score", 0.0)

        # ===== LLM MODE: Direct OpenAI calls to populate trajectory =====
        else:
            # Import OpenAI client
            try:
                from openai import AsyncOpenAI
            except ImportError:
                raise ImportError("openai package required for LLM mode")

            # Create OpenAI client (following 2048.py pattern)
            client = AsyncOpenAI(
                base_url=model.inference_base_url,
                api_key=model.inference_api_key,
            )

            # ===== Step 1: Generate 8 bars with Composer =====
            # Build user prompt
            composer_user_prompt = _build_composer_user_prompt(jam_state, memory, bars_per_call=8)

            # Add user message to trajectory
            trajectory.messages_and_choices.append({
                "role": "user",
                "content": composer_user_prompt
            })

            # Call LLM and get choice object
            try:
                messages = trajectory.messages()  # Get conversation history
                chat_completion = await client.chat.completions.create(
                    model=model.get_inference_name(),
                    messages=messages,
                    max_completion_tokens=8000,  # 8-bar JamJSON needs ~6000-7000 tokens
                    temperature=0.7,
                )
            except Exception as e:
                logging.error(f"Composer LLM call failed: {e}")
                raise e

            # Add choice to trajectory (CRITICAL for training!)
            choice = chat_completion.choices[0]
            content = choice.message.content
            assert isinstance(content, str), "LLM returned None content"
            trajectory.messages_and_choices.append(choice)

            # Parse and validate JamJSON
            try:
                jam_json = extract_json_from_response(content)
            except json.JSONDecodeError as e:
                logging.error(f"Failed to parse Composer response: {content[:200]}...")
                trajectory.reward = -1.0
                # Don't store error message - ART API only accepts numeric metrics
                return trajectory

            is_valid, error_msg, cleaned_jam = validate_jam_json(jam_json)
            if not is_valid:
                logging.warning(f"Generated invalid JamJSON: {error_msg}")
                trajectory.reward = -1.0
                # Don't store error message - ART API only accepts numeric metrics
                return trajectory

            jam_json = cleaned_jam

            # ===== Step 2: Get Judge critique =====
            # Note: For now we keep Judge separate from the training trajectory
            # (only Composer responses are trained). We could add Judge to trajectory later.
            judge_user_prompt = _build_judge_user_prompt(
                jam_json=jam_json,
                summary=f"RLVR training step {scenario.step}, 8-bar Latin jazz"
            )

            # Call Judge (not added to trajectory - Judge is evaluator, not trainee)
            try:
                judge_completion = await client.chat.completions.create(
                    model=model.get_inference_name(),
                    messages=[
                        {"role": "system", "content": judge_system_prompt},
                        {"role": "user", "content": judge_user_prompt},
                    ],
                    max_completion_tokens=1500,
                    temperature=0.5,  # Lower temp for consistent critiques
                )
            except Exception as e:
                logging.warning(f"Judge LLM call failed: {e}")
                # Use default low score if Judge fails
                critique_result = {"overall_score": 3.0, "scores": {}, "rationale": "Judge call failed", "suggestions": []}
                judge_score = 3.0
            else:
                judge_content = judge_completion.choices[0].message.content
                try:
                    critique_result = extract_json_from_response(judge_content)
                    _validate_critique_structure(critique_result)
                    judge_score = critique_result.get("overall_score", 0.0)
                except (json.JSONDecodeError, ValueError) as e:
                    logging.warning(f"Failed to parse Judge response: {e}")
                    critique_result = {"overall_score": 3.0, "scores": {}, "rationale": "Parse failed", "suggestions": []}
                    judge_score = 3.0

        # ===== Step 3: Compute verifiable metrics =====
        metrics = compute_all_metrics(jam_json, memory)

        # ===== Step 4: Calculate reward =====
        reward_result = calculate_reward(
            step=scenario.step,
            metrics=metrics,
            judge_score=judge_score,
            jam_json=jam_json,
            is_valid=is_valid,
            session_id=scenario.session_id,
        )

        # ===== Step 5: Build trajectory =====
        trajectory.reward = reward_result["total_reward"]

        # Store all metrics and reward breakdown (NUMERIC ONLY - ART API requirement)
        trajectory.metrics.update({
            # Core metrics
            **metrics,
            "judge_score": judge_score,

            # Reward breakdown
            "base_reward": reward_result["base_reward"],
            "exploration_bonus": reward_result["exploration_bonus"],
            "penalty": reward_result["penalty"],

            # Per-metric reward contributions
            **{f"reward_{k}": v for k, v in reward_result["breakdown"].items()},
        })

        # Note: Do NOT store complex objects in metadata - ART API only accepts primitives
        # JamJSON and critique are logged to Weave via @weave.op decorator instead

        # ===== Step 6: Export MIDI artifact =====
        try:
            midi_path = export_midi_artifact(
                jam_json=jam_json,
                step=scenario.step,
                session_id=scenario.session_id,
                reward=trajectory.reward,
            )
            trajectory.metadata["midi_path"] = str(midi_path)
        except Exception as e:
            logging.warning(f"Failed to export MIDI: {e}")

        return trajectory

    except Exception as e:
        logging.error(f"Rollout failed: {e}", exc_info=True)
        # Return trajectory with error reward
        # Don't store error message - ART API only accepts numeric metrics
        trajectory.reward = -1.0
        return trajectory


def get_curriculum_phase_name(step: int) -> str:
    """Get human-readable curriculum phase name."""
    if step <= 5:
        return "Phase A: Rhythm Focus"
    elif step <= 10:
        return "Phase B: Harmony Added"
    else:
        return "Phase C: Full Training"


def export_midi_artifact(
    jam_json: Dict,
    step: int,
    session_id: str,
    reward: float,
) -> Path:
    """
    Export JamJSON to MIDI file for listening and analysis.

    Args:
        jam_json: JamJSON dictionary
        step: Training step number
        session_id: Unique session ID
        reward: Reward score (for filename)

    Returns:
        Path to exported MIDI file
    """
    # Create artifacts directory
    artifacts_dir = Path(__file__).parent.parent / "artifacts" / "rlvr_checkpoints"
    artifacts_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename
    reward_str = f"{reward:.3f}".replace(".", "p")  # 0.753 -> "0p753"
    filename = f"step_{step:03d}_reward_{reward_str}.mid"
    midi_path = artifacts_dir / filename

    # Build and export MIDI
    builder = ScoreBuilder()  # Use default orchestra
    score = builder.from_jam_json(jam_json)
    builder.export_midi(score, midi_path)

    return midi_path


# ============================================================================
# TRAINING LOOP
# ============================================================================

async def train_rlvr(
    num_steps: int = 20,
    rollouts_per_step: int = 8,
    learning_rate: float = 1e-5,
    dry_run: bool = False,
    project: str = "jazz-band-rlvr",
    model_name: str = "composer-rlvr-001",
    base_model: str = "OpenPipe/Qwen3-14B-Instruct",
    use_rlvr_prompts: bool = True,
) -> Dict:
    """
    Main RLVR training loop.

    Args:
        num_steps: Number of training steps (default 20)
        rollouts_per_step: Trajectories to collect per step (default 8)
        learning_rate: Learning rate for training (default 1e-5)
        dry_run: If True, run without LLM (for testing)
        project: W&B project name
        model_name: Model name for this run
        base_model: Base LLM to fine-tune

    Returns:
        Dict with training summary (best reward, final metrics, etc.)
    """
    # Initialize Weave and W&B (only if not dry-run and API key available)
    if not dry_run:
        # Set WANDB_API_KEY from WANDBAPIKEY if needed (following 2048.py pattern)
        api_key = os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY")
        if api_key:
            os.environ["WANDB_API_KEY"] = api_key
            weave.init(project)
            # Initialize wandb for metrics tracking
            wandb.init(
                project=project,
                config={
                    "num_steps": num_steps,
                    "rollouts_per_step": rollouts_per_step,
                    "learning_rate": learning_rate,
                    "base_model": base_model,
                    "model_name": model_name,
                },
                tags=["rlvr", "jazz-band", "composer"],
            )
        else:
            print("⚠️  WANDB_API_KEY not set - Weave and W&B logging disabled")

    # Reset exploration bonuses
    reset_exploration_bonuses()

    # Initialize model (or None for dry-run)
    if dry_run:
        model = None
        print("🔧 Running in DRY-RUN mode (no LLM calls, no Weave logging)")
    else:
        print(f"🚀 Initializing model: {model_name}")
        model = await init_model(
            project=project,
            model_name=model_name,
            base_model=base_model,
            dry_run=False,
        )

    # Tracking for early stopping
    checkpoint_history: deque[CheckpointMetrics] = deque(maxlen=3)
    best_reward = float("-inf")
    best_judge_score = 0.0
    early_stop_triggered = False

    # Training loop
    for step in range(num_steps):
        print(f"\n{'='*60}")
        print(f"Step {step}/{num_steps} - {get_curriculum_phase_name(step)}")
        print(f"{'='*60}")

        # Generate scenarios for this step
        scenarios = [
            JazzScenario(
                step=step,
                key="C",  # Fixed key for now
                tempo=120,
                session_id=f"{model_name}_{step}",
            )
            for _ in range(rollouts_per_step)
        ]

        # Collect trajectories (in parallel if using ART - following 2048.py pattern exactly)
        if model is not None and art is not None:
            # Use ART's gather for parallel rollouts
            train_groups = await art.gather_trajectory_groups(
                (
                    art.TrajectoryGroup(
                        rollout(model, scenario)
                        for scenario in scenarios
                    )
                    for _ in range(1)
                ),
                pbar_desc=f"Step {step}",
                max_exceptions=rollouts_per_step,
            )
            # Note: Metrics are shown in the progress bar above
            # ART handles trajectory iteration internally during training
            print(f"  ✅ Collected {rollouts_per_step} rollouts")

            # Extract metrics from completed trajectories (LLM mode)
            all_trajectories = []
            for group in train_groups:
                all_trajectories.extend(group.trajectories)

            # Handle case where all rollouts failed
            if len(all_trajectories) == 0:
                print(f"  ⚠️  WARNING: All rollouts failed at step {step}. Skipping this step.")
                continue

            step_rewards = [t.reward for t in all_trajectories]
            step_judge_scores = [t.metrics.get("judge_score", 0.0) for t in all_trajectories]

            avg_reward = sum(step_rewards) / len(step_rewards)
            avg_judge = sum(step_judge_scores) / len(step_judge_scores)
            max_reward = max(step_rewards)
            max_judge = max(step_judge_scores)

            print(f"  Avg Reward: {avg_reward:.3f} | Max Reward: {max_reward:.3f}")
            print(f"  Avg Judge:  {avg_judge:.2f}/10 | Max Judge:  {max_judge:.2f}/10")

            # Track for early stopping (LLM mode)
            if avg_reward > best_reward:
                best_reward = avg_reward
                print(f"  🎉 New best average reward: {best_reward:.3f}")

            if avg_judge > best_judge_score:
                best_judge_score = avg_judge
                print(f"  🎵 New best Judge score: {best_judge_score:.2f}/10")

            # Track checkpoint metrics (LLM mode)
            checkpoint = CheckpointMetrics(
                step=step,
                avg_reward=avg_reward,
                avg_judge_score=avg_judge,
                best_reward=best_reward,
                best_judge_score=best_judge_score,
            )
            checkpoint_history.append(checkpoint)

            # Log to wandb (LLM mode)
            if not dry_run:
                wandb.log({
                    "step": step,
                    "avg_reward": avg_reward,
                    "max_reward": max_reward,
                    "avg_judge_score": avg_judge,
                    "max_judge_score": max_judge,
                    "best_reward": best_reward,
                    "best_judge_score": best_judge_score,
                    "curriculum_phase": get_curriculum_phase_name(step),
                })

            # Early stopping check (LLM mode)
            if len(checkpoint_history) == 3 and step >= 6:
                recent_scores = [cp.avg_judge_score for cp in checkpoint_history]
                if max(recent_scores[1:]) <= recent_scores[0]:
                    print(f"\n⚠️  EARLY STOPPING: No Judge score improvement for 3 steps")
                    early_stop_triggered = True
                    # Don't train on this step if early stopping
                    continue

        else:
            # Dry-run: sequential rollouts
            train_groups = None
            trajectories = []
            for scenario in scenarios:
                traj = await rollout(None, scenario)
                trajectories.append(traj)

            # Compute step metrics (dry-run only)
            step_rewards = [t.reward for t in trajectories]
            step_judge_scores = [t.metrics.get("judge_score", 0.0) for t in trajectories]

            avg_reward = sum(step_rewards) / len(step_rewards)
            avg_judge = sum(step_judge_scores) / len(step_judge_scores)
            max_reward = max(step_rewards)
            max_judge = max(step_judge_scores)

            print(f"  Avg Reward: {avg_reward:.3f} | Max Reward: {max_reward:.3f}")
            print(f"  Avg Judge:  {avg_judge:.2f}/10 | Max Judge:  {max_judge:.2f}/10")

            # Track for early stopping (dry-run)
            if avg_reward > best_reward:
                best_reward = avg_reward
                print(f"  🎉 New best average reward: {best_reward:.3f}")

            if avg_judge > best_judge_score:
                best_judge_score = avg_judge
                print(f"  🎵 New best Judge score: {best_judge_score:.2f}/10")

            # Track checkpoint metrics (dry-run only)
            checkpoint = CheckpointMetrics(
                step=step,
                avg_reward=avg_reward,
                avg_judge_score=avg_judge,
                best_reward=best_reward,
                best_judge_score=best_judge_score,
            )
            checkpoint_history.append(checkpoint)

            # Early stopping check (dry-run)
            if len(checkpoint_history) == 3 and step >= 6:
                recent_scores = [cp.avg_judge_score for cp in checkpoint_history]
                if max(recent_scores[1:]) <= recent_scores[0]:
                    print(f"\n⚠️  EARLY STOPPING: No Judge score improvement for 3 steps")
                    early_stop_triggered = True
                    break

        # ===== Train Model (LLM mode only) =====
        if model is not None and art is not None:
            print(f"  🔄 Training on {rollouts_per_step} trajectories...")
            await model.delete_checkpoints()  # Prune old checkpoints
            await model.train(
                train_groups,
                config=art.TrainConfig(learning_rate=learning_rate),
            )
            print(f"  ✅ Training complete")

    # ===== Training Summary =====
    print(f"\n{'='*60}")
    print(f"Training Complete!")
    print(f"{'='*60}")
    print(f"Total Steps: {step + 1}")
    print(f"Early Stop Triggered: {early_stop_triggered}")
    print(f"Best Average Reward: {best_reward:.3f}")
    print(f"Best Judge Score: {best_judge_score:.2f}/10")

    # Finish wandb run
    if not dry_run:
        wandb.finish()

    return {
        "num_steps": step + 1,
        "early_stop": early_stop_triggered,
        "best_reward": best_reward,
        "best_judge_score": best_judge_score,
    }


# ============================================================================
# CLI INTERFACE
# ============================================================================

async def main():
    """CLI entry point for RLVR training."""
    import argparse

    parser = argparse.ArgumentParser(description="RLVR Training for Jazz Band Composer")
    parser.add_argument("--steps", type=int, default=20, help="Number of training steps")
    parser.add_argument("--rollouts", type=int, default=8, help="Rollouts per step")
    parser.add_argument("--lr", type=float, default=1e-5, help="Learning rate")
    parser.add_argument("--dry-run", action="store_true", help="Run without LLM")
    parser.add_argument("--project", default="jazz-band-rlvr", help="W&B project name")
    parser.add_argument("--model-name", default="composer-rlvr-001", help="Model name")
    parser.add_argument("--use-base-prompts", action="store_true",
                        help="Use original prompts instead of RLVR versions")

    args = parser.parse_args()

    # Run training
    summary = await train_rlvr(
        num_steps=args.steps,
        rollouts_per_step=args.rollouts,
        learning_rate=args.lr,
        dry_run=args.dry_run,
        project=args.project,
        model_name=args.model_name,
        use_rlvr_prompts=not args.use_base_prompts,
    )

    print(f"\n✅ Training summary: {json.dumps(summary, indent=2)}")


if __name__ == "__main__":
    asyncio.run(main())
