
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
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Fm7 - Bb7 - Eb7 - Ab7 (roots & fifths with chromatic approaches)
bass_notes = [
    (1.5, 43), (1.75, 45), (2.0, 42), (2.25, 44),
    (2.5, 45), (2.75, 47), (3.0, 43), (3.25, 45)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb)
    (1.5, 65), (1.5, 63), (1.5, 60), (1.5, 57),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (2.5, 62), (2.5, 55), (2.5, 60), (2.5, 63),
    # Bar 4: Eb7 (Eb, G, Bb, D)
    (3.5, 62), (3.5, 65), (3.5, 62), (3.5, 58)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Motif (F, Ab, G, Eb) - short, sing, leave it hanging
sax_notes = [
    (1.5, 65), (1.75, 63), (2.0, 62), (2.25, 57)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line continues
bass_notes = [
    (3.5, 47), (3.75, 45), (4.0, 44), (4.25, 42),
    (4.5, 42), (4.75, 44), (5.0, 45), (5.25, 47)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, resolve on the last bar
piano_notes = [
    # Bar 3: Eb7 (Eb, G, Bb, D)
    (3.5, 62), (3.5, 65), (3.5, 62), (3.5, 58),
    # Bar 4: Ab7 (Ab, C, Eb, G)
    (4.5, 63), (4.5, 60), (4.5, 62), (4.5, 65)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.5, 36), (3.875, 42), (4.25, 36), (4.625, 42),
    (5.0, 38), (5.375, 42), (5.75, 38), (6.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Repeat motif with variation
sax_notes = [
    (3.75, 63), (4.0, 62), (4.25, 65), (4.5, 57)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line continues
bass_notes = [
    (5.5, 47), (5.75, 45), (6.0, 42), (6.25, 44)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Resolve on Ab7
piano_notes = [
    (5.5, 63), (5.5, 60), (5.5, 62), (5.5, 65)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Sax: Finish the motif with a resolution
sax_notes = [
    (5.5, 65), (5.75, 63), (6.0, 62), (6.25, 57)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
