
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on Dm7
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # C
    # Bar 3: Dm7 again
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # C
]
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start motif (E, F#, D)
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D
    # Bar 3: Repeat first two notes
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # F#
    # Bar 4: Finish it with a resolution to C
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # C
]
sax.notes.extend(sax_notes)

# Bar 3: Drums (3.0 - 4.5s)
# Same pattern as bar 1, shifted forward
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
drums.notes.extend([note for note in drum_notes])

# Bar 4: Drums (4.5 - 6.0s)
# Same pattern as bar 1, shifted forward again
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
drums.notes.extend([note for note in drum_notes])

# Bar 4: Bass (4.5 - 6.0s)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (4.5 - 6.0s)
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Sax (4.5 - 6.0s)
sax_notes = [
    # Finish with a high C
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
