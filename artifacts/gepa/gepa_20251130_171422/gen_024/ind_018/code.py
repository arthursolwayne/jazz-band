
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (1.5, 59), # D
    (1.875, 60), # Eb
    (2.25, 62), # F
    (2.625, 63), # Gb
    (3.0, 64), # G
    (3.375, 65), # Ab
    (3.75, 67), # Bb
    (4.125, 69), # B
    (4.5, 70), # C
    (4.875, 71), # Db
    (5.25, 72), # D
    (5.625, 74), # Eb
]

for time, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 62), # F7 (Bb, D, F, Ab)
    (1.5, 64),
    (1.5, 67),
    (1.5, 69),
    (1.875, 62),
    (1.875, 64),
    (1.875, 67),
    (1.875, 69),
    (2.25, 62), # G7 (B, D, F, G)
    (2.25, 64),
    (2.25, 67),
    (2.25, 69),
    (2.625, 62),
    (2.625, 64),
    (2.625, 67),
    (2.625, 69),
    (3.0, 62), # A7 (C, E, G, A)
    (3.0, 64),
    (3.0, 67),
    (3.0, 69),
    (3.375, 62),
    (3.375, 64),
    (3.375, 67),
    (3.375, 69),
    (3.75, 62), # B7 (D, F#, A, B)
    (3.75, 64),
    (3.75, 67),
    (3.75, 69),
    (4.125, 62),
    (4.125, 64),
    (4.125, 67),
    (4.125, 69),
    (4.5, 62), # C7 (E, G, B, C)
    (4.5, 64),
    (4.5, 67),
    (4.5, 69),
    (4.875, 62),
    (4.875, 64),
    (4.875, 67),
    (4.875, 69),
    (5.25, 62), # D7 (F, A, C, D)
    (5.25, 64),
    (5.25, 67),
    (5.25, 69),
    (5.625, 62),
    (5.625, 64),
    (5.625, 67),
    (5.625, 69),
]

for time, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25))

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Dm7 -> G7 -> C7 -> F7 (Dm key)
sax_notes = [
    (1.5, 62),  # D
    (1.75, 64),  # E
    (2.0, 67),  # G
    (2.25, 69),  # A
    (2.5, 67),  # G
    (2.75, 64),  # E
    (3.0, 62),  # D
    (3.25, 64),  # E
    (3.5, 67),  # G
    (3.75, 69),  # A
    (4.0, 67),  # G
    (4.25, 64),  # E
    (4.5, 62),  # D
    (4.75, 64),  # E
    (5.0, 67),  # G
    (5.25, 71),  # Bb
    (5.5, 67),  # G
    (5.75, 64),  # E
    (6.0, 62),  # D
]

for time, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125))

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for i in range(8):
    time = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time + 0.375, end=time + 0.375 + 0.125))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
