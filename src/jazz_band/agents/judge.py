"""
Judge Agent

Evaluates JamJSON arrangements and provides structured feedback.
Scores compositions on harmony, rhythm, melody, and interplay.

Supports both monolithic (single LLM call) and parallel (5 criterion judges + aggregator) modes.
"""

import asyncio
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


# ============================================================================
# PARALLEL CRITIQUE MODE (5 criterion judges + aggregator)
# ============================================================================

@weave.op
async def critique_parallel(
    model,
    jam_json: Dict,
    summary: str = "",
) -> Dict:
    """
    Evaluate a JamJSON arrangement using parallel criterion-specific judges.

    This function makes 5 parallel LLM calls (one per criterion) followed by
    1 aggregator call to combine results. Returns the same structure as critique().

    Args:
        model: art.TrainableModel instance (or None for dry-run)
        jam_json: Complete JamJSON dictionary to evaluate
        summary: Optional high-level context (bar count, purpose, etc.)

    Returns:
        Dictionary with structure:
        {
            "overall_score": float (0-10),
            "scores": {
                "jazz_harmony": int (0-10),
                "latin_jazz_rhythm": int (0-10),
                "jazz_melody": int (0-10),
                "interplay_space": int (0-10),
                "jazz_authenticity": int (0-10)
            },
            "rationale": str (2-4 sentences),
            "suggestions": [str, ...] (3-5 actionable suggestions),
            "prompt_mutation": str (hint for GEPA)
        }

    Raises:
        ValueError: If response fails validation
        Exception: If LLM call fails
    """

    # Dry-run mode: return deterministic stub
    if model is None:
        return _generate_dry_run_critique(jam_json)

    # Build user prompt (shared by all judges)
    user_prompt = _build_judge_user_prompt(jam_json, summary)

    # Define the 5 criterion judges
    criteria = [
        ("harmony", "judges/harmony"),
        ("rhythm", "judges/rhythm"),
        ("melody", "judges/melody"),
        ("interplay", "judges/interplay"),
        ("authenticity", "judges/authenticity"),
    ]

    # Step 1: Call all 5 criterion judges in parallel
    logging.info("Calling 5 criterion judges in parallel...")
    criterion_tasks = [
        _call_criterion_judge(model, criterion_name, prompt_path, user_prompt)
        for criterion_name, prompt_path in criteria
    ]
    criterion_results_list = await asyncio.gather(*criterion_tasks)

    # Convert list to dictionary
    criterion_results = {
        criterion_name: result
        for (criterion_name, _), result in zip(criteria, criterion_results_list)
    }

    logging.info(f"Received criterion results: {list(criterion_results.keys())}")

    # Step 2: Call aggregator to combine results
    logging.info("Calling aggregator to combine results...")
    final_critique = await _call_aggregator(
        model, criterion_results, jam_json, summary
    )

    # Validate final structure
    _validate_critique_structure(final_critique)

    return final_critique


@weave.op
async def _call_criterion_judge(
    model,
    criterion_name: str,
    prompt_path: str,
    user_prompt: str,
) -> Dict:
    """
    Call a single criterion-specific judge.

    Args:
        model: art.TrainableModel instance
        criterion_name: Name of criterion (for logging)
        prompt_path: Path to criterion prompt (e.g., "judges/harmony")
        user_prompt: User prompt with JamJSON

    Returns:
        Dictionary with {score: int, rationale: str, suggestion: str}
    """
    # Load criterion-specific prompt
    system_prompt = load_prompt(prompt_path)

    # Call LLM
    response = await call_llm(
        model=model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=800,  # Shorter than full critique
        temperature=0.5,
    )

    # Extract and validate JSON
    try:
        result = extract_json_from_response(response)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse {criterion_name} judge response: {response[:200]}...")
        raise ValueError(f"{criterion_name} judge returned invalid JSON: {e}")

    # Validate structure
    required_fields = ["score", "rationale", "suggestion"]
    for field in required_fields:
        if field not in result:
            raise ValueError(f"{criterion_name} judge missing field: {field}")

    # Validate score range
    score = result.get("score")
    if not isinstance(score, (int, float)) or not (0 <= score <= 10):
        raise ValueError(f"{criterion_name} judge invalid score: {score}")

    logging.info(f"{criterion_name} judge score: {score}/10")
    return result


@weave.op
async def _call_aggregator(
    model,
    criterion_results: Dict,
    jam_json: Dict,
    summary: str,
) -> Dict:
    """
    Call the aggregator to combine criterion results into final critique.

    Args:
        model: art.TrainableModel instance
        criterion_results: Dictionary with keys (harmony, rhythm, melody, interplay, authenticity)
        jam_json: Original JamJSON (for context)
        summary: High-level context

    Returns:
        Final critique dictionary matching critique() output format
    """
    # Load aggregator prompt
    system_prompt = load_prompt("judges/aggregator")

    # Build aggregator user prompt
    user_prompt = _build_aggregator_user_prompt(criterion_results, jam_json, summary)

    # Call LLM
    response = await call_llm(
        model=model,
        system_prompt=system_prompt,
        user_prompt=user_prompt,
        max_tokens=1500,
        temperature=0.5,
    )

    # Extract and validate JSON
    try:
        final_critique = extract_json_from_response(response)
    except json.JSONDecodeError as e:
        logging.error(f"Failed to parse aggregator response: {response[:200]}...")
        raise ValueError(f"Aggregator returned invalid JSON: {e}")

    logging.info(f"Aggregator overall score: {final_critique.get('overall_score')}/10")
    return final_critique


def _build_aggregator_user_prompt(
    criterion_results: Dict,
    jam_json: Dict,
    summary: str,
) -> str:
    """
    Build the user prompt for the aggregator.

    Args:
        criterion_results: Dictionary with criterion evaluations
        jam_json: Original JamJSON
        summary: High-level context

    Returns:
        Formatted user prompt string
    """
    prompt_parts = [
        "# Aggregation Request\n",
        "## Individual Criterion Results\n",
    ]

    # Add each criterion result
    criterion_map = {
        "harmony": "jazz_harmony",
        "rhythm": "latin_jazz_rhythm",
        "melody": "jazz_melody",
        "interplay": "interplay_space",
        "authenticity": "jazz_authenticity",
    }

    for criterion_key, criterion_name in criterion_map.items():
        result = criterion_results.get(criterion_key, {})
        prompt_parts.append(f"### {criterion_name}")
        prompt_parts.append(f"- **Score**: {result.get('score', 0)}/10")
        prompt_parts.append(f"- **Rationale**: {result.get('rationale', 'N/A')}")
        prompt_parts.append(f"- **Suggestion**: {result.get('suggestion', 'N/A')}")
        prompt_parts.append("")

    # Add context
    prompt_parts.append("## Context")
    prompt_parts.append(f"- Bars: {jam_json['num_bars']}")
    prompt_parts.append(f"- Key: {jam_json['key']}")
    prompt_parts.append(f"- Tempo: {jam_json['tempo']} BPM")
    prompt_parts.append(f"- Time Signature: {jam_json['time_sig']}")

    if summary:
        prompt_parts.append(f"- Purpose: {summary}")

    prompt_parts.append("\n## Original Arrangement (for reference)")
    prompt_parts.append("```json")
    prompt_parts.append(json.dumps(jam_json, indent=2))
    prompt_parts.append("```")

    prompt_parts.append("\n## Task")
    prompt_parts.append(
        "Combine these criterion evaluations into a final critique. "
        "Apply threshold caps, calculate overall score, synthesize rationale, "
        "prioritize suggestions by lowest scores. "
        "Output pure JSON only (no markdown, no explanation)."
    )

    return "\n".join(prompt_parts)
