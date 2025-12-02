
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

# Bass line: walking line, chromatic approaches
bass_notes = [
    (59, 1.5, 0.375),  # D
    (60, 1.875, 0.375),  # Eb (chromatic)
    (62, 2.25, 0.375),  # F
    (64, 2.625, 0.375),  # G
    (65, 2.625, 0.375),  # G# (chromatic)
    (67, 3.0, 0.375),  # A
    (69, 3.375, 0.375),  # Bb
    (71, 3.75, 0.375),  # B
    (72, 4.125, 0.375),  # C
    (73, 4.5, 0.375),  # C# (chromatic)
    (74, 4.875, 0.375),  # D
    (76, 5.25, 0.375),  # Eb
    (77, 5.625, 0.375),  # E (chromatic)
    (79, 6.0, 0.375)     # F
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375),  # F7 (F, A, C, Eb)
    (64, 1.5, 0.375),
    (65, 1.5, 0.375),
    (67, 1.5, 0.375),
    (62, 2.25, 0.375),  # F7
    (64, 2.25, 0.375),
    (65, 2.25, 0.375),
    (67, 2.25, 0.375),

    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 0.375),  # F7
    (64, 3.0, 0.375),
    (65, 3.0, 0.375),
    (67, 3.0, 0.375),
    (62, 3.75, 0.375),  # F7
    (64, 3.75, 0.375),
    (65, 3.75, 0.375),
    (67, 3.75, 0.375),

    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.375),  # F7
    (64, 4.5, 0.375),
    (65, 4.5, 0.375),
    (67, 4.5, 0.375),
    (62, 5.25, 0.375),  # F7
    (64, 5.25, 0.375),
    (65, 5.25, 0.375),
    (67, 5.25, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: short motif, start it, leave it hanging, come back and finish it
# Dm7 - Eb7 - F7 - G7 - Dm7
sax_notes = [
    (62, 1.5, 0.375),  # D
    (65, 1.875, 0.375),  # F
    (67, 2.25, 0.375),  # A
    (71, 2.625, 0.375),  # C (F7)
    (62, 3.0, 0.375),  # D
    (65, 3.375, 0.375),  # F
    (67, 3.75, 0.375),  # A
    (71, 4.125, 0.375),  # C (F7)
    (62, 4.5, 0.375),  # D
    (65, 4.875, 0.375),  # F
    (67, 5.25, 0.375),  # A
    (71, 5.625, 0.375)   # C
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4

    # Bar 3 (3.0 - 4.5s)
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4

    # Bar 4 (4.5 - 6.0s)
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
