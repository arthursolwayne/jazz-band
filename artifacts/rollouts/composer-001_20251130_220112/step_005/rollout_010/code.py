
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
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 36), (1.125, 42),
    (1.5, 38), (1.875, 42), (2.25, 38), (2.625, 42),
    (3.0, 36), (3.375, 42), (3.75, 36), (4.125, 42),
    (4.5, 38), (4.875, 42), (5.25, 38), (5.625, 42),
]

for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.125))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62), (1.875, 63), (2.25, 64), (2.625, 65),
    (3.0, 65), (3.375, 64), (3.75, 63), (4.125, 62),
    (4.5, 62), (4.875, 63), (5.25, 64), (5.625, 65),
    (6.0, 65), (6.375, 64), (6.75, 63), (7.125, 62)
]

for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.5, 67), (1.5, 71), (1.5, 74), (1.5, 76),
    (2.0, 67), (2.0, 71), (2.0, 74), (2.0, 76),
    # Bar 3
    (3.0, 65), (3.0, 69), (3.0, 72), (3.0, 76),
    (3.5, 65), (3.5, 69), (3.5, 72), (3.5, 76),
    # Bar 4
    (4.5, 67), (4.5, 71), (4.5, 74), (4.5, 76),
    (5.0, 67), (5.0, 71), (5.0, 74), (5.0, 76)
]

for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + 0.25))

# Sax: Motif - D (62), F# (66), B (71), leave it hanging on 71
sax_notes = [
    (1.5, 62), (1.5, 66), (1.5, 71),
    (2.5, 71)  # Leave it hanging here
]

for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
