
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
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

# Bar 2: Full quartet (1.5 - 3.0s)
start = 1.5
# Sax melody: D, E, F#, G, A (motif)
note_d = pretty_midi.Note(velocity=110, pitch=62, start=start, end=start + 0.375)
sax.notes.append(note_d)
note_e = pretty_midi.Note(velocity=110, pitch=64, start=start + 0.375, end=start + 0.75)
sax.notes.append(note_e)
note_fs = pretty_midi.Note(velocity=110, pitch=66, start=start + 0.75, end=start + 1.125)
sax.notes.append(note_fs)
note_g = pretty_midi.Note(velocity=110, pitch=67, start=start + 1.125, end=start + 1.5)
sax.notes.append(note_g)

# Bass: walking line starting on D (62)
note_d = pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.375)
bass.notes.append(note_d)
note_f = pretty_midi.Note(velocity=80, pitch=64, start=start + 0.375, end=start + 0.75)
bass.notes.append(note_f)
note_fs = pretty_midi.Note(velocity=80, pitch=66, start=start + 0.75, end=start + 1.125)
bass.notes.append(note_fs)
note_a = pretty_midi.Note(velocity=80, pitch=69, start=start + 1.125, end=start + 1.5)
bass.notes.append(note_a)

# Piano: 7th chords on 2 and 4
# D7 on 2
note_d7 = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_d7)
note_f7 = pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_f7)
note_a7 = pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_a7)
note_c7 = pretty_midi.Note(velocity=100, pitch=72, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_c7)

# D7 on 4
note_d7 = pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_d7)
note_f7 = pretty_midi.Note(velocity=100, pitch=64, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_f7)
note_a7 = pretty_midi.Note(velocity=100, pitch=69, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_a7)
note_c7 = pretty_midi.Note(velocity=100, pitch=72, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_c7)

# Bar 3: Full quartet (3.0 - 4.5s)
start = 3.0
# Sax: repeat the motif with a slight variation
note_d = pretty_midi.Note(velocity=110, pitch=62, start=start, end=start + 0.375)
sax.notes.append(note_d)
note_e = pretty_midi.Note(velocity=110, pitch=64, start=start + 0.375, end=start + 0.75)
sax.notes.append(note_e)
note_fs = pretty_midi.Note(velocity=110, pitch=66, start=start + 0.75, end=start + 1.125)
sax.notes.append(note_fs)
note_g = pretty_midi.Note(velocity=110, pitch=67, start=start + 1.125, end=start + 1.5)
sax.notes.append(note_g)

# Bass: walking line starting on D (62)
note_d = pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.375)
bass.notes.append(note_d)
note_f = pretty_midi.Note(velocity=80, pitch=64, start=start + 0.375, end=start + 0.75)
bass.notes.append(note_f)
note_fs = pretty_midi.Note(velocity=80, pitch=66, start=start + 0.75, end=start + 1.125)
bass.notes.append(note_fs)
note_a = pretty_midi.Note(velocity=80, pitch=69, start=start + 1.125, end=start + 1.5)
bass.notes.append(note_a)

# Piano: 7th chords on 2 and 4
# D7 on 2
note_d7 = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_d7)
note_f7 = pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_f7)
note_a7 = pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_a7)
note_c7 = pretty_midi.Note(velocity=100, pitch=72, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_c7)

# D7 on 4
note_d7 = pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_d7)
note_f7 = pretty_midi.Note(velocity=100, pitch=64, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_f7)
note_a7 = pretty_midi.Note(velocity=100, pitch=69, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_a7)
note_c7 = pretty_midi.Note(velocity=100, pitch=72, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_c7)

# Bar 4: Full quartet (4.5 - 6.0s)
start = 4.5
# Sax: start the motif again but leave it hanging
note_d = pretty_midi.Note(velocity=110, pitch=62, start=start, end=start + 0.375)
sax.notes.append(note_d)
note_e = pretty_midi.Note(velocity=110, pitch=64, start=start + 0.375, end=start + 0.75)
sax.notes.append(note_e)
note_fs = pretty_midi.Note(velocity=110, pitch=66, start=start + 0.75, end=start + 1.125)
sax.notes.append(note_fs)
# Leave the G out, it's the resolution — let Wayne wait for it

# Bass: walking line starting on D (62)
note_d = pretty_midi.Note(velocity=80, pitch=62, start=start, end=start + 0.375)
bass.notes.append(note_d)
note_f = pretty_midi.Note(velocity=80, pitch=64, start=start + 0.375, end=start + 0.75)
bass.notes.append(note_f)
note_fs = pretty_midi.Note(velocity=80, pitch=66, start=start + 0.75, end=start + 1.125)
bass.notes.append(note_fs)
note_a = pretty_midi.Note(velocity=80, pitch=69, start=start + 1.125, end=start + 1.5)
bass.notes.append(note_a)

# Piano: 7th chords on 2 and 4
# D7 on 2
note_d7 = pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_d7)
note_f7 = pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_f7)
note_a7 = pretty_midi.Note(velocity=100, pitch=69, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_a7)
note_c7 = pretty_midi.Note(velocity=100, pitch=72, start=start + 0.375, end=start + 0.75)
piano.notes.append(note_c7)

# D7 on 4
note_d7 = pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_d7)
note_f7 = pretty_midi.Note(velocity=100, pitch=64, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_f7)
note_a7 = pretty_midi.Note(velocity=100, pitch=69, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_a7)
note_c7 = pretty_midi.Note(velocity=100, pitch=72, start=start + 1.125, end=start + 1.5)
piano.notes.append(note_c7)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    drums.notes.append(kick)
    kick = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    drums.notes.append(kick)
    # Snare on 2 and 4
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75)
    drums.notes.append(snare)
    snare = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5)
    drums.notes.append(snare)
    # Hihat on every eighth
    for i in range(8):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.125)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
