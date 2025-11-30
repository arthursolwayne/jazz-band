"""
Baseline runner: test Claude models on composer prompt without training.
Uses Claude CLI for auth.
"""

import argparse
import json
import subprocess
from datetime import datetime
from pathlib import Path

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from jazz_band.symbol_engine import SYSTEM_PROMPT, execute_midi_code, compute_reward

MODELS = {
    "opus": "claude-opus-4-5-20251101",
    "sonnet": "claude-sonnet-4-5-20250929",
    "haiku": "claude-haiku-4-5-20251001",
}

BASELINES_DIR = Path(__file__).parent


def call_claude(model_id: str, prompt: str) -> str:
    """Call Claude CLI and return the response text."""
    result = subprocess.run(
        ["claude", "-p", prompt, "--model", model_id, "--output-format", "json"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(f"Claude CLI failed: {result.stderr}")

    response = json.loads(result.stdout)
    return response.get("result", "")


def run_baseline(model_name: str, model_id: str, n_runs: int):
    """Run N generations for a single model."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    run_dir = BASELINES_DIR / model_name / timestamp
    run_dir.mkdir(parents=True, exist_ok=True)

    results = []
    valid_count = 0
    best_reward = 0.0

    print(f"\n{model_name.upper()} ({model_id})")
    print("=" * 50)

    for i in range(n_runs):
        # Call Claude CLI
        try:
            code = call_claude(model_id, SYSTEM_PROMPT)
        except Exception as e:
            print(f"  Run {i}: CLI error - {e}")
            continue

        # Execute and score
        midi, cleaned_code, error = execute_midi_code(code)
        reward = compute_reward(midi)  # handles None internally (returns 0.0)

        # Track stats
        if midi:
            valid_count += 1
        if reward > best_reward:
            best_reward = reward

        # Save artifacts
        run_subdir = run_dir / f"run_{i:03d}"
        run_subdir.mkdir(exist_ok=True)

        (run_subdir / "code.py").write_text(cleaned_code or code)
        if midi:
            midi.write(str(run_subdir / "output.mid"))

        meta = {
            "run": i,
            "model": model_id,
            "reward": reward,
            "has_midi": midi is not None,
            "error": error,
            "duration": midi.get_end_time() if midi else None,
        }
        (run_subdir / "meta.json").write_text(json.dumps(meta, indent=2))
        results.append(meta)

        status = "✓" if reward > 0 else "✗"
        print(f"  Run {i}: reward={reward:+.2f} {status}")

    # Summary
    summary = {
        "model": model_id,
        "n_runs": n_runs,
        "valid": valid_count,
        "best_reward": best_reward,
        "timestamp": timestamp,
    }
    (run_dir / "summary.json").write_text(json.dumps(summary, indent=2))

    print(f"  Valid: {valid_count}/{n_runs} ({100*valid_count/n_runs:.0f}%)")
    print(f"  Best:  {best_reward:+.2f}")

    return summary


def main():
    parser = argparse.ArgumentParser(description="Run baseline tests on Claude models")
    parser.add_argument("--models", nargs="+", default=["sonnet", "haiku", "opus"],
                        choices=["sonnet", "haiku", "opus"], help="Models to test")
    parser.add_argument("--runs", type=int, default=5, help="Runs per model")
    args = parser.parse_args()

    print("=" * 50)
    print("BASELINE RUNS")
    print("=" * 50)

    for model_name in args.models:
        run_baseline(model_name, MODELS[model_name], args.runs)

    print("\nDone.")


if __name__ == "__main__":
    main()
