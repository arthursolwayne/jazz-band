
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),  # Bar 1
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42),  # Bar 2
    (3.0, 36), (3.375, 42), (3.75, 38), (4.125, 42),  # Bar 3
    (4.5, 36), (4.875, 42), (5.25, 38), (5.625, 42)   # Bar 4
]
for start, note in drum_notes:
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    drums.notes.append(dr)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 60), (1.875, 61), (2.25, 62), (2.625, 63),
    (3.0, 63), (3.375, 62), (3.75, 61), (4.125, 60),
    (4.5, 60), (4.875, 61), (5.25, 62), (5.625, 63)
]
for start, note in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    bass.notes.append(n)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (1.875, 60), (1.875, 64), (1.875, 67), (1.875, 71),
    # Bar 3
    (3.375, 60), (3.375, 64), (3.375, 67), (3.375, 71),
    # Bar 4
    (4.875, 60), (4.875, 64), (4.875, 67), (4.875, 71)
]
for start, note in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    piano.notes.append(n)

# Sax: Motif in C, simple and haunting
sax_notes = [
    (1.5, 62), (1.875, 64), (2.25, 62), (2.625, 60),
    (3.0, 62), (3.375, 64), (3.75, 62), (4.125, 60),
    (4.5, 62), (4.875, 64), (5.25, 62), (5.625, 60)
]
for start, note in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + 0.375)
    sax.notes.append(n)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
