"""
Agent System for Jazz Band

LLM-based agents for composition and critique:
- Composer: Generates new bars of music in JamJSON format
- Judge: Evaluates arrangements and provides feedback
- LLM: Inference wrapper with dry-run mode for testing
"""

from .composer import compose_bars
from .judge import critique
from .llm import get_llm_client, load_prompt

__all__ = [
    "compose_bars",
    "critique",
    "get_llm_client",
    "load_prompt",
]
