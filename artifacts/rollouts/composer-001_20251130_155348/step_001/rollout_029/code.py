
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking in Fm, chromatic approach to Bb
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),   # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=6.0),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # Db
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # Db
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Saxophone - short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # B
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # B
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
