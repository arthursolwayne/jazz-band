"""
RLVR Training Loop

Rollout → metrics → reward → gradient descent (via ART).
"""

import sys
import asyncio
from pathlib import Path
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    import pretty_midi

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jazz_band.metrics import compute_all
from .eval import compute_reward


async def rollout(model, scenario: Dict) -> Dict:
    """
    Single rollout: generate MIDI → compute metrics → compute reward.

    Args:
        model: ART model (or None for dry-run)
        scenario: {key, tempo, step}

    Returns:
        {midi, metrics, reward}
    """
    # TODO: Execute LLM-generated pretty_midi code
    # TODO: Compute metrics on PrettyMIDI object
    # TODO: Compute reward from metrics
    raise NotImplementedError


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
        dry_run: Skip LLM calls

    Returns:
        Summary dict
    """
    # TODO: Implement training loop
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(train(dry_run=True))
