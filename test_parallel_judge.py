#!/usr/bin/env python3
"""
Test script for parallel judge implementation.

Tests the new critique_parallel() function in dry-run mode
to verify it produces the same output structure as critique().
"""

import asyncio
import json
from pathlib import Path
import sys

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from jazz_band.agents import critique, critique_parallel


# Sample JamJSON for testing
SAMPLE_JAM_JSON = {
    "num_bars": 8,
    "key": "C",
    "tempo": 120,
    "time_sig": "4/4",
    "bars": [
        {
            "bar_num": 1,
            "piano": [{"start": 0.0, "pitch": 60, "duration": 1.0}],
            "bass": [{"start": 0.0, "pitch": 36, "duration": 1.0}],
            "snare": [],
            "hihat": [{"start": 0.0, "duration": 0.5}],
            "sax": [],
        },
        {
            "bar_num": 2,
            "piano": [{"start": 0.0, "pitch": 62, "duration": 1.0}],
            "bass": [{"start": 0.0, "pitch": 38, "duration": 1.0}],
            "snare": [{"start": 1.0, "duration": 0.25}],
            "hihat": [{"start": 0.0, "duration": 0.5}],
            "sax": [],
        },
        {
            "bar_num": 3,
            "piano": [{"start": 0.0, "pitch": 64, "duration": 1.0}],
            "bass": [{"start": 0.0, "pitch": 40, "duration": 1.0}],
            "snare": [{"start": 1.0, "duration": 0.25}],
            "hihat": [{"start": 0.0, "duration": 0.5}],
            "sax": [],
        },
        {
            "bar_num": 4,
            "piano": [{"start": 0.0, "pitch": 65, "duration": 1.0}],
            "bass": [{"start": 0.0, "pitch": 41, "duration": 1.0}],
            "snare": [{"start": 1.0, "duration": 0.25}],
            "hihat": [{"start": 0.0, "duration": 0.5}],
            "sax": [],
        },
        {
            "bar_num": 5,
            "piano": [{"start": 0.0, "pitch": 67, "duration": 1.0}],
            "bass": [{"start": 0.0, "pitch": 43, "duration": 1.0}],
            "snare": [{"start": 1.0, "duration": 0.25}],
            "hihat": [{"start": 0.0, "duration": 0.5}],
            "sax": [{"start": 2.0, "pitch": 72, "duration": 0.5}],
        },
        {
            "bar_num": 6,
            "piano": [{"start": 0.0, "pitch": 69, "duration": 1.0}],
            "bass": [{"start": 0.0, "pitch": 45, "duration": 1.0}],
            "snare": [{"start": 1.0, "duration": 0.25}],
            "hihat": [{"start": 0.0, "duration": 0.5}],
            "sax": [{"start": 2.0, "pitch": 74, "duration": 0.5}],
        },
        {
            "bar_num": 7,
            "piano": [{"start": 0.0, "pitch": 71, "duration": 1.0}],
            "bass": [{"start": 0.0, "pitch": 47, "duration": 1.0}],
            "snare": [{"start": 1.0, "duration": 0.25}],
            "hihat": [{"start": 0.0, "duration": 0.5}],
            "sax": [{"start": 2.0, "pitch": 76, "duration": 0.5}],
        },
        {
            "bar_num": 8,
            "piano": [{"start": 0.0, "pitch": 72, "duration": 1.0}],
            "bass": [{"start": 0.0, "pitch": 48, "duration": 1.0}],
            "snare": [{"start": 1.0, "duration": 0.25}],
            "hihat": [{"start": 0.0, "duration": 0.5}],
            "sax": [{"start": 2.0, "pitch": 77, "duration": 0.5}],
        },
    ]
}


async def test_both_modes():
    """Test both monolithic and parallel critique modes."""
    print("=" * 70)
    print("TESTING JAZZ JUDGE REFACTORING")
    print("=" * 70)
    print()

    # Test 1: Monolithic mode (original)
    print("1. Testing MONOLITHIC mode (original critique function)...")
    print("-" * 70)
    try:
        result_monolithic = await critique(
            model=None,  # Dry-run mode
            jam_json=SAMPLE_JAM_JSON,
            summary="Test arrangement: 8 bars in C major"
        )
        print("✅ Monolithic mode succeeded")
        print(f"   Overall score: {result_monolithic['overall_score']}/10")
        print(f"   Scores: {result_monolithic['scores']}")
        print()
    except Exception as e:
        print(f"❌ Monolithic mode failed: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test 2: Parallel mode (new)
    print("2. Testing PARALLEL mode (new critique_parallel function)...")
    print("-" * 70)
    try:
        result_parallel = await critique_parallel(
            model=None,  # Dry-run mode
            jam_json=SAMPLE_JAM_JSON,
            summary="Test arrangement: 8 bars in C major"
        )
        print("✅ Parallel mode succeeded")
        print(f"   Overall score: {result_parallel['overall_score']}/10")
        print(f"   Scores: {result_parallel['scores']}")
        print()
    except Exception as e:
        print(f"❌ Parallel mode failed: {e}")
        import traceback
        traceback.print_exc()
        return False

    # Test 3: Compare structures
    print("3. Comparing output structures...")
    print("-" * 70)

    # Check required fields
    required_fields = ["overall_score", "scores", "rationale", "suggestions"]
    required_scores = ["jazz_harmony", "latin_jazz_rhythm", "jazz_melody",
                       "interplay_space", "jazz_authenticity"]

    all_valid = True

    for mode, result in [("monolithic", result_monolithic), ("parallel", result_parallel)]:
        print(f"\n   Validating {mode} mode:")

        # Check top-level fields
        for field in required_fields:
            if field in result:
                print(f"   ✅ Has '{field}' field")
            else:
                print(f"   ❌ Missing '{field}' field")
                all_valid = False

        # Check score fields
        for score_name in required_scores:
            if score_name in result.get("scores", {}):
                print(f"   ✅ Has '{score_name}' score")
            else:
                print(f"   ❌ Missing '{score_name}' score")
                all_valid = False

    print()
    print("=" * 70)
    if all_valid:
        print("✅ ALL TESTS PASSED")
        print()
        print("Both monolithic and parallel modes produce valid output structures.")
        print("The parallel architecture is ready to use!")
    else:
        print("❌ SOME TESTS FAILED")
        print()
        print("Please check the error messages above.")
    print("=" * 70)

    return all_valid


async def main():
    """Main entry point."""
    success = await test_both_modes()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    asyncio.run(main())
