
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    (1.5, 70), (1.75, 69), (2.0, 71), (2.25, 72)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (1.75, 72), (1.75, 74), (1.75, 76), (1.75, 77),
    (2.25, 72), (2.25, 74), (2.25, 76), (2.25, 77)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: motif on D (C# is leading tone, D is resolution)
sax_notes = [
    (1.5, 62), (1.75, 61), (2.0, 62), (2.25, 64)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Everyone in (3.0 - 4.5s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    (3.0, 72), (3.25, 71), (3.5, 70), (3.75, 69)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (3.25, 72), (3.25, 74), (3.25, 76), (3.25, 77),
    (3.75, 72), (3.75, 74), (3.75, 76), (3.75, 77)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: motif continuation
sax_notes = [
    (3.0, 62), (3.25, 61), (3.5, 62), (3.75, 64)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: same pattern
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Everyone in (4.5 - 6.0s)
# Bass line: walking line with chromatic approaches
bass_notes = [
    (4.5, 69), (4.75, 70), (5.0, 72), (5.25, 74)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (4.75, 72), (4.75, 74), (4.75, 76), (4.75, 77),
    (5.25, 72), (5.25, 74), (5.25, 76), (5.25, 77)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: motif conclusion
sax_notes = [
    (4.5, 62), (4.75, 61), (5.0, 62), (5.25, 64)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: same pattern
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42),
    (6.0, 36), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
