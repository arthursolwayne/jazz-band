
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.0, 0.1875),  # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in Dm
bass_notes = [
    (62, 1.5, 0.375),   # D (1)
    (60, 1.875, 0.375),  # Bb (2)
    (59, 2.25, 0.375),   # A (3)
    (62, 2.625, 0.375),  # D (4)
    (64, 3.0, 0.375),    # F (1)
    (62, 3.375, 0.375),  # D (2)
    (60, 3.75, 0.375),   # Bb (3)
    (59, 4.125, 0.375),  # A (4)
    (62, 4.5, 0.375),    # D (1)
    (64, 4.875, 0.375),  # F (2)
    (65, 5.25, 0.375),   # G (3)
    (62, 5.625, 0.375)   # D (4)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane - Piano comping on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2
    (64, 1.5, 0.1875),  # F7 (root)
    (67, 1.5, 0.1875),  # A
    (69, 1.5, 0.1875),  # C
    (71, 1.5, 0.1875),  # D
    (62, 1.875, 0.1875), # Bb7 (root)
    (65, 1.875, 0.1875), # D
    (67, 1.875, 0.1875), # F
    (69, 1.875, 0.1875), # G
    # Bar 3
    (64, 2.25, 0.1875),  # F7 (root)
    (67, 2.25, 0.1875),  # A
    (69, 2.25, 0.1875),  # C
    (71, 2.25, 0.1875),  # D
    (62, 2.625, 0.1875), # Bb7 (root)
    (65, 2.625, 0.1875), # D
    (67, 2.625, 0.1875), # F
    (69, 2.625, 0.1875), # G
    # Bar 4
    (64, 3.0, 0.1875),   # F7 (root)
    (67, 3.0, 0.1875),   # A
    (69, 3.0, 0.1875),   # C
    (71, 3.0, 0.1875),   # D
    (62, 3.375, 0.1875), # Bb7 (root)
    (65, 3.375, 0.1875), # D
    (67, 3.375, 0.1875), # F
    (69, 3.375, 0.1875), # G
    (64, 4.5, 0.1875),   # F7 (root)
    (67, 4.5, 0.1875),   # A
    (69, 4.5, 0.1875),   # C
    (71, 4.5, 0.1875),   # D
    (62, 4.875, 0.1875), # Bb7 (root)
    (65, 4.875, 0.1875), # D
    (67, 4.875, 0.1875), # F
    (69, 4.875, 0.1875)  # G
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Little Ray - Drums on bars 2-4
drum_notes_bars2_4 = [
    # Bar 2
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.5, 0.1875),  # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875),# Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875),# Hihat on 4
    # Bar 3
    (36, 3.0, 0.375),   # Kick on 1
    (42, 3.0, 0.1875),  # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875),# Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875),# Hihat on 4
    # Bar 4
    (36, 4.5, 0.375),   # Kick on 1
    (42, 4.5, 0.1875),  # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875),# Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes_bars2_4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - Tenor sax motif
# Motif: Dm7 -> G7 -> Cm7 -> F7
# D (62), F (64), A (67), C (69) -> G (67), Bb (62), D (64), F (66) -> C (60), Eb (62), G (67), Bb (69) -> F (64), A (67), C (69), E (71)
sax_notes = [
    # Bar 2
    (62, 1.5, 0.375),   # D (1)
    (67, 1.875, 0.375),  # G (2)
    (60, 2.25, 0.375),   # C (3)
    (64, 2.625, 0.375),  # F (4)
    # Bar 3
    (67, 3.0, 0.375),    # G (1)
    (62, 3.375, 0.375),  # Bb (2)
    (64, 3.75, 0.375),   # D (3)
    (66, 4.125, 0.375),  # F (4)
    # Bar 4
    (60, 4.5, 0.375),    # C (1)
    (62, 4.875, 0.375),  # Eb (2)
    (67, 5.25, 0.375),   # G (3)
    (69, 5.625, 0.375)   # Bb (4)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
