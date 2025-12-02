
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

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
# Sax: Start a motif, leave it hanging
# F7, G7, A7, Bb7 (F7 in F major, but with a twist)
# Play F7 (F, A, C, E), then G7 (G, B, D, F#), then A7 (A, C#, E, G), then Bb7 (Bb, D, F, Ab)

# F7 (F, A, C, E) - start on beat 1, end on beat 2
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75)
sax.notes.append(note)

# Bass: F (D2), then Bb (F2), then Eb (A2), then Ab (C3)
note = pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.5 + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=43, start=1.5 + 0.375, end=1.5 + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=40, start=1.5 + 0.75, end=1.5 + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=44, start=1.5 + 1.125, end=1.5 + 1.5)
bass.notes.append(note)

# Piano: Fmaj7 (F, A, C, E) on bar 2
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: G7 (G, B, D, F#) - start on beat 1, end on beat 2
note = pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.25)
sax.notes.append(note)

# Bass: Bb (F2), then Eb (A2), then Ab (C3), then F (D2)
note = pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.0 + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=40, start=3.0 + 0.375, end=3.0 + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=44, start=3.0 + 0.75, end=3.0 + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=38, start=3.0 + 1.125, end=3.0 + 1.5)
bass.notes.append(note)

# Piano: G7 (G, B, D, F#) on bar 3
note = pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: A7 (A, C#, E, G) - start on beat 1, end on beat 2
note = pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=85, start=4.5, end=4.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.75)
sax.notes.append(note)

# Bass: Eb (A2), then Ab (C3), then F (D2), then G (E2)
note = pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.5 + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=44, start=4.5 + 0.375, end=4.5 + 0.75)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=38, start=4.5 + 0.75, end=4.5 + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=41, start=4.5 + 1.125, end=4.5 + 1.5)
bass.notes.append(note)

# Piano: A7 (A, C#, E, G) on bar 4
note = pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=85, start=4.5, end=4.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.5 + 0.375)
piano.notes.append(note)

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

midi.write('dante_intro.mid')
