
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking, chromatic approaches)
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5),  # G#
    pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=3.0),  # A#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=100, pitch=56, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=100, pitch=58, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.25, end=4.5),  # D#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # G#
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # A (F7)
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # C (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G (Bb7)
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.25),  # D (Bb7)
    pretty_midi.Note(velocity=100, pitch=73, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A (F7)
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # C (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G
]
piano.notes.extend(piano_notes)

# Dante - Sax (melody in bar 2, 1 short motif, make it sing)
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.875, end=3.0),  # E
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=3.125, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.625),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=3.875, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.375),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=68, start=4.625, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.125),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=5.375, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=5.875),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=6.0, end=6.125),  # F
]
sax.notes.extend(sax_notes)

# Drums continue with same pattern for bars 2-4
for i in range(2):
    for note in drum_notes:
        note.start += 1.5
        note.end += 1.5
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_piece.mid")
