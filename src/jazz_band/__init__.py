"""
Jazz Band - Symbolic music generation for LLM training.
"""

__version__ = "0.1.0"

from .symbol_engine import (
    SYSTEM_PROMPT,
    execute_midi_code,
    compute_reward,
    TARGET_DURATION,
    DURATION_TOLERANCE,
)

__all__ = [
    "SYSTEM_PROMPT",
    "execute_midi_code",
    "compute_reward",
    "TARGET_DURATION",
    "DURATION_TOLERANCE",
]
