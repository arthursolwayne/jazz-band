
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 2: Full ensemble enters
# Saxophone starts with a simple motif: F (78) -> A (90) -> C (60) -> Bb (70)
# Rest on beat 3, resolve on beat 4
sax_notes = [
    (1.5, 78), (1.875, 90), (2.25, 60), (2.625, 70)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1875))

# Bass: Walking line with chromatic approaches
# F (78) -> G (79) -> Ab (80) -> A (90) -> Bb (70) -> B (71) -> C (60) -> Db (61)
bass_notes = [
    (1.5, 78), (1.875, 79), (2.25, 80), (2.625, 90),
    (3.0, 70), (3.375, 71), (3.75, 60), (4.125, 61)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1875))

# Piano: 7th chords on 2 and 4
# F7 on beat 2 (F, A, C, Eb), G7 on beat 4 (G, B, D, F)
piano_notes = [
    (2.25, 78), (2.25, 90), (2.25, 60), (2.25, 64),
    (3.75, 79), (3.75, 82), (3.75, 62), (3.75, 78)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 3: Sax repeats motif with slight variation
sax_notes = [
    (3.0, 78), (3.375, 90), (3.75, 60), (4.125, 70)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1875))

# Bar 4: Sax resolves with a descending line
sax_notes = [
    (4.5, 70), (4.875, 60), (5.25, 62), (5.625, 59)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.1875))

# Drums continue: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bass continues with walking line
bass_notes = [
    (3.0, 62), (3.375, 60), (3.75, 61), (4.125, 59),
    (4.5, 60), (4.875, 62), (5.25, 63), (5.625, 61)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.1875))

# Piano continues with 7th chords on 2 and 4
piano_notes = [
    (4.125, 78), (4.125, 90), (4.125, 60), (4.125, 64),
    (5.625, 79), (5.625, 82), (5.625, 62), (5.625, 78)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
