
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=beat * 0.375, end=(beat + 1) * 0.375)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: C E D C (melody)
note = pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=1.5 + 0.375, end=1.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=60, start=1.5 + 1.125, end=1.5 + 1.5)
sax.notes.append(note)

# Bass: Walking line with chromatic approaches
note = pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.5 + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=49, start=1.5 + 0.375, end=1.5 + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=50, start=1.5 + 0.75, end=1.5 + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=51, start=1.5 + 1.125, end=1.5 + 1.5)
bass.notes.append(note)

# Piano: 7th chords on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=60, start=1.5 + 0.75, end=1.5 + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=1.5 + 0.75, end=1.5 + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=1.5 + 0.75, end=1.5 + 1.125)
piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=1.5 + beat * 0.375, end=1.5 + (beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=1.5 + beat * 0.375, end=1.5 + (beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=1.5 + beat * 0.375, end=1.5 + (beat + 1) * 0.375)
    drums.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat and slightly vary the melody
note = pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.0 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=3.0 + 0.375, end=3.0 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=3.0 + 0.75, end=3.0 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=60, start=3.0 + 1.125, end=3.0 + 1.5)
sax.notes.append(note)

# Bass: Walking line with chromatic approaches
note = pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.0 + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=52, start=3.0 + 0.375, end=3.0 + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=53, start=3.0 + 0.75, end=3.0 + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=55, start=3.0 + 1.125, end=3.0 + 1.5)
bass.notes.append(note)

# Piano: 7th chords on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=60, start=3.0 + 0.75, end=3.0 + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=3.0 + 0.75, end=3.0 + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=3.0 + 0.75, end=3.0 + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=3.0 + 0.75, end=3.0 + 1.125)
piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=3.0 + beat * 0.375, end=3.0 + (beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=3.0 + beat * 0.375, end=3.0 + (beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=3.0 + beat * 0.375, end=3.0 + (beat + 1) * 0.375)
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End the motif with a resolution
note = pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=64, start=4.5 + 0.375, end=4.5 + 0.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=62, start=4.5 + 0.75, end=4.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=110, pitch=60, start=4.5 + 1.125, end=4.5 + 1.5)
sax.notes.append(note)

# Bass: Walking line with chromatic approaches
note = pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.5 + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=56, start=4.5 + 0.375, end=4.5 + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=57, start=4.5 + 0.75, end=4.5 + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=59, start=4.5 + 1.125, end=4.5 + 1.5)
bass.notes.append(note)

# Piano: 7th chords on 2 and 4
note = pretty_midi.Note(velocity=90, pitch=60, start=4.5 + 0.75, end=4.5 + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=64, start=4.5 + 0.75, end=4.5 + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=4.5 + 0.75, end=4.5 + 1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=4.5 + 0.75, end=4.5 + 1.125)
piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in [0, 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=4.5 + beat * 0.375, end=4.5 + (beat + 1) * 0.375)
    drums.notes.append(note)
for beat in [1, 3]:
    note = pretty_midi.Note(velocity=100, pitch=38, start=4.5 + beat * 0.375, end=4.5 + (beat + 1) * 0.375)
    drums.notes.append(note)
for beat in range(4):
    note = pretty_midi.Note(velocity=80, pitch=42, start=4.5 + beat * 0.375, end=4.5 + (beat + 1) * 0.375)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
