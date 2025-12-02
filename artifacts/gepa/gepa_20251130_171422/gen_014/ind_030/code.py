
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line with chromatic approaches
bass_notes = [
    (1.5, 69), (1.75, 70), (2.0, 71), (2.25, 72),
    (2.5, 71), (2.75, 70), (3.0, 69), (3.25, 68)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (1.75, 64), (1.75, 67), (1.75, 71), (1.75, 72),  # D7
    (2.25, 64), (2.25, 67), (2.25, 71), (2.25, 72),  # D7
    (2.75, 64), (2.75, 67), (2.75, 71), (2.75, 72),  # D7
    (3.25, 64), (3.25, 67), (3.25, 71), (3.25, 72)   # D7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: Melody with tension and space
sax_notes = [
    (1.5, 62), (1.75, 65), (2.0, 67), (2.25, 65),
    (2.5, 64), (2.75, 62), (3.0, 65), (3.25, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line with chromatic approaches
bass_notes = [
    (3.0, 68), (3.25, 69), (3.5, 71), (3.75, 72),
    (4.0, 71), (4.25, 70), (4.5, 69), (4.75, 68)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (3.25, 64), (3.25, 67), (3.25, 71), (3.25, 72),  # D7
    (3.75, 64), (3.75, 67), (3.75, 71), (3.75, 72),  # D7
    (4.25, 64), (4.25, 67), (4.25, 71), (4.25, 72),  # D7
    (4.75, 64), (4.75, 67), (4.75, 71), (4.75, 72)   # D7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: Melody with tension and space
sax_notes = [
    (3.0, 65), (3.25, 67), (3.5, 69), (3.75, 67),
    (4.0, 65), (4.25, 64), (4.5, 67), (4.75, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line with chromatic approaches
bass_notes = [
    (4.5, 68), (4.75, 69), (5.0, 71), (5.25, 72),
    (5.5, 71), (5.75, 70), (6.0, 68), (6.25, 67)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords on 2 and 4
piano_notes = [
    (4.75, 64), (4.75, 67), (4.75, 71), (4.75, 72),  # D7
    (5.25, 64), (5.25, 67), (5.25, 71), (5.25, 72),  # D7
    (5.75, 64), (5.75, 67), (5.75, 71), (5.75, 72),  # D7
    (6.25, 64), (6.25, 67), (6.25, 71), (6.25, 72)   # D7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: Melody with tension and space
sax_notes = [
    (4.5, 67), (4.75, 69), (5.0, 71), (5.25, 69),
    (5.5, 67), (5.75, 65), (6.0, 67), (6.25, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
