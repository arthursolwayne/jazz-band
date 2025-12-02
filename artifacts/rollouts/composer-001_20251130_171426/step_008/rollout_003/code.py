
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 64), (1.75, 65), (2.0, 63), (2.25, 62),  # F -> Gb -> E -> D
    (2.5, 60), (2.75, 61), (3.0, 59), (3.25, 58),  # C -> C# -> B -> A
    (3.5, 64), (3.75, 65), (4.0, 63), (4.25, 62),  # F -> Gb -> E -> D
    (4.5, 60), (4.75, 61), (5.0, 59), (5.25, 58)   # C -> C# -> B -> A
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 64), (2.0, 67), (2.0, 71), (2.0, 72),  # F7
    # Bar 3
    (3.5, 64), (3.5, 67), (3.5, 71), (3.5, 72),  # F7
    # Bar 4
    (5.0, 64), (5.0, 67), (5.0, 71), (5.0, 72)   # F7
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: Motif in Fm, short and singable
sax_notes = [
    (2.0, 64), (2.25, 66), (2.5, 64), (2.75, 67),  # F -> G -> F -> G#
    (3.0, 64), (3.25, 66), (3.5, 64), (3.75, 67),  # F -> G -> F -> G#
    (4.0, 64), (4.25, 66), (4.5, 64), (4.75, 67),  # F -> G -> F -> G#
    (5.0, 64), (5.25, 66), (5.5, 64), (5.75, 67)   # F -> G -> F -> G#
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start_time = bar * 1.5
    for i in range(4):
        time = start_time + i * 0.375
        if i == 0 or i == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        elif i == 1 or i == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
