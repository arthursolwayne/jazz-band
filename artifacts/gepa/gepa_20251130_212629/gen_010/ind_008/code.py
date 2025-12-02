
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches
# F7 chord: F, A, C, E
# Walking line: F, Gb, G, A, Bb, B, C, Db, D, Eb, E, F#, G, Ab, A, Bb
# F -> Gb -> G -> A -> Bb -> B -> C -> Db -> D -> Eb -> E -> F# -> G -> Ab -> A -> Bb

bass_notes = [77, 78, 79, 82, 80, 81, 82, 79, 80, 79, 82, 84, 82, 80, 82, 80]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: Diane - 7th chords, comp on 2 and 4
# F7: F, A, C, E
# Bb7: Bb, D, F, Ab
# F7: F, A, C, E
# Bb7: Bb, D, F, Ab

# Bar 2 (1.5 - 3.0s) - F7 on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.875 - 2.0)
    77, 82, 87, 84,
    # Bar 2, beat 4 (3.0 - 3.125)
    77, 82, 87, 84
]
for i, note in enumerate(piano_notes):
    start = 1.875 + (i * 0.125)
    end = start + 0.125
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=end))

# Bar 3 (3.0 - 4.5s) - Bb7 on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (3.875 - 4.0)
    71, 76, 82, 78,
    # Bar 3, beat 4 (4.5 - 4.625)
    71, 76, 82, 78
]
for i, note in enumerate(piano_notes):
    start = 3.875 + (i * 0.125)
    end = start + 0.125
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=end))

# Bar 4 (4.5 - 6.0s) - F7 on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (5.375 - 5.5)
    77, 82, 87, 84,
    # Bar 4, beat 4 (6.0 - 6.125)
    77, 82, 87, 84
]
for i, note in enumerate(piano_notes):
    start = 5.375 + (i * 0.125)
    end = start + 0.125
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=end))

# Sax: Dante - short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Motif: F, G, Ab, F (1.5 - 2.125)
# Then rest until 4.5, then repeat to finish

# First run (1.5 - 2.125)
sax_notes = [77, 79, 80, 77]
for i, note in enumerate(sax_notes):
    start = 1.5 + (i * 0.125)
    end = start + 0.125
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Second run (4.5 - 5.125)
sax_notes = [77, 79, 80, 77]
for i, note in enumerate(sax_notes):
    start = 4.5 + (i * 0.125)
    end = start + 0.125
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Drums: Continue the same pattern from bar 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375))

# Hi-hat on every eighth
for i in range(4, 16):
    start = 1.5 + (i * 0.375)
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
