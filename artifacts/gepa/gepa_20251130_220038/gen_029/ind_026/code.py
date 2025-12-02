
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
    dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(dr)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm motif
sax_notes = [
    (62, 1.5, 0.375),    # D
    (65, 1.875, 0.375),  # F
    (67, 2.25, 0.375),   # G
    (62, 2.625, 0.375)   # D
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in Dm
bass_notes = [
    (62, 1.5, 0.375),    # D
    (64, 1.875, 0.375),  # Eb
    (67, 2.25, 0.375),   # G
    (65, 2.625, 0.375)   # F
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4 (Cm7, F7)
piano_notes = [
    # Cm7 (C, Eb, Gb, Bb)
    (60, 1.875, 0.375),
    (64, 1.875, 0.375),
    (66, 1.875, 0.375),
    (67, 1.875, 0.375),
    # F7 (F, A, C, Eb)
    (65, 2.625, 0.375),
    (69, 2.625, 0.375),
    (72, 2.625, 0.375),
    (64, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    drum_notes = [
        (36, start, 0.375),   # Kick on 1
        (42, start, 0.1875),  # Hihat on 1
        (38, start + 0.375, 0.375), # Snare on 2
        (42, start + 0.375, 0.1875),# Hihat on 2
        (36, start + 0.75, 0.375),  # Kick on 3
        (42, start + 0.75, 0.1875), # Hihat on 3
        (38, start + 1.125, 0.375), # Snare on 4
        (42, start + 1.125, 0.1875) # Hihat on 4
    ]
    for note, start, duration in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
        drums.notes.append(dr)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif an octave higher
sax_notes = [
    (74, 3.0, 0.375),    # D
    (77, 3.375, 0.375),  # F
    (79, 3.75, 0.375),   # G
    (74, 4.125, 0.375)   # D
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in Dm
bass_notes = [
    (62, 3.0, 0.375),    # D
    (64, 3.375, 0.375),  # Eb
    (67, 3.75, 0.375),   # G
    (65, 4.125, 0.375)   # F
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4 (Cm7, F7)
piano_notes = [
    # Cm7 (C, Eb, Gb, Bb)
    (60, 3.375, 0.375),
    (64, 3.375, 0.375),
    (66, 3.375, 0.375),
    (67, 3.375, 0.375),
    # F7 (F, A, C, Eb)
    (65, 4.125, 0.375),
    (69, 4.125, 0.375),
    (72, 4.125, 0.375),
    (64, 4.125, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(3, 4):
    start = bar * 1.5
    drum_notes = [
        (36, start, 0.375),   # Kick on 1
        (42, start, 0.1875),  # Hihat on 1
        (38, start + 0.375, 0.375), # Snare on 2
        (42, start + 0.375, 0.1875),# Hihat on 2
        (36, start + 0.75, 0.375),  # Kick on 3
        (42, start + 0.75, 0.1875), # Hihat on 3
        (38, start + 1.125, 0.375), # Snare on 4
        (42, start + 1.125, 0.1875) # Hihat on 4
    ]
    for note, start, duration in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
        drums.notes.append(dr)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif with a twist on the last note
sax_notes = [
    (74, 4.5, 0.375),    # D
    (77, 4.875, 0.375),  # F
    (79, 5.25, 0.375),   # G
    (76, 5.625, 0.375)   # Eb (twist)
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in Dm
bass_notes = [
    (62, 4.5, 0.375),    # D
    (64, 4.875, 0.375),  # Eb
    (67, 5.25, 0.375),   # G
    (65, 5.625, 0.375)   # F
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4 (Cm7, F7)
piano_notes = [
    # Cm7 (C, Eb, Gb, Bb)
    (60, 4.875, 0.375),
    (64, 4.875, 0.375),
    (66, 4.875, 0.375),
    (67, 4.875, 0.375),
    # F7 (F, A, C, Eb)
    (65, 5.625, 0.375),
    (69, 5.625, 0.375),
    (72, 5.625, 0.375),
    (64, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(4, 4):
    start = bar * 1.5
    drum_notes = [
        (36, start, 0.375),   # Kick on 1
        (42, start, 0.1875),  # Hihat on 1
        (38, start + 0.375, 0.375), # Snare on 2
        (42, start + 0.375, 0.1875),# Hihat on 2
        (36, start + 0.75, 0.375),  # Kick on 3
        (42, start + 0.75, 0.1875), # Hihat on 3
        (38, start + 1.125, 0.375), # Snare on 4
        (42, start + 1.125, 0.1875) # Hihat on 4
    ]
    for note, start, duration in drum_notes:
        dr = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
        drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])

midi.save('dante_intro.mid')
