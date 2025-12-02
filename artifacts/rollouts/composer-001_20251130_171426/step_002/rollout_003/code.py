
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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    hihat1 = pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375)
    hihat2 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75)
    hihat3 = pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125)
    hihat4 = pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2, snare1, snare2, hihat1, hihat2, hihat3, hihat4])

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line with chromatic approaches
for bar in range(2, 5):
    start = bar * 1.5
    # Fm bass line: F, Gb, Ab, A, Bb, B, C, Db
    bass_notes = [65, 66, 67, 68, 69, 70, 71, 72]
    for i, note in enumerate(bass_notes):
        if i % 2 == 0:
            duration = 0.75
        else:
            duration = 0.75
        note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start + i * 0.75, end=start + i * 0.75 + duration)
        bass.notes.append(note_obj)

# Piano: 7th chords, comp on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    # Fm7 = F, Ab, Bb, C
    # Bbm7 = Bb, Db, F, Ab
    # Am7 = A, C, Eb, G
    # Dm7 = D, F, Ab, B
    if bar == 2:
        chords = [[65, 68, 71, 72], [71, 74, 65, 68]]
    elif bar == 3:
        chords = [[69, 71, 67, 72], [74, 76, 65, 68]]
    elif bar == 4:
        chords = [[67, 69, 65, 68], [71, 74, 67, 69]]
    for i, chord in enumerate(chords):
        for note in chord:
            note_obj = pretty_midi.Note(velocity=90, pitch=note, start=start + i * 0.75, end=start + i * 0.75 + 0.375)
            piano.notes.append(note_obj)

# Sax: motif in Fm, one short phrase, leave it hanging
# Motif: F, Ab, Bb, D (Fm scale: F, Gb, Ab, A, Bb, B, C, Db)
# Start at 1.5s
motif = [65, 68, 71, 69]
for i, note in enumerate(motif):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=1.5 + i * 0.375, end=1.5 + i * 0.375 + 0.1875)
    sax.notes.append(note_obj)

# Repeat last note of motif for a suspension
note_obj = pretty_midi.Note(velocity=100, pitch=motif[-1], start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note_obj)

# Repeat motif starting at 3.0s
for i, note in enumerate(motif):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=3.0 + i * 0.375, end=3.0 + i * 0.375 + 0.1875)
    sax.notes.append(note_obj)

# Repeat last note of motif for a suspension
note_obj = pretty_midi.Note(velocity=100, pitch=motif[-1], start=3.0 + 0.75, end=3.0 + 1.125)
sax.notes.append(note_obj)

# Repeat motif starting at 4.5s
for i, note in enumerate(motif):
    note_obj = pretty_midi.Note(velocity=100, pitch=note, start=4.5 + i * 0.375, end=4.5 + i * 0.375 + 0.1875)
    sax.notes.append(note_obj)

# Repeat last note of motif for a suspension
note_obj = pretty_midi.Note(velocity=100, pitch=motif[-1], start=4.5 + 0.75, end=4.5 + 1.125)
sax.notes.append(note_obj)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
