
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with subtle dynamics and space
drum_notes = [
    # Kick on 1 (0.0s)
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    # Snare on 2 (0.75s)
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.5),
    # Kick on 3 (1.125s)
    pretty_midi.Note(velocity=75, pitch=36, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full Quartet (1.5 - 3.0s)

# Saxophone: Melodic motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # Fm7
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),  # A (resolve)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Chromatic walking line, melodic
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=2.0, end=2.125),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=2.375, end=2.5),  # Gb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.625),  # F7
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.625),
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.625),
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=1.875),  # F7 (2nd beat)
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=95, pitch=69, start=1.75, end=1.875),
    pretty_midi.Note(velocity=95, pitch=71, start=1.75, end=1.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full Quartet (3.0 - 4.5s)

# Saxophone: Repeat and expand the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.875, end=4.0),  # Gb (deviate slightly)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Chromatic line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.125),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.5),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=3.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=3.875, end=4.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.125),  # F7
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=71, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.375),  # F7 (2nd beat)
    pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=95, pitch=69, start=3.25, end=3.375),
    pretty_midi.Note(velocity=95, pitch=71, start=3.25, end=3.375),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full Quartet (4.5 - 6.0s)

# Saxophone: Motif again, with a slight modulation to Gbm
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.375, end=5.5),  # Gb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Chromatic line continues
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.625),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=4.875),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=5.125, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.375),  # E
    pretty_midi.Note(velocity=90, pitch=47, start=5.375, end=5.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.625),  # F7
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.625),
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.625),
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.625),
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=4.875),  # F7 (2nd beat)
    pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=95, pitch=69, start=4.75, end=4.875),
    pretty_midi.Note(velocity=95, pitch=71, start=4.75, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 (4.5s)
    pretty_midi.Note(velocity=85, pitch=36, start=4.5, end=4.875),
    # Snare on 2 (5.25s)
    pretty_midi.Note(velocity=95, pitch=38, start=5.25, end=5.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=65, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=65, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=65, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=65, pitch=42, start=5.625, end=6.0),
    # Kick on 3 (5.625s)
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
