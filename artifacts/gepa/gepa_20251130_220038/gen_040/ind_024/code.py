
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: Dm7 -> F -> Bb -> C (whisper)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # C
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm (D -> C -> Bb -> A)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.5),  # A
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: F -> G -> A -> Bb (cry)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm (G -> F -> Eb -> D)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: Bb -> C -> D -> Eb (resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.5),  # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm (C -> Bb -> A -> G)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 on beat 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
