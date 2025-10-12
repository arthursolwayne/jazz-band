"""
Agent Smoke Test for Subplan 2

Tests the complete agent pipeline:
1. Initialize ART model (OpenPipe/Qwen3-14B-Instruct via W&B Serverless)
2. Load Subplan 1 smoke jam (session_000.mid)
3. Run Judge to evaluate and get feedback
4. Update chemistry memory with patterns
5. Run Composer to add 4 more bars
6. Export session_001.mid
7. Log everything to W&B Weave

Usage:
    # Dry-run mode (no LLM calls)
    python tests/agents_smoke_test.py --dry-run

    # With LLM (requires WANDB_API_KEY)
    python tests/agents_smoke_test.py --use-llm
"""

import os
import sys
import argparse
import asyncio
from pathlib import Path
from dotenv import load_dotenv

# Add src to path for local imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from jazz_band.schema import validate_jam_json
from jazz_band.score_builder import ScoreBuilder
from jazz_band.memory import ChemistryMemory
from jazz_band.agents import compose_bars, critique
from jazz_band.agents.llm import init_model

import weave

# Load environment variables
load_dotenv()


async def load_subplan1_jam():
    """
    Load the Subplan 1 smoke jam (4 bars from session_000).

    Returns:
        JamJSON dictionary
    """
    # Recreate the original 4-bar jam from Subplan 1
    bass_pattern = [
        {"pitch": "C2", "dur": "q", "vel": "med"},
        {"pitch": "G2", "dur": "q", "vel": "med"},
        {"pitch": "C2", "dur": "q", "vel": "med"},
        {"pitch": "G2", "dur": "q", "vel": "med"},
    ]

    snare_pattern = [
        {"pitch": "rest", "dur": "q"},
        {"pitch": "snare", "dur": "q", "vel": "hi"},
        {"pitch": "rest", "dur": "q"},
        {"pitch": "snare", "dur": "q", "vel": "hi"},
    ]

    hihat_pattern = [
        {"pitch": "hihat", "dur": "q", "vel": "med"},
        {"pitch": "hihat", "dur": "q", "vel": "med"},
        {"pitch": "hihat", "dur": "q", "vel": "med"},
        {"pitch": "hihat", "dur": "q", "vel": "med"},
    ]

    piano_pattern = [
        {"pitch": "C4", "dur": "h", "vel": "med"},
        {"pitch": "C4", "dur": "h", "vel": "med"},
    ]

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
    sax_bar3_4 = [{"pitch": "rest", "dur": "w"}]

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

    jam_json = {
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
async def run_agent_smoke_test(dry_run: bool = True):
    """
    Main smoke test for Subplan 2 agents.

    Args:
        dry_run: If True, use deterministic stubs; if False, call actual LLMs

    Returns:
        Dictionary with test results
    """

    print("=" * 60)
    print("Agent Jazz Band - Subplan 2 Smoke Test")
    print("=" * 60)
    print(f"Mode: {'DRY-RUN (no LLM)' if dry_run else 'LLM-ENABLED'}")
    print()

    # Initialize ART model (following 2048.py pattern)
    print("Step 0: Initializing ART model...")
    if dry_run:
        print("  ✓ Dry-run mode: model = None")
        model = None
    else:
        print("  Initializing OpenPipe/Qwen3-14B-Instruct via W&B Serverless...")
        model = await init_model(
            project="jazz-band",
            model_name="composer-001",
            dry_run=False
        )
        print(f"  ✓ Model initialized: {model.get_inference_name()}")
    print()

    # Step 1: Load Subplan 1 jam
    print("Step 1: Loading Subplan 1 smoke jam (4 bars)...")
    jam_json_original = await load_subplan1_jam()
    print(f"  ✓ Loaded {jam_json_original['num_bars']} bars in {jam_json_original['key']}")
    print()

    # Step 2: Run Judge
    print("Step 2: Running Judge agent to evaluate...")
    critique_result = await critique(
        model=model,
        jam_json=jam_json_original,
        summary="Initial 4-bar jam from Subplan 1",
    )

    print(f"  ✓ Overall Score: {critique_result['overall_score']}/10")
    print(f"  Scores:")
    for criterion, score in critique_result['scores'].items():
        print(f"    - {criterion}: {score}/10")
    print(f"  Rationale: {critique_result['rationale'][:100]}...")
    print(f"  Suggestions ({len(critique_result['suggestions'])}):")
    for i, suggestion in enumerate(critique_result['suggestions'][:3], 1):
        print(f"    {i}. {suggestion[:60]}...")
    print()

    # Step 3: Update chemistry memory
    print("Step 3: Updating chemistry memory...")
    memory = ChemistryMemory()
    memory.update_from_jam_json(jam_json_original)

    memory_summary = memory.get_summary()
    print(f"  ✓ Tracked {len(memory_summary['top_motifs'])} instrument motifs")
    print(f"  ✓ Style syncopation: {memory_summary['style']['syncopation']}")
    print(f"  ✓ Interplay interactions: {memory_summary['interplay']['total_interactions']}")

    # Save memory
    memory_path = Path(__file__).parent.parent / "artifacts" / "memory.json"
    memory.save(memory_path)
    print(f"  ✓ Saved memory to {memory_path}")
    print()

    # Step 4: Compose 4 new bars
    print("Step 4: Composing 4 new bars with Composer agent...")
    jam_state = {
        "key": jam_json_original["key"],
        "tempo": jam_json_original["tempo"],
        "time_sig": jam_json_original["time_sig"],
        "last_n_bars": jam_json_original["bars"],
        "form_position": "continuation",
    }

    new_bars_json = await compose_bars(
        model=model,
        jam_state=jam_state,
        memory=memory,
        bars_per_call=4,
    )

    print(f"  ✓ Generated {new_bars_json['num_bars']} new bars")
    print()

    # Step 5: Merge and export
    print("Step 5: Merging and exporting to MIDI...")

    # Combine original and new bars
    combined_jam = {
        "tempo": jam_json_original["tempo"],
        "key": jam_json_original["key"],
        "time_sig": jam_json_original["time_sig"],
        "num_bars": jam_json_original["num_bars"] + new_bars_json["num_bars"],
        "bars": jam_json_original["bars"] + new_bars_json["bars"],
    }

    # Export to MIDI
    builder = ScoreBuilder()
    score = builder.from_jam_json(combined_jam)

    output_path = Path(__file__).parent.parent / "artifacts" / "session_001.mid"
    builder.export_midi(score, output_path)
    print(f"  ✓ Exported to {output_path}")
    print()

    # Display summary
    print(builder.summarize(score))
    print()

    # Step 6: Weave logging (automatic via @weave.op decorator)
    print("Step 6: Logging to W&B Weave...")
    result = {
        "status": "success",
        "mode": "dry-run" if dry_run else "llm",
        "original_bars": jam_json_original["num_bars"],
        "new_bars": new_bars_json["num_bars"],
        "total_bars": combined_jam["num_bars"],
        "critique": critique_result,
        "memory_summary": memory_summary,
        "jam_json_original": jam_json_original,
        "jam_json_combined": combined_jam,
        "midi_path": str(output_path),
    }

    print("  ✓ Logged to Weave (via @weave.op decorator)")
    print()

    print("=" * 60)
    print("Subplan 2 Smoke Test Complete!")
    print("=" * 60)
    print()
    print("Results:")
    print(f"  - Judge Score: {critique_result['overall_score']}/10")
    print(f"  - Total Bars: {combined_jam['num_bars']}")
    print(f"  - MIDI: {output_path}")
    print(f"  - Memory: {memory_path}")
    print()
    print("Next steps:")
    print("  1. Check W&B Weave dashboard for logged run")
    print("  2. Play session_001.mid to hear the extended arrangement")
    print("  3. Review TODO.md for Subplan 3 (RLVR training)")
    print()

    return result


def main():
    """Parse arguments and run smoke test."""
    parser = argparse.ArgumentParser(description="Agent Jazz Band - Subplan 2 Smoke Test")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Use dry-run mode (no LLM calls, deterministic outputs)"
    )
    parser.add_argument(
        "--use-llm",
        action="store_true",
        help="Enable LLM mode (requires WANDBAPIKEY or OPENAI_API_KEY)"
    )

    args = parser.parse_args()

    # Determine mode
    if args.use_llm:
        dry_run = False
        # Validate API key (following 2048.py pattern)
        if not (os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY")):
            print("ERROR: WANDB_API_KEY required for --use-llm mode")
            print("Set it in .env file or environment, or use --dry-run mode")
            sys.exit(1)
    else:
        dry_run = True

    # Initialize Weave (following 2048.py pattern)
    api_key = os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY", "")
    os.environ["WANDB_API_KEY"] = api_key
    weave.init("jazz-band")

    # Run test
    result = asyncio.run(run_agent_smoke_test(dry_run=dry_run))

    sys.exit(0)


if __name__ == "__main__":
    main()
