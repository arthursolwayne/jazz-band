
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
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bar 2: Full quartet (1.5 - 3.0s)
# Diane: C7, Eb7, F7, Ab7 (comp on 2 and 4)
for i in range(2):
    start = 1.5 + i * 1.5
    # Diane
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start + 0.375, end=start + 0.75))  # C7
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start + 1.125, end=start + 1.5))  # C7
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 1.125, end=start + 1.5))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 1.125, end=start + 1.5))
    # Marcus
    # Walking line in Fm: F, Gb, E, D, C, Bb, A, Ab
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=34, start=start, end=start + 0.375))
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=35, start=start + 0.375, end=start + 0.75))
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=33, start=start + 0.75, end=start + 1.125))
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=31, start=start + 1.125, end=start + 1.5))
    # Dante
    # Sax motif: F, Ab, Bb, D (start, leave it hanging)
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=start, end=start + 0.375))
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=start + 0.375, end=start + 0.75))
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=start + 0.75, end=start + 1.125))
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=start + 1.125, end=start + 1.5))
    # Drums
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bar 3: Full quartet (3.0 - 4.5s)
# Diane: C7, Eb7, F7, Ab7 (comp on 2 and 4)
for i in range(2):
    start = 3.0 + i * 1.5
    # Diane
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start + 0.375, end=start + 0.75))  # C7
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start + 1.125, end=start + 1.5))  # C7
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 1.125, end=start + 1.5))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 1.125, end=start + 1.5))
    # Marcus
    # Walking line in Fm: F, Gb, E, D, C, Bb, A, Ab
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=34, start=start, end=start + 0.375))
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=35, start=start + 0.375, end=start + 0.75))
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=33, start=start + 0.75, end=start + 1.125))
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=31, start=start + 1.125, end=start + 1.5))
    # Dante
    # Sax motif: F, Ab, Bb, D (come back and finish it)
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=start, end=start + 0.375))
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=start + 0.375, end=start + 0.75))
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=start + 0.75, end=start + 1.125))
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=start + 1.125, end=start + 1.5))
    # Drums
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

# Bar 4: Full quartet (4.5 - 6.0s)
# Diane: C7, Eb7, F7, Ab7 (comp on 2 and 4)
for i in range(2):
    start = 4.5 + i * 1.5
    # Diane
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start + 0.375, end=start + 0.75))  # C7
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 0.375, end=start + 0.75))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=start + 1.125, end=start + 1.5))  # C7
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=start + 1.125, end=start + 1.5))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=start + 1.125, end=start + 1.5))
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=start + 1.125, end=start + 1.5))
    # Marcus
    # Walking line in Fm: F, Gb, E, D, C, Bb, A, Ab
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=34, start=start, end=start + 0.375))
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=35, start=start + 0.375, end=start + 0.75))
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=33, start=start + 0.75, end=start + 1.125))
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=31, start=start + 1.125, end=start + 1.5))
    # Dante
    # Sax motif: F, Ab, Bb, D (finish it)
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=65, start=start, end=start + 0.375))
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=68, start=start + 0.375, end=start + 0.75))
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=start + 0.75, end=start + 1.125))
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=start + 1.125, end=start + 1.5))
    # Drums
    # Kick on 1 and 3
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare on 2 and 4
    snare1 = pretty_midi.Note(velocity=110, pitch=38, start=start + 0.375, end=start + 0.75)
    snare2 = pretty_midi.Note(velocity=110, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat on every eighth
    for i in range(4):
        hihat = pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)
        drums.notes.append(hihat)
    drums.notes.extend([kick1, kick2, snare1, snare2])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
