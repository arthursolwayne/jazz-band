
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Bass: Walking line in Fm
bass_notes = [
    (1.5, 64), (1.875, 63), (2.25, 62), (2.625, 60),
    (3.0, 62), (3.375, 61), (3.75, 60), (4.125, 59)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 64), (1.5, 67), (1.5, 69), (1.5, 71),
    (2.625, 64), (2.625, 67), (2.625, 69), (2.625, 71),
    (3.0, 64), (3.0, 67), (3.0, 69), (3.0, 71),
    (4.125, 64), (4.125, 67), (4.125, 69), (4.125, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Sax: Melody - start with a whisper, build to a cry
sax_notes = [
    (1.5, 62), (1.875, 64), (2.25, 62), (2.625, 64),
    (3.0, 62), (3.375, 64), (3.75, 62), (4.125, 64),
    (4.5, 62), (4.875, 64), (5.25, 62), (5.625, 64)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm
bass_notes = [
    (3.0, 64), (3.375, 63), (3.75, 62), (4.125, 60),
    (4.5, 62), (4.875, 61), (5.25, 60), (5.625, 59)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (3.0, 64), (3.0, 67), (3.0, 69), (3.0, 71),
    (4.125, 64), (4.125, 67), (4.125, 69), (4.125, 71),
    (4.5, 64), (4.5, 67), (4.5, 69), (4.5, 71),
    (5.625, 64), (5.625, 67), (5.625, 69), (5.625, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Sax: Melody - continue with tension
sax_notes = [
    (3.0, 62), (3.375, 64), (3.75, 62), (4.125, 64),
    (4.5, 62), (4.875, 64), (5.25, 62), (5.625, 64),
    (6.0, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm
bass_notes = [
    (4.5, 64), (4.875, 63), (5.25, 62), (5.625, 60)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (4.5, 64), (4.5, 67), (4.5, 69), (4.5, 71),
    (5.625, 64), (5.625, 67), (5.625, 69), (5.625, 71)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Sax: Melody - resolve with something unexpected
sax_notes = [
    (4.5, 62), (4.875, 64), (5.25, 62), (5.625, 64),
    (6.0, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.125))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_in_Fm.mid")
