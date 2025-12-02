
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
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
        for eighth in range(2):
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Start of melody, sax
# D7 chord: D, F#, A, C#
# Diane: 7th chords on 2 and 4
# Marcus: walking bass line
# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2 (1.5 - 3.0s)
# Sax motif: D, G, F#, D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.125))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=2.375, end=2.5))  # D

# Diane: D7 on 2 and 4
# Bar 2, beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875))  # C#

# Bar 2, beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.375, end=2.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.5))  # C#

# Marcus: Walking bass line
# D, F#, G, A, D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.0))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=2.125, end=2.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=49, start=2.375, end=2.5))  # A

# Bar 3: sax continues motif, Diane plays D7 on 2 and 4, Marcus walks, drums
# Bar 3 (3.0 - 4.5s)
# Repeat sax motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.625))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0))  # D

# Diane: D7 on 2 and 4
# Bar 3, beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.375))  # C#

# Bar 3, beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.875, end=4.0))  # C#

# Marcus: Walking bass line
# D, F#, G, A, D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.125))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.5))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=3.625, end=3.75))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=49, start=3.875, end=4.0))  # A

# Drums
for beat in range(4):
    time = 3.0 + beat * 0.375
    if beat == 0 or beat == 2:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    if beat == 1 or beat == 3:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    for eighth in range(2):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

# Bar 4: sax continues motif, Diane plays D7 on 2 and 4, Marcus walks, drums
# Bar 4 (4.5 - 6.0s)
# Repeat sax motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625))  # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875))  # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.125))  # F#
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.375, end=5.5))  # D

# Diane: D7 on 2 and 4
# Bar 4, beat 2
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=4.875))  # C#

# Bar 4, beat 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.375, end=5.5))  # C#

# Marcus: Walking bass line
# D, F#, G, A, D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.625))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.0))  # F#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=48, start=5.125, end=5.25))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=49, start=5.375, end=5.5))  # A

# Drums
for beat in range(4):
    time = 4.5 + beat * 0.375
    if beat == 0 or beat == 2:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.125))
    if beat == 1 or beat == 3:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.125))
    for eighth in range(2):
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.0625))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
