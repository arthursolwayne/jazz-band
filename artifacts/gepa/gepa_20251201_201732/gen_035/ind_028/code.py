
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
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (1.5, 38), (1.75, 40), (2.0, 37), (2.25, 39),
    (2.5, 40), (2.75, 42), (3.0, 38), (3.25, 40)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (1.5, 44), (1.5, 47), (1.5, 50), (1.5, 59),  # Fm7
    (2.0, 47), (2.0, 50), (2.0, 53), (2.0, 62),  # Bb7
    (2.5, 46), (2.5, 49), (2.5, 52), (2.5, 60),  # Dm7
    (3.0, 43), (3.0, 47), (3.0, 50), (3.0, 60)   # Fm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: One short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    (1.5, 62), (1.75, 66), (2.0, 62), (2.25, 66),
    (2.5, 62), (2.75, 66), (3.0, 62), (3.25, 66)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (3.0, 38), (3.25, 40), (3.5, 37), (3.75, 39),
    (4.0, 40), (4.25, 42), (4.5, 38), (4.75, 40)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (3.0, 44), (3.0, 47), (3.0, 50), (3.0, 59),  # Fm7
    (3.5, 47), (3.5, 50), (3.5, 53), (3.5, 62),  # Bb7
    (4.0, 46), (4.0, 49), (4.0, 52), (4.0, 60),  # Dm7
    (4.5, 43), (4.5, 47), (4.5, 50), (4.5, 60)   # Fm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Continue motif, leave it hanging, come back and finish it
sax_notes = [
    (3.0, 62), (3.25, 66), (3.5, 62), (3.75, 66),
    (4.0, 62), (4.25, 66), (4.5, 62), (4.75, 66)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
bass_notes = [
    (4.5, 38), (4.75, 40), (5.0, 37), (5.25, 39),
    (5.5, 40), (5.75, 42), (6.0, 38), (6.25, 40)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    (4.5, 44), (4.5, 47), (4.5, 50), (4.5, 59),  # Fm7
    (5.0, 47), (5.0, 50), (5.0, 53), (5.0, 62),  # Bb7
    (5.5, 46), (5.5, 49), (5.5, 52), (5.5, 60),  # Dm7
    (6.0, 43), (6.0, 47), (6.0, 50), (6.0, 60)   # Fm7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Finish the motif
sax_notes = [
    (4.5, 62), (4.75, 66), (5.0, 62), (5.25, 66),
    (5.5, 62), (5.75, 66), (6.0, 62), (6.25, 66)
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
