
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

# Hi-hat on every eighth note
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
# Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (1.5, 62, 0.375),  # D
    (1.875, 63, 0.375), # Eb
    (2.25, 60, 0.375),  # C
    (2.625, 61, 0.375), # Db
    (2.875, 59, 0.375), # Bb
    (3.25, 60, 0.375),  # C
    (3.625, 62, 0.375), # D
    (4.0, 63, 0.375),   # Eb
    (4.375, 61, 0.375), # Db
    (4.75, 60, 0.375),  # C
    (5.125, 59, 0.375), # Bb
    (5.5, 60, 0.375),   # C
    (5.875, 62, 0.375), # D
]

for start, pitch, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Piano - Diane
# 7th chords on 2 and 4, comp, stay out of the way
diane_notes = [
    # Bar 2 (1.5 - 2.0s)
    (1.5, 62, 0.125),  # D7: D, F#, A, C
    (1.5, 64, 0.125),
    (1.5, 67, 0.125),
    (1.5, 60, 0.125),
    (1.625, 62, 0.125),
    (1.625, 64, 0.125),
    (1.625, 67, 0.125),
    (1.625, 60, 0.125),
    (1.75, 62, 0.125),
    (1.75, 64, 0.125),
    (1.75, 67, 0.125),
    (1.75, 60, 0.125),

    # Bar 3 (2.0 - 2.5s)
    (2.0, 62, 0.125),  # D7
    (2.0, 64, 0.125),
    (2.0, 67, 0.125),
    (2.0, 60, 0.125),
    (2.125, 62, 0.125),
    (2.125, 64, 0.125),
    (2.125, 67, 0.125),
    (2.125, 60, 0.125),
    (2.25, 62, 0.125),
    (2.25, 64, 0.125),
    (2.25, 67, 0.125),
    (2.25, 60, 0.125),

    # Bar 4 (2.5 - 3.0s)
    (2.5, 62, 0.125),  # D7
    (2.5, 64, 0.125),
    (2.5, 67, 0.125),
    (2.5, 60, 0.125),
    (2.625, 62, 0.125),
    (2.625, 64, 0.125),
    (2.625, 67, 0.125),
    (2.625, 60, 0.125),
    (2.75, 62, 0.125),
    (2.75, 64, 0.125),
    (2.75, 67, 0.125),
    (2.75, 60, 0.125),
]

for start, pitch, duration in diane_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Sax - Dante
# Short motif, starts on 2 and 3, ends on 4 with a rest
# Dm7: D, F#, A, C
sax_notes = [
    (1.75, 62, 0.2),    # D (start on 2)
    (1.95, 64, 0.3),    # F#
    (2.25, 67, 0.2),    # A
    (2.45, 60, 0.3),    # C
    (2.75, 62, 0.2),    # D (start on 3)
    (2.95, 64, 0.3),    # F#
    (3.25, 67, 0.2),    # A
    (3.45, 60, 0.3),    # C
    (3.75, 62, 0.2),    # D (start on 4)
    (3.95, 64, 0.3),    # F#
    (4.25, 67, 0.2),    # A
    (4.45, 60, 0.3),    # C
    (4.75, 62, 0.2),    # D (start on 4)
    (4.95, 64, 0.3),    # F#
    (5.25, 67, 0.2),    # A
    (5.45, 60, 0.3),    # C
    (5.75, 62, 0.2),    # D
    (5.95, 64, 0.2),    # F#
]

for start, pitch, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + duration))

# Drums continue
# Bar 2 (1.5 - 2.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.625, end=1.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.75, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0))

# Bar 3 (2.0 - 2.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.125, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.5))

# Bar 4 (2.5 - 3.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=2.875))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=2.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.0))

# Final bar (3.0 - 6.0s) - lead into the melody with space and tension
# Bar 5: No drums, but sax and bass continue
# Bar 6: No drums, but sax and bass continue
# Bar 7: No drums, but sax and bass continue
# Bar 8: No drums, but sax and bass continue

# Keep the same rhythm but add variation
# Bar 5 (3.0 - 3.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.375))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.125, end=3.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.5))

# Bar 6 (3.5 - 4.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=3.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.625, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=3.875, end=4.0))

# Bar 7 (4.0 - 4.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.375))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.375, end=4.5))

# Bar 8 (4.5 - 5.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=4.875))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.625, end=4.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.75, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0))

# Bar 9 (5.0 - 5.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.0, end=5.375))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.125, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.5))

# Bar 10 (5.5 - 6.0s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.5, end=5.875))  # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.75, end=5.875))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.75, end=5.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=5.875, end=6.0))

# Add final rest in sax to make it a question
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.95, end=6.0))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
