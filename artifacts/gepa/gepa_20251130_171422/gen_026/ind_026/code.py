
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Saxophone motif: Fm, concise and emotive
sax_notes = [
    # Bar 2: Fm, Gb, Ab, Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=2.625, end=3.0),  # Bb

    # Bar 3: Fm, Eb, D, C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # C

    # Bar 4: Fm, Gb, Ab, Bb (return to motif)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # Ab
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: chromatic, melodic, active
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=70, pitch=55, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=70, pitch=56, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=70, pitch=57, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=70, pitch=58, start=2.625, end=3.0),   # D#

    # Bar 3
    pretty_midi.Note(velocity=70, pitch=59, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=70, pitch=60, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=70, pitch=61, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=70, pitch=62, start=4.125, end=4.5),   # F#

    # Bar 4
    pretty_midi.Note(velocity=70, pitch=63, start=4.5, end=4.875),  # Gb
    pretty_midi.Note(velocity=70, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=70, pitch=65, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=70, pitch=66, start=5.625, end=6.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2 (2.25s)
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # Gb
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),  # C

    # Bar 3: Fm7 on beat 2 (3.75s)
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125),  # C

    # Bar 4: Fm7 on beat 2 (5.25s)
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),  # Gb
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # C
]

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
