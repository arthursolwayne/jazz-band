
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bass: Walking line with chromatic approaches
# Bar 2: D2 (D) -> C#2 (chromatic approach) -> F2 (F) -> E2 (chromatic approach)
bass_notes = [
    (1.5, 38), (1.75, 37), (2.0, 43), (2.25, 42)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicing, D7sus4 (D, G, A, C) on beat 2, resolving to D7 (D, F#, A, C) on beat 4
piano_notes = [
    (1.75, 62), (1.75, 67), (1.75, 69), (1.75, 64),  # D7sus4
    (2.0, 62), (2.0, 67), (2.0, 69), (2.0, 64),  # D7sus4
    (2.25, 62), (2.25, 67), (2.25, 69), (2.25, 64),  # D7sus4
    (2.5, 62), (2.5, 69), (2.5, 67), (2.5, 64)  # D7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Melody starts, haunting, incomplete
# Bar 2: D (D4) on beat 1, B (B4) on beat 2, A (A4) on beat 3, D (D4) on beat 4
sax_notes = [
    (1.5, 62), (2.0, 66), (2.25, 69), (2.5, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bass: Walking line with chromatic approaches
# Bar 3: G2 (G) -> F#2 (chromatic approach) -> A2 (A) -> G2 (chromatic approach)
bass_notes = [
    (3.0, 43), (3.25, 42), (3.5, 45), (3.75, 44)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicing, G7sus4 (G, C, D, F) on beat 2, resolving to G7 (G, B, D, F) on beat 4
piano_notes = [
    (3.25, 67), (3.25, 72), (3.25, 74), (3.25, 71),  # G7sus4
    (3.5, 67), (3.5, 72), (3.5, 74), (3.5, 71),  # G7sus4
    (3.75, 67), (3.75, 72), (3.75, 74), (3.75, 71),  # G7sus4
    (4.0, 67), (4.0, 76), (4.0, 74), (4.0, 71)  # G7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Melody continues, unresolved tension
# Bar 3: G (G4) on beat 1, E (E4) on beat 2, D (D4) on beat 3, G (G4) on beat 4
sax_notes = [
    (3.0, 67), (3.5, 64), (3.75, 62), (4.0, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bass: Walking line with chromatic approaches
# Bar 4: A2 (A) -> G#2 (chromatic approach) -> B2 (B) -> A2 (chromatic approach)
bass_notes = [
    (4.5, 45), (4.75, 44), (5.0, 47), (5.25, 46)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicing, A7sus4 (A, D, E, G) on beat 2, resolving to A7 (A, C#, E, G) on beat 4
piano_notes = [
    (4.75, 69), (4.75, 74), (4.75, 76), (4.75, 71),  # A7sus4
    (5.0, 69), (5.0, 74), (5.0, 76), (5.0, 71),  # A7sus4
    (5.25, 69), (5.25, 74), (5.25, 76), (5.25, 71),  # A7sus4
    (5.5, 69), (5.5, 74), (5.5, 76), (5.5, 71)  # A7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Sax: Melody ends, unresolved
# Bar 4: A (A4) on beat 1, F# (F#4) on beat 2, E (E4) on beat 3, A (A4) on beat 4
sax_notes = [
    (4.5, 69), (5.0, 66), (5.25, 64), (5.5, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write to file
# midi.write disabled
