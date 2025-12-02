
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
for bar in range(1):
    start = bar * 1.5
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane: 7th chords, comp on 2 and 4
# C7 on beat 2, E7 on beat 4
for bar in range(1, 2):
    start = bar * 1.5
    # Diane: piano chords
    # C7 on beat 2 (0.375s)
    note_c = pretty_midi.Note(velocity=100, pitch=60, start=start + 0.375, end=start + 0.75)
    note_b = pretty_midi.Note(velocity=100, pitch=61, start=start + 0.375, end=start + 0.75)
    note_g = pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75)
    note_e = pretty_midi.Note(velocity=100, pitch=71, start=start + 0.375, end=start + 0.75)
    # E7 on beat 4 (1.125s)
    note_e2 = pretty_midi.Note(velocity=100, pitch=71, start=start + 1.125, end=start + 1.5)
    note_d = pretty_midi.Note(velocity=100, pitch=70, start=start + 1.125, end=start + 1.5)
    note_b2 = pretty_midi.Note(velocity=100, pitch=61, start=start + 1.125, end=start + 1.5)
    note_g2 = pretty_midi.Note(velocity=100, pitch=67, start=start + 1.125, end=start + 1.5)
    piano.notes.extend([note_c, note_b, note_g, note_e, note_e2, note_d, note_b2, note_g2])

    # Marcus: walking line in F
    # F -> G -> Ab -> A -> Bb -> B -> C -> Db -> D -> Eb -> F
    # Each note is 0.375s
    notes = [59, 61, 62, 64, 65, 67, 68, 69, 71, 72, 59]
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        bass.notes.append(note)

    # Dante: sax melody (F -> G -> Ab -> F)
    note_f = pretty_midi.Note(velocity=110, pitch=59, start=start, end=start + 0.375)
    note_g = pretty_midi.Note(velocity=110, pitch=61, start=start + 0.375, end=start + 0.75)
    note_ab = pretty_midi.Note(velocity=110, pitch=62, start=start + 0.75, end=start + 1.125)
    note_f2 = pretty_midi.Note(velocity=110, pitch=59, start=start + 1.125, end=start + 1.5)
    sax.notes.extend([note_f, note_g, note_ab, note_f2])

    # Drums: same pattern
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2])

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane: 7th chords, comp on 2 and 4
# Bb7 on beat 2, D7 on beat 4
for bar in range(2, 3):
    start = bar * 1.5
    # Diane: piano chords
    # Bb7 on beat 2 (0.375s)
    note_bb = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
    note_a = pretty_midi.Note(velocity=100, pitch=61, start=start + 0.375, end=start + 0.75)
    note_f2 = pretty_midi.Note(velocity=100, pitch=59, start=start + 0.375, end=start + 0.75)
    note_d = pretty_midi.Note(velocity=100, pitch=70, start=start + 0.375, end=start + 0.75)
    # D7 on beat 4 (1.125s)
    note_d2 = pretty_midi.Note(velocity=100, pitch=70, start=start + 1.125, end=start + 1.5)
    note_c2 = pretty_midi.Note(velocity=100, pitch=60, start=start + 1.125, end=start + 1.5)
    note_f3 = pretty_midi.Note(velocity=100, pitch=59, start=start + 1.125, end=start + 1.5)
    note_a2 = pretty_midi.Note(velocity=100, pitch=61, start=start + 1.125, end=start + 1.5)
    piano.notes.extend([note_bb, note_a, note_f2, note_d, note_d2, note_c2, note_f3, note_a2])

    # Marcus: walking line in F
    # F -> G -> Ab -> A -> Bb -> B -> C -> Db -> D -> Eb -> F
    notes = [59, 61, 62, 64, 65, 67, 68, 69, 71, 72, 59]
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        bass.notes.append(note)

    # Dante: sax melody (Ab -> Bb -> C -> Ab)
    note_ab2 = pretty_midi.Note(velocity=110, pitch=62, start=start, end=start + 0.375)
    note_bb2 = pretty_midi.Note(velocity=110, pitch=62, start=start + 0.375, end=start + 0.75)
    note_c2 = pretty_midi.Note(velocity=110, pitch=60, start=start + 0.75, end=start + 1.125)
    note_ab3 = pretty_midi.Note(velocity=110, pitch=62, start=start + 1.125, end=start + 1.5)
    sax.notes.extend([note_ab2, note_bb2, note_c2, note_ab3])

    # Drums: same pattern
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2])

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane: 7th chords, comp on 2 and 4
# Eb7 on beat 2, G7 on beat 4
for bar in range(3, 4):
    start = bar * 1.5
    # Diane: piano chords
    # Eb7 on beat 2 (0.375s)
    note_eb = pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75)
    note_d2 = pretty_midi.Note(velocity=100, pitch=70, start=start + 0.375, end=start + 0.75)
    note_bb3 = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
    note_g = pretty_midi.Note(velocity=100, pitch=67, start=start + 0.375, end=start + 0.75)
    # G7 on beat 4 (1.125s)
    note_g2 = pretty_midi.Note(velocity=100, pitch=67, start=start + 1.125, end=start + 1.5)
    note_f3 = pretty_midi.Note(velocity=100, pitch=59, start=start + 1.125, end=start + 1.5)
    note_bb4 = pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)
    note_d3 = pretty_midi.Note(velocity=100, pitch=70, start=start + 1.125, end=start + 1.5)
    piano.notes.extend([note_eb, note_d2, note_bb3, note_g, note_g2, note_f3, note_bb4, note_d3])

    # Marcus: walking line in F
    # F -> G -> Ab -> A -> Bb -> B -> C -> Db -> D -> Eb -> F
    notes = [59, 61, 62, 64, 65, 67, 68, 69, 71, 72, 59]
    for i, pitch in enumerate(notes):
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=start + i * 0.375, end=start + i * 0.375 + 0.375)
        bass.notes.append(note)

    # Dante: sax melody (C -> D -> Eb -> C)
    note_c3 = pretty_midi.Note(velocity=110, pitch=60, start=start, end=start + 0.375)
    note_d3 = pretty_midi.Note(velocity=110, pitch=62, start=start + 0.375, end=start + 0.75)
    note_eb2 = pretty_midi.Note(velocity=110, pitch=64, start=start + 0.75, end=start + 1.125)
    note_c4 = pretty_midi.Note(velocity=110, pitch=60, start=start + 1.125, end=start + 1.5)
    sax.notes.extend([note_c3, note_d3, note_eb2, note_c4])

    # Drums: same pattern
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick, kick2, snare, snare2])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
