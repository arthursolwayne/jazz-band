
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
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 72), (1.875, 71), (2.25, 73), (2.625, 76),
    (3.0, 77), (3.375, 76), (3.75, 74), (4.125, 72),
    (4.5, 71), (4.875, 72), (5.25, 74), (5.625, 76)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.375))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 62), (1.875, 67), (1.875, 71), (1.875, 72),
    (2.625, 62), (2.625, 67), (2.625, 71), (2.625, 72),
    (3.375, 64), (3.375, 69), (3.375, 73), (3.375, 74),
    (4.125, 64), (4.125, 69), (4.125, 73), (4.125, 74)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (1.5, 65), (1.875, 67), (2.25, 69), (2.625, 67),
    (3.0, 65), (3.375, 67), (3.75, 69), (4.125, 67),
    (4.5, 65), (4.875, 67), (5.25, 69), (5.625, 67)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.375))

# Drums: continue for bars 2-4
for bar in range(2, 4):
    start = bar * 1.5
    drum_notes = [
        (start, 36), (start + 0.375, 42), (start + 0.75, 38), (start + 1.125, 42),
        (start + 1.5, 36), (start + 1.875, 42), (start + 2.25, 38), (start + 2.625, 42)
    ]
    for time, note in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
