
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
for time, note in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (1.5, 45), (1.75, 46), (2.0, 44), (2.25, 43),
    (2.5, 45), (2.75, 46), (3.0, 44), (3.25, 43)
]
for time, note in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 76),
    (2.0, 62), (2.0, 67), (2.0, 71), (2.0, 76),
    (2.5, 62), (2.5, 67), (2.5, 71), (2.5, 76),
    (3.0, 62), (3.0, 67), (3.0, 71), (3.0, 76)
]
for time, note in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Motif - starts on 1.5, ends on 2.0, leaves it hanging
sax_notes = [
    (1.5, 62), (1.625, 65), (1.75, 66), (2.0, 62),
    (2.25, 65), (2.5, 66), (2.75, 65), (3.0, 62)
]
for time, note in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (3.0, 45), (3.25, 46), (3.5, 44), (3.75, 43),
    (4.0, 45), (4.25, 46), (4.5, 44), (4.75, 43)
]
for time, note in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (3.0, 62), (3.0, 67), (3.0, 71), (3.0, 76),
    (3.5, 62), (3.5, 67), (3.5, 71), (3.5, 76),
    (4.0, 62), (4.0, 67), (4.0, 71), (4.0, 76),
    (4.5, 62), (4.5, 67), (4.5, 71), (4.5, 76)
]
for time, note in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Motif variation, continues the search
sax_notes = [
    (3.0, 65), (3.125, 66), (3.25, 67), (3.5, 65),
    (3.75, 66), (4.0, 67), (4.25, 66), (4.5, 65)
]
for time, note in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    (4.5, 45), (4.75, 46), (5.0, 44), (5.25, 43),
    (5.5, 45), (5.75, 46), (6.0, 44), (6.25, 43)
]
for time, note in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (4.5, 62), (4.5, 67), (4.5, 71), (4.5, 76),
    (5.0, 62), (5.0, 67), (5.0, 71), (5.0, 76),
    (5.5, 62), (5.5, 67), (5.5, 71), (5.5, 76),
    (6.0, 62), (6.0, 67), (6.0, 71), (6.0, 76)
]
for time, note in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25)
    piano.notes.append(note)

# Sax: Motif resolution, returns to the start and finishes it
sax_notes = [
    (4.5, 65), (4.625, 66), (4.75, 67), (5.0, 65),
    (5.25, 66), (5.5, 67), (5.75, 66), (6.0, 65)
]
for time, note in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.save('wayne_intro.mid')
