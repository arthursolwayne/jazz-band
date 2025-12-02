
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.0),   # D#
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.375),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.375, end=2.5),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, B)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),
    # Bar 3: E7 (E, G#, D)
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.75),
    # Bar 4: A7 (A, C#, G)
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=71, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=67, start=3.5, end=3.75),
]
piano.notes.extend(piano_notes)

# Sax: Motif (starts on bar 2, ends on bar 4)
sax_notes = [
    # Bar 2: C - E - B (short motif)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    # Bar 3: Rest
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),  # C again, but delayed
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),
    # Bar 4: C - E - B (variation)
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=64, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file to disk
midi.write("wayne_intro.mid")
