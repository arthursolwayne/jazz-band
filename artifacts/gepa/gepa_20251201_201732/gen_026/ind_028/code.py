
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
            note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
            drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Diane plays Fm7 (F, A, C, D), comp on 2 and 4
# Bar 3: Diane plays Bbm7 (Bb, Db, F, G), comp on 2 and 4
# Bar 4: Diane plays Eb7 (Eb, G, Bb, D), comp on 2 and 4

# Marcus: Walking line, roots and fifths with chromatic approaches
# Bar 2: F, Gb, G, A
# Bar 3: Bb, B, C, Db
# Bar 4: Eb, E, F, G

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2 (1.5s - 3.0s)
# Sax: F (70), Ab (78), Bb (71)
note = pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=1.5 + 0.75, end=1.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.875)
sax.notes.append(note)

# Diane: Fm7 (F, A, C, D)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=1.5 + 0.375)
piano.notes.append(note)

# Marcus: F, Gb, G, A
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=1.5 + 2.25, end=1.5 + 2.625)
bass.notes.append(note)

# Drums
for beat in range(4):
    time = 1.5 + beat * 0.375
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

# Bar 3 (3.0s - 4.5s)
# Sax: Bb (71), C (72), D (74), Eb (73)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.0 + 0.75, end=3.0 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=3.0 + 1.5, end=3.0 + 1.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=73, start=3.0 + 2.25, end=3.0 + 2.625)
sax.notes.append(note)

# Diane: Bbm7 (Bb, Db, F, G)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.0 + 0.375)
piano.notes.append(note)

# Marcus: Bb, B, C, Db
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.0 + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=72, start=3.0 + 0.75, end=3.0 + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=3.0 + 1.5, end=3.0 + 1.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=69, start=3.0 + 2.25, end=3.0 + 2.625)
bass.notes.append(note)

# Drums
for beat in range(4):
    time = 3.0 + beat * 0.375
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125)
        drums.notes.append(note)
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125)
        drums.notes.append(note)
    for eighth in range(2):
        note = pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625)
        drums.notes.append(note)

# Bar 4 (4.5s - 6.0s)
# Sax: Eb (73), F (76), G (78), A (77)
note = pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.5 + 0.375)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=4.5 + 0.75, end=4.5 + 1.125)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=4.5 + 1.5, end=4.5 + 1.875)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=77, start=4.5 + 2.25, end=4.5 + 2.625)
sax.notes.append(note)

# Diane: Eb7 (Eb, G, Bb, D)
note = pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.375)
piano.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=4.5 + 0.375)
piano.notes.append(note)

# Marcus: Eb, E, F, G
note = pretty_midi.Note(velocity=100, pitch=73, start=4.5, end=4.5 + 0.375)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=74, start=4.5 + 0.75, end=4.5 + 1.125)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=76, start=4.5 + 1.5, end=4.5 + 1.875)
bass.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=78, start=4.5 + 2.25, end=4.5 + 2.625)
bass.notes.append(note)

# Drums
for beat in range(4):
    time = 4.5 + beat * 0.375
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
# midi.write disabled
