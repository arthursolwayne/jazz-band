#!/usr/bin/env python
"""
MIDI Player Script

Plays MIDI files using FluidSynth via the midi2audio Python wrapper.

Usage:
    uv run python scripts/play_midi.py artifacts/session_000.mid
    uv run python scripts/play_midi.py artifacts/session_000.mid --soundfont path/to/soundfont.sf2
"""

import sys
import subprocess
from pathlib import Path
import tempfile
import argparse


def check_fluidsynth():
    """Check if FluidSynth is installed."""
    try:
        result = subprocess.run(
            ["fluidsynth", "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        return result.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def install_fluidsynth_instructions():
    """Print instructions for installing FluidSynth."""
    print("FluidSynth is not installed!")
    print()
    print("Install with Homebrew:")
    print("  brew install fluid-synth")
    print()
    print("Or download from: https://www.fluidsynth.org/")


def get_default_soundfont():
    """Get path to default soundfont, downloading if needed."""
    soundfont_dir = Path.home() / ".soundfonts"
    soundfont_path = soundfont_dir / "FluidR3Mono_GM.sf3"

    if soundfont_path.exists():
        return soundfont_path

    print(f"Soundfont not found at {soundfont_path}")
    print("Downloading default soundfont (one-time setup)...")

    soundfont_dir.mkdir(parents=True, exist_ok=True)

    # Download soundfont
    try:
        subprocess.run(
            [
                "curl", "-L", "-o", str(soundfont_path),
                "https://github.com/musescore/MuseScore/raw/2.3.2/share/sound/FluidR3Mono_GM.sf3"
            ],
            check=True,
            timeout=60
        )
        print(f"✓ Soundfont downloaded to {soundfont_path}")
        return soundfont_path
    except subprocess.CalledProcessError:
        print("Failed to download soundfont")
        return None


def play_midi_fluidsynth(midi_path: Path, soundfont_path: Path):
    """Play MIDI using FluidSynth directly."""
    print(f"Playing {midi_path} with FluidSynth...")
    print(f"Using soundfont: {soundfont_path}")
    print("(Press Ctrl+C to stop)")
    print()

    try:
        subprocess.run(
            [
                "fluidsynth",
                "-a", "coreaudio",  # macOS audio driver
                "-ni",              # Non-interactive mode (plays MIDI file and exits)
                str(soundfont_path),
                str(midi_path)
            ],
            check=True
        )
    except KeyboardInterrupt:
        print("\nPlayback stopped")
    except subprocess.CalledProcessError as e:
        print(f"Error playing MIDI: {e}")


def play_midi_midi2audio(midi_path: Path, soundfont_path: Path):
    """Play MIDI using midi2audio Python wrapper."""
    try:
        from midi2audio import FluidSynth
        import os

        print(f"Playing {midi_path} with midi2audio...")
        print(f"Using soundfont: {soundfont_path}")
        print()

        # Convert to temporary WAV file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_wav = tmp.name

        try:
            # Convert MIDI to WAV
            fs = FluidSynth(sound_font=str(soundfont_path))
            fs.midi_to_audio(str(midi_path), tmp_wav)

            # Play WAV with afplay (macOS)
            print("Playing audio...")
            subprocess.run(["afplay", tmp_wav], check=True)

        finally:
            # Clean up temporary file
            if os.path.exists(tmp_wav):
                os.remove(tmp_wav)

    except ImportError:
        print("midi2audio not installed. Install with: uv pip install midi2audio")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Play MIDI files")
    parser.add_argument("midi_file", type=Path, help="Path to MIDI file")
    parser.add_argument(
        "--soundfont", "-s",
        type=Path,
        help="Path to soundfont file (default: auto-download)"
    )
    parser.add_argument(
        "--method", "-m",
        choices=["direct", "python", "auto"],
        default="auto",
        help="Playback method (default: auto)"
    )

    args = parser.parse_args()

    # Check if MIDI file exists
    if not args.midi_file.exists():
        print(f"Error: MIDI file not found: {args.midi_file}")
        sys.exit(1)

    # Get soundfont
    if args.soundfont:
        soundfont_path = args.soundfont
        if not soundfont_path.exists():
            print(f"Error: Soundfont not found: {soundfont_path}")
            sys.exit(1)
    else:
        soundfont_path = get_default_soundfont()
        if soundfont_path is None:
            sys.exit(1)

    # Check if FluidSynth is installed
    has_fluidsynth = check_fluidsynth()

    # Choose playback method
    if args.method == "auto":
        method = "direct" if has_fluidsynth else "python"
    else:
        method = args.method

    # Play MIDI
    if method == "direct":
        if not has_fluidsynth:
            install_fluidsynth_instructions()
            sys.exit(1)
        play_midi_fluidsynth(args.midi_file, soundfont_path)
    else:
        play_midi_midi2audio(args.midi_file, soundfont_path)


if __name__ == "__main__":
    main()
