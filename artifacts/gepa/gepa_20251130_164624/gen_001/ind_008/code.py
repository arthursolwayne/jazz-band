
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1 (0.0 - 1.5s): Little Ray alone
drum_notes = [
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.1875),   # Hihat on 1 &
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.1875),  # Hihat on 3 &
    (38, 1.125, 0.375),  # Snare on 2
    (42, 1.125, 0.1875), # Hihat on 2 &
    (38, 1.5, 0.375),    # Snare on 4
    (42, 1.5, 0.1875),   # Hihat on 4 &
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass line (Marcus)
bass_notes = [
    (62, 1.5, 1.5),      # D (root)
    (64, 1.875, 2.25),   # Eb (chromatic approach)
    (65, 2.25, 2.625),   # E (chromatic approach)
    (62, 2.625, 3.0),    # D (root)
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane)
piano_notes = [
    (62, 1.5, 1.875),    # D7 (D, F#, A, C)
    (62, 1.875, 2.25),
    (62, 2.25, 2.625),
    (62, 2.625, 3.0),
    (66, 1.5, 1.875),    # A (7th)
    (66, 1.875, 2.25),
    (66, 2.25, 2.625),
    (66, 2.625, 3.0),
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax (Dante) - motif starting on D (62), with a suspension and release
sax_notes = [
    (62, 1.5, 1.875),    # D
    (62, 1.875, 2.25),   # D (suspension)
    (65, 2.25, 2.625),   # E (resolution)
    (62, 2.625, 3.0),    # D (return)
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bar 3 (3.0 - 4.5s): Full quartet
# Bass line (Marcus)
bass_notes = [
    (64, 3.0, 3.375),    # Eb
    (65, 3.375, 3.75),   # E
    (62, 3.75, 4.125),   # D
    (62, 4.125, 4.5),    # D
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane)
piano_notes = [
    (62, 3.0, 3.375),    # D7
    (62, 3.375, 3.75),
    (62, 3.75, 4.125),
    (62, 4.125, 4.5),
    (66, 3.0, 3.375),
    (66, 3.375, 3.75),
    (66, 3.75, 4.125),
    (66, 4.125, 4.5),
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax (Dante) - repeat motif with slight variation
sax_notes = [
    (62, 3.0, 3.375),    # D
    (62, 3.375, 3.75),   # D (suspension)
    (65, 3.75, 4.125),   # E (resolution)
    (62, 4.125, 4.5),    # D (return)
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Bar 4 (4.5 - 6.0s): Full quartet
# Bass line (Marcus)
bass_notes = [
    (65, 4.5, 4.875),    # E
    (64, 4.875, 5.25),   # Eb
    (62, 5.25, 5.625),   # D
    (62, 5.625, 6.0),    # D
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane)
piano_notes = [
    (62, 4.5, 4.875),    # D7
    (62, 4.875, 5.25),
    (62, 5.25, 5.625),
    (62, 5.625, 6.0),
    (66, 4.5, 4.875),
    (66, 4.875, 5.25),
    (66, 5.25, 5.625),
    (66, 5.625, 6.0),
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax (Dante) - complete the motif with an upward motion
sax_notes = [
    (62, 4.5, 4.875),    # D
    (62, 4.875, 5.25),   # D
    (65, 5.25, 5.625),   # E
    (67, 5.625, 6.0),    # F (surprise resolution)
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Drums for bar 2-4 (1.5 - 6.0s)
for bar in range(2, 5):
    start = 1.5 + (bar - 2) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1 &
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on 2 &
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.5625))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Hihat on 3 &
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 0.9375))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on 4 &
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.3125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
