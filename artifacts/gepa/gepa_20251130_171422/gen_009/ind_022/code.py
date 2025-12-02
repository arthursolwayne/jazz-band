
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=85, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=85, pitch=74, start=1.875, end=2.25),  # D
    # D7 on beat 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=85, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=85, pitch=74, start=2.625, end=3.0),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax - Motif (start at 1.5s)
# D (62) -> Eb (63) -> F# (66) -> D (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=63, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=66, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # Db
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=85, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=85, pitch=74, start=3.375, end=3.75),  # D
    # D7 on beat 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=85, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=85, pitch=74, start=4.125, end=4.5),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Drum pattern same as bar 1
for note in drum_notes:
    # Offset by bar length (1.5s)
    new_start = note.start + 1.5
    new_end = note.end + 1.5
    drums.notes.append(pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=new_start, end=new_end))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),   # Db
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=85, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=85, pitch=74, start=4.875, end=5.25),  # D
    # D7 on beat 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=85, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=85, pitch=74, start=5.625, end=6.0),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Drum pattern same as bar 1
for note in drum_notes:
    # Offset by bar length (3.0s)
    new_start = note.start + 3.0
    new_end = note.end + 3.0
    drums.notes.append(pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=new_start, end=new_end))

# Sax - Motif again, with variation
# D (62) -> Eb (63) -> F# (66) -> D (62) -> Eb (63) -> F# (66) -> G (67)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=63, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=62, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=110, pitch=63, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=110, pitch=66, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.8125),
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
