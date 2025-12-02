
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F
bass_notes = [
    (45, 1.5, 0.375),   # F
    (46, 1.875, 0.375), # G
    (47, 2.25, 0.375),  # Ab
    (44, 2.625, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (53, 1.875, 0.375), # F7 (53 = F, 55 = A, 57 = C, 59 = E)
    (55, 1.875, 0.375),
    (57, 1.875, 0.375),
    (59, 1.875, 0.375),
    (53, 2.625, 0.375),
    (55, 2.625, 0.375),
    (57, 2.625, 0.375),
    (59, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: fill the bar
for i in range(4):
    start = 1.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625))

# Sax: Motif (1.5 - 3.0s)
sax_notes = [
    (62, 1.5, 0.375),   # G (start of motif)
    (65, 1.875, 0.375), # Bb
    (62, 2.25, 0.375),  # G
    (64, 2.625, 0.375)  # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in F
bass_notes = [
    (45, 3.0, 0.375),   # F
    (46, 3.375, 0.375), # G
    (47, 3.75, 0.375),  # Ab
    (44, 4.125, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (53, 3.375, 0.375), # F7
    (55, 3.375, 0.375),
    (57, 3.375, 0.375),
    (59, 3.375, 0.375),
    (53, 4.125, 0.375),
    (55, 4.125, 0.375),
    (57, 4.125, 0.375),
    (59, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: fill the bar
for i in range(4):
    start = 3.0 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125))

# Sax: Motif (3.0 - 4.5s)
sax_notes = [
    (62, 3.0, 0.375),   # G
    (65, 3.375, 0.375), # Bb
    (62, 3.75, 0.375),  # G
    (64, 4.125, 0.375)  # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in F
bass_notes = [
    (45, 4.5, 0.375),   # F
    (46, 4.875, 0.375), # G
    (47, 5.25, 0.375),  # Ab
    (44, 5.625, 0.375)  # E
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (53, 4.875, 0.375), # F7
    (55, 4.875, 0.375),
    (57, 4.875, 0.375),
    (59, 4.875, 0.375),
    (53, 5.625, 0.375),
    (55, 5.625, 0.375),
    (57, 5.625, 0.375),
    (59, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: fill the bar
for i in range(4):
    start = 4.5 + i * 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625))

# Sax: Motif (4.5 - 6.0s)
sax_notes = [
    (62, 4.5, 0.375),   # G
    (65, 4.875, 0.375), # Bb
    (62, 5.25, 0.375),  # G
    (64, 5.625, 0.375), # A
    (62, 6.0, 0.375)    # G (end on G)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
