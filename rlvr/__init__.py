"""
RLVR (Reinforcement Learning with Verifiable Rewards)

Training loop using ART. LLM generates code → execute → reward → gradient descent.
"""

from .loop import train, rollout, JazzScenario

__all__ = [
    "train",
    "rollout",
    "JazzScenario",
]
