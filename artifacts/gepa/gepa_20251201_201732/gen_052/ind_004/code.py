
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: one short motif, make it sing. Start it, leave it hanging.

# Dm7 -> G7 -> Cm7 -> F7
# Sax: D, F, C, E, D
sax_notes = [
    (1.5, 62), (1.625, 65), (1.75, 60), (1.875, 64), (2.0, 62)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Bass: walking line, roots and fifths with chromatic approaches
# D2 -> F2 -> C2 -> E2 -> D2
bass_notes = [
    (1.5, 38), (1.75, 40), (2.0, 36), (2.25, 39), (2.5, 38)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (1.5, 62), (1.5, 65), (1.5, 69), (1.5, 67)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=1.5, end=1.75))

# Bar 3: G7 (G, B, D, F)
piano_notes = [
    (2.0, 67), (2.0, 71), (2.0, 69), (2.0, 65)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=2.0, end=2.25))

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    (2.5, 60), (2.5, 63), (2.5, 67), (2.5, 62)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=2.5, end=2.75))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but with variation, leave it hanging again
sax_notes = [
    (3.0, 62), (3.125, 65), (3.25, 60), (3.375, 64), (3.5, 62)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Bass: walking line, roots and fifths with chromatic approaches
# D2 -> F2 -> C2 -> E2 -> D2
bass_notes = [
    (3.0, 38), (3.25, 40), (3.5, 36), (3.75, 39), (4.0, 38)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Dm7 (D, F, A, C)
piano_notes = [
    (3.0, 62), (3.0, 65), (3.0, 69), (3.0, 67)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.0, end=3.25))

# Bar 4: G7 (G, B, D, F)
piano_notes = [
    (3.5, 67), (3.5, 71), (3.5, 69), (3.5, 65)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=3.5, end=3.75))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Complete the motif, resolve on the last note
sax_notes = [
    (4.5, 62), (4.625, 65), (4.75, 60), (4.875, 64), (5.0, 62)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Bass: walking line, roots and fifths with chromatic approaches
# D2 -> F2 -> C2 -> E2 -> D2
bass_notes = [
    (4.5, 38), (4.75, 40), (5.0, 36), (5.25, 39), (5.5, 38)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    (4.5, 60), (4.5, 63), (4.5, 67), (4.5, 62)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=4.5, end=4.75))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Add instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
