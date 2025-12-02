
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass line (walking, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G#
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: F7
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),   # B
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),   # D
    # Bar 3: B7
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),   # B
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),   # D#
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),   # F#
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),   # A
    # Bar 4: F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax melody (short motif, singable, leaves it hanging)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # A (resolve)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # B (leave it hanging)
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C#
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # C (resolve)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),   # B (leave it hanging)
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums (same pattern)
for note in drum_notes:
    new_start = note.start + 1.5
    new_end = note.end + 1.5
    new_note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=new_start, end=new_end)
    drums.notes.append(new_note)

# Bar 4: Drums (same pattern)
for note in drum_notes:
    new_start = note.start + 3.0
    new_end = note.end + 3.0
    new_note = pretty_midi.Note(velocity=note.velocity, pitch=note.pitch, start=new_start, end=new_end)
    drums.notes.append(new_note)

# Bar 3: Bass (walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # D
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 4: Bass (walking line)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),   # A
]

for note in bass_notes:
    bass.notes.append(note)

# Bar 3: Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 3: B7
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),   # B
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),   # D#
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),   # F#
    pretty_midi.Note(velocity=90, pitch=81, start=3.0, end=3.375),   # A
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 4: F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),   # D
]

for note in piano_notes:
    piano.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
