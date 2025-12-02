
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
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 2: Full quartet (1.5s - 3.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 62), (1.75, 63), (2.0, 64), (2.25, 62),
    (2.5, 60), (2.75, 61), (3.0, 62), (3.25, 63)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, measure 1
    (1.75, 71), (1.75, 74), (1.75, 77), (1.75, 81),
    # Bar 2, measure 2
    (2.25, 71), (2.25, 74), (2.25, 77), (2.25, 81),
    # Bar 2, measure 3
    (2.75, 71), (2.75, 74), (2.75, 77), (2.75, 81),
    # Bar 2, measure 4
    (3.25, 71), (3.25, 74), (3.25, 77), (3.25, 81)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - start it, leave it hanging
sax_notes = [
    (1.5, 62), (1.625, 67), (1.75, 65), (1.875, 62),
    (2.0, 62), (2.125, 67), (2.25, 65), (2.375, 62),
    (2.5, 62), (2.625, 67), (2.75, 65), (2.875, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 3: Full quartet (3.0s - 4.5s)

# Bass: Walking line
bass_notes = [
    (3.0, 62), (3.25, 64), (3.5, 65), (3.75, 67),
    (4.0, 65), (4.25, 64), (4.5, 62), (4.75, 60)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, measure 1
    (3.25, 71), (3.25, 74), (3.25, 77), (3.25, 81),
    # Bar 3, measure 2
    (3.75, 71), (3.75, 74), (3.75, 77), (3.75, 81),
    # Bar 3, measure 3
    (4.25, 71), (4.25, 74), (4.25, 77), (4.25, 81),
    # Bar 3, measure 4
    (4.75, 71), (4.75, 74), (4.75, 77), (4.75, 81)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - continue and resolve
sax_notes = [
    (3.0, 62), (3.125, 67), (3.25, 65), (3.375, 62),
    (3.5, 62), (3.625, 67), (3.75, 65), (3.875, 62),
    (4.0, 62), (4.125, 67), (4.25, 65), (4.375, 62),
    (4.5, 62), (4.625, 67), (4.75, 65), (4.875, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bar 4: Full quartet (4.5s - 6.0s)

# Bass: Walking line
bass_notes = [
    (4.5, 62), (4.75, 64), (5.0, 65), (5.25, 67),
    (5.5, 65), (5.75, 64), (6.0, 62), (6.25, 60)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, measure 1
    (4.75, 71), (4.75, 74), (4.75, 77), (4.75, 81),
    # Bar 4, measure 2
    (5.25, 71), (5.25, 74), (5.25, 77), (5.25, 81),
    # Bar 4, measure 3
    (5.75, 71), (5.75, 74), (5.75, 77), (5.75, 81),
    # Bar 4, measure 4
    (6.25, 71), (6.25, 74), (6.25, 77), (6.25, 81)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.25))

# Sax: Motif - resolve and end
sax_notes = [
    (4.5, 62), (4.625, 67), (4.75, 65), (4.875, 62),
    (5.0, 62), (5.125, 67), (5.25, 65), (5.375, 62),
    (5.5, 62), (5.625, 67), (5.75, 65), (5.875, 62),
    (6.0, 62), (6.125, 67), (6.25, 65), (6.375, 62)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Drums: Bar 4
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
