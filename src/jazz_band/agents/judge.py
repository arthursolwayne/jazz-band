"""
Judge Agent

Evaluates JamJSON arrangements and provides structured feedback.
Scores compositions on harmony, rhythm, melody, and interplay.
"""

import json
import logging
from typing import Dict

import weave

from .llm import load_prompt, call_llm, extract_json_from_response


@weave.op
async def critique(
    model,
    jam_json: Dict,
    summary: str = "",
) -> Dict:
    """
    Evaluate a JamJSON arrangement and provide structured feedback.

    Args:
        model: art.TrainableModel instance (or None for dry-run)
        jam_json: Complete JamJSON dictionary to evaluate
        summary: Optional high-level context (bar count, purpose, etc.)

    Returns:
        Dictionary with structure:
        {
            "overall_score": float (0-10),
            "scores": {
                "harmonic_coherence": int (0-10),
                "rhythmic_groove": int (0-10),
                "melodic_interest": int (0-10),
                "interplay_balance": int (0-10)
            },
            "rationale": str (2-4 sentences),
            "suggestions": [str, ...] (3-5 actionable suggestions),
            "prompt_mutation": str (hint for GEPA in Subplan 4)
        }

    Raises:
        ValueError: If response fails validation
        Exception: If LLM call fails
    """

    # Dry-run mode: return deterministic stub
    if model is None:
        return _generate_dry_run_critique(jam_json)

    # Load judge prompt
    system_prompt = load_prompt("judge")

    # Build user prompt
    user_prompt = _build_judge_user_prompt(jam_json, summary)

    # Call LLM (using ART model's inference endpoint)
    response = await call_llm(
        model=model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=1500,
        temperature=0.5,  # Lower temperature for more consistent critiques
    )

    # Extract and validate JSON
    try:
        critique_json = extract_json_from_response(response)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse judge response: {response[:200]}...")
        raise ValueError(f"Judge returned invalid JSON: {e}")

    # Basic validation
    _validate_critique_structure(critique_json)

    return critique_json


def _build_judge_user_prompt(jam_json: Dict, summary: str) -> str:
    """
    Build the user prompt for the judge.

    Args:
        jam_json: JamJSON to evaluate
        summary: Optional context string

    Returns:
        Formatted user prompt string
    """
    prompt_parts = [
        f"# Evaluation Request\n",
        f"## Context",
        f"- Bars: {jam_json['num_bars']}",
        f"- Key: {jam_json['key']}",
        f"- Tempo: {jam_json['tempo']} BPM",
        f"- Time Signature: {jam_json['time_sig']}",
    ]

    if summary:
        prompt_parts.append(f"- Purpose: {summary}")

    prompt_parts.append(f"\n## Arrangement to Evaluate")
    prompt_parts.append("```json")
    prompt_parts.append(json.dumps(jam_json, indent=2))
    prompt_parts.append("```")

    prompt_parts.append(f"\n## Task")
    prompt_parts.append(
        "Evaluate this jazz arrangement according to the rubric. "
        "Provide scores, rationale, and specific suggestions. "
        "Output pure JSON only (no markdown, no explanation)."
    )

    return "\n".join(prompt_parts)


def _validate_critique_structure(critique: Dict) -> None:
    """
    Validate that critique has required fields.

    Args:
        critique: Critique dictionary to validate

    Raises:
        ValueError: If required fields are missing or invalid
    """
    required_fields = ["overall_score", "scores", "rationale", "suggestions"]
    for field in required_fields:
        if field not in critique:
            raise ValueError(f"Critique missing required field: {field}")

    # Validate scores structure (updated for new jazz-focused criteria)
    required_scores = [
        "jazz_harmony",
        "latin_jazz_rhythm",
        "jazz_melody",
        "interplay_space",
        "jazz_authenticity"
    ]
    scores = critique.get("scores", {})
    for score_name in required_scores:
        if score_name not in scores:
            raise ValueError(f"Critique missing score: {score_name}")

        score_val = scores[score_name]
        if not isinstance(score_val, (int, float)) or not (0 <= score_val <= 10):
            raise ValueError(f"Invalid score value for {score_name}: {score_val}")

    # Validate overall score
    overall = critique.get("overall_score")
    if not isinstance(overall, (int, float)) or not (0 <= overall <= 10):
        raise ValueError(f"Invalid overall_score: {overall}")

    # Validate suggestions is a list
    if not isinstance(critique.get("suggestions", []), list):
        raise ValueError("suggestions must be a list")


def _generate_dry_run_critique(jam_json: Dict) -> Dict:
    """
    Generate deterministic stub critique for dry-run mode.

    Args:
        jam_json: JamJSON being evaluated

    Returns:
        Valid critique dictionary (with strict jazz standards - dry-run gets low scores)
    """
    num_bars = jam_json.get("num_bars", 0)
    key = jam_json.get("key", "C")

    return {
        "overall_score": 4.2,  # Lowered for strict jazz standards
        "scores": {
            "jazz_harmony": 3,  # Basic triads, not jazz
            "latin_jazz_rhythm": 4,  # Downbeat-heavy, no upbeat syncopation
            "jazz_melody": 5,  # Simple scales, no bebop
            "interplay_space": 5,  # Some call-response but basic
            "jazz_authenticity": 4  # Sounds like exercise music
        },
        "rationale": (
            f"This {num_bars}-bar arrangement in {key} uses basic triads and simple scale patterns - "
            f"sounds more like a music theory exercise than jazz. The rhythm section is metronomic "
            f"with no swing feel. Melodic lines lack bebop vocabulary and blues inflection. "
            f"Some call-response between horns but overall feel is too stiff and academic."
        ),
        "suggestions": [
            "Replace piano triads with 7th chords (Cmaj7, Dm7, G7) minimum",
            "Add chromatic approach notes to sax/trumpet lines for bebop flavor",
            "Introduce swing eighth notes in hihat pattern instead of straight quarters",
            "Use walking bass (roots, 3rds, 5ths, 7ths) instead of just root notes",
            "Add ii-V-I progressions for authentic jazz harmony"
        ],
        "prompt_mutation": (
            "Emphasize jazz-specific requirements: mandate 7th chords in piano, "
            "demand chromatic approach notes in horn lines, require swing feel in rhythm section. "
            "Add examples of ii-V-I progressions and bebop phrasing patterns."
        )
    }
