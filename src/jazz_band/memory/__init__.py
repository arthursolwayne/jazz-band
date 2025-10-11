"""
Chemistry Memory System

Tracks musical patterns, style characteristics, and interplay dynamics
to inform future composition decisions.

Components:
- MotifBank: Pitch-class n-grams per instrument
- StyleVector: Running averages of musical features
- InterplayLedger: Call-response patterns between instruments
- ChemistryMemory: Container with JSON persistence
"""

from .chemistry import (
    MotifBank,
    StyleVector,
    InterplayLedger,
    ChemistryMemory,
)

__all__ = [
    "MotifBank",
    "StyleVector",
    "InterplayLedger",
    "ChemistryMemory",
]
