"""
RLVR Smoke Test

Verifies that the RLVR training pipeline works end-to-end without crashes.
Runs a short training session (3 steps, 2 rollouts per step) in dry-run mode.

Usage:
    uv run python -m rlvr.smoke_test
    uv run python -m rlvr.smoke_test --use-llm  # Optional: with real LLM calls
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rlvr.loop import train_rlvr


async def test_rlvr_dry_run():
    """Test RLVR training in dry-run mode (no LLM calls)."""
    print("="*60)
    print("RLVR Smoke Test - Dry Run Mode")
    print("="*60)

    summary = await train_rlvr(
        num_steps=3,
        rollouts_per_step=2,
        learning_rate=1e-5,
        dry_run=True,
        project="jazz-band-rlvr-smoke-test",
        model_name="smoke-test-dry-run",
    )

    print("\n" + "="*60)
    print("Smoke Test Results")
    print("="*60)
    print(f"✅ Training completed successfully!")
    print(f"   Steps completed: {summary['num_steps']}")
    print(f"   Best reward: {summary['best_reward']:.3f}")
    print(f"   Best Judge score: {summary['best_judge_score']:.2f}/10")
    print(f"   Early stop triggered: {summary['early_stop']}")

    # Basic assertions
    assert summary["num_steps"] == 3, "Expected 3 steps"
    assert summary["best_reward"] >= -1.0, "Reward should be >= -1.0"
    assert 0.0 <= summary["best_judge_score"] <= 10.0, "Judge score should be 0-10"

    print("\n✅ All assertions passed!")


async def test_rlvr_with_llm():
    """Test RLVR training with real LLM calls (requires WANDBAPIKEY)."""
    print("="*60)
    print("RLVR Smoke Test - LLM Mode")
    print("="*60)
    print("⚠️  This will make real LLM calls and use W&B Training")

    summary = await train_rlvr(
        num_steps=2,  # Shorter for smoke test with LLM
        rollouts_per_step=2,
        learning_rate=1e-5,
        dry_run=False,
        project="jazz-band-rlvr-smoke-test",
        model_name="smoke-test-llm",
    )

    print("\n" + "="*60)
    print("LLM Smoke Test Results")
    print("="*60)
    print(f"✅ LLM training completed successfully!")
    print(f"   Steps completed: {summary['num_steps']}")
    print(f"   Best reward: {summary['best_reward']:.3f}")
    print(f"   Best Judge score: {summary['best_judge_score']:.2f}/10")

    assert summary["num_steps"] >= 1, "Expected at least 1 step"
    print("\n✅ LLM test passed!")


async def main():
    """Run smoke tests."""
    import argparse

    parser = argparse.ArgumentParser(description="RLVR Smoke Test")
    parser.add_argument("--use-llm", action="store_true",
                        help="Run LLM test (requires WANDBAPIKEY)")

    args = parser.parse_args()

    # Always run dry-run test
    try:
        await test_rlvr_dry_run()
    except Exception as e:
        print(f"\n❌ Dry-run test FAILED: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # Optionally run LLM test
    if args.use_llm:
        try:
            await test_rlvr_with_llm()
        except Exception as e:
            print(f"\n❌ LLM test FAILED: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)

    print("\n" + "="*60)
    print("🎉 All smoke tests passed!")
    print("="*60)


if __name__ == "__main__":
    asyncio.run(main())
