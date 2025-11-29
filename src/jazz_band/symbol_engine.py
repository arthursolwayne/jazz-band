"""
Symbol Engine: Shared MIDI generation logic for RLVR and GEPA.

- SYSTEM_PROMPT: Instructions for LLM to generate pretty_midi code
- execute_midi_code(): Run LLM-generated code, return PrettyMIDI object
- compute_reward(): Validity check (has notes, correct duration)
"""

from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pretty_midi

# Timing constants (120 BPM, 4/4 time)
TARGET_DURATION = 8.0  # 4 bars = 8 seconds
DURATION_TOLERANCE = 0.5  # Allow +/- 0.5 seconds

# Load system prompt from markdown file
PROMPT_FILE = Path(__file__).parent.parent.parent / "prompts" / "composer.md"
SYSTEM_PROMPT = PROMPT_FILE.read_text().strip()


def execute_midi_code(code: str):
    """
    Execute LLM-generated code and return PrettyMIDI object.

    Returns:
        (midi, cleaned_code, error) - midi is None if execution failed
    """
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
        return namespace.get("midi", None), code, None
    except Exception as e:
        return None, code, str(e)


def compute_reward(midi: "pretty_midi.PrettyMIDI") -> float:
    """
    Compute reward based on validity:
    1. Has notes
    2. Duration is ~8 seconds (4 bars at 120 BPM)

    Returns:
        1.0 if valid
       -1.0 if invalid
    """
    if midi is None:
        return -1.0

    # Check has notes
    total_notes = sum(len(inst.notes) for inst in midi.instruments)
    if total_notes == 0:
        return -1.0

    # Check duration (latest note end time)
    max_end = 0.0
    for inst in midi.instruments:
        for note in inst.notes:
            if note.end > max_end:
                max_end = note.end

    # Must be within tolerance of 8 seconds
    if abs(max_end - TARGET_DURATION) > DURATION_TOLERANCE:
        return -1.0

    return 1.0
