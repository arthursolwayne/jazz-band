
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
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0))

# Hi-hat on every eighth
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
# F7 chord: F, A, C, E
# Bass line: F -> E -> D -> C -> B -> A -> G -> F
# Walking line with chromatic approaches

bass_notes = [
    # Bar 2
    (1.5, 77),  # F
    (1.875, 76),  # E
    (2.25, 74),  # D
    (2.625, 72),  # C

    # Bar 3
    (2.75, 71),  # B
    (3.125, 70),  # A
    (3.5, 69),  # G
    (3.875, 72),  # C

    # Bar 4
    (4.25, 72),  # C
    (4.625, 74),  # D
    (5.0, 76),  # E
    (5.375, 77)  # F
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25))

# Diane on piano: 7th chords on 2 and 4
# F7 chord: F (77), A (82), C (72), E (69)
# Rootless voicings: A (82), C (72), E (69), Bb (71)

piano_notes = [
    # Bar 2 (on 2 and 4)
    (1.875, 82),  # A
    (1.875, 72),  # C
    (1.875, 69),  # E
    (1.875, 71),  # Bb

    # Bar 3 (on 2 and 4)
    (3.125, 82),  # A
    (3.125, 72),  # C
    (3.125, 69),  # E
    (3.125, 71),  # Bb

    # Bar 4 (on 2 and 4)
    (4.625, 82),  # A
    (4.625, 72),  # C
    (4.625, 69),  # E
    (4.625, 71)   # Bb
]

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25))

# Dante on sax: one short motif, make it sing
# Start it, leave it hanging, come back and finish it

# F (87), G (88), Bb (80), A (82), G (88), F (87)
# Bar 2, beat 1
sax.notes.append(pretty_midi.Note(velocity=110, pitch=87, start=1.5, end=1.625))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=88, start=1.625, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=80, start=1.75, end=1.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=82, start=1.875, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=88, start=2.0, end=2.125))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=87, start=2.125, end=2.25))

# Bar 4, beat 3
sax.notes.append(pretty_midi.Note(velocity=110, pitch=88, start=4.625, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=80, start=4.75, end=4.875))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=82, start=4.875, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=87, start=5.0, end=5.125))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
