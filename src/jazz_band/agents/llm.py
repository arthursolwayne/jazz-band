"""
LLM Inference Wrapper

Mirrors the 2048.py pattern for ART TrainableModel usage with Weave logging.
Supports dry-run mode for testing without LLM calls.

Usage:
    from jazz_band.agents.llm import init_model, load_prompt

    model = await init_model(project="jazz-band", dry_run=False)
    prompt = load_prompt("composer")
    response = await call_llm(model, system_prompt, user_prompt)
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


async def init_model(
    project: str = "jazz-band",
    model_name: str = "composer-001",
    base_model: str = "OpenPipe/Qwen3-14B-Instruct",
    dry_run: bool = False
):
    """
    Initialize ART TrainableModel with ServerlessBackend.

    Mirrors 2048.py pattern exactly. In dry-run mode, returns None.

    Args:
        project: W&B project name for this model
        model_name: Name for this model instance
        base_model: Base model to use (default: OpenPipe/Qwen3-14B-Instruct)
        dry_run: If True, return None (for testing without LLM)

    Returns:
        art.TrainableModel instance or None

    Raises:
        ValueError: If WANDB_API_KEY not set and not in dry-run mode
    """
    if dry_run:
        return None

    # Check for API key (following 2048.py pattern)
    api_key = os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY")
    if not api_key:
        raise ValueError(
            "WANDB_API_KEY is required for inference and training. "
            "Set it in your environment or use --dry-run mode."
        )

    # Set environment variable for ART
    os.environ["WANDB_API_KEY"] = api_key

    # Import here to avoid dependency in dry-run mode
    try:
        import art
        from art.serverless.backend import ServerlessBackend
    except ImportError:
        raise ImportError(
            "openpipe-art package required for LLM mode. "
            "Install with: uv pip install openpipe-art"
        )

    # Create model (following 2048.py pattern)
    model = art.TrainableModel(
        name=model_name,
        project=project,
        base_model=base_model,
    )

    # Initialize the serverless backend
    backend = ServerlessBackend()

    # Register model with backend (sets up logging, inference, and training)
    await model.register(backend)

    return model


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
    model,
    system_prompt: str,
    user_prompt: str,
    max_tokens: int = 2000,
    temperature: float = 0.7,
) -> str:
    """
    Call LLM with system and user prompts.

    Mirrors 2048.py pattern: uses ART model's inference endpoint.
    Decorated with @weave.op for automatic Weave logging.

    Args:
        model: art.TrainableModel instance (or None for dry-run)
        system_prompt: System message (role definition)
        user_prompt: User message (task description)
        max_tokens: Maximum response tokens
        temperature: Sampling temperature

    Returns:
        Response content as string

    Raises:
        Exception: If LLM call fails
    """
    if model is None:
        # Dry-run mode: return placeholder
        return '{"dry_run": true, "message": "This is a dry-run response"}'

    # Import here to avoid dependency in dry-run mode
    try:
        from openai import AsyncOpenAI
    except ImportError:
        raise ImportError(
            "openai package required for LLM mode. "
            "Install with: uv pip install openai"
        )

    try:
        # Create client using model's inference endpoint (following 2048.py pattern)
        client = AsyncOpenAI(
            base_url=model.inference_base_url,
            api_key=model.inference_api_key,
        )

        # Call with model's inference name (following 2048.py pattern)
        response = await client.chat.completions.create(
            model=model.get_inference_name(),
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_completion_tokens=max_tokens,
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
