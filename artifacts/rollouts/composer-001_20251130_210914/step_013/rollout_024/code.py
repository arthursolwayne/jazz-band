
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
            note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
            drums.notes.append(note)
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm motif
note = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75)  # D
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25)  # G
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5)  # D
sax.notes.append(note)

# Bass: Walking line
note = pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75)  # D
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=2.0)  # Eb
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.25)  # C
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5)  # D
bass.notes.append(note)

# Piano: 7th chords on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75)  # Bb
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75)  # F
piano.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25)  # Bb
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25)  # F
piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = 1.5 + beat * 0.375
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif starting with F
note = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5)  # G
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75)  # D
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0)  # F
sax.notes.append(note)

# Bass: Walking line
note = pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25)  # F
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.5)  # G
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.75)  # D
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0)  # F
bass.notes.append(note)

# Piano: 7th chords on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.25)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25)  # Bb
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25)  # G
piano.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.75)  # F
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75)  # Bb
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.75)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75)  # G
piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = 3.0 + beat * 0.375
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif
note = pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75)  # D
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0)  # F
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25)  # G
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5)  # D
sax.notes.append(note)

# Bass: Walking line
note = pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75)  # D
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=51, start=4.75, end=5.0)  # Eb
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25)  # C
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.5)  # D
bass.notes.append(note)

# Piano: 7th chords on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75)  # Bb
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75)  # F
piano.notes.append(note)

note = pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25)  # D
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25)  # G
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.25)  # Bb
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25)  # F
piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = 4.5 + beat * 0.375
    if beat in [0, 2]:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat in [1, 3]:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
