
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane: 7th chords, comp on 2 and 4
# Fm7: F, Ab, C, Eb
# 7th chords on 2 and 4
for i in range(2):
    time = 1.5 + i * 1.5
    # 2nd beat
    note = pretty_midi.Note(velocity=100, pitch=53, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=51, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=48, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=50, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    # 4th beat
    note = pretty_midi.Note(velocity=100, pitch=53, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=51, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=48, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=50, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Fm walking bass line: F, Gb, Eb, D, C, Bb, Ab, G
bass_notes = [53, 52, 50, 49, 48, 45, 47, 46]
for i in range(2):
    time = 1.5 + i * 1.5
    for j in range(4):
        note = pretty_midi.Note(velocity=90, pitch=bass_notes[j + i * 4], start=time + j * 0.375, end=time + j * 0.375 + 0.125)
        bass.notes.append(note)

# Dante: Start a motif, leave it hanging, come back and finish it
# Fm motif: F, Ab, Eb, F
note = pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.5 + 0.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=48, start=1.5 + 0.375, end=1.5 + 0.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=50, start=1.5 + 0.75, end=1.5 + 0.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.0 + 0.125)
sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane: 7th chords, comp on 2 and 4
for i in range(2):
    time = 3.0 + i * 1.5
    # 2nd beat
    note = pretty_midi.Note(velocity=100, pitch=53, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=51, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=48, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=50, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    # 4th beat
    note = pretty_midi.Note(velocity=100, pitch=53, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=51, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=48, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=50, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Fm walking bass line: F, Gb, Eb, D, C, Bb, Ab, G
bass_notes = [53, 52, 50, 49, 48, 45, 47, 46]
for i in range(2):
    time = 3.0 + i * 1.5
    for j in range(4):
        note = pretty_midi.Note(velocity=90, pitch=bass_notes[j + i * 4], start=time + j * 0.375, end=time + j * 0.375 + 0.125)
        bass.notes.append(note)

# Dante: Continue the motif
# Ab, F, D, Ab
note = pretty_midi.Note(velocity=110, pitch=48, start=3.0, end=3.0 + 0.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=53, start=3.0 + 0.375, end=3.0 + 0.5)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=49, start=3.0 + 0.75, end=3.0 + 0.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=48, start=4.5, end=4.5 + 0.125)
sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane: 7th chords, comp on 2 and 4
for i in range(2):
    time = 4.5 + i * 1.5
    # 2nd beat
    note = pretty_midi.Note(velocity=100, pitch=53, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=51, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=48, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=50, start=time + 0.375, end=time + 0.5)
    piano.notes.append(note)
    # 4th beat
    note = pretty_midi.Note(velocity=100, pitch=53, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=51, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=48, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)
    note = pretty_midi.Note(velocity=100, pitch=50, start=time + 0.75, end=time + 0.875)
    piano.notes.append(note)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Fm walking bass line: F, Gb, Eb, D, C, Bb, Ab, G
bass_notes = [53, 52, 50, 49, 48, 45, 47, 46]
for i in range(2):
    time = 4.5 + i * 1.5
    for j in range(4):
        note = pretty_midi.Note(velocity=90, pitch=bass_notes[j + i * 4], start=time + j * 0.375, end=time + j * 0.375 + 0.125)
        bass.notes.append(note)

# Dante: Finish the motif
# F, finish it with a rest
note = pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.5 + 0.125)
sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
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
midi.write("dante_russo.mid")
