
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Piano: Dm7 (F, A, C, D) on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # D

    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Bass: Walking line in Dm (D, C, Bb, A)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # A

    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Sax: Motif (D, F, G, Bb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Piano: Dm7 again on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # D

    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.375),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.375),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.375),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.375),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Bass: Walking line in Dm (D, C, Bb, A)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # A

    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.5),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Sax: Motif repeats with variation (D, F#, A, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Piano: Dm7 again on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # D

    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.875),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=5.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Bass: Walking line in Dm (D, C, Bb, A)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),  # A

    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=5.875),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Sax: Motif resolves with a minor 3rd (D, F, G, Bb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Continue pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),

    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
