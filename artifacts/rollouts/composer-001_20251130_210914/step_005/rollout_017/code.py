
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375),    # D
    (63, 1.875, 0.375),  # Eb
    (64, 2.25, 0.375),   # E
    (65, 2.625, 0.375),  # F
    (67, 2.625, 0.375),  # G
    (69, 3.0, 0.375),    # A
    (71, 3.375, 0.375),  # Bb
    (72, 3.75, 0.375),   # B
    (74, 4.125, 0.375),  # C
    (76, 4.5, 0.375),    # C#
    (77, 4.875, 0.375),  # D
    (79, 5.25, 0.375),   # D#
    (81, 5.625, 0.375),  # E
    (82, 6.0, 0.375)     # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    (67, 1.5, 0.375),    # G7 on 1
    (71, 1.5, 0.375),
    (74, 1.5, 0.375),
    (69, 1.5, 0.375),
    (71, 1.875, 0.375),  # Bb7 on 2
    (74, 1.875, 0.375),
    (76, 1.875, 0.375),
    (71, 1.875, 0.375),
    (67, 2.25, 0.375),   # G7 on 3
    (71, 2.25, 0.375),
    (74, 2.25, 0.375),
    (69, 2.25, 0.375),
    (71, 2.625, 0.375),  # Bb7 on 4
    (74, 2.625, 0.375),
    (76, 2.625, 0.375),
    (71, 2.625, 0.375),
    (67, 3.0, 0.375),    # G7 on 1
    (71, 3.0, 0.375),
    (74, 3.0, 0.375),
    (69, 3.0, 0.375),
    (71, 3.375, 0.375),  # Bb7 on 2
    (74, 3.375, 0.375),
    (76, 3.375, 0.375),
    (71, 3.375, 0.375),
    (67, 3.75, 0.375),   # G7 on 3
    (71, 3.75, 0.375),
    (74, 3.75, 0.375),
    (69, 3.75, 0.375),
    (71, 4.125, 0.375),  # Bb7 on 4
    (74, 4.125, 0.375),
    (76, 4.125, 0.375),
    (71, 4.125, 0.375),
    (67, 4.5, 0.375),    # G7 on 1
    (71, 4.5, 0.375),
    (74, 4.5, 0.375),
    (69, 4.5, 0.375),
    (71, 4.875, 0.375),  # Bb7 on 2
    (74, 4.875, 0.375),
    (76, 4.875, 0.375),
    (71, 4.875, 0.375),
    (67, 5.25, 0.375),   # G7 on 3
    (71, 5.25, 0.375),
    (74, 5.25, 0.375),
    (69, 5.25, 0.375),
    (71, 5.625, 0.375),  # Bb7 on 4
    (74, 5.625, 0.375),
    (76, 5.625, 0.375),
    (71, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(3):  # 3 bars
    for measure in [1.5 + bar * 1.5, 1.5 + bar * 1.5 + 0.375, 1.5 + bar * 1.5 + 0.75, 1.5 + bar * 1.5 + 1.125]:
        if measure % 1.5 == 0:  # Kick on 1 and 3
            drum_notes.append((36, measure, 0.375))
        if measure % 1.5 == 0.375:  # Snare on 2 and 4
            drum_notes.append((38, measure, 0.375))
        if measure % 0.375 == 0:  # Hihat on every eighth
            drum_notes.append((42, measure, 0.375))

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (69, 1.5, 0.375),    # D
    (71, 1.875, 0.375),  # E
    (72, 2.25, 0.375),   # F
    (69, 2.625, 0.375),  # D
    (67, 3.0, 0.375),    # G
    (69, 3.375, 0.375),  # D
    (71, 3.75, 0.375),   # E
    (72, 4.125, 0.375),  # F
    (69, 4.5, 0.375),    # D
    (71, 4.875, 0.375),  # E
    (72, 5.25, 0.375),   # F
    (69, 5.625, 0.375)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
