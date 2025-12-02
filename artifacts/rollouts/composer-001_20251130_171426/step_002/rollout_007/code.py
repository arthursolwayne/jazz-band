
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
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif starts here
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 1.125, end=1.5 + 1.5)
sax.notes.append(note)

# Bass: walking line with chromatic approaches
notes = [57, 59, 60, 62, 64, 65, 67, 69]
for i, pitch in enumerate(notes):
    time = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
chords = [[62, 67, 72, 74], [64, 69, 74, 76]]
for i, chord in enumerate(chords):
    time = 1.5 + i * 0.75
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
        piano.notes.append(note)

# Drums: same pattern
for bar in range(1):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: motif returns
note = pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.0 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=3.0 + 0.75, end=3.0 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=3.0 + 1.125, end=3.0 + 1.5)
sax.notes.append(note)

# Bass: walking line with chromatic approaches
notes = [62, 64, 65, 67, 69, 71, 72, 74]
for i, pitch in enumerate(notes):
    time = 3.0 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
chords = [[64, 69, 74, 76], [66, 71, 76, 78]]
for i, chord in enumerate(chords):
    time = 3.0 + i * 0.75
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
        piano.notes.append(note)

# Drums: same pattern
for bar in range(1):
    for beat in range(4):
        time = 3.0 + bar * 1.5 + beat * 0.375
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: motif completes
note = pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=66, start=4.5 + 0.75, end=4.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=67, start=4.5 + 1.125, end=4.5 + 1.5)
sax.notes.append(note)

# Bass: walking line with chromatic approaches
notes = [64, 66, 67, 69, 71, 72, 74, 76]
for i, pitch in enumerate(notes):
    time = 4.5 + i * 0.375
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
chords = [[66, 71, 76, 78], [68, 73, 78, 80]]
for i, chord in enumerate(chords):
    time = 4.5 + i * 0.75
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.375)
        piano.notes.append(note)

# Drums: same pattern
for bar in range(1):
    for beat in range(4):
        time = 4.5 + bar * 1.5 + beat * 0.375
        if beat in [0, 2]:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
            drums.notes.append(note)
        if beat in [1, 3]:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.125)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
