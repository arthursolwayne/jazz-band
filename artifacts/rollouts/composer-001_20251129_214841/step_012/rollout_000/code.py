
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

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hihat on every eighth
for i in range(4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches
# C - B - Bb - A - G - F - Eb - D - C
bass_notes = [60, 61, 60, 59, 58, 57, 56, 55, 60]
for i, note in enumerate(bass_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# C7 on 2, F7 on 4
# C7: C, E, Bb, B
# F7: F, A, D, E
chords = [
    # Bar 2, beat 1: rest
    # Bar 2, beat 2: C7
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.375),
    # Bar 2, beat 3: rest
    # Bar 2, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.125),
]

for note in chords:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C, D, Bb, C (saxophone in Bb, so C = Bb in concert)
# Play on 1, 2, 3, and 4 of bar 2
sax_notes = [60, 62, 67, 60]
for i, note in enumerate(sax_notes):
    start = 1.5 + (i * 0.375)
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line, chromatic approaches
# C - B - Bb - A - G - F - Eb - D - C
bass_notes = [60, 61, 60, 59, 58, 57, 56, 55, 60]
for i, note in enumerate(bass_notes):
    start = 3.0 + (i * 0.375)
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# C7 on 2, F7 on 4
# C7: C, E, Bb, B
# F7: F, A, D, E
chords = [
    # Bar 3, beat 1: rest
    # Bar 3, beat 2: C7
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=3.875),
    # Bar 3, beat 3: rest
    # Bar 3, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.625),
]

for note in chords:
    piano.notes.append(note)

# Sax: Motif again, but with a slight variation
# Motif: C, D, Bb, C
sax_notes = [60, 62, 67, 60]
for i, note in enumerate(sax_notes):
    start = 3.0 + (i * 0.375)
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=6.375, end=6.5))

# Hihat on every eighth
for i in range(4):
    start = 4.5 + (i * 0.375)
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bass: Walking line, chromatic approaches
# C - B - Bb - A - G - F - Eb - D - C
bass_notes = [60, 61, 60, 59, 58, 57, 56, 55, 60]
for i, note in enumerate(bass_notes):
    start = 4.5 + (i * 0.375)
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# C7 on 2, F7 on 4
# C7: C, E, Bb, B
# F7: F, A, D, E
chords = [
    # Bar 4, beat 1: rest
    # Bar 4, beat 2: C7
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.375),
    # Bar 4, beat 3: rest
    # Bar 4, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=53, start=6.0, end=6.125),
    pretty_midi.Note(velocity=90, pitch=58, start=6.0, end=6.125),
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.125),
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.125),
]

for note in chords:
    piano.notes.append(note)

# Sax: Motif again, but with a slight variation
# Motif: C, D, Bb, C
sax_notes = [60, 62, 67, 60]
for i, note in enumerate(sax_notes):
    start = 4.5 + (i * 0.375)
    end = start + 0.375
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
