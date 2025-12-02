
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 72), (1.75, 71), (2.0, 70), (2.25, 69),
    (2.5, 67), (2.75, 68), (3.0, 69), (3.25, 70)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.75, 64), (1.75, 69), (1.75, 71), (1.75, 74),
    (2.25, 64), (2.25, 69), (2.25, 71), (2.25, 74),
    (2.75, 64), (2.75, 69), (2.75, 71), (2.75, 74)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - F, G, Ab, Bb (F7 chord), leave it hanging
sax_notes = [
    (1.5, 65), (1.625, 66), (1.75, 67), (1.875, 68)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (3.0, 69), (3.25, 70), (3.5, 71), (3.75, 72),
    (4.0, 74), (4.25, 72), (4.5, 71), (4.75, 70)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (3.25, 64), (3.25, 69), (3.25, 71), (3.25, 74),
    (3.75, 64), (3.75, 69), (3.75, 71), (3.75, 74),
    (4.25, 64), (4.25, 69), (4.25, 71), (4.25, 74)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Continue motif, resolve on 4th beat
sax_notes = [
    (3.0, 68), (3.125, 67), (3.25, 66), (3.375, 65)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    (4.5, 70), (4.75, 71), (5.0, 72), (5.25, 74),
    (5.5, 72), (5.75, 71), (6.0, 70), (6.25, 69)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (4.75, 64), (4.75, 69), (4.75, 71), (4.75, 74),
    (5.25, 64), (5.25, 69), (5.25, 71), (5.25, 74),
    (5.75, 64), (5.75, 69), (5.75, 71), (5.75, 74)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Return to motif, end on Bb (F7 chord)
sax_notes = [
    (4.5, 65), (4.625, 66), (4.75, 67), (4.875, 68)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
