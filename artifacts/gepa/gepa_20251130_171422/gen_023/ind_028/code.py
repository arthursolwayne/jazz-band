
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
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 65), (1.875, 66), (2.25, 67), (2.625, 64),
    (3.0, 62), (3.375, 63), (3.75, 64), (4.125, 61),
    (4.5, 60), (4.875, 61), (5.25, 62), (5.625, 63)
]
for start, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + 0.375))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.25, 64), (2.25, 69), (2.25, 71), (2.25, 76),
    # Bar 3
    (3.75, 64), (3.75, 69), (3.75, 71), (3.75, 76),
    # Bar 4
    (5.25, 64), (5.25, 69), (5.25, 71), (5.25, 76)
]
for start, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for start, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375))

# Dante: Tenor sax. One short motif, make it sing.
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    (1.5, 69), (1.75, 71), (2.0, 72), 
    # Bar 3
    (3.0, 69), (3.25, 71), 
    # Bar 4
    (4.5, 72), (4.75, 71), (5.0, 69)
]
for start, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("waynes_moment.mid")
