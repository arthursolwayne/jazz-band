"""
RLVR Training Loop

Rollout → metrics → reward → gradient descent (via ART).
"""

import asyncio
import random
from typing import Dict

from pydantic import BaseModel

# ART imports (optional for dry-run)
try:
    import art
    from art.serverless.backend import ServerlessBackend
    HAS_ART = True
except ImportError:
    art = None
    HAS_ART = False

from .eval import compute_reward, WEIGHTS


class JazzScenario(BaseModel):
    """Scenario for a single rollout."""
    step: int
    key: str = "C"
    tempo: int = 120


def _mock_metrics() -> Dict[str, float]:
    """Return plausible fake metrics for dry-run."""
    return {k: random.uniform(0.3, 0.8) for k in WEIGHTS}


async def rollout(model, scenario: JazzScenario):
    """
    Single rollout: generate MIDI → compute metrics → compute reward.

    Returns art.Trajectory (or mock dict in dry-run).
    """
    # Dry-run mode: return mock trajectory
    if model is None:
        metrics = _mock_metrics()
        reward = compute_reward(metrics)
        return {
            "messages_and_choices": [
                {"role": "system", "content": "You are a jazz composer."},
                {"role": "user", "content": f"Compose in {scenario.key} at {scenario.tempo} BPM."},
            ],
            "reward": reward,
            "metrics": metrics,
        }

    # LLM mode: use ART
    # TODO: Implement real LLM calls
    # 1. Build trajectory with system prompt
    # 2. Add user prompt with scenario
    # 3. Call LLM → get pretty_midi code
    # 4. Execute code → PrettyMIDI object
    # 5. compute_all(midi) → metrics
    # 6. compute_reward(metrics) → scalar
    raise NotImplementedError("LLM mode not yet implemented")


async def train(
    num_steps: int = 20,
    rollouts_per_step: int = 8,
    dry_run: bool = False,
) -> Dict:
    """
    Main training loop.

    Args:
        num_steps: Training steps
        rollouts_per_step: Trajectories per step
        dry_run: Skip LLM calls, use mock metrics

    Returns:
        Summary dict with num_steps, best_reward
    """
    best_reward = float("-inf")

    if dry_run:
        # Dry-run: sequential mock rollouts
        for step in range(num_steps):
            rewards = []
            for _ in range(rollouts_per_step):
                traj = await rollout(None, JazzScenario(step=step))
                rewards.append(traj["reward"])

            avg_reward = sum(rewards) / len(rewards)
            if avg_reward > best_reward:
                best_reward = avg_reward
            print(f"Step {step}: avg_reward={avg_reward:.3f}")

        return {"num_steps": num_steps, "best_reward": best_reward}

    # LLM mode with ART
    if not HAS_ART:
        raise ImportError("openpipe-art required for LLM mode")

    # TODO: Initialize model and run real training
    # model = art.TrainableModel(...)
    # backend = ServerlessBackend()
    # await model.register(backend)
    #
    # for step in range(num_steps):
    #     train_groups = await art.gather_trajectory_groups(
    #         (art.TrajectoryGroup(
    #             rollout(model, JazzScenario(step=step))
    #             for _ in range(rollouts_per_step)
    #         ) for _ in range(1)),
    #         max_exceptions=rollouts_per_step,
    #     )
    #     await model.train(train_groups)

    raise NotImplementedError("LLM mode not yet implemented")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="RLVR Training")
    parser.add_argument("--steps", type=int, default=20, help="Training steps")
    parser.add_argument("--rollouts", type=int, default=8, help="Rollouts per step")
    parser.add_argument("--dry-run", action="store_true", help="Use mock metrics")
    args = parser.parse_args()

    summary = asyncio.run(train(
        num_steps=args.steps,
        rollouts_per_step=args.rollouts,
        dry_run=args.dry_run,
    ))
    print(f"Done: {summary}")
