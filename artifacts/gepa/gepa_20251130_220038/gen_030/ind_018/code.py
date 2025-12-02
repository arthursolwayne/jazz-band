
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))  # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5))  # Hihat on every eighth

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 57),   # F (root)
    (1.875, 56), # E (chromatic)
    (2.25, 58),  # Gb (b3)
    (2.625, 55), # Eb (7)
    (2.875, 54), # D (chromatic)
    (3.25, 56),  # E (chromatic)
    (3.625, 58), # Gb
    (4.0, 55),   # Eb
    (4.25, 53),  # Db (chromatic)
    (4.625, 54), # D
    (5.0, 56),   # E
    (5.375, 58), # Gb
    (5.75, 55),  # Eb
    (6.0, 57)    # F
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Diane: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2
    (1.5, 62), (1.5, 69), (1.5, 71), (1.5, 74), # F7
    # Bar 3
    (2.25, 62), (2.25, 69), (2.25, 71), (2.25, 74), # F7
    # Bar 4
    (3.0, 62), (3.0, 69), (3.0, 71), (3.0, 74), # F7
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0))  # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0))    # Hihat on every eighth

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5))  # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5))    # Hihat on every eighth

drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)) # Kick on 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))  # Snare on 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0))    # Hihat on every eighth

# Dante: Tenor sax, one short motif, make it sing
# Fm motif: F, Ab, Bb, Eb (F - Ab - Bb - Eb)
# Start on 1.5, leave it hanging, come back and finish it
sax_notes = [
    (1.5, 65),     # F
    (1.875, 68),   # Ab
    (2.25, 67),    # Bb
    (2.625, 61),   # Eb
    (3.0, 65),     # F (repeat)
    (3.375, 68),   # Ab
    (3.75, 67),    # Bb
    (4.125, 61),   # Eb
    (4.5, 65),     # F
    (4.875, 68),   # Ab
    (5.25, 67),    # Bb
    (5.625, 61),   # Eb
    (6.0, 65)      # F
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
