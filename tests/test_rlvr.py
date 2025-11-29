"""Tests for RLVR training loop."""

import asyncio
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from rlvr.loop import train, execute_midi_code, save_rollout, JazzScenario, ARTIFACTS_DIR
from rlvr.eval import compute_reward


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
    midi, cleaned = execute_midi_code(code)
    assert midi is not None
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
    midi, cleaned = execute_midi_code(code)
    assert midi is not None
    print("✓ test_execute_midi_code_with_markdown")


def test_execute_midi_code_invalid():
    """Verify execute_midi_code handles invalid code."""
    code = "this is not valid python"
    midi, cleaned = execute_midi_code(code)
    assert midi is None
    print("✓ test_execute_midi_code_invalid")


def test_compute_reward_with_notes():
    """Verify reward is 1.0 when MIDI has notes."""
    import pretty_midi
    midi = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=0)
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=0.0, end=0.5))
    midi.instruments.append(piano)

    reward = compute_reward(midi)
    assert reward == 1.0
    print("✓ test_compute_reward_with_notes")


def test_compute_reward_empty():
    """Verify reward is -1.0 when MIDI has no notes."""
    import pretty_midi
    midi = pretty_midi.PrettyMIDI()

    reward = compute_reward(midi)
    assert reward == -1.0
    print("✓ test_compute_reward_empty")


def test_compute_reward_none():
    """Verify reward is -1.0 when MIDI is None."""
    reward = compute_reward(None)
    assert reward == -1.0
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


if __name__ == "__main__":
    test_dry_run_one_step()
    test_dry_run_multiple_steps()
    test_execute_midi_code_valid()
    test_execute_midi_code_with_markdown()
    test_execute_midi_code_invalid()
    test_compute_reward_with_notes()
    test_compute_reward_empty()
    test_compute_reward_none()
    test_save_rollout()
    print("\nAll tests passed!")
