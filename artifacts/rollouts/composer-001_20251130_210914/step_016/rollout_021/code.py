
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
            note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: Fm scale with a twist. Start with a motif, leave it hanging.

# Fm scale: F, Gb, Ab, Bb, B, Db, Eb
motif = [78, 77, 75, 72, 71, 69, 67]  # F, Gb, Ab, Bb, B, Db, Eb
note1 = pretty_midi.Note(velocity=110, pitch=motif[0], start=1.5, end=1.75)
note2 = pretty_midi.Note(velocity=110, pitch=motif[2], start=1.75, end=2.0)
sax.notes.append(note1)
sax.notes.append(note2)

# Marcus: Walking bass line in Fm
bass_notes = [72, 70, 69, 67, 67, 65, 64, 62]  # F, Eb, D, C, C, Bb, B, Ab
for i in range(4):
    start = 1.5 + i * 0.375
    end = start + 0.25
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i * 2], start=start, end=end)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i * 2 + 1], start=end, end=end + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, Fm7, Ab7, Bb7, Db7
chords = [78, 77, 75, 72]  # Fm7: F, Ab, Bb, Db
for i in range(2):
    start = 1.5 + (i + 1) * 0.375
    for pitch in chords:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.125)
        piano.notes.append(note)

# Drums: same pattern
for beat in range(4):
    time = 1.5 + beat * 0.375
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue motif, resolve on the fourth beat

# Complete the motif from bar 2
note3 = pretty_midi.Note(velocity=110, pitch=motif[4], start=3.0, end=3.25)
note4 = pretty_midi.Note(velocity=110, pitch=motif[5], start=3.25, end=3.5)
note5 = pretty_midi.Note(velocity=110, pitch=motif[6], start=3.5, end=3.75)
note6 = pretty_midi.Note(velocity=110, pitch=motif[0], start=3.75, end=4.0)
sax.notes.append(note3)
sax.notes.append(note4)
sax.notes.append(note5)
sax.notes.append(note6)

# Marcus: Walking bass line in Fm
for i in range(4):
    start = 3.0 + i * 0.375
    end = start + 0.25
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i * 2 + 4], start=start, end=end)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i * 2 + 5], start=end, end=end + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, Fm7, Ab7, Bb7, Db7
for i in range(2):
    start = 3.0 + (i + 1) * 0.375
    for pitch in chords:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.125)
        piano.notes.append(note)

# Drums: same pattern
for beat in range(4):
    time = 3.0 + beat * 0.375
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif, leave it hanging for a moment

note7 = pretty_midi.Note(velocity=110, pitch=motif[1], start=4.5, end=4.75)
note8 = pretty_midi.Note(velocity=110, pitch=motif[2], start=4.75, end=5.0)
note9 = pretty_midi.Note(velocity=110, pitch=motif[3], start=5.0, end=5.25)
note10 = pretty_midi.Note(velocity=110, pitch=motif[0], start=5.25, end=5.5)
note11 = pretty_midi.Note(velocity=110, pitch=motif[1], start=5.5, end=5.75)
note12 = pretty_midi.Note(velocity=110, pitch=motif[2], start=5.75, end=6.0)
sax.notes.append(note7)
sax.notes.append(note8)
sax.notes.append(note9)
sax.notes.append(note10)
sax.notes.append(note11)
sax.notes.append(note12)

# Marcus: Walking bass line in Fm
for i in range(4):
    start = 4.5 + i * 0.375
    end = start + 0.25
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i * 2 + 8], start=start, end=end)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=90, pitch=bass_notes[i * 2 + 9], start=end, end=end + 0.25)
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4, Fm7, Ab7, Bb7, Db7
for i in range(2):
    start = 4.5 + (i + 1) * 0.375
    for pitch in chords:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.125)
        piano.notes.append(note)

# Drums: same pattern
for beat in range(4):
    time = 4.5 + beat * 0.375
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=60, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
