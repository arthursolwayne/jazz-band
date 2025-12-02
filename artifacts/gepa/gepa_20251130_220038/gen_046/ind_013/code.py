
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line with chromatic approaches
bass_notes = [
    (1.5, 62), (1.875, 63), (2.25, 60), (2.625, 59),
    (3.0, 62), (3.375, 63), (3.75, 60), (4.125, 59),
    (4.5, 62), (4.875, 63), (5.25, 60), (5.625, 59)
]
for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (1.5, 67), (1.5, 71), (1.5, 72), (1.5, 69),  # D7
    (2.25, 67), (2.25, 71), (2.25, 72), (2.25, 69),  # D7
    (3.0, 69), (3.0, 73), (3.0, 74), (3.0, 71),  # G7
    (3.75, 67), (3.75, 71), (3.75, 72), (3.75, 69),  # D7
    (4.5, 69), (4.5, 73), (4.5, 74), (4.5, 71),  # G7
    (5.25, 67), (5.25, 71), (5.25, 72), (5.25, 69)   # D7
]
for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.375))

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on every eighth
    for i in range(0, 4):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875))

# Dante on sax: short motif, make it sing, start it, leave it hanging, come back and finish
# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75))       # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0))       # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25))       # G
# Bar 3: Leave it hanging, let it breathe
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25))       # E
# Bar 4: Come back and finish it
sax.notes.append(pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75))       # D
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0))       # E
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25))       # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5))       # A
sax.notes.append(pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75))       # G
sax.notes.append(pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0))       # E

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
