
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))
for i in range(0, 1.5, 0.375):
    if i != 0.0 and i != 0.75 and i != 1.125:
        drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i, end=i + 0.375))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm with chromatic approaches
# Fm7: F, Ab, Bb, D
# Walking line with chromatic approaches
bass_notes = [
    (0.0, 53),  # F
    (0.375, 51),  # Eb (chromatic)
    (0.75, 50),  # D
    (1.125, 52),  # F
    (1.5, 53),  # F
    (1.875, 51),  # Eb
    (2.25, 50),  # D
    (2.625, 52),  # F
    (3.0, 53),  # F
    (3.375, 51),  # Eb
    (3.75, 50),  # D
    (4.125, 52),  # F
    (4.5, 53),  # F
    (4.875, 51),  # Eb
    (5.25, 50),  # D
    (5.625, 52),  # F
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start + 1.5, end=start + 1.5 + 0.375))

# Piano: 7th chords on 2 and 4
# Fm7: F, Ab, Bb, D
# Bb7: Bb, D, F, Ab

# Bar 2: Fm7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.25))

# Bar 3: Bb7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75))

# Bar 4: Fm7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25))

# Saxophone: Melody over the next 4.5 seconds (bars 2-4)
# Simple motif: F, Ab, Bb, F (one phrase with a space)
# Bar 2: F, Ab, Bb
# Bar 3: Rest
# Bar 4: F, Ab, Bb, F
sax_notes = [
    (1.5, 53),  # F
    (1.875, 51),  # Ab
    (2.25, 50),  # Bb
    (2.625, 53),  # F
    (3.0, 53),  # F
    (3.375, 51),  # Ab
    (3.75, 50),  # Bb
    (4.125, 53),  # F
    (4.5, 53),  # F
    (4.875, 51),  # Ab
    (5.25, 50),  # Bb
    (5.625, 53),  # F
]
for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Drums in bars 2-4: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on every eighth
    for i in range(0, 1.5, 0.375):
        if i != 0.0 and i != 0.75 and i != 1.125:
            drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i, end=bar_start + i + 0.375))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
