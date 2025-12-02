
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
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (38, 0.75, 0.375),    # Snare on 2
    (42, 0.9375, 0.1875), # Hihat on &2
    (36, 1.125, 0.375),   # Kick on 3
    (42, 1.3125, 0.1875), # Hihat on &3
    (38, 1.875, 0.375),   # Snare on 4
    (42, 2.0625, 0.1875)  # Hihat on &4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line
bass_notes = [
    (62, 1.5, 1.5),       # D (root)
    (64, 1.875, 1.875),   # Eb (chromatic approach)
    (65, 2.25, 2.25),     # F (3rd)
    (62, 2.625, 2.625)    # D (root)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 1.875, 1.875),   # F7 (F, A, C, Eb)
    (69, 1.875, 1.875),
    (67, 1.875, 1.875),
    (65, 1.875, 1.875),
    (64, 2.625, 2.625),
    (69, 2.625, 2.625),
    (67, 2.625, 2.625),
    (65, 2.625, 2.625)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Dante: Melody
sax_notes = [
    (62, 1.5, 1.6875),    # D
    (64, 1.6875, 1.875),  # Eb
    (67, 1.875, 2.25),    # G
    (64, 2.25, 2.625),    # Eb
    (62, 2.625, 3.0)      # D
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line
bass_notes = [
    (65, 3.0, 3.0),       # F
    (67, 3.375, 3.375),   # G (chromatic approach)
    (69, 3.75, 3.75),     # A (5th)
    (67, 4.125, 4.125)    # G
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 3.375, 3.375),
    (69, 3.375, 3.375),
    (67, 3.375, 3.375),
    (65, 3.375, 3.375),
    (64, 4.125, 4.125),
    (69, 4.125, 4.125),
    (67, 4.125, 4.125),
    (65, 4.125, 4.125)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Dante: Melody
sax_notes = [
    (65, 3.0, 3.1875),    # F
    (67, 3.1875, 3.375),  # G
    (69, 3.375, 3.75),    # A
    (67, 3.75, 4.125),    # G
    (65, 4.125, 4.5)      # F
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line
bass_notes = [
    (67, 4.5, 4.5),       # G
    (69, 4.875, 4.875),   # A (chromatic approach)
    (71, 5.25, 5.25),     # Bb (7th)
    (69, 5.625, 5.625)    # A
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note[0], start=note[1], end=note[2]))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (64, 4.875, 4.875),
    (69, 4.875, 4.875),
    (67, 4.875, 4.875),
    (65, 4.875, 4.875),
    (64, 5.625, 5.625),
    (69, 5.625, 5.625),
    (67, 5.625, 5.625),
    (65, 5.625, 5.625)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Dante: Melody
sax_notes = [
    (67, 4.5, 4.6875),    # G
    (69, 4.6875, 4.875),  # A
    (72, 4.875, 5.25),    # C (chromatic off the beat)
    (69, 5.25, 5.625),    # A
    (67, 5.625, 6.0)      # G
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on &1
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + 0.1875, end=start + 0.1875 + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.75 + 0.375))
    # Hihat on &2
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + 0.9375, end=start + 0.9375 + 0.1875))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.125 + 0.375))
    # Hihat on &3
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + 1.3125, end=start + 1.3125 + 0.1875))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 1.875 + 0.375))
    # Hihat on &4
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start + 2.0625, end=start + 2.0625 + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
