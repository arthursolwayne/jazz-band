
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
# Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches
# F7 chord: F A C E
# Bass line: F - Gb - G - A - Bb - B - C - Db
bass_notes = [78, 77, 79, 81, 80, 82, 84, 83]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# F7: F A C E
# Bb7: Bb D F A
# C7: C E G B
# E7: E G# B D
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (1.5 + 0.375, 77),  # A
    (1.5 + 0.375, 78),  # C
    (1.5 + 0.375, 80),  # E
    (1.5 + 0.375, 87),  # F
    (1.5 + 0.75, 77),   # A
    (1.5 + 0.75, 78),   # C
    (1.5 + 0.75, 80),   # E
    (1.5 + 0.75, 87),   # F

    # Bar 3: Bb7 on 2 and 4
    (3.0 + 0.375, 73),  # D
    (3.0 + 0.375, 77),  # F
    (3.0 + 0.375, 80),  # A
    (3.0 + 0.375, 76),  # Bb
    (3.0 + 0.75, 73),   # D
    (3.0 + 0.75, 77),   # F
    (3.0 + 0.75, 80),   # A
    (3.0 + 0.75, 76),   # Bb

    # Bar 4: C7 on 2 and 4
    (4.5 + 0.375, 79),  # E
    (4.5 + 0.375, 81),  # G
    (4.5 + 0.375, 84),  # B
    (4.5 + 0.375, 78),  # C
    (4.5 + 0.75, 79),   # E
    (4.5 + 0.75, 81),   # G
    (4.5 + 0.75, 84),   # B
    (4.5 + 0.75, 78),   # C
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Drums: Bar 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))

# Drums: Bar 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))

# Drums: Bar 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F7: F A C E
# Motif: F - A - C - E (2nd bar), then F - A (4th bar)
# Bar 2: F (1.5), A (1.875), C (2.25), E (2.625)
# Bar 4: F (5.25), A (5.625)
sax_notes = [
    (1.5, 78),  # F
    (1.875, 80),  # A
    (2.25, 77),  # C
    (2.625, 80),  # E
    (5.25, 78),  # F
    (5.625, 80)   # A
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
