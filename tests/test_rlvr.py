"""Tests for RLVR training loop."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from rlvr.loop import train, save_rollout, JazzScenario, ARTIFACTS_DIR
from jazz_band.symbol_engine import execute_midi_code, compute_reward


def test_dry_run_one_step():
    """Verify train() completes 1 step in dry-run mode."""
    summary = asyncio.run(train(num_steps=1, rollouts_per_step=2, dry_run=True))
    assert summary["num_steps"] == 1
    assert "best_reward" in summary
    print("✓ test_dry_run_one_step")


def test_dry_run_multiple_steps():
    """Verify train() completes multiple steps."""
    summary = asyncio.run(train(num_steps=3, rollouts_per_step=4, dry_run=True))
    assert summary["num_steps"] == 3
    print("✓ test_dry_run_multiple_steps")


def test_execute_midi_code_valid():
    """Verify execute_midi_code works with valid code."""
    code = """
import pretty_midi
midi = pretty_midi.PrettyMIDI()
piano = pretty_midi.Instrument(program=0)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
midi.instruments.append(piano)
"""
    midi, cleaned, error = execute_midi_code(code)
    assert midi is not None
    assert error is None
    assert len(midi.instruments) == 1
    assert len(midi.instruments[0].notes) == 1
    print("✓ test_execute_midi_code_valid")


def test_execute_midi_code_with_markdown():
    """Verify execute_midi_code strips markdown fences."""
    code = """```python
import pretty_midi
midi = pretty_midi.PrettyMIDI()
piano = pretty_midi.Instrument(program=0)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
midi.instruments.append(piano)
```"""
    midi, cleaned, error = execute_midi_code(code)
    assert midi is not None
    print("✓ test_execute_midi_code_with_markdown")


def test_execute_midi_code_invalid():
    """Verify execute_midi_code handles invalid code."""
    code = "this is not valid python"
    midi, cleaned, error = execute_midi_code(code)
    assert midi is None
    assert error is not None
    print("✓ test_execute_midi_code_invalid")


def test_compute_reward_valid():
    """Verify reward is in valid range for MIDI with correct structure."""
    import pretty_midi
    midi = pretty_midi.PrettyMIDI()
    sax = pretty_midi.Instrument(program=66)  # Tenor sax
    # 4 bars at 160 BPM = 6 seconds, varied durations with rests
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=0.7, end=1.5))  # rest before
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=3.0))  # rest before
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=4.0))  # blue note (Eb)
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=6.0))
    midi.instruments.append(sax)

    reward = compute_reward(midi)
    # Full scoring (passes sanity + gates): 0.3 to 1.0
    assert 0.3 <= reward <= 1.0, f"Expected full scoring range, got {reward}"
    print("✓ test_compute_reward_valid")


def test_compute_reward_wrong_duration():
    """Verify reward is partial credit when MIDI has wrong duration."""
    import pretty_midi
    midi = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)
    # Only 2 seconds - too short
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=2.0))
    midi.instruments.append(piano)

    reward = compute_reward(midi)
    # Partial credit: has notes (0.05) + log bonus (~0.03) = ~0.08
    assert 0.0 < reward <= 0.25, f"Expected partial credit, got {reward}"
    print("✓ test_compute_reward_wrong_duration")


def test_compute_reward_empty():
    """Verify reward is 0.0 when MIDI has no notes (no partial credit)."""
    import pretty_midi
    midi = pretty_midi.PrettyMIDI()

    reward = compute_reward(midi)
    assert reward == 0.0
    print("✓ test_compute_reward_empty")


def test_compute_reward_none():
    """Verify reward is 0.0 when MIDI is None."""
    reward = compute_reward(None)
    assert reward == 0.0
    print("✓ test_compute_reward_none")


def test_save_rollout():
    """Verify save_rollout creates expected files."""
    import pretty_midi
    import shutil

    # Create test MIDI
    midi = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
    midi.instruments.append(piano)

    scenario = JazzScenario(step=0, rollout_id=0)
    run_id = "test_run"

    rollout_dir = save_rollout(scenario, "# test code", midi, 1.0, run_id)

    assert rollout_dir.exists()
    assert (rollout_dir / "code.py").exists()
    assert (rollout_dir / "output.mid").exists()
    assert (rollout_dir / "meta.json").exists()

    # Cleanup
    shutil.rmtree(ARTIFACTS_DIR / run_id)
    print("✓ test_save_rollout")


def test_real_model_one_step():
    """Test 1 real training step with W&B serverless. Requires WANDB_API_KEY."""
    import os
    if not (os.environ.get("WANDB_API_KEY") or os.environ.get("WANDBAPIKEY")):
        print("⏭ test_real_model_one_step (skipped - no API key)")
        return

    summary = asyncio.run(train(num_steps=1, rollouts_per_step=2, dry_run=False))
    assert summary["num_steps"] == 1
    assert summary["total_rollouts"] == 2
    assert "run_id" in summary
    print("✓ test_real_model_one_step")


if __name__ == "__main__":
    test_dry_run_one_step()
    test_dry_run_multiple_steps()
    test_execute_midi_code_valid()
    test_execute_midi_code_with_markdown()
    test_execute_midi_code_invalid()
    test_compute_reward_valid()
    test_compute_reward_wrong_duration()
    test_compute_reward_empty()
    test_compute_reward_none()
    test_save_rollout()
    test_real_model_one_step()
    print("\nAll tests passed!")
