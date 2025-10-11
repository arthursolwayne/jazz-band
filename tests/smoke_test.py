"""
Smoke Test for Agent Jazz Band - Subplan 1

Tests the core functionality:
1. JamJSON schema validation
2. JamJSON to music21 Score conversion
3. MIDI export
4. W&B Weave telemetry logging

Generates a simple 4-bar jazz arrangement with:
- Bass: Root-fifth walking pattern
- Drums: Kick on 1 & 3, snare on 2 & 4, hihat on all eighths
- Piano: Simple C major triads
- Sax: 2-bar melody phrase
- Trumpet: Call-response to sax in bars 3-4
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add src to path for local imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jazz_band.schema import validate_jam_json, JamJSON
from jazz_band.orchestra import DEFAULT_ORCHESTRA
from jazz_band.score_builder import ScoreBuilder

# Import Weave for telemetry
import weave

# Load environment variables
load_dotenv()

# Validate WANDBAPIKEY is set (following 2048.py pattern)
if not os.environ.get("WANDBAPIKEY"):
    raise ValueError("WANDBAPIKEY is required for logging to Weights & Biases.")


def generate_4bar_jam() -> JamJSON:
    """
    Generate a hardcoded 4-bar jazz arrangement for testing.

    Arrangement:
    - Bass: Root-fifth walking pattern (C2-G2 repeating)
    - Snare: Backbeat on beats 2 and 4
    - Hi-hat: Quarter notes on all four beats
    - Piano: Simple C major triads on beats 1 and 3
    - Sax: 2-bar melody (bars 1-2), then rest
    - Trumpet: Call-response melody (bars 3-4)

    Returns:
        Valid JamJSON structure
    """

    # Bass line: alternating root (C2) and fifth (G2) on quarter notes
    bass_pattern = [
        {"pitch": "C2", "dur": "q", "vel": "med"},
        {"pitch": "G2", "dur": "q", "vel": "med"},
        {"pitch": "C2", "dur": "q", "vel": "med"},
        {"pitch": "G2", "dur": "q", "vel": "med"},
    ]

    # Snare: backbeat on beats 2 and 4
    snare_pattern = [
        {"pitch": "rest", "dur": "q"},      # Beat 1 (rest)
        {"pitch": "snare", "dur": "q", "vel": "hi"},   # Beat 2 (snare)
        {"pitch": "rest", "dur": "q"},      # Beat 3 (rest)
        {"pitch": "snare", "dur": "q", "vel": "hi"},   # Beat 4 (snare)
    ]

    # Hi-hat: quarter notes on all four beats
    hihat_pattern = [
        {"pitch": "hihat", "dur": "q", "vel": "med"},  # Beat 1
        {"pitch": "hihat", "dur": "q", "vel": "med"},  # Beat 2
        {"pitch": "hihat", "dur": "q", "vel": "med"},  # Beat 3
        {"pitch": "hihat", "dur": "q", "vel": "med"},  # Beat 4
    ]

    # Piano: C major triad on beats 1 and 3 (half notes)
    piano_pattern = [
        {"pitch": "C4", "dur": "h", "vel": "med"},
        {"pitch": "C4", "dur": "h", "vel": "med"},
    ]

    # Sax: melody in bars 1-2
    sax_bar1 = [
        {"pitch": "E4", "dur": "q", "vel": "med"},
        {"pitch": "G4", "dur": "q", "vel": "med"},
        {"pitch": "C5", "dur": "h", "vel": "hi"},
    ]
    sax_bar2 = [
        {"pitch": "B4", "dur": "q", "vel": "med"},
        {"pitch": "A4", "dur": "q", "vel": "med"},
        {"pitch": "G4", "dur": "h", "vel": "med"},
    ]
    sax_bar3_4 = [{"pitch": "rest", "dur": "w"}]  # Rest in bars 3-4

    # Trumpet: rest in bars 1-2, call-response in bars 3-4
    trumpet_bar1_2 = [{"pitch": "rest", "dur": "w"}]
    trumpet_bar3 = [
        {"pitch": "G4", "dur": "q", "vel": "hi"},
        {"pitch": "A4", "dur": "q", "vel": "hi"},
        {"pitch": "B4", "dur": "h", "vel": "hi"},
    ]
    trumpet_bar4 = [
        {"pitch": "C5", "dur": "h", "vel": "hi"},
        {"pitch": "G4", "dur": "h", "vel": "med"},
    ]

    jam_json: JamJSON = {
        "tempo": 120,
        "key": "C",
        "time_sig": "4/4",
        "num_bars": 4,
        "bars": [
            {
                "bar_num": 1,
                "parts": {
                    "bass": bass_pattern,
                    "snare": snare_pattern,
                    "hihat": hihat_pattern,
                    "piano": piano_pattern,
                    "sax": sax_bar1,
                    "trumpet": trumpet_bar1_2,
                }
            },
            {
                "bar_num": 2,
                "parts": {
                    "bass": bass_pattern,
                    "snare": snare_pattern,
                    "hihat": hihat_pattern,
                    "piano": piano_pattern,
                    "sax": sax_bar2,
                    "trumpet": trumpet_bar1_2,
                }
            },
            {
                "bar_num": 3,
                "parts": {
                    "bass": bass_pattern,
                    "snare": snare_pattern,
                    "hihat": hihat_pattern,
                    "piano": piano_pattern,
                    "sax": sax_bar3_4,
                    "trumpet": trumpet_bar3,
                }
            },
            {
                "bar_num": 4,
                "parts": {
                    "bass": bass_pattern,
                    "snare": snare_pattern,
                    "hihat": hihat_pattern,
                    "piano": piano_pattern,
                    "sax": sax_bar3_4,
                    "trumpet": trumpet_bar4,
                }
            },
        ]
    }

    return jam_json


@weave.op
def run_smoke_test():
    """
    Main smoke test function.

    Generates a 4-bar jam, validates it, converts to MIDI, and logs to Weave.
    """

    print("=" * 60)
    print("Agent Jazz Band - Smoke Test (Subplan 1)")
    print("=" * 60)
    print()

    # Display orchestra configuration
    print(DEFAULT_ORCHESTRA.summary())
    print()

    # Generate test JamJSON
    print("Generating 4-bar test arrangement...")
    jam_json = generate_4bar_jam()

    # Validate JamJSON
    print("Validating JamJSON schema...")
    is_valid, error_msg, cleaned_json = validate_jam_json(jam_json)

    if not is_valid:
        print(f"ERROR: JamJSON validation failed: {error_msg}")
        sys.exit(1)

    print("  ✓ JamJSON is valid")
    print()

    # Convert to music21 Score
    print("Converting to music21 Score...")
    builder = ScoreBuilder()
    score = builder.from_jam_json(jam_json)
    print("  ✓ Score created successfully")
    print()

    # Generate summary
    print(builder.summarize(score))
    print()

    # Export to MIDI
    output_path = Path(__file__).parent.parent / "artifacts" / "session_000.mid"
    print(f"Exporting MIDI to {output_path}...")
    builder.export_midi(score, output_path)
    print(f"  ✓ MIDI file saved: {output_path}")
    print()

    # Prepare telemetry data
    print("Logging to W&B Weave...")

    config = {
        "tempo": jam_json["tempo"],
        "key": jam_json["key"],
        "time_sig": jam_json["time_sig"],
        "num_bars": jam_json["num_bars"],
        "subplan": "1-core-score-schema",
    }

    # Data logged automatically by @weave.op decorator when returned
    result = {
        "status": "success",
        "config": config,
        "jam_json": jam_json,
        "midi_path": str(output_path),
    }

    print("  ✓ Logged to Weave (via @weave.op decorator)")
    print()

    print("=" * 60)
    print("Smoke Test Complete!")
    print("=" * 60)
    print()
    print("Next steps:")
    print("  1. Check W&B Weave dashboard for logged run")
    print("  2. Play the MIDI file to verify audio output")
    print("  3. Review TODO.md for Subplan 2 roadmap")
    print()

    return result


if __name__ == "__main__":
    # Initialize Weave (following 2048.py pattern, but using WANDBAPIKEY)
    os.environ["WANDB_API_KEY"] = os.environ["WANDBAPIKEY"]

    # Initialize Weave project
    # Format: weave.init("entity/project-name") or just "project-name"
    weave.init("jazz-band")

    # Run the test
    result = run_smoke_test()

    # Exit with success
    sys.exit(0)
