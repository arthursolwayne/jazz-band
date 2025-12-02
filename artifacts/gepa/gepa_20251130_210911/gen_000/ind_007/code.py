
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
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
# Sax melody: F7 -> A7 -> Bb7 -> C7 (Motif)
sax_notes = [
    (84, 1.5, 0.375),   # F7
    (87, 1.875, 0.375), # A7
    (88, 2.25, 0.375),  # Bb7
    (90, 2.625, 0.375)  # C7
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in F (F -> G -> A -> Bb -> C -> D -> Eb -> F)
bass_notes = [
    (53, 1.5, 0.375),   # F
    (55, 1.875, 0.375), # G
    (57, 2.25, 0.375),  # A
    (58, 2.625, 0.375), # Bb
    (60, 3.0, 0.375),   # C
    (62, 3.375, 0.375), # D
    (63, 3.75, 0.375),  # Eb
    (53, 4.125, 0.375)  # F
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    (53, 1.875, 0.375), # F
    (57, 1.875, 0.375), # Bb
    # Bar 3: A7 on beat 2
    (58, 3.375, 0.375), # A
    (62, 3.375, 0.375), # D
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax repeats motif but an octave lower (F6 -> A6 -> Bb6 -> C6)
sax_notes = [
    (72, 3.0, 0.375),   # F6
    (75, 3.375, 0.375), # A6
    (76, 3.75, 0.375),  # Bb6
    (78, 4.125, 0.375)  # C6
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in F (F -> G -> A -> Bb -> C -> D -> Eb -> F)
bass_notes = [
    (53, 3.0, 0.375),   # F
    (55, 3.375, 0.375), # G
    (57, 3.75, 0.375),  # A
    (58, 4.125, 0.375), # Bb
    (60, 4.5, 0.375),   # C
    (62, 4.875, 0.375), # D
    (63, 5.25, 0.375),  # Eb
    (53, 5.625, 0.375)  # F
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: A7 on beat 2
    (58, 3.375, 0.375), # A
    (62, 3.375, 0.375), # D
    # Bar 4: C7 on beat 2
    (60, 4.875, 0.375), # C
    (64, 4.875, 0.375), # E
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif again, but with a chromatic approach on the first note
sax_notes = [
    (83, 4.5, 0.375),   # Eb (chromatic approach)
    (84, 4.875, 0.375), # F7
    (87, 5.25, 0.375),  # A7
    (88, 5.625, 0.375)  # Bb7
]
for note, start, duration in sax_notes:
    n = pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration)
    sax.notes.append(n)

# Bass: Walking line in F (F -> G -> A -> Bb -> C -> D -> Eb -> F)
bass_notes = [
    (53, 4.5, 0.375),   # F
    (55, 4.875, 0.375), # G
    (57, 5.25, 0.375),  # A
    (58, 5.625, 0.375), # Bb
    (60, 6.0, 0.375),   # C
    (62, 6.375, 0.375), # D
    (63, 6.75, 0.375),  # Eb
    (53, 7.125, 0.375)  # F
]
for note, start, duration in bass_notes:
    n = pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration)
    bass.notes.append(n)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: C7 on beat 2
    (60, 4.875, 0.375), # C
    (64, 4.875, 0.375), # E
    # Bar 5: F7 on beat 2 (trimmed to fit 6s)
    (53, 6.375, 0.375), # F
    (57, 6.375, 0.375), # Bb
]
for note, start, duration in piano_notes:
    n = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(n)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2
    if bar == 2:
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
    # Bar 3
    elif bar == 3:
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
    # Bar 4
    elif bar == 4:
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

midi.write("dante_intro.mid")
