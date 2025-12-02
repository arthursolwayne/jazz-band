
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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

# Hi-hat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
# C D Eb F G Ab A Bb
bass_notes = [
    (1.5, 60),  # C
    (1.875, 62),  # D
    (2.25, 61),  # Eb
    (2.625, 64),  # F
    (3.0, 67),  # G
    (3.375, 65),  # Ab
    (3.75, 69),  # A
    (4.125, 67),  # Bb
    (4.5, 67),  # Bb
    (4.875, 69),  # A
    (5.25, 67),  # G
    (5.625, 64),  # F
    (6.0, 62),  # D
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Piano (Diane) - 7th chords on 2 and 4
# C7 on 2 (1.875)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.0))

# F7 on 4 (3.375)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.5))

# Sax melody (Dante) - short motif, make it sing
# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0))   # F

# Bar 3: Fill in the space
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.625))   # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0))   # F

# Bar 4: End the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75))   # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0))   # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25))   # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5))   # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75))   # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0))   # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25))   # C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5))   # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75))   # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0))   # G

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write('dante_intro.mid')
