"""
Judge Agent

Evaluates JamJSON arrangements and provides structured feedback.
Scores compositions on harmony, rhythm, melody, and interplay.
"""

import json
import logging
from typing import Dict

import weave

from .llm import get_llm_client, load_prompt, call_llm, extract_json_from_response


@weave.op
async def critique(
    jam_json: Dict,
    summary: str = "",
    dry_run: bool = False,
    model: str = "gpt-4o-mini",
) -> Dict:
    """
    Evaluate a JamJSON arrangement and provide structured feedback.

    Args:
        jam_json: Complete JamJSON dictionary to evaluate
        summary: Optional high-level context (bar count, purpose, etc.)
        dry_run: If True, return deterministic stub instead of calling LLM
        model: LLM model name (default: gpt-4o-mini)

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
    if dry_run:
        return _generate_dry_run_critique(jam_json)

    # Get LLM client
    client = get_llm_client(dry_run=False)

    # Load judge prompt
    system_prompt = load_prompt("judge")

    # Build user prompt
    user_prompt = _build_judge_user_prompt(jam_json, summary)

    # Call LLM
    response = await call_llm(
        client=client,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        model=model,
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

    # Validate scores structure
    required_scores = [
        "harmonic_coherence",
        "rhythmic_groove",
        "melodic_interest",
        "interplay_balance"
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
        Valid critique dictionary
    """
    num_bars = jam_json.get("num_bars", 0)
    key = jam_json.get("key", "C")

    return {
        "overall_score": 7.0,
        "scores": {
            "harmonic_coherence": 7,
            "rhythmic_groove": 7,
            "melodic_interest": 6,
            "interplay_balance": 8
        },
        "rationale": (
            f"This {num_bars}-bar arrangement in {key} demonstrates solid fundamentals. "
            f"The rhythm section locks in well with clear snare backbeat. "
            f"Harmonic structure is coherent, though melodic lines could be more developed. "
            f"Good call-response moments between sax and trumpet."
        ),
        "suggestions": [
            "Develop the sax motif with variations across bars",
            "Add more rhythmic variety to the hihat pattern",
            "Experiment with piano voicings beyond simple triads",
            "Create more dynamic contrast between bars",
            "Consider adding brief rests for breathing room"
        ],
        "prompt_mutation": (
            "Encourage more motivic development and rhythmic variety. "
            "Suggest specific syncopation patterns for piano and bass. "
            "Emphasize the importance of space and dynamics."
        )
    }
