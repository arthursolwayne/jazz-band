
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
for i in range(4):
    time = i * 0.375
    drums.notes.append(pretty_midi.Note(100, 36, time, time + 0.125))  # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(100, 38, time + 0.375, time + 0.5))  # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(100, 42, time, time + 0.125))  # Hihat on every eighth

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 64),    # F
    (1.875, 63),  # Eb
    (2.25, 62),   # D
    (2.625, 61),  # C
    (3.0, 64),    # F
    (3.375, 63),  # Eb
    (3.75, 62),   # D
    (4.125, 61),  # C
    (4.5, 64),    # F
    (4.875, 63),  # Eb
    (5.25, 62),   # D
    (5.625, 61),  # C
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Cm7 = C, Eb, G, Bb
# Eb7 = Eb, G, Bb, D
piano_notes = [
    (1.5, 71), (1.5, 69), (1.5, 67), (1.5, 66),  # Fm7 on 1
    (1.875, 70), (1.875, 68), (1.875, 67), (1.875, 66),  # Cm7 on 2
    (2.25, 71), (2.25, 69), (2.25, 67), (2.25, 66),  # Fm7 on 3
    (2.625, 70), (2.625, 68), (2.625, 67), (2.625, 66),  # Cm7 on 4
    (3.0, 71), (3.0, 69), (3.0, 67), (3.0, 66),  # Fm7 on 1
    (3.375, 70), (3.375, 68), (3.375, 67), (3.375, 66),  # Cm7 on 2
    (3.75, 71), (3.75, 69), (3.75, 67), (3.75, 66),  # Fm7 on 3
    (4.125, 70), (4.125, 68), (4.125, 67), (4.125, 66),  # Cm7 on 4
    (4.5, 71), (4.5, 69), (4.5, 67), (4.5, 66),  # Fm7 on 1
    (4.875, 70), (4.875, 68), (4.875, 67), (4.875, 66),  # Cm7 on 2
    (5.25, 71), (5.25, 69), (5.25, 67), (5.25, 66),  # Fm7 on 3
    (5.625, 70), (5.625, 68), (5.625, 67), (5.625, 66),  # Cm7 on 4
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(100, note, time, time + 0.25))

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(6):
    time = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(100, 36, time, time + 0.125))  # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(100, 38, time + 0.375, time + 0.5))  # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(100, 42, time, time + 0.125))  # Hihat on every eighth

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (66) - Ab (67) - C (69) - Eb (68) -> F (66)
# First part: F - Ab - C
sax.notes.append(pretty_midi.Note(100, 66, 1.5, 1.75))
sax.notes.append(pretty_midi.Note(100, 67, 1.75, 2.0))
sax.notes.append(pretty_midi.Note(100, 69, 2.0, 2.25))

# Leave it hanging
sax.notes.append(pretty_midi.Note(100, 68, 2.625, 2.875))

# Come back and finish it
sax.notes.append(pretty_midi.Note(100, 66, 3.0, 3.25))
sax.notes.append(pretty_midi.Note(100, 67, 3.25, 3.5))
sax.notes.append(pretty_midi.Note(100, 69, 3.5, 3.75))
sax.notes.append(pretty_midi.Note(100, 68, 3.75, 4.0))

# Add final resolution
sax.notes.append(pretty_midi.Note(100, 66, 5.25, 5.5))
sax.notes.append(pretty_midi.Note(100, 67, 5.5, 5.75))
sax.notes.append(pretty_midi.Note(100, 69, 5.75, 6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("waynes_intro.mid")
