"""
Judge Agent

Evaluates compositions using LLM-based critique.
Used in GEPA for reflective mutation.
"""

from typing import Dict, TYPE_CHECKING

import weave

if TYPE_CHECKING:
    import pretty_midi


@weave.op
async def critique(
    model,
    midi: "pretty_midi.PrettyMIDI",
    metrics: Dict[str, float],
    summary: str = "",
) -> Dict:
    """
    Evaluate a composition using LLM-based critique.

    Args:
        model: LLM model (or None for dry-run)
        midi: PrettyMIDI object to evaluate
        metrics: Pre-computed metrics for context
        summary: Optional high-level context

    Returns:
        Dictionary with:
        {
            "overall_score": float (0-10),
            "rationale": str,
            "suggestions": [str, ...],
            "prompt_mutation": str (hint for GEPA mutation)
        }
    """
    # TODO: Build prompt from metrics + summary (not raw MIDI)
    # TODO: Call LLM, parse response
    raise NotImplementedError


@weave.op
async def critique_parallel(
    model,
    midi: "pretty_midi.PrettyMIDI",
    metrics: Dict[str, float],
    summary: str = "",
) -> Dict:
    """
    Evaluate using parallel criterion-specific judges + aggregator.

    Args:
        model: LLM model (or None for dry-run)
        midi: PrettyMIDI object to evaluate
        metrics: Pre-computed metrics for context
        summary: Optional high-level context

    Returns:
        Same structure as critique()
    """
    # TODO: Implement parallel judge architecture
    raise NotImplementedError
