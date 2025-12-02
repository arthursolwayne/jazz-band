
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # Fm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Fm7 (rest after)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=75, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=75, pitch=47, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=75, pitch=49, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=75, pitch=50, start=2.25, end=2.5),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: Cm7 (Fm7's 5th chord)
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    # Bar 2, beat 4: Dm7 (Fm7's 9th chord)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # Fm7
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # Fm7 (rest after)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=75, pitch=50, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=75, pitch=48, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=75, pitch=47, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=75, pitch=49, start=3.75, end=4.0),  # F#
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2: Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F
    # Bar 3, beat 4: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a question
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # Fm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # Fm7
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=75, pitch=49, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=75, pitch=50, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=75, pitch=48, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=75, pitch=47, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=75, pitch=49, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=75, pitch=50, start=5.75, end=6.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2: Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    # Bar 4, beat 4: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.75),  # B
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Add additional drum patterns for bar 3 and 4
# Bar 3: Same drum pattern but with more energy
for note in drum_notes:
    note.start += 1.5
    note.end += 1.5
    drums.notes.append(note)

# Bar 4: Same drum pattern but with more energy
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("intro.mid")
