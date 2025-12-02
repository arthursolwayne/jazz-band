
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=59, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line - walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=1.625, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=1.875, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=55, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=80, pitch=60, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.875, end=3.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # D
    # Bar 3: E7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=68, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),  # F#
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Drums continue
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Continue rhythm, add sax resolution
# Sax resolves the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bass continues walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5),  # Db
    pretty_midi.Note(velocity=80, pitch=74, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=3.625, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=77, start=3.75, end=3.875),  # F#
    pretty_midi.Note(velocity=80, pitch=79, start=3.875, end=4.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 4: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Drums end on beat 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
