
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

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    (1.5, 62),    # D4
    (1.875, 63),  # Eb4
    (2.25, 64),   # E4
    (2.625, 65),  # F4
    (2.875, 67),  # G4
    (3.25, 65),   # F4
    (3.625, 64),  # E4
    (4.0, 62),    # D4
    (4.375, 60),  # C4
    (4.75, 62),   # D4
    (5.125, 64),  # E4
    (5.5, 65),    # F4
    (5.875, 67),  # G4
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    (1.875, 67), (1.875, 71), (1.875, 72), (1.875, 74),  # G7
    (2.625, 67), (2.625, 71), (2.625, 72), (2.625, 74),  # G7
    (3.625, 69), (3.625, 73), (3.625, 74), (3.625, 76),  # A7
    (4.75, 69), (4.75, 73), (4.75, 74), (4.75, 76)       # A7
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Sax (Dante) - short motif, make it sing
sax_notes = [
    (1.5, 65),   # E5
    (1.75, 67),  # G5
    (2.0, 65),   # E5
    (2.25, 67),  # G5
    (2.5, 69),   # A5
    (2.75, 67),  # G5
    (3.0, 65),   # E5
    (3.25, 62),  # D5
    (3.5, 65),   # E5
    (3.75, 67),  # G5
    (4.0, 69),   # A5
    (4.25, 67),  # G5
    (4.5, 65),   # E5
    (4.75, 62),  # D5
    (5.0, 65),   # E5
    (5.25, 67),  # G5
    (5.5, 69),   # A5
    (5.75, 67),  # G5
    (6.0, 65)    # E5
]

for start, pitch in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start, end=start + 0.125))

# Drums in bars 2-4
# Kick on 1 and 3
for i in range(2, 4):
    start = i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5))

# Snare on 2 and 4
for i in range(2, 4):
    start = i * 1.5
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0))

# Hi-hat on every eighth
for i in range(2, 4):
    for j in range(0, 4):
        start = i * 1.5 + j * 0.375
        end = start + 0.125
        drums.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
