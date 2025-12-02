
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(8):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    (1.5, 60),  # C
    (1.875, 61),  # C#
    (2.25, 62),  # D
    (2.625, 63),  # D#
    (3.0, 64),  # E
    (3.375, 65),  # F
    (3.75, 66),  # F#
    (4.125, 67),  # G
    (4.5, 68),  # G#
    (4.875, 69),  # A
    (5.25, 70),  # A#
    (5.625, 71),  # B
    (6.0, 72),  # C
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.375))

# Piano: 7th chords, comp on 2 and 4
# Bar 2: C7 (C, E, B, D)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875))

# Bar 3: D7 (D, F#, C#, E)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875))

# Bar 4: G7 (G, B, D, F)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125))
piano.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125))

# Sax: Motif
# First statement: C, D, E, B (1.5 - 2.0s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5))

# Second statement: E, D, C, B (3.0 - 3.5s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0))

# Final statement: C, D, E, B (5.0 - 5.5s)
sax.notes.append(pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.75, end=6.0))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
