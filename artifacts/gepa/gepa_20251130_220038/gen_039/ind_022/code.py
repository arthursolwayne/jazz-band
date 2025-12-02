
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    (1.5, 50), (1.875, 49), (2.25, 51), (2.625, 50),
    (3.0, 48), (3.375, 47), (3.75, 49), (4.125, 50),
    (4.5, 51), (4.875, 50), (5.25, 48), (5.625, 47)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), (1.5, 67), (1.5, 71), (1.5, 65),
    (2.625, 62), (2.625, 67), (2.625, 71), (2.625, 65),
    (3.75, 62), (3.75, 67), (3.75, 71), (3.75, 65),
    (4.875, 62), (4.875, 67), (4.875, 71), (4.875, 65)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody in Dm (D, F, G, Bb)
sax_notes = [
    (1.5, 62), (1.75, 65), (1.9, 62), (2.0, 58),
    (2.5, 62), (2.75, 65), (2.9, 62), (3.0, 58),
    (3.5, 62), (3.75, 65), (3.9, 62), (4.0, 58),
    (4.5, 62), (4.75, 65), (4.9, 62), (5.0, 58)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.15))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
