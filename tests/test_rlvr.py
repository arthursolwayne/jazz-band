"""Tests for RLVR training loop."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rlvr.loop import train, rollout, JazzScenario
from rlvr.eval import WEIGHTS


def test_dry_run_one_step():
    """Verify train() completes 1 step in dry-run mode."""
    summary = asyncio.run(train(num_steps=1, rollouts_per_step=2, dry_run=True))
    assert summary["num_steps"] == 1
    assert "best_reward" in summary
    assert isinstance(summary["best_reward"], float)
    print("✓ test_dry_run_one_step")


def test_dry_run_multiple_steps():
    """Verify train() completes multiple steps."""
    summary = asyncio.run(train(num_steps=3, rollouts_per_step=4, dry_run=True))
    assert summary["num_steps"] == 3
    print("✓ test_dry_run_multiple_steps")


def test_rollout_returns_valid_structure():
    """Verify rollout returns expected trajectory structure."""
    scenario = JazzScenario(step=0, key="C", tempo=120)
    traj = asyncio.run(rollout(None, scenario))

    assert "messages_and_choices" in traj
    assert "reward" in traj
    assert "metrics" in traj
    assert isinstance(traj["reward"], float)
    print("✓ test_rollout_returns_valid_structure")


def test_rollout_metrics_match_weights():
    """Verify rollout returns all expected metrics."""
    scenario = JazzScenario(step=0)
    traj = asyncio.run(rollout(None, scenario))

    for metric_name in WEIGHTS:
        assert metric_name in traj["metrics"], f"Missing metric: {metric_name}"
        assert 0.0 <= traj["metrics"][metric_name] <= 1.0
    print("✓ test_rollout_metrics_match_weights")


if __name__ == "__main__":
    test_dry_run_one_step()
    test_dry_run_multiple_steps()
    test_rollout_returns_valid_structure()
    test_rollout_metrics_match_weights()
    print("\nAll tests passed!")
