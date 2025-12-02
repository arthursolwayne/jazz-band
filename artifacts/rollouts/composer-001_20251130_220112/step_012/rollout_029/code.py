
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=110, pitch=36, start=0.0, end=0.375),    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),    # Hihat on 1
    pretty_midi.Note(velocity=110, pitch=36, start=0.75, end=1.125),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),    # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4 (1.5 - 6.0s)

# Sax: D (D4), F# (F#4), A (A4), C (C5) — triad with chromatic passing tone
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),    # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),    # F#4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),    # G4 (chromatic passing)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),    # A4
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=2.75),    # C5
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),    # B4 (chromatic passing)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),    # A4
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),    # Bb4 (chromatic passing)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),    # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),    # F#4
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),    # Bb4
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),    # A4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),    # Bb4
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),    # F#4
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),    # D4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),    # B4
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),    # A4
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),    # Bb4
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),    # D3
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0),    # E3
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),    # Eb3
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),    # F3
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.75),    # G3
    pretty_midi.Note(velocity=80, pitch=49, start=2.75, end=3.0),    # Gb3
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25),    # A3
    pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5),    # Bb3
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75),    # Ab3
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),    # Bb3
    pretty_midi.Note(velocity=80, pitch=55, start=4.0, end=4.25),    # C4
    pretty_midi.Note(velocity=80, pitch=54, start=4.25, end=4.5),    # B3
    pretty_midi.Note(velocity=80, pitch=52, start=4.5, end=4.75),    # A3
    pretty_midi.Note(velocity=80, pitch=50, start=4.75, end=5.0),    # G3
    pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25),    # F3
    pretty_midi.Note(velocity=80, pitch=46, start=5.25, end=5.5),    # Eb3
    pretty_midi.Note(velocity=80, pitch=50, start=5.5, end=5.75),    # G3
    pretty_midi.Note(velocity=80, pitch=52, start=5.75, end=6.0),    # A3
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=85, pitch=62, start=1.75, end=2.0),    # D4
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0),    # B4
    pretty_midi.Note(velocity=85, pitch=69, start=1.75, end=2.0),    # A4
    pretty_midi.Note(velocity=85, pitch=74, start=1.75, end=2.0),    # C#5
    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=85, pitch=62, start=2.75, end=3.0),    # D4
    pretty_midi.Note(velocity=85, pitch=67, start=2.75, end=3.0),    # B4
    pretty_midi.Note(velocity=85, pitch=69, start=2.75, end=3.0),    # A4
    pretty_midi.Note(velocity=85, pitch=74, start=2.75, end=3.0),    # C#5
    # Bar 4 (3.0 - 3.75s)
    pretty_midi.Note(velocity=85, pitch=62, start=3.5, end=3.75),    # D4
    pretty_midi.Note(velocity=85, pitch=67, start=3.5, end=3.75),    # B4
    pretty_midi.Note(velocity=85, pitch=69, start=3.5, end=3.75),    # A4
    pretty_midi.Note(velocity=85, pitch=74, start=3.5, end=3.75),    # C#5
    # Bar 4 (3.75 - 4.5s)
    pretty_midi.Note(velocity=85, pitch=62, start=4.25, end=4.5),    # D4
    pretty_midi.Note(velocity=85, pitch=67, start=4.25, end=4.5),    # B4
    pretty_midi.Note(velocity=85, pitch=69, start=4.25, end=4.5),    # A4
    pretty_midi.Note(velocity=85, pitch=74, start=4.25, end=4.5),    # C#5
    # Bar 4 (4.5 - 5.25s)
    pretty_midi.Note(velocity=85, pitch=62, start=5.0, end=5.25),    # D4
    pretty_midi.Note(velocity=85, pitch=67, start=5.0, end=5.25),    # B4
    pretty_midi.Note(velocity=85, pitch=69, start=5.0, end=5.25),    # A4
    pretty_midi.Note(velocity=85, pitch=74, start=5.0, end=5.25),    # C#5
    # Bar 4 (5.25 - 6.0s)
    pretty_midi.Note(velocity=85, pitch=62, start=5.75, end=6.0),    # D4
    pretty_midi.Note(velocity=85, pitch=67, start=5.75, end=6.0),    # B4
    pretty_midi.Note(velocity=85, pitch=69, start=5.75, end=6.0),    # A4
    pretty_midi.Note(velocity=85, pitch=74, start=5.75, end=6.0),    # C#5
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bars 2-4 (1.5 - 6.0s)
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.125),# Hihat on 3
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=36, start=2.25, end=2.625), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.75),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.875),# Hihat on 3
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.5),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.625),# Hihat on 3
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=36, start=3.75, end=4.125), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.25),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.375),# Hihat on 3
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.125),# Hihat on 3
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=36, start=5.25, end=5.625), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.75),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.875),# Hihat on 3
    # Final hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.875, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
