"""
RLVR (Reinforcement Learning with Verifiable Rewards)

Training loop using ART. Metrics → reward → gradient descent.
"""

from .loop import train, rollout, JazzScenario
from .eval import compute_reward, WEIGHTS

__all__ = [
    "train",
    "rollout",
    "JazzScenario",
    "compute_reward",
    "WEIGHTS",
]
