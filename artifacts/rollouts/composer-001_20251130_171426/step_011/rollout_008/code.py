
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
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: chromatic walking line in D minor
bass_notes = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        pitch = bass_notes[(bar - 2) * 4 + beat]
        note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.125)
        bass.notes.append(note)

# Piano: 7th chords on 2 and 4, in D minor
# Dm7 = D F A C
# Gm7 = G Bb D F
# Am7 = A C E G
# Bm7 = B D F# A
chords = [
    [50, 53, 57, 60],  # Dm7
    [55, 57, 60, 63],  # Gm7
    [57, 60, 64, 67],  # Am7
    [59, 62, 64, 67],  # Bm7
]
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 1 or beat == 3:
            chord = chords[bar - 2]
            for pitch in chord:
                note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.125)
                piano.notes.append(note)

# Sax: Motif
# D (50) - F (53) - Bb (57) - D (50) -> D (50) - F (53) - Bb (57) - D (50)
# First phrase (bars 2-3)
sax_notes = [
    (50, 0.0, 0.375),  # D
    (53, 0.375, 0.75), # F
    (57, 0.75, 1.125), # Bb
    (50, 1.125, 1.5),  # D
    (50, 1.5, 1.875),  # D
    (53, 1.875, 2.25), # F
    (57, 2.25, 2.625), # Bb
    (50, 2.625, 3.0),  # D
    (50, 3.0, 3.375),  # D
    (53, 3.375, 3.75), # F
    (57, 3.75, 4.125), # Bb
    (50, 4.125, 4.5),  # D
]
for note in sax_notes:
    pitch, start, end = note
    sax_note = pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end)
    sax.notes.append(sax_note)

# Drums: continue
for bar in range(2, 5):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
