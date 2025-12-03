
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.75, 40), (2.0, 38), (2.25, 41),
    (2.5, 39), (2.75, 41), (3.0, 39), (3.25, 40)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chords each bar, resolve on the last
# Bar 2: Fmaj7
piano_notes = [
    (1.5, 65), (1.5, 72), (1.5, 76), (1.5, 81),  # Fmaj7
    (1.75, 65), (1.75, 72), (1.75, 76), (1.75, 81),
    (2.0, 65), (2.0, 72), (2.0, 76), (2.0, 81),
    (2.25, 65), (2.25, 72), (2.25, 76), (2.25, 81)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Start motif (F - Bb - G - F)
sax_notes = [
    (1.5, 84), (1.75, 80), (2.0, 81), (2.25, 84)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3 (3.0 - 4.5s): Full quartet
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 39), (3.25, 41), (3.5, 39), (3.75, 40),
    (4.0, 38), (4.25, 40), (4.5, 38), (4.75, 41)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: A7sus4
piano_notes = [
    (3.0, 69), (3.0, 76), (3.0, 78), (3.0, 84),  # A7sus4
    (3.25, 69), (3.25, 76), (3.25, 78), (3.25, 84),
    (3.5, 69), (3.5, 76), (3.5, 78), (3.5, 84),
    (3.75, 69), (3.75, 76), (3.75, 78), (3.75, 84)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Repeat motif with small variation (F - Bb - G - F)
sax_notes = [
    (3.0, 84), (3.25, 80), (3.5, 81), (3.75, 84)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4 (4.5 - 6.0s): Full quartet
# Bass: Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 40), (4.75, 41), (5.0, 40), (5.25, 38),
    (5.5, 39), (5.75, 41), (6.0, 39), (6.25, 40)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: C7 (resolve)
piano_notes = [
    (4.5, 60), (4.5, 68), (4.5, 71), (4.5, 76),  # C7
    (4.75, 60), (4.75, 68), (4.75, 71), (4.75, 76),
    (5.0, 60), (5.0, 68), (5.0, 71), (5.0, 76),
    (5.25, 60), (5.25, 68), (5.25, 71), (5.25, 76)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: End motif (F - Bb - G - F)
sax_notes = [
    (4.5, 84), (4.75, 80), (5.0, 81), (5.25, 84)
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
# midi.write disabled
