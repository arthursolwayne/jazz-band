"""
Composer Agent

Generates new bars of music in JamJSON format using LLM or dry-run mode.
Maintains musical continuity by considering previous bars and chemistry memory.
"""

import json
import logging
from typing import Optional, Dict, List

import weave

from ..schema import validate_jam_json
from ..memory.chemistry import ChemistryMemory
from .llm import load_prompt, call_llm, extract_json_from_response


@weave.op
async def compose_bars(
    model,
    jam_state: Dict,
    memory: ChemistryMemory,
    bars_per_call: int = 4,
) -> Dict:
    """
    Generate new bars of music using the Composer agent.

    Takes current musical context (key, tempo, previous bars) and chemistry
    memory, then generates 1-4 new bars in strict JamJSON format.

    Args:
        model: art.TrainableModel instance (or None for dry-run)
        jam_state: Musical context dictionary containing:
            - key: Key signature (e.g., "C", "Dm")
            - tempo: BPM (e.g., 120)
            - time_sig: Time signature (e.g., "4/4")
            - last_n_bars: List of previous bars for continuity (max 4)
            - form_position: Optional description of where we are (e.g., "verse", "chorus")
        memory: ChemistryMemory instance with motifs, style, interplay patterns
        bars_per_call: Number of bars to generate (1-4)

    Returns:
        JamJSON dictionary containing the newly generated bars

    Raises:
        ValueError: If generated JSON fails validation
        Exception: If LLM call fails
    """

    # Dry-run mode: return deterministic stub
    if model is None:
        return _generate_dry_run_bars(jam_state, bars_per_call)

    # Load composer prompt
    system_prompt = load_prompt("composer")

    # Build user prompt with context
    user_prompt = _build_composer_user_prompt(jam_state, memory, bars_per_call)

    # Call LLM (using ART model's inference endpoint)
    # Increased max_tokens to 18000 to accommodate 16-bar JamJSON (~15000 tokens)
    # Qwen3-14B-Instruct has 32K context window
    # Set max_tokens to 8000 for 8-bar JamJSON (~6000-7000 tokens)
    response = await call_llm(
        model=model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=8000,  # Reduced from 18000 for 8 bars
        temperature=0.7,
    )

    # Extract and validate JSON
    try:
        jam_json = extract_json_from_response(response)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse composer response: {response[:200]}...")
        raise ValueError(f"Composer returned invalid JSON: {e}")

    # Validate JamJSON schema
    is_valid, error_msg, cleaned = validate_jam_json(jam_json)
    if not is_valid:
        logging.error(f"Composer generated invalid JamJSON: {error_msg}")
        raise ValueError(f"Generated JamJSON failed validation: {error_msg}")

    return cleaned


def _build_composer_user_prompt(
    jam_state: Dict,
    memory: ChemistryMemory,
    bars_per_call: int
) -> str:
    """
    Build the user prompt for the composer with context.

    Args:
        jam_state: Musical context
        memory: Chemistry memory
        bars_per_call: Number of bars to generate

    Returns:
        Formatted user prompt string
    """
    prompt_parts = [
        f"# Composition Request\n",
        f"\n## Musical Context",
        f"- Key: {jam_state.get('key', 'C')}",
        f"- Tempo: {jam_state.get('tempo', 120)} BPM",
        f"- Time Signature: {jam_state.get('time_sig', '4/4')}",
        f"- Form Position: {jam_state.get('form_position', 'continuation')}",
        f"- Generate: {bars_per_call} bar(s)",
    ]

    # Add previous bars for continuity
    last_bars = jam_state.get("last_n_bars", [])
    if last_bars:
        prompt_parts.append(f"\n## Previous Bars (for continuity)")
        for bar in last_bars[-4:]:  # Last 4 bars max
            prompt_parts.append(f"### Bar {bar['bar_num']}")
            for inst, events in bar["parts"].items():
                pitches = [e["pitch"] for e in events if e["pitch"] != "rest"]
                if pitches:
                    prompt_parts.append(f"- {inst}: {', '.join(pitches)}")

    # Add memory summary
    memory_summary = memory.get_summary()
    prompt_parts.append(f"\n## Memory (Successful Patterns)")

    # Top motifs
    prompt_parts.append(f"### Common Motifs")
    for inst, motifs in memory_summary["top_motifs"].items():
        if motifs:
            motif_strs = [f"{motif} ({count}x)" for motif, count in motifs[:2]]
            prompt_parts.append(f"- {inst}: {', '.join(motif_strs)}")

    # Style characteristics
    style = memory_summary["style"]
    prompt_parts.append(f"\n### Style Characteristics")
    for inst, density in style["note_densities"].items():
        prompt_parts.append(f"- {inst} density: {density:.1f} notes/bar")
    prompt_parts.append(f"- Syncopation level: {style['syncopation']}")
    prompt_parts.append(f"- Harmonic tension: {style['tension']}")

    # Interplay patterns
    interplay = memory_summary["interplay"]
    if interplay["common_pairs"]:
        prompt_parts.append(f"\n### Successful Interplay")
        for (caller, responder), count in interplay["common_pairs"][:3]:
            prompt_parts.append(f"- {caller} → {responder} ({count} times)")

    prompt_parts.append(f"\n## Task")
    prompt_parts.append(
        f"Generate {bars_per_call} bar(s) that continue this composition. "
        f"Build on the motifs and patterns from memory. "
        f"Create interplay between instruments. "
        f"Output pure JSON only (no markdown, no explanation)."
    )

    return "\n".join(prompt_parts)


def _generate_dry_run_bars(jam_state: Dict, bars_per_call: int) -> Dict:
    """
    Generate deterministic stub bars for dry-run mode.

    Args:
        jam_state: Musical context
        bars_per_call: Number of bars to generate

    Returns:
        Valid JamJSON with simple patterns
    """
    key = jam_state.get("key", "C")
    tempo = jam_state.get("tempo", 120)
    time_sig = jam_state.get("time_sig", "4/4")

    # Determine starting bar number
    last_bars = jam_state.get("last_n_bars", [])
    start_bar_num = (last_bars[-1]["bar_num"] + 1) if last_bars else 1

    # Simple walking bass pattern
    bass_pattern = [
        {"pitch": "C2", "dur": "q", "vel": "med"},
        {"pitch": "G2", "dur": "q", "vel": "med"},
        {"pitch": "C2", "dur": "q", "vel": "med"},
        {"pitch": "G2", "dur": "q", "vel": "med"},
    ]

    # Simple snare backbeat
    snare_pattern = [
        {"pitch": "rest", "dur": "q"},
        {"pitch": "snare", "dur": "q", "vel": "hi"},
        {"pitch": "rest", "dur": "q"},
        {"pitch": "snare", "dur": "q", "vel": "hi"},
    ]

    # Steady hihat
    hihat_pattern = [
        {"pitch": "hihat", "dur": "q", "vel": "med"},
        {"pitch": "hihat", "dur": "q", "vel": "med"},
        {"pitch": "hihat", "dur": "q", "vel": "med"},
        {"pitch": "hihat", "dur": "q", "vel": "med"},
    ]

    # Simple piano comp
    piano_pattern = [
        {"pitch": "C4", "dur": "h", "vel": "med"},
        {"pitch": "C4", "dur": "h", "vel": "med"},
    ]

    # Alternating sax and trumpet
    bars = []
    for i in range(bars_per_call):
        bar_num = start_bar_num + i

        if i % 2 == 0:
            # Sax bar
            sax_events = [
                {"pitch": "E4", "dur": "q", "vel": "med"},
                {"pitch": "G4", "dur": "q", "vel": "med"},
                {"pitch": "C5", "dur": "h", "vel": "hi"},
            ]
            trumpet_events = [{"pitch": "rest", "dur": "w"}]
        else:
            # Trumpet bar
            sax_events = [{"pitch": "rest", "dur": "w"}]
            trumpet_events = [
                {"pitch": "G4", "dur": "q", "vel": "hi"},
                {"pitch": "C5", "dur": "q", "vel": "hi"},
                {"pitch": "G4", "dur": "h", "vel": "med"},
            ]

        bars.append({
            "bar_num": bar_num,
            "parts": {
                "bass": bass_pattern,
                "snare": snare_pattern,
                "hihat": hihat_pattern,
                "piano": piano_pattern,
                "sax": sax_events,
                "trumpet": trumpet_events,
            }
        })

    return {
        "tempo": tempo,
        "key": key,
        "time_sig": time_sig,
        "num_bars": bars_per_call,
        "bars": bars,
    }
