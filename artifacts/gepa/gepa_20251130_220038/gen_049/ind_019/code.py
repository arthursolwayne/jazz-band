
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5)
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.0, end=2.125),  # A#
    pretty_midi.Note(velocity=100, pitch=71, start=2.125, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=100, pitch=73, start=2.375, end=2.5),  # C#
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=77, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=78, start=2.875, end=3.0),  # F#
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (F7: F A C E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.0),
    # Bar 2, beat 4 (F7 again)
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=2.75),
    # Bar 3, beat 2 (F7 again)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.5),
    # Bar 3, beat 4 (F7 again)
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=76, start=4.125, end=4.25),
    # Bar 4, beat 2 (F7 again)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.0),
    # Bar 4, beat 4 (F7 again)
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=5.75),
]

piano.notes.extend(piano_notes)

# Sax: Melody (Bar 2, 1st 4 notes)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=2.375, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=3.625, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=4.375, end=4.5),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=5.125, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=76, start=5.375, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.875, end=6.0),  # A
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums: same pattern as bar 1
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

# Bass: Walking line in F
for note in bass_notes:
    note.start += 1.5
    note.end += 1.5
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
for note in piano_notes:
    note.start += 1.5
    note.end += 1.5
    piano.notes.append(note)

# Sax: Melody (Bar 3, 1st 4 notes)
for note in sax_notes:
    note.start += 1.5
    note.end += 1.5
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: same pattern as bar 1
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Bass: Walking line in F
for note in bass_notes:
    note.start += 3.0
    note.end += 3.0
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
for note in piano_notes:
    note.start += 3.0
    note.end += 3.0
    piano.notes.append(note)

# Sax: Melody (Bar 4, 1st 4 notes)
for note in sax_notes:
    note.start += 3.0
    note.end += 3.0
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
