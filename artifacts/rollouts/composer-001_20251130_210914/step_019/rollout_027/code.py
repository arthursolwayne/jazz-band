
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

# Hihat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm
bass_notes = [59, 60, 62, 58, 59, 62, 60, 58]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 1: Dm7 (D, F, A, C)
    (50, 1.5, 1.75), (53, 1.5, 1.75), (57, 1.5, 1.75), (60, 1.5, 1.75),
    # Bar 2, beat 2: G7 (G, B, D, F)
    (55, 1.875, 2.125), (58, 1.875, 2.125), (62, 1.875, 2.125), (64, 1.875, 2.125),
    # Bar 2, beat 3: Dm7 (D, F, A, C)
    (50, 2.25, 2.5), (53, 2.25, 2.5), (57, 2.25, 2.5), (60, 2.25, 2.5),
    # Bar 2, beat 4: C7 (C, E, G, B)
    (60, 2.625, 2.875), (64, 2.625, 2.875), (67, 2.625, 2.875), (71, 2.625, 2.875)
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax: Motif (D, F, G, C)
sax_notes = [
    (50, 1.5, 1.75),  # D
    (53, 1.75, 2.0),  # F
    (57, 2.0, 2.25),  # G
    (60, 2.25, 2.5)   # C
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm
bass_notes = [59, 60, 62, 58, 59, 62, 60, 58]
for i, note in enumerate(bass_notes):
    start = 3.0 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 1: Dm7 (D, F, A, C)
    (50, 3.0, 3.25), (53, 3.0, 3.25), (57, 3.0, 3.25), (60, 3.0, 3.25),
    # Bar 3, beat 2: G7 (G, B, D, F)
    (55, 3.375, 3.625), (58, 3.375, 3.625), (62, 3.375, 3.625), (64, 3.375, 3.625),
    # Bar 3, beat 3: Dm7 (D, F, A, C)
    (50, 3.75, 4.0), (53, 3.75, 4.0), (57, 3.75, 4.0), (60, 3.75, 4.0),
    # Bar 3, beat 4: C7 (C, E, G, B)
    (60, 4.125, 4.375), (64, 4.125, 4.375), (67, 4.125, 4.375), (71, 4.125, 4.375)
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax: Motif variation (D, F, Bb, D)
sax_notes = [
    (50, 3.0, 3.25),  # D
    (53, 3.25, 3.5),  # F
    (58, 3.5, 3.75),  # Bb
    (50, 3.75, 4.0)   # D
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm
bass_notes = [59, 60, 62, 58, 59, 62, 60, 58]
for i, note in enumerate(bass_notes):
    start = 4.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 1: Dm7 (D, F, A, C)
    (50, 4.5, 4.75), (53, 4.5, 4.75), (57, 4.5, 4.75), (60, 4.5, 4.75),
    # Bar 4, beat 2: G7 (G, B, D, F)
    (55, 4.875, 5.125), (58, 4.875, 5.125), (62, 4.875, 5.125), (64, 4.875, 5.125),
    # Bar 4, beat 3: Dm7 (D, F, A, C)
    (50, 5.25, 5.5), (53, 5.25, 5.5), (57, 5.25, 5.5), (60, 5.25, 5.5),
    # Bar 4, beat 4: Dm7 (D, F, A, C)
    (50, 5.625, 5.875), (53, 5.625, 5.875), (57, 5.625, 5.875), (60, 5.625, 5.875)
]
for pitch, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end))

# Sax: Motif resolution (D, F, G, D)
sax_notes = [
    (50, 4.5, 4.75),  # D
    (53, 4.75, 5.0),  # F
    (57, 5.0, 5.25),  # G
    (50, 5.25, 5.5)   # D
]
for pitch, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=end))

# Drums: Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.875, end=6.0))

# Hihat on every eighth
for i in range(0, 4):
    start = 4.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
