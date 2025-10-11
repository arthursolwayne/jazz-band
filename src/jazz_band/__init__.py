"""
Agent Jazz Band - Multi-instrument symbolic music jam system.

Subplan 1: Core Score & Schema
- JamJSON: Structured music representation (6 parts: bass, snare, hihat, piano, sax, trumpet)
- Orchestra: Instrument configuration and MIDI mapping
- ScoreBuilder: Conversion from JamJSON to music21 scores
"""

__version__ = "0.1.0"

from .schema import JamEvent, JamBar, JamJSON, validate_jam_json
from .orchestra import OrchestraSpec, Instrument
from .score_builder import ScoreBuilder

__all__ = [
    "JamEvent",
    "JamBar",
    "JamJSON",
    "validate_jam_json",
    "OrchestraSpec",
    "Instrument",
    "ScoreBuilder",
]
