
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass (Marcus): Walking line, chromatic approaches
bass_notes = [
    (1.5, 45), (1.875, 46), (2.25, 47), (2.625, 49),
    (3.0, 50), (3.375, 51), (3.75, 52), (4.125, 53),
    (4.5, 51), (4.875, 50), (5.25, 49), (5.625, 47)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 62), (1.875, 67), (1.875, 71), (1.875, 74),
    (3.375, 62), (3.375, 67), (3.375, 71), (3.375, 74),
    (4.875, 62), (4.875, 67), (4.875, 71), (4.875, 74)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (1.5, 36), (1.875, 42), (2.25, 36), (2.625, 42),
    (3.0, 38), (3.375, 42), (3.75, 38), (4.125, 42),
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F major scale: F, G, A, Bb, B, C, D
# Motif: F - Bb - B - C (half note, quarter note, eighth note, eighth note)
sax_notes = [
    (1.5, 70), (2.0, 74), (2.25, 75), (2.5, 72)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Repeat motif with a twist at the end
# F - Bb - B - C (half note, quarter note, eighth note, eighth note)
sax_notes = [
    (3.0, 70), (3.5, 74), (3.75, 75), (4.0, 72)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Final motif with a resolution to F
sax_notes = [
    (4.5, 70), (5.0, 74), (5.25, 75), (5.5, 72)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
