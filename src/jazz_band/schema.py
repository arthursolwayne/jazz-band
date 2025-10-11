"""
JamJSON Schema and Validator

Defines the structured format for representing multi-instrument jazz performances.
Each performance consists of bars containing events for 5 parts: bass, drums, piano, sax, trumpet.

JamJSON Structure:
- Top-level: tempo, key, time_sig, num_bars, bars
- Per bar: bar_num, parts (dict with 5 instrument arrays)
- Per event: pitch (note or "rest"), dur (duration), optional tie/vel

This module provides a validator stub that performs basic structure and type checking.
Future versions will include LLM-based repair for malformed tokens.
"""

from typing import Any, TypedDict, Literal, Optional


# Type definitions for JamJSON structure
Duration = Literal["e", "q", "h", "w"]  # eighth, quarter, half, whole
Velocity = Literal["lo", "med", "hi"]
PitchType = str  # e.g., "C4", "rest", "kick", "snare", "hihat"


class JamEvent(TypedDict, total=False):
    """
    A single musical event for one instrument.

    Fields:
    - pitch: Note name (e.g., "C4", "Eb3"), "rest", or drum name (kick/snare/hihat)
    - dur: Duration as string - "e" (eighth), "q" (quarter), "h" (half), "w" (whole)
    - tie: Optional boolean indicating if note is tied to next
    - vel: Optional velocity - "lo" (40), "med" (70), "hi" (100)
    """
    pitch: PitchType
    dur: Duration
    tie: bool
    vel: Velocity


class JamParts(TypedDict):
    """Six-part arrangement: bass, snare, hihat, piano, sax, trumpet."""
    bass: list[JamEvent]
    snare: list[JamEvent]
    hihat: list[JamEvent]
    piano: list[JamEvent]
    sax: list[JamEvent]
    trumpet: list[JamEvent]


class JamBar(TypedDict):
    """A single bar containing events for all six parts."""
    bar_num: int
    parts: JamParts


class JamJSON(TypedDict):
    """
    Complete performance specification.

    Fields:
    - tempo: BPM (e.g., 120)
    - key: Key signature (e.g., "C", "Dm", "F#")
    - time_sig: Time signature (e.g., "4/4", "3/4")
    - num_bars: Number of bars in the performance
    - bars: List of JamBar objects
    """
    tempo: int
    key: str
    time_sig: str
    num_bars: int
    bars: list[JamBar]


def validate_jam_json(data: dict[str, Any]) -> tuple[bool, Optional[str], Optional[JamJSON]]:
    """
    Validates JamJSON structure and types.

    This is a basic validator stub that checks:
    - Required top-level fields exist and have correct types
    - Bars structure is valid
    - Parts contain correct instrument names
    - Events have required fields

    Future versions will include:
    - LLM-based repair for malformed tokens
    - Musical validity checks (pitch ranges, duration sums per bar)
    - Automatic correction of common errors

    Args:
        data: Dictionary to validate as JamJSON

    Returns:
        Tuple of (is_valid, error_message, cleaned_data)
        - is_valid: True if data conforms to schema
        - error_message: None if valid, otherwise description of error
        - cleaned_data: Validated and cleaned JamJSON, or None if invalid
    """

    # Check top-level required fields
    required_top_level = ["tempo", "key", "time_sig", "num_bars", "bars"]
    for field in required_top_level:
        if field not in data:
            return False, f"Missing required field: {field}", None

    # Validate types of top-level fields
    if not isinstance(data["tempo"], int) or data["tempo"] <= 0:
        return False, "tempo must be a positive integer", None

    if not isinstance(data["key"], str) or len(data["key"]) == 0:
        return False, "key must be a non-empty string", None

    if not isinstance(data["time_sig"], str):
        return False, "time_sig must be a string", None

    if not isinstance(data["num_bars"], int) or data["num_bars"] <= 0:
        return False, "num_bars must be a positive integer", None

    if not isinstance(data["bars"], list):
        return False, "bars must be a list", None

    # Validate bars
    if len(data["bars"]) != data["num_bars"]:
        return False, f"bars length ({len(data['bars'])}) does not match num_bars ({data['num_bars']})", None

    required_parts = {"bass", "snare", "hihat", "piano", "sax", "trumpet"}
    valid_durations = {"e", "q", "h", "w"}
    valid_velocities = {"lo", "med", "hi"}

    for i, bar in enumerate(data["bars"]):
        if not isinstance(bar, dict):
            return False, f"Bar {i} is not a dictionary", None

        if "bar_num" not in bar:
            return False, f"Bar {i} missing bar_num", None

        if "parts" not in bar:
            return False, f"Bar {i} missing parts", None

        parts = bar["parts"]
        if not isinstance(parts, dict):
            return False, f"Bar {i} parts is not a dictionary", None

        # Check all required parts exist
        if set(parts.keys()) != required_parts:
            missing = required_parts - set(parts.keys())
            extra = set(parts.keys()) - required_parts
            msg = []
            if missing:
                msg.append(f"missing parts: {missing}")
            if extra:
                msg.append(f"extra parts: {extra}")
            return False, f"Bar {i}: {', '.join(msg)}", None

        # Validate events in each part
        for part_name, events in parts.items():
            if not isinstance(events, list):
                return False, f"Bar {i}, part {part_name}: events must be a list", None

            for j, event in enumerate(events):
                if not isinstance(event, dict):
                    return False, f"Bar {i}, part {part_name}, event {j}: not a dictionary", None

                # Check required event fields
                if "pitch" not in event:
                    return False, f"Bar {i}, part {part_name}, event {j}: missing pitch", None

                if "dur" not in event:
                    return False, f"Bar {i}, part {part_name}, event {j}: missing dur", None

                # Validate duration
                if event["dur"] not in valid_durations:
                    return False, f"Bar {i}, part {part_name}, event {j}: invalid duration '{event['dur']}' (must be one of {valid_durations})", None

                # Validate velocity if present
                if "vel" in event and event["vel"] not in valid_velocities:
                    return False, f"Bar {i}, part {part_name}, event {j}: invalid velocity '{event['vel']}' (must be one of {valid_velocities})", None

                # Validate tie if present
                if "tie" in event and not isinstance(event["tie"], bool):
                    return False, f"Bar {i}, part {part_name}, event {j}: tie must be boolean", None

    # If all checks pass, return the data as valid JamJSON
    return True, None, data  # type: ignore


def create_empty_jam(tempo: int = 120, key: str = "C", time_sig: str = "4/4", num_bars: int = 4) -> JamJSON:
    """
    Creates an empty JamJSON structure with no events.

    Useful for initializing a new composition.

    Args:
        tempo: Beats per minute (default 120)
        key: Key signature (default "C")
        time_sig: Time signature (default "4/4")
        num_bars: Number of bars (default 4)

    Returns:
        Empty JamJSON structure with all parts initialized to empty lists
    """
    return {
        "tempo": tempo,
        "key": key,
        "time_sig": time_sig,
        "num_bars": num_bars,
        "bars": [
            {
                "bar_num": i + 1,
                "parts": {
                    "bass": [],
                    "snare": [],
                    "hihat": [],
                    "piano": [],
                    "sax": [],
                    "trumpet": [],
                }
            }
            for i in range(num_bars)
        ]
    }
