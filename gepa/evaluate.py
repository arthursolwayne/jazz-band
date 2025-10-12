"""
Objective Evaluation for GEPA

Computes 6D objective vector from JamJSON and Judge output:
1. Consonance: % notes in key scale
2. Groove alignment: bass-drum correlation on downbeats
3. Motif coherence: n-gram repetition/variation balance
4. Interplay: call-response event count
5. Density regularity: variance of note counts per bar
6. Judge score: 0-10 from Judge agent

All objectives are maximized (higher is better).
"""

import sys
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from collections import Counter
import statistics

import weave

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jazz_band.schema import validate_jam_json
from jazz_band.memory import ChemistryMemory
from jazz_band.agents import compose_bars, critique


@dataclass
class ObjectiveVector:
    """6D objective vector for multi-objective optimization."""
    consonance: float  # 0.0 to 1.0
    groove_alignment: float  # 0.0 to 1.0
    motif_coherence: float  # 0.0 to 1.0
    interplay: float  # 0.0 to 1.0
    density_regularity: float  # 0.0 to 1.0
    judge_score: float  # 0.0 to 10.0 (normalized to 0-1 for comparison)

    def to_list(self) -> List[float]:
        """Convert to list for Pareto computations."""
        return [
            self.consonance,
            self.groove_alignment,
            self.motif_coherence,
            self.interplay,
            self.density_regularity,
            self.judge_score / 10.0,  # Normalize to 0-1
        ]

    def to_dict(self) -> Dict[str, float]:
        """Convert to dictionary for logging."""
        return {
            "consonance": self.consonance,
            "groove_alignment": self.groove_alignment,
            "motif_coherence": self.motif_coherence,
            "interplay": self.interplay,
            "density_regularity": self.density_regularity,
            "judge_score": self.judge_score,
        }


# Musical scale definitions (for consonance calculation)
SCALES = {
    "C": ["C", "D", "E", "F", "G", "A", "B"],
    "Dm": ["D", "E", "F", "G", "A", "Bb", "C"],
    "F": ["F", "G", "A", "Bb", "C", "D", "E"],
    "G": ["G", "A", "B", "C", "D", "E", "F#"],
    # Add more as needed
}


def compute_consonance(jam_json: Dict) -> float:
    """
    Objective 1: Consonance
    Percentage of notes that fit in the key scale (avoid chromatic tension).

    Args:
        jam_json: JamJSON dictionary

    Returns:
        Consonance score 0.0 to 1.0
    """
    key = jam_json.get("key", "C")
    scale = SCALES.get(key, SCALES["C"])  # Default to C major

    # Extract pitch classes (remove octave numbers)
    total_notes = 0
    in_scale_notes = 0

    for bar in jam_json["bars"]:
        for part_name, events in bar["parts"].items():
            # Skip drums
            if part_name in ["snare", "hihat"]:
                continue

            for event in events:
                pitch = event.get("pitch", "rest")
                if pitch == "rest":
                    continue

                # Extract pitch class (remove octave)
                pitch_class = pitch.rstrip("0123456789")

                total_notes += 1
                if pitch_class in scale:
                    in_scale_notes += 1

    if total_notes == 0:
        return 0.5  # Neutral score for empty arrangements

    return in_scale_notes / total_notes


def compute_groove_alignment(jam_json: Dict) -> float:
    """
    Objective 2: Groove Alignment
    Correlation between bass and drum hits on downbeats (beat 1 of each bar).

    Args:
        jam_json: JamJSON dictionary

    Returns:
        Groove alignment score 0.0 to 1.0
    """
    alignment_count = 0
    total_bars = len(jam_json["bars"])

    for bar in jam_json["bars"]:
        # Check if bass has a note on beat 1 (first event)
        bass_events = bar["parts"].get("bass", [])
        has_bass_downbeat = len(bass_events) > 0 and bass_events[0].get("pitch") != "rest"

        # Check if snare or hihat has a hit on beat 1
        snare_events = bar["parts"].get("snare", [])
        hihat_events = bar["parts"].get("hihat", [])
        has_drum_downbeat = (
            (len(snare_events) > 0 and snare_events[0].get("pitch") != "rest") or
            (len(hihat_events) > 0 and hihat_events[0].get("pitch") != "rest")
        )

        # Both hit on downbeat = aligned
        if has_bass_downbeat and has_drum_downbeat:
            alignment_count += 1

    if total_bars == 0:
        return 0.5

    return alignment_count / total_bars


def compute_motif_coherence(jam_json: Dict, memory: ChemistryMemory) -> float:
    """
    Objective 3: Motif Coherence
    Balance between repetition (using motifs from memory) and variation.

    Args:
        jam_json: JamJSON dictionary
        memory: ChemistryMemory instance

    Returns:
        Motif coherence score 0.0 to 1.0
    """
    # Update memory with new jam
    memory.update_from_jam_json(jam_json)

    # Measure: average motif count (higher = more coherent patterns)
    total_motifs = 0
    instrument_count = 0

    for inst in ["bass", "piano", "sax", "trumpet"]:
        top_motifs = memory.motifs.get_top_motifs(inst, k=5)
        if top_motifs:
            total_count = sum(count for _, count in top_motifs)
            total_motifs += total_count
            instrument_count += 1

    if instrument_count == 0:
        return 0.5

    # Average motif occurrences per instrument (normalize by bar count)
    avg_motifs = total_motifs / instrument_count
    num_bars = jam_json.get("num_bars", 1)

    # Score: higher repetition = higher coherence (up to threshold)
    # Target ~3-5 motif occurrences per instrument per 4 bars
    target = 4.0
    score = min(avg_motifs / (num_bars / 4.0) / target, 1.0)

    return score


def compute_interplay(jam_json: Dict, memory: ChemistryMemory) -> float:
    """
    Objective 4: Interplay
    Number of call-response interactions between instruments (from InterplayLedger).

    Args:
        jam_json: JamJSON dictionary
        memory: ChemistryMemory instance

    Returns:
        Interplay score 0.0 to 1.0
    """
    # Update memory to extract interplay
    memory.update_from_jam_json(jam_json)

    # Count interactions
    interaction_count = len(memory.interplay.interactions)

    # Normalize by number of bars (target ~1 interaction per 4 bars)
    num_bars = jam_json.get("num_bars", 1)
    target_per_4_bars = 1.0

    score = min(interaction_count / (num_bars / 4.0) / target_per_4_bars, 1.0)

    return score


def compute_density_regularity(jam_json: Dict) -> float:
    """
    Objective 5: Density Regularity
    Inverse of variance in note counts per bar per instrument.
    Regular density = consistent phrasing.

    Args:
        jam_json: JamJSON dictionary

    Returns:
        Density regularity score 0.0 to 1.0
    """
    # Collect note counts per bar for each instrument
    instrument_densities = {
        "bass": [],
        "piano": [],
        "sax": [],
        "trumpet": [],
    }

    for bar in jam_json["bars"]:
        for inst in instrument_densities.keys():
            events = bar["parts"].get(inst, [])
            note_count = sum(1 for e in events if e.get("pitch") != "rest")
            instrument_densities[inst].append(note_count)

    # Compute variance for each instrument
    total_variance = 0.0
    inst_count = 0

    for inst, densities in instrument_densities.items():
        if len(densities) > 1:
            variance = statistics.variance(densities)
            total_variance += variance
            inst_count += 1

    if inst_count == 0:
        return 0.5

    avg_variance = total_variance / inst_count

    # Score: lower variance = higher regularity
    # Normalize by expected variance (~2.0 for typical jazz)
    expected_variance = 2.0
    score = max(0.0, 1.0 - (avg_variance / expected_variance))

    return score


@weave.op
async def evaluate_individual(
    model,
    individual_prompt: str,
    individual_genes: Dict,
    jam_state: Dict,
    memory: ChemistryMemory,
    bars_to_generate: int = 8,  # Reduced from 16 based on user feedback
) -> Tuple[Dict, ObjectiveVector, Dict]:
    """
    Evaluate a single individual by generating music and computing objectives.

    Args:
        model: ART model (or None for dry-run)
        individual_prompt: Composer prompt text
        individual_genes: Gene knobs dictionary
        jam_state: Musical context (key, tempo, etc.)
        memory: ChemistryMemory instance
        bars_to_generate: Number of bars to generate

    Returns:
        Tuple of (jam_json, objective_vector, critique_result)
    """
    # Temporarily inject prompt (for now, genes not directly used in composition)
    # In production, genes would be incorporated into prompt text
    # For this implementation, we use genes to guide evaluation weight/interpretation

    # Generate jam using Composer
    jam_json = await compose_bars(
        model=model,
        jam_state=jam_state,
        memory=memory,
        bars_per_call=bars_to_generate,
    )

    # Get Judge critique
    critique_result = await critique(
        model=model,
        jam_json=jam_json,
        summary=f"GEPA evaluation: {bars_to_generate} bars",
    )

    judge_score = critique_result.get("overall_score", 5.0)

    # Compute verifiable objectives
    consonance = compute_consonance(jam_json)
    groove_alignment = compute_groove_alignment(jam_json)
    motif_coherence = compute_motif_coherence(jam_json, memory)
    interplay = compute_interplay(jam_json, memory)
    density_regularity = compute_density_regularity(jam_json)

    objectives = ObjectiveVector(
        consonance=consonance,
        groove_alignment=groove_alignment,
        motif_coherence=motif_coherence,
        interplay=interplay,
        density_regularity=density_regularity,
        judge_score=judge_score,
    )

    return jam_json, objectives, critique_result
