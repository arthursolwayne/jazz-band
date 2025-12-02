
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth note
for i in range(0, 4):
    hihat_start = i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Walking bass line in Fm (F, Eb, D, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=1.875, end=2.0),   # C
]
bass.notes.extend(bass_notes)

# Diane - 7th chords, comp on 2 and 4
# Fm7 on 1, Ab7 on 2, Bbm7 on 3, C7 on 4
# 2 and 4: comping
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.625),  # D

    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=61, start=1.75, end=1.875),  # Db
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=1.75, end=1.875),  # Bb

    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=2.0, end=2.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.125),  # D
]
piano.notes.extend(piano_notes)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875))
for i in range(4):
    hihat_start = 1.5 + i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - Walking bass line in Fm (F, Eb, D, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.5),   # C
]
bass.notes.extend(bass_notes)

# Diane - 7th chords, comp on 2 and 4
# Fm7 on 1, Ab7 on 2, Bbm7 on 3, C7 on 4
# 2 and 4: comping
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.125),  # D

    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=61, start=3.25, end=3.375),  # Db
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=3.25, end=3.375),  # Bb

    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=3.5, end=3.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=3.5, end=3.625),  # D
]
piano.notes.extend(piano_notes)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.375))
for i in range(4):
    hihat_start = 3.0 + i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - Walking bass line in Fm (F, Eb, D, C)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.0),   # C
]
bass.notes.extend(bass_notes)

# Diane - 7th chords, comp on 2 and 4
# Fm7 on 1, Ab7 on 2, Bbm7 on 3, C7 on 4
# 2 and 4: comping
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.625),  # D

    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=61, start=4.75, end=4.875),  # Db
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=4.75, end=4.875),  # Bb

    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.0, end=5.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.125),  # D
]
piano.notes.extend(piano_notes)

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=4.875))
for i in range(4):
    hihat_start = 4.5 + i * 0.375
    hihat_end = hihat_start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_end))

# Sax - Melody in Fm
# Whisper at first, then a cry. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: F, Ab, D, C (first bar)
# Then repeat with a slight variation

# Bar 2
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0))   # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.5))  # C

# Bar 3
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0))  # C

# Bar 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.5))  # C

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_russo.mid')
