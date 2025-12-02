
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
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.75),   # Hihat on 1 and 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.875), # Hihat on 3 and 4
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25), # Hihat on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approaches
# C7 -> Bb -> B -> C
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625), # C7
    pretty_midi.Note(velocity=90, pitch=64, start=1.625, end=1.75), # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875), # B
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0), # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (comping)
# Bar 2: F7 (F, A, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=71, start=1.75, end=2.0), # F7 (F)
    pretty_midi.Note(velocity=85, pitch=76, start=1.75, end=2.0), # A
    pretty_midi.Note(velocity=85, pitch=78, start=1.75, end=2.0), # C
    pretty_midi.Note(velocity=85, pitch=74, start=1.75, end=2.0), # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif (F, Bb, C, rest)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125), # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approaches (G7 -> F -> F# -> G)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125), # G7
    pretty_midi.Note(velocity=90, pitch=60, start=3.125, end=3.25), # F
    pretty_midi.Note(velocity=90, pitch=61, start=3.25, end=3.375), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.5), # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (comping)
# Bar 3: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=73, start=3.25, end=3.5), # G7 (G)
    pretty_midi.Note(velocity=85, pitch=78, start=3.25, end=3.5), # B
    pretty_midi.Note(velocity=85, pitch=76, start=3.25, end=3.5), # D
    pretty_midi.Note(velocity=85, pitch=74, start=3.25, end=3.5), # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif continuation (G, F#, rest, rest)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25), # G
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.5), # F#
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approaches (A7 -> G -> G# -> A)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.625), # A7
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.75), # G
    pretty_midi.Note(velocity=90, pitch=68, start=4.75, end=4.875), # G#
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0), # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (comping)
# Bar 4: A7 (A, C#, E, G)
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=74, start=4.75, end=5.0), # A7 (A)
    pretty_midi.Note(velocity=85, pitch=79, start=4.75, end=5.0), # C#
    pretty_midi.Note(velocity=85, pitch=81, start=4.75, end=5.0), # E
    pretty_midi.Note(velocity=85, pitch=76, start=4.75, end=5.0), # G
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: motif again (A, G#, rest, rest)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75), # A
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0), # G#
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),   # Hihat on 1 and 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=6.0),   # Hihat on 3 and 4
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('wayne_intro.mid')
