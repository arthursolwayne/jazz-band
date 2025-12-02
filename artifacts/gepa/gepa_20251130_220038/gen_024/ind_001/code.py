
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm7 -> Bb -> Eb -> Ab (motif)
sax_notes = [
    (87, 1.5, 0.375),  # Fm7 (F, Ab, Bb, Db) -> F (87)
    (80, 1.875, 0.375),  # Bb (80)
    (83, 2.25, 0.375),  # Eb (83)
    (86, 2.625, 0.375)  # Ab (86)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (87, 1.5, 0.375),  # F
    (86, 1.875, 0.375),  # Eb
    (84, 2.25, 0.375),  # D
    (82, 2.625, 0.375),  # C
    (83, 3.0, 0.375)    # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (87, 1.875, 1.0),  # Fm7: F, Ab, Bb, Db
    (84, 1.875, 1.0),
    (80, 1.875, 1.0),
    (82, 1.875, 1.0),
    (87, 2.625, 1.0),  # Fm7 again
    (84, 2.625, 1.0),
    (80, 2.625, 1.0),
    (82, 2.625, 1.0)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif starting from Bb, but with variation
sax_notes = [
    (80, 3.0, 0.375),  # Bb
    (83, 3.375, 0.375),  # Eb
    (86, 3.75, 0.375),  # Ab
    (87, 4.125, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (80, 3.0, 0.375),  # Bb
    (82, 3.375, 0.375),  # C
    (83, 3.75, 0.375),  # Eb
    (84, 4.125, 0.375),  # D
    (87, 4.5, 0.375)     # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (80, 3.375, 1.0),  # Bb7: Bb, Db, F, Ab
    (82, 3.375, 1.0),
    (87, 3.375, 1.0),
    (86, 3.375, 1.0),
    (80, 4.125, 1.0),  # Bb7 again
    (82, 4.125, 1.0),
    (87, 4.125, 1.0),
    (86, 4.125, 1.0)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif again, but with a slight twist
sax_notes = [
    (87, 4.5, 0.375),  # F
    (80, 4.875, 0.375),  # Bb
    (83, 5.25, 0.375),  # Eb
    (86, 5.625, 0.375)  # Ab
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bass: Walking line in Fm
bass_notes = [
    (87, 4.5, 0.375),  # F
    (82, 4.875, 0.375),  # C
    (83, 5.25, 0.375),  # Eb
    (84, 5.625, 0.375),  # D
    (87, 6.0, 0.375)     # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    (87, 4.875, 1.0),  # Fm7: F, Ab, Bb, Db
    (84, 4.875, 1.0),
    (80, 4.875, 1.0),
    (82, 4.875, 1.0),
    (87, 5.625, 1.0),  # Fm7 again
    (84, 5.625, 1.0),
    (80, 5.625, 1.0),
    (82, 5.625, 1.0)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Bar 2
    if bar == 2:
        drum_notes = [
            (36, start, 0.375),  # Kick on 1
            (42, start, 0.375),  # Hihat on 1
            (38, start + 0.375, 0.375),  # Snare on 2
            (42, start + 0.375, 0.375),  # Hihat on 2
            (36, start + 0.75, 0.375),  # Kick on 3
            (42, start + 0.75, 0.375),  # Hihat on 3
            (38, start + 1.125, 0.375),  # Snare on 4
            (42, start + 1.125, 0.375)   # Hihat on 4
        ]
    # Bar 3
    elif bar == 3:
        drum_notes = [
            (36, start, 0.375),  # Kick on 1
            (42, start, 0.375),  # Hihat on 1
            (38, start + 0.375, 0.375),  # Snare on 2
            (42, start + 0.375, 0.375),  # Hihat on 2
            (36, start + 0.75, 0.375),  # Kick on 3
            (42, start + 0.75, 0.375),  # Hihat on 3
            (38, start + 1.125, 0.375),  # Snare on 4
            (42, start + 1.125, 0.375)   # Hihat on 4
        ]
    # Bar 4
    elif bar == 4:
        drum_notes = [
            (36, start, 0.375),  # Kick on 1
            (42, start, 0.375),  # Hihat on 1
            (38, start + 0.375, 0.375),  # Snare on 2
            (42, start + 0.375, 0.375),  # Hihat on 2
            (36, start + 0.75, 0.375),  # Kick on 3
            (42, start + 0.75, 0.375),  # Hihat on 3
            (38, start + 1.125, 0.375),  # Snare on 4
            (42, start + 1.125, 0.375)   # Hihat on 4
        ]
    for note, start_time, duration in drum_notes:
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=start_time + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
