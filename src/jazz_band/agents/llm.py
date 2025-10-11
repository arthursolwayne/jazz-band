"""
LLM Inference Wrapper

Mirrors the 2048.py pattern for OpenAI client usage with Weave logging.
Supports dry-run mode for testing without LLM calls.

Usage:
    from jazz_band.agents.llm import get_llm_client, load_prompt

    client = get_llm_client(dry_run=False)
    prompt = load_prompt("composer")
    response = await client.chat.completions.create(...)
"""

import os
import json
import logging
from pathlib import Path
from typing import Optional
from dotenv import load_dotenv

import weave

# Suppress weave logs (following 2048.py pattern)
logging.getLogger("weave").setLevel(logging.CRITICAL)

# Load environment variables
load_dotenv()


def get_llm_client(dry_run: bool = False):
    """
    Get OpenAI client for LLM inference.

    Mirrors 2048.py pattern: uses WANDBAPIKEY for authentication.
    In dry-run mode, returns None (calls will be mocked).

    Args:
        dry_run: If True, return None (for testing without LLM)

    Returns:
        AsyncOpenAI client or None

    Raises:
        ValueError: If WANDBAPIKEY not set and not in dry-run mode
    """
    if dry_run:
        return None

    # Check for API key (following 2048.py pattern)
    api_key = os.environ.get("WANDBAPIKEY") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError(
            "WANDBAPIKEY or OPENAI_API_KEY is required for LLM inference. "
            "Set it in your environment or use --dry-run mode."
        )

    # Import here to avoid dependency in dry-run mode
    try:
        from openai import AsyncOpenAI
    except ImportError:
        raise ImportError(
            "openai package required for LLM mode. "
            "Install with: uv pip install openai"
        )

    # Create client
    # For now, use OpenAI directly. Later subplans will use ART/W&B infrastructure
    client = AsyncOpenAI(api_key=api_key)

    return client


def load_prompt(prompt_name: str) -> str:
    """
    Load a prompt template from the prompts directory.

    Args:
        prompt_name: Name of prompt file (without .md extension)
                    e.g., "composer" or "judge"

    Returns:
        Prompt content as string

    Raises:
        FileNotFoundError: If prompt file doesn't exist
    """
    # Get project root (3 levels up from this file)
    project_root = Path(__file__).parent.parent.parent.parent
    prompt_path = project_root / "prompts" / f"{prompt_name}.md"

    if not prompt_path.exists():
        raise FileNotFoundError(
            f"Prompt file not found: {prompt_path}\n"
            f"Expected prompts in: {project_root / 'prompts'}"
        )

    with open(prompt_path, 'r') as f:
        return f.read()


@weave.op
async def call_llm(
    client,
    system_prompt: str,
    user_prompt: str,
    model: str = "gpt-4o-mini",
    max_tokens: int = 2000,
    temperature: float = 0.7,
) -> str:
    """
    Call LLM with system and user prompts.

    Decorated with @weave.op for automatic Weave logging (following 2048.py pattern).

    Args:
        client: AsyncOpenAI client (or None for dry-run)
        system_prompt: System message (role definition)
        user_prompt: User message (task description)
        model: Model name (default: gpt-4o-mini for cost efficiency)
        max_tokens: Maximum response tokens
        temperature: Sampling temperature

    Returns:
        Response content as string

    Raises:
        Exception: If LLM call fails
    """
    if client is None:
        # Dry-run mode: return placeholder
        return '{"dry_run": true, "message": "This is a dry-run response"}'

    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        content = response.choices[0].message.content
        if content is None:
            raise ValueError("LLM returned None content")

        return content

    except Exception as e:
        logging.error(f"LLM call failed: {e}")
        raise


def extract_json_from_response(response: str) -> dict:
    """
    Extract JSON from LLM response.

    Handles cases where LLM wraps JSON in markdown code blocks or adds text.

    Args:
        response: Raw LLM response string

    Returns:
        Parsed JSON dictionary

    Raises:
        json.JSONDecodeError: If no valid JSON found
    """
    # Remove markdown code blocks if present
    if "```json" in response:
        start = response.find("```json") + 7
        end = response.find("```", start)
        response = response[start:end].strip()
    elif "```" in response:
        start = response.find("```") + 3
        end = response.find("```", start)
        response = response[start:end].strip()

    # Try to parse
    try:
        return json.loads(response)
    except json.JSONDecodeError as e:
        # Try to find JSON object in the response
        start_idx = response.find("{")
        end_idx = response.rfind("}") + 1

        if start_idx != -1 and end_idx > start_idx:
            try:
                return json.loads(response[start_idx:end_idx])
            except json.JSONDecodeError:
                pass

        logging.error(f"Failed to extract JSON from response: {response[:200]}...")
        raise e
