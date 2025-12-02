
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line, chromatic approaches
bass_notes = [
    (62, 1.5, 0.375),  # D3 on 1
    (63, 1.875, 0.375),  # Eb3 on 2
    (64, 2.25, 0.375),  # E3 on 3
    (65, 2.625, 0.375),  # F3 on 4
    (67, 3.0, 0.375),  # G3 on 1
    (68, 3.375, 0.375),  # G#3 on 2
    (69, 3.75, 0.375),  # A3 on 3
    (70, 4.125, 0.375),  # Bb3 on 4
    (72, 4.5, 0.375),  # B3 on 1
    (73, 4.875, 0.375),  # C4 on 2
    (74, 5.25, 0.375),  # C#4 on 3
    (75, 5.625, 0.375)   # D4 on 4
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 1.875, 0.375),  # G7 on 2
    (69, 1.875, 0.375),
    (71, 1.875, 0.375),
    (72, 1.875, 0.375),
    (67, 2.625, 0.375),  # G7 on 4
    (69, 2.625, 0.375),
    (71, 2.625, 0.375),
    (72, 2.625, 0.375),
    (67, 4.875, 0.375),  # G7 on 2
    (69, 4.875, 0.375),
    (71, 4.875, 0.375),
    (72, 4.875, 0.375),
    (67, 5.625, 0.375),  # G7 on 4
    (69, 5.625, 0.375),
    (71, 5.625, 0.375),
    (72, 5.625, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375))
    # Hihat on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.375))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 0.375, end=start + 0.75))
    # Hihat on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.375, end=start + 0.75))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125))
    # Hihat on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 0.75, end=start + 1.125))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start + 1.125, end=start + 1.5))
    # Hihat on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start + 1.125, end=start + 1.5))

# Dante on sax: one short motif, make it sing
# D5 -> C#5 -> D5 -> C#5 -> B4 -> A4 -> B4 -> A4 -> Bb4 -> A4 -> Bb4 -> A4
sax_notes = [
    (84, 1.5, 0.375),  # D5 on 1
    (83, 1.875, 0.375),  # C#5 on 2
    (84, 2.25, 0.375),  # D5 on 3
    (83, 2.625, 0.375),  # C#5 on 4
    (82, 3.0, 0.375),  # B4 on 1
    (80, 3.375, 0.375),  # A4 on 2
    (82, 3.75, 0.375),  # B4 on 3
    (80, 4.125, 0.375),  # A4 on 4
    (79, 4.5, 0.375),  # Bb4 on 1
    (80, 4.875, 0.375),  # A4 on 2
    (79, 5.25, 0.375),  # Bb4 on 3
    (80, 5.625, 0.375)   # A4 on 4
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
