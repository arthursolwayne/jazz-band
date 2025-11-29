"""
Symbol Engine: Shared MIDI generation logic for RLVR and GEPA.

- SYSTEM_PROMPT: Instructions for LLM to generate pretty_midi code
- execute_midi_code(): Run LLM-generated code, return PrettyMIDI object
- compute_reward(): Validity check (has notes, correct duration)
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pretty_midi

# Timing constants (120 BPM, 4/4 time)
TARGET_DURATION = 8.0  # 4 bars = 8 seconds
DURATION_TOLERANCE = 0.5  # Allow +/- 0.5 seconds

# System prompt for generating pretty_midi code
SYSTEM_PROMPT = """You are a jazz composer. Generate Python code using pretty_midi to create exactly 4 bars of jazz.

TIMING (120 BPM, 4/4 time):
- 1 beat = 0.5 seconds
- 1 bar = 4 beats = 2.0 seconds
- 4 bars = 8.0 seconds total
- All notes must start >= 0.0 and end <= 8.0

Your code must:
1. Create a PrettyMIDI object
2. Add instruments and notes within the 8-second duration
3. Assign the result to a variable called `midi`

Example:
```python
import pretty_midi

midi = pretty_midi.PrettyMIDI()
piano = pretty_midi.Instrument(program=0)
# Bar 1: beats 0-2 seconds
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=0.5, end=1.0))
midi.instruments.append(piano)
```

Only output Python code. No explanations."""


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
