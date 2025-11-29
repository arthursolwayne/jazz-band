"""
GEPA Evolution Loop

Rollout → metrics → Pareto select → LLM reflect → mutate prompt.
"""

import sys
import asyncio
from pathlib import Path
from typing import Dict, List, TYPE_CHECKING

if TYPE_CHECKING:
    import pretty_midi

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jazz_band.metrics import compute_all
from .eval import compute_pareto_front, select_survivors, mutate_prompt


async def evaluate_individual(model, prompt: str, key: str, tempo: float) -> Dict:
    """
    Evaluate one individual: generate MIDI → compute metrics.

    Args:
        model: LLM model
        prompt: Composer prompt
        key: Musical key
        tempo: BPM

    Returns:
        {midi, metrics}
    """
    # TODO: Implement
    raise NotImplementedError


async def evolve(
    generations: int = 10,
    population_size: int = 8,
    dry_run: bool = False,
) -> Dict:
    """
    Main evolution loop.

    Args:
        generations: Number of generations
        population_size: Individuals per generation
        dry_run: Skip LLM calls

    Returns:
        Summary dict
    """
    # TODO: Implement evolution loop
    raise NotImplementedError


if __name__ == "__main__":
    asyncio.run(evolve(dry_run=True))
