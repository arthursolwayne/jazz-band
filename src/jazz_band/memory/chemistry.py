"""
Chemistry Memory - Lightweight pattern tracking for jazz compositions

Tracks musical patterns that emerge during composition and critique cycles.
Used to maintain stylistic consistency and build on successful ideas.
"""

import json
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from collections import defaultdict, Counter
from dataclasses import dataclass, field, asdict


@dataclass
class MotifBank:
    """
    Tracks pitch-class n-grams (melodic fragments) per instrument.

    Stores the most common melodic patterns to encourage motif development
    and thematic unity across the composition.

    Example:
        motifs["sax"] = {("C4", "E4", "G4"): 3, ("G4", "F4", "E4"): 2}
    """

    # Dict[instrument_name, Dict[pitch_tuple, count]]
    motifs: Dict[str, Dict[Tuple[str, ...], int]] = field(default_factory=lambda: defaultdict(Counter))

    def add_motif(self, instrument: str, pitches: List[str], n: int = 3) -> None:
        """
        Extract and track n-grams from a pitch sequence.

        Args:
            instrument: Instrument name (bass, piano, sax, trumpet)
            pitches: List of pitch names (e.g., ["C4", "E4", "G4", "C5"])
            n: N-gram size (default 3)
        """
        if len(pitches) < n:
            return

        # Extract n-grams
        for i in range(len(pitches) - n + 1):
            motif = tuple(pitches[i:i+n])
            if instrument not in self.motifs:
                self.motifs[instrument] = Counter()
            self.motifs[instrument][motif] += 1

    def get_top_motifs(self, instrument: str, k: int = 5) -> List[Tuple[Tuple[str, ...], int]]:
        """
        Get the top k most common motifs for an instrument.

        Args:
            instrument: Instrument name
            k: Number of top motifs to return

        Returns:
            List of (motif_tuple, count) pairs
        """
        if instrument not in self.motifs:
            return []
        return self.motifs[instrument].most_common(k)

    def to_dict(self) -> dict:
        """Convert to JSON-serializable dict."""
        return {
            inst: {str(motif): count for motif, count in counter.items()}
            for inst, counter in self.motifs.items()
        }

    @classmethod
    def from_dict(cls, data: dict) -> "MotifBank":
        """Load from dict."""
        bank = cls()
        for inst, motifs_dict in data.items():
            bank.motifs[inst] = Counter()
            for motif_str, count in motifs_dict.items():
                # Convert string back to tuple
                motif_tuple = eval(motif_str)  # Safe here since we control the data
                bank.motifs[inst][motif_tuple] = count
        return bank


@dataclass
class StyleVector:
    """
    Running averages of musical style characteristics.

    Tracks aggregate features to maintain stylistic consistency:
    - note_density: Average notes per bar per instrument
    - syncopation_proxy: Ratio of off-beat to on-beat events
    - chord_tension: Average dissonance level (simple heuristic)

    Values are updated incrementally using exponential moving average.
    """

    note_density: Dict[str, float] = field(default_factory=dict)  # notes per bar
    syncopation_proxy: float = 0.5  # 0 (on-beat) to 1 (highly syncopated)
    chord_tension: float = 0.3  # 0 (consonant) to 1 (dissonant)

    # EMA smoothing factor (0 = ignore new, 1 = only use new)
    alpha: float = 0.2

    def update_density(self, instrument: str, notes_per_bar: float) -> None:
        """Update note density for an instrument using EMA."""
        if instrument not in self.note_density:
            self.note_density[instrument] = notes_per_bar
        else:
            self.note_density[instrument] = (
                self.alpha * notes_per_bar +
                (1 - self.alpha) * self.note_density[instrument]
            )

    def update_syncopation(self, new_value: float) -> None:
        """Update syncopation proxy using EMA."""
        self.syncopation_proxy = (
            self.alpha * new_value +
            (1 - self.alpha) * self.syncopation_proxy
        )

    def update_tension(self, new_value: float) -> None:
        """Update chord tension using EMA."""
        self.chord_tension = (
            self.alpha * new_value +
            (1 - self.alpha) * self.chord_tension
        )

    def to_dict(self) -> dict:
        """Convert to JSON-serializable dict."""
        return {
            "note_density": self.note_density,
            "syncopation_proxy": self.syncopation_proxy,
            "chord_tension": self.chord_tension,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "StyleVector":
        """Load from dict."""
        return cls(
            note_density=data.get("note_density", {}),
            syncopation_proxy=data.get("syncopation_proxy", 0.5),
            chord_tension=data.get("chord_tension", 0.3),
        )


@dataclass
class InterplayLedger:
    """
    Tracks call-response patterns between instruments.

    Records successful musical conversations to encourage interplay:
    - Which instrument "called" (played a motif)
    - Which bar the call occurred
    - Which instrument "responded"
    - The delay between call and response (in bars)

    Example entry: ("sax", 2, "trumpet", 2) means sax played in bar 2,
    trumpet responded 2 bars later in bar 4.
    """

    # List of (caller_instrument, call_bar, responder_instrument, response_delay)
    interactions: List[Tuple[str, int, str, int]] = field(default_factory=list)

    def add_interaction(
        self,
        caller: str,
        call_bar: int,
        responder: str,
        response_delay: int
    ) -> None:
        """
        Record a call-response interaction.

        Args:
            caller: Instrument that played the initial motif
            call_bar: Bar number where the call occurred
            responder: Instrument that responded
            response_delay: Number of bars between call and response
        """
        self.interactions.append((caller, call_bar, responder, response_delay))

    def get_common_pairs(self, k: int = 5) -> List[Tuple[Tuple[str, str], int]]:
        """
        Get the most common call-response pairs.

        Args:
            k: Number of top pairs to return

        Returns:
            List of ((caller, responder), count) pairs
        """
        pairs = Counter((caller, responder) for caller, _, responder, _ in self.interactions)
        return pairs.most_common(k)

    def to_dict(self) -> dict:
        """Convert to JSON-serializable dict."""
        return {
            "interactions": [
                {"caller": c, "call_bar": cb, "responder": r, "delay": d}
                for c, cb, r, d in self.interactions
            ]
        }

    @classmethod
    def from_dict(cls, data: dict) -> "InterplayLedger":
        """Load from dict."""
        ledger = cls()
        for item in data.get("interactions", []):
            ledger.interactions.append((
                item["caller"],
                item["call_bar"],
                item["responder"],
                item["delay"]
            ))
        return ledger


class ChemistryMemory:
    """
    Container for all chemistry memory components.

    Provides unified interface for:
    - Tracking motifs (MotifBank)
    - Tracking style (StyleVector)
    - Tracking interplay (InterplayLedger)
    - Persistence to/from JSON

    Memory is updated after each judge critique and used to inform
    the composer during subsequent generation cycles.
    """

    def __init__(self):
        self.motifs = MotifBank()
        self.style = StyleVector()
        self.interplay = InterplayLedger()

    def update_from_jam_json(self, jam_json: dict) -> None:
        """
        Extract and update memory from a JamJSON structure.

        This is a simple heuristic-based extraction. More sophisticated
        analysis could be added later.

        Args:
            jam_json: Valid JamJSON dictionary
        """
        # Extract motifs from melodic instruments (sax, trumpet, bass)
        for bar in jam_json.get("bars", []):
            bar_num = bar["bar_num"]
            parts = bar["parts"]

            for instrument in ["bass", "sax", "trumpet", "piano"]:
                if instrument in parts:
                    # Extract pitch sequence (excluding rests and drums)
                    pitches = [
                        event["pitch"]
                        for event in parts[instrument]
                        if event["pitch"] not in ["rest", "snare", "hihat"]
                    ]
                    if pitches:
                        self.motifs.add_motif(instrument, pitches)

                        # Update density
                        notes_per_bar = len([p for p in pitches if p != "rest"])
                        self.style.update_density(instrument, notes_per_bar)

            # Simple interplay detection: if sax plays then trumpet plays next bar
            # (This is a placeholder - more sophisticated analysis could be added)
            if bar_num < jam_json["num_bars"]:
                sax_events = parts.get("sax", [])
                has_sax = any(e["pitch"] != "rest" for e in sax_events)

                if has_sax and bar_num < len(jam_json["bars"]):
                    next_bar = jam_json["bars"][bar_num]  # bar_num is 1-indexed
                    trumpet_events = next_bar["parts"].get("trumpet", [])
                    has_trumpet = any(e["pitch"] != "rest" for e in trumpet_events)

                    if has_trumpet:
                        self.interplay.add_interaction("sax", bar_num, "trumpet", 1)

    def get_summary(self) -> dict:
        """
        Get a human-readable summary of memory contents.

        Returns:
            Dictionary with summary statistics
        """
        return {
            "top_motifs": {
                inst: self.motifs.get_top_motifs(inst, k=3)
                for inst in ["bass", "sax", "trumpet", "piano"]
            },
            "style": {
                "note_densities": self.style.note_density,
                "syncopation": round(self.style.syncopation_proxy, 2),
                "tension": round(self.style.chord_tension, 2),
            },
            "interplay": {
                "total_interactions": len(self.interplay.interactions),
                "common_pairs": self.interplay.get_common_pairs(k=3),
            }
        }

    def save(self, filepath: Path) -> None:
        """
        Save memory to JSON file.

        Args:
            filepath: Path to save JSON (typically artifacts/memory.json)
        """
        data = {
            "motifs": self.motifs.to_dict(),
            "style": self.style.to_dict(),
            "interplay": self.interplay.to_dict(),
        }

        filepath.parent.mkdir(parents=True, exist_ok=True)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def load(cls, filepath: Path) -> "ChemistryMemory":
        """
        Load memory from JSON file.

        Args:
            filepath: Path to JSON file

        Returns:
            ChemistryMemory instance
        """
        if not filepath.exists():
            return cls()  # Return empty memory if file doesn't exist

        with open(filepath, 'r') as f:
            data = json.load(f)

        memory = cls()
        memory.motifs = MotifBank.from_dict(data.get("motifs", {}))
        memory.style = StyleVector.from_dict(data.get("style", {}))
        memory.interplay = InterplayLedger.from_dict(data.get("interplay", {}))
        return memory
