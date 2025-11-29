"""Open a MIDI file in GarageBand."""

import sys
import subprocess
from pathlib import Path


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run python -m rlvr.play <midi_file>")
        print("       uv run python -m rlvr.play artifacts/rollouts/<run_id>/step_000/rollout_000/output.mid")
        sys.exit(1)

    midi_path = Path(sys.argv[1])
    if not midi_path.exists():
        print(f"File not found: {midi_path}")
        sys.exit(1)

    print(f"Opening in GarageBand: {midi_path}")
    subprocess.run(["open", "-a", "GarageBand", str(midi_path)])


if __name__ == "__main__":
    main()
