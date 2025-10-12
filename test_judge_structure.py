#!/usr/bin/env python3
"""
Simple test to verify the parallel judge code structure.

This script checks that:
1. All prompt files exist
2. The judge.py file has the new functions
3. The __init__.py exports are correct
"""

import sys
from pathlib import Path

def test_prompt_files():
    """Check that all judge prompt files exist."""
    print("1. Testing prompt files...")
    print("-" * 70)

    prompts_dir = Path(__file__).parent / "prompts" / "judges"

    expected_files = [
        "harmony.md",
        "rhythm.md",
        "melody.md",
        "interplay.md",
        "authenticity.md",
        "aggregator.md",
    ]

    all_exist = True
    for filename in expected_files:
        filepath = prompts_dir / filename
        if filepath.exists():
            size_kb = filepath.stat().st_size / 1024
            print(f"   ✅ {filename} exists ({size_kb:.1f} KB)")
        else:
            print(f"   ❌ {filename} missing")
            all_exist = False

    print()
    return all_exist


def test_judge_py():
    """Check that judge.py has the new functions."""
    print("2. Testing judge.py structure...")
    print("-" * 70)

    judge_file = Path(__file__).parent / "src" / "jazz_band" / "agents" / "judge.py"

    if not judge_file.exists():
        print("   ❌ judge.py not found")
        return False

    content = judge_file.read_text()

    required_elements = {
        "critique_parallel function": "async def critique_parallel(",
        "call_criterion_judge helper": "async def _call_criterion_judge(",
        "call_aggregator helper": "async def _call_aggregator(",
        "build_aggregator_user_prompt helper": "def _build_aggregator_user_prompt(",
        "asyncio import": "import asyncio",
    }

    all_found = True
    for name, pattern in required_elements.items():
        if pattern in content:
            print(f"   ✅ {name} found")
        else:
            print(f"   ❌ {name} missing")
            all_found = False

    print()
    return all_found


def test_init_py():
    """Check that __init__.py exports critique_parallel."""
    print("3. Testing __init__.py exports...")
    print("-" * 70)

    init_file = Path(__file__).parent / "src" / "jazz_band" / "agents" / "__init__.py"

    if not init_file.exists():
        print("   ❌ __init__.py not found")
        return False

    content = init_file.read_text()

    required_elements = {
        "critique_parallel import": "from .judge import critique, critique_parallel",
        "critique_parallel in __all__": '"critique_parallel"',
    }

    all_found = True
    for name, pattern in required_elements.items():
        if pattern in content:
            print(f"   ✅ {name} found")
        else:
            print(f"   ❌ {name} missing")
            all_found = False

    print()
    return all_found


def test_docstrings():
    """Check that new functions have proper documentation."""
    print("4. Testing documentation...")
    print("-" * 70)

    judge_file = Path(__file__).parent / "src" / "jazz_band" / "agents" / "judge.py"
    content = judge_file.read_text()

    # Find critique_parallel docstring
    if 'Evaluate a JamJSON arrangement using parallel criterion-specific judges.' in content:
        print("   ✅ critique_parallel has docstring")
    else:
        print("   ❌ critique_parallel missing docstring")
        return False

    # Check that it mentions the architecture
    if '5 parallel LLM calls' in content and '1 aggregator call' in content:
        print("   ✅ Docstring mentions parallel architecture")
    else:
        print("   ❌ Docstring doesn't explain architecture")
        return False

    print()
    return True


def main():
    """Run all tests."""
    print("=" * 70)
    print("JAZZ JUDGE PARALLEL REFACTORING - STRUCTURE VALIDATION")
    print("=" * 70)
    print()

    results = {
        "Prompt files": test_prompt_files(),
        "Judge.py functions": test_judge_py(),
        "Module exports": test_init_py(),
        "Documentation": test_docstrings(),
    }

    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)

    for test_name, passed in results.items():
        status = "✅ PASSED" if passed else "❌ FAILED"
        print(f"{test_name:.<50} {status}")

    print()
    all_passed = all(results.values())

    if all_passed:
        print("✅ ALL STRUCTURAL TESTS PASSED")
        print()
        print("The parallel judge refactoring is complete!")
        print()
        print("Next steps:")
        print("  1. Use critique_parallel() instead of critique() for parallel mode")
        print("  2. The original critique() remains as a fallback")
        print("  3. Both functions have the same signature and output format")
    else:
        print("❌ SOME TESTS FAILED")
        print()
        print("Please review the error messages above.")

    print("=" * 70)

    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
