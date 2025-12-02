
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in - sax melody
# Fm scale: F, Gb, Ab, A, Bb, C, Db
# Motif: F, Ab, Bb, C, Ab, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (tenor sax is transposed)
    pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: walking line in Fm
# F, Gb, Ab, A, Bb, C, Db, Eb
# Bars 2-4
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125), # Db
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),  # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Fm7 on 2, Ab7 on 4
piano_notes = [
    # Fm7: F, Ab, Bb, Db
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # Db
    # Ab7: Ab, C, Eb, Gb
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # Gb
]

for note in piano_notes:
    piano.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
