
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking in Fm, chromatic approaches
bass_notes = [
    # Bar 2: Fm7 -> Bb
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.0),  # G
    # Bar 3: Bb7 -> Eb
    pretty_midi.Note(velocity=100, pitch=55, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=2.375, end=2.5),  # F
    # Bar 4: Eb7 -> Ab
    pretty_midi.Note(velocity=100, pitch=53, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=2.875, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping in Fm
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=1.75, end=2.0),  # Eb
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5),  # Eb
    # Bar 4: Eb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=51, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=46, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=2.75, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=50, start=2.75, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Fm motif, one short phrase, leave it hanging
sax_notes = [
    # Bar 2: D (Bb7) -> F (Fm7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    # Bar 3: G (Bb7)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G
    # Bar 4: F (Fm7), end on a question
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Drums continue with same pattern
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note.copy() for note in drum_notes])

# Bar 4: Drums continue with same pattern
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note.copy() for note in drum_notes])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
