
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
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Fm7 = F, Ab, Bb, Db
# Walking bass line: F, Gb, Ab, A, Bb, B, C, Db, D, Eb, F, Gb, etc.

bass_notes = [
    (1.5, 65), (1.75, 64), (2.0, 67), (2.25, 68),
    (2.5, 69), (2.75, 70), (3.0, 71), (3.25, 69),
    (3.5, 67), (3.75, 65), (4.0, 64), (4.25, 67),
    (4.5, 68), (4.75, 69), (5.0, 71), (5.25, 72)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane: 7th chords, comp on 2 and 4
# Fm7 on 1, Ab7 on 2, Bb7 on 3, Db7 on 4

piano_notes = [
    # Bar 2: Fm7 (F, Ab, Bb, Db)
    (1.5, 65), (1.5, 76), (1.5, 71), (1.5, 68),
    # Bar 3: Ab7 (Ab, C, Db, F)
    (2.5, 76), (2.5, 79), (2.5, 71), (2.5, 65),
    # Bar 4: Bb7 (Bb, D, Eb, F)
    (3.5, 71), (3.5, 74), (3.5, 76), (3.5, 65)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Dante: Tenor sax melody
# Whisper at first, then a cry — start with a short motif, leave it hanging

# Bar 2: Start the motif
# F (65), Ab (76), Bb (71), rest
sax_notes = [
    (1.5, 65), (1.5, 76), (1.5, 71), (1.5, 69),
    (2.125, 67), (2.125, 76), (2.125, 71), (2.125, 69),
    (2.75, 65), (2.75, 76), (2.75, 71), (2.75, 69),
    (3.375, 67), (3.375, 76), (3.375, 71), (3.375, 69)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = (bar - 1) * 1.5
    drum_notes = [
        (start + 0.0, 36), (start + 0.375, 42), (start + 0.75, 36), (start + 1.125, 42),
        (start + 1.5, 38), (start + 1.875, 42), (start + 2.25, 38), (start + 2.625, 42)
    ]
    for time, note in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
