
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm7 - G7 - Cm7 - F7
sax_notes = [
    # Dm7: D, F, A, C
    (1.5, 62), (1.5, 65), (1.5, 67), (1.5, 69),
    # G7: G, B, D, F
    (2.0, 67), (2.0, 71), (2.0, 62), (2.0, 65),
    # Cm7: C, Eb, G, Bb
    (2.5, 60), (2.5, 63), (2.5, 67), (2.5, 62),
    # F7: F, A, C, Eb
    (3.0, 65), (3.0, 69), (3.0, 60), (3.0, 63)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Dm7: D - Eb - F - G
    (1.5, 62), (1.75, 63), (2.0, 65), (2.25, 67),
    # G7: G - A - B - C
    (2.5, 67), (2.75, 69), (3.0, 71), (3.25, 60),
    # Cm7: C - Db - Eb - F
    (3.5, 60), (3.75, 61), (4.0, 63), (4.25, 65),
    # F7: F - G - A - Bb
    (4.5, 65), (4.75, 67), (5.0, 69), (5.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    (2.0, 62), (2.0, 65), (2.0, 67), (2.0, 69),
    # G7 on beat 4
    (3.0, 67), (3.0, 71), (3.0, 62), (3.0, 65),
    # Cm7 on beat 2
    (4.0, 60), (4.0, 63), (4.0, 67), (4.0, 62),
    # F7 on beat 4
    (5.0, 65), (5.0, 69), (5.0, 60), (5.0, 63)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Dm7 - G7 - Cm7 - F7 (repeats motif)
sax_notes = [
    # Dm7: D, F, A, C
    (3.0, 62), (3.0, 65), (3.0, 67), (3.0, 69),
    # G7: G, B, D, F
    (3.5, 67), (3.5, 71), (3.5, 62), (3.5, 65),
    # Cm7: C, Eb, G, Bb
    (4.0, 60), (4.0, 63), (4.0, 67), (4.0, 62),
    # F7: F, A, C, Eb
    (4.5, 65), (4.5, 69), (4.5, 60), (4.5, 63)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Dm7: D - Eb - F - G
    (3.0, 62), (3.25, 63), (3.5, 65), (3.75, 67),
    # G7: G - A - B - C
    (4.0, 67), (4.25, 69), (4.5, 71), (4.75, 60),
    # Cm7: C - Db - Eb - F
    (5.0, 60), (5.25, 61), (5.5, 63), (5.75, 65),
    # F7: F - G - A - Bb
    (6.0, 65), (6.25, 67), (6.5, 69), (6.75, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    (3.5, 62), (3.5, 65), (3.5, 67), (3.5, 69),
    # G7 on beat 4
    (4.5, 67), (4.5, 71), (4.5, 62), (4.5, 65),
    # Cm7 on beat 2
    (5.5, 60), (5.5, 63), (5.5, 67), (5.5, 62),
    # F7 on beat 4
    (6.5, 65), (6.5, 69), (6.5, 60), (6.5, 63)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Dm7 - G7 - Cm7 - F7 (repeats motif)
sax_notes = [
    # Dm7: D, F, A, C
    (4.5, 62), (4.5, 65), (4.5, 67), (4.5, 69),
    # G7: G, B, D, F
    (5.0, 67), (5.0, 71), (5.0, 62), (5.0, 65),
    # Cm7: C, Eb, G, Bb
    (5.5, 60), (5.5, 63), (5.5, 67), (5.5, 62),
    # F7: F, A, C, Eb
    (6.0, 65), (6.0, 69), (6.0, 60), (6.0, 63)
]
for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Bass: Walking line with chromatic approaches
bass_notes = [
    # Dm7: D - Eb - F - G
    (4.5, 62), (4.75, 63), (5.0, 65), (5.25, 67),
    # G7: G - A - B - C
    (5.5, 67), (5.75, 69), (6.0, 71), (6.25, 60),
    # Cm7: C - Db - Eb - F
    (6.5, 60), (6.75, 61), (7.0, 63), (7.25, 65),
    # F7: F - G - A - Bb
    (7.5, 65), (7.75, 67), (8.0, 69), (8.25, 62)
]
for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    (5.0, 62), (5.0, 65), (5.0, 67), (5.0, 69),
    # G7 on beat 4
    (6.0, 67), (6.0, 71), (6.0, 62), (6.0, 65),
    # Cm7 on beat 2
    (7.0, 60), (7.0, 63), (7.0, 67), (7.0, 62),
    # F7 on beat 4
    (8.0, 65), (8.0, 69), (8.0, 60), (8.0, 63)
]
for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (4.5, 36), (4.875, 42), (5.25, 36), (5.625, 42),
    (6.0, 38), (6.375, 42), (6.75, 38), (7.125, 42)
]
for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
