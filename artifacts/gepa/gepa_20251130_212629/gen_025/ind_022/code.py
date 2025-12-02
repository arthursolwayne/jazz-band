
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
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
# Walking line with chromatic approaches
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.6875))    # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=1.6875, end=1.875))  # C#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0625))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=2.0625, end=2.25))   # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.4375))   # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=2.4375, end=2.625))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=2.8125))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=2.8125, end=3.0))    # C#

bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.1875))    # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=3.1875, end=3.375))  # C#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.5625))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.5625, end=3.75))   # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=3.9375))   # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.9375, end=4.125))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.3125))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=4.3125, end=4.5))    # C#

bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.6875))    # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=4.6875, end=4.875))  # C#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.0625))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=5.0625, end=5.25))   # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.4375))   # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=5.4375, end=5.625))  # F
bass.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=5.8125))  # D
bass.notes.append(pretty_midi.Note(velocity=90, pitch=49, start=5.8125, end=6.0))    # C#

# Piano (Diane) - 7th chords, comp on 2 and 4
# Bar 2 (1.5 - 2.25s)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.6875))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=1.6875))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=1.5, end=1.6875))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=77, start=1.5, end=1.6875))  # Bb

# Bar 3 (2.25 - 3.0s)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=72, start=2.25, end=2.4375))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.4375))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.4375))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=77, start=2.25, end=2.4375))  # Bb

# Bar 4 (3.0 - 3.75s)
piano.notes.append(pretty_midi.Note(velocity=85, pitch=72, start=3.0, end=3.1875))  # D
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.1875))  # F
piano.notes.append(pretty_midi.Note(velocity=85, pitch=76, start=3.0, end=3.1875))  # A
piano.notes.append(pretty_midi.Note(velocity=85, pitch=77, start=3.0, end=3.1875))  # Bb

# Saxophone (Dante) - short motif, make it sing
# Bar 2 (1.5 - 2.25s)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.75))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.0, end=2.25))  # Bb

# Bar 3 (2.25 - 3.0s)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=2.75, end=3.0))  # D

# Bar 4 (3.0 - 3.75s)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25))  # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.75))  # Bb

# Drums for bars 2-4
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.1875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=5.75))

# Hihat on every eighth
for i in range(1.5, 6.0, 0.1875):
    if i % 0.375 < 0.1875:  # every eighth note
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i, end=i + 0.1875))

# Add the instruments
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dante_intro.mid")
