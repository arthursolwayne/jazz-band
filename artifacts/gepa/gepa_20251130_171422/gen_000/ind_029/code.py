
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
    (42, 0.375, 0.125),  # Hihat on 1&
    (38, 0.75, 0.375),   # Snare on 2
    (42, 0.75, 0.125),   # Hihat on 2&
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.125),  # Hihat on 3&
    (38, 1.5, 0.375),    # Snare on 4
    (42, 1.5, 0.125)     # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, Dm7 -> G7 -> Cm7 -> F7
bass_notes = [
    (62, 1.5, 0.375),      # D (root)
    (63, 1.875, 0.375),    # Eb (chromatic approach to G)
    (67, 2.25, 0.375),     # G
    (65, 2.625, 0.375),    # F# (chromatic approach to A)
    (69, 3.0, 0.375),      # A
    (67, 3.375, 0.375),    # G (chromatic approach to B)
    (71, 3.75, 0.375),     # B
    (69, 4.125, 0.375),    # A (chromatic approach to C)
    (72, 4.5, 0.375),      # C
    (71, 4.875, 0.375),    # B (chromatic approach to D)
    (74, 5.25, 0.375),     # D
    (72, 5.625, 0.375)     # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords on 2 and 4, Dm7, G7, Cm7, F7
piano_notes = [
    # Bar 2
    (62, 1.5, 0.125),  # D
    (67, 1.5, 0.125),  # G
    (69, 1.5, 0.125),  # Bb
    (72, 1.5, 0.125),  # C
    (67, 1.875, 0.125), # G
    (72, 1.875, 0.125), # C
    (74, 1.875, 0.125), # D
    (77, 1.875, 0.125), # F
    # Bar 3
    (67, 2.25, 0.125),  # G
    (72, 2.25, 0.125),  # B
    (74, 2.25, 0.125),  # D
    (77, 2.25, 0.125),  # F
    (67, 2.625, 0.125), # G
    (72, 2.625, 0.125), # B
    (74, 2.625, 0.125), # D
    (77, 2.625, 0.125), # F
    # Bar 4
    (60, 3.0, 0.125),   # C
    (65, 3.0, 0.125),   # G
    (67, 3.0, 0.125),   # Bb
    (72, 3.0, 0.125),   # C
    (65, 3.375, 0.125), # G
    (67, 3.375, 0.125), # Bb
    (72, 3.375, 0.125), # C
    (76, 3.375, 0.125), # E
    (60, 3.75, 0.125),  # C
    (64, 3.75, 0.125),  # F
    (67, 3.75, 0.125),  # A
    (72, 3.75, 0.125),  # C
    (64, 4.125, 0.125), # F
    (67, 4.125, 0.125), # A
    (72, 4.125, 0.125), # C
    (76, 4.125, 0.125)  # E
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.125),   # D
    (65, 1.625, 0.125), # F
    (67, 1.75, 0.125),  # G
    (69, 1.875, 0.125), # A
    (67, 2.0, 0.125),   # G
    (65, 2.125, 0.125), # F
    (62, 2.25, 0.125),  # D
    (60, 2.375, 0.125), # C
    (62, 2.5, 0.125),   # D
    (64, 2.625, 0.125), # Eb
    (66, 2.75, 0.125),  # F
    (67, 2.875, 0.125), # G
    (69, 3.0, 0.125),   # A
    (67, 3.125, 0.125), # G
    (65, 3.25, 0.125),  # F
    (62, 3.375, 0.125), # D
    (60, 3.5, 0.125),   # C
    (62, 3.625, 0.125), # D
    (64, 3.75, 0.125),  # Eb
    (66, 3.875, 0.125), # F
    (67, 4.0, 0.125),   # G
    (69, 4.125, 0.125), # A
    (67, 4.25, 0.125),  # G
    (65, 4.375, 0.125), # F
    (62, 4.5, 0.125)    # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.125),    # Hihat on 1&
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.125),  # Hihat on 2&
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.125),   # Hihat on 3&
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.125),  # Hihat on 4&
    # Bar 3
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.125),    # Hihat on 1&
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.125),  # Hihat on 2&
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.125),   # Hihat on 3&
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.125),  # Hihat on 4&
    # Bar 4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.125),    # Hihat on 1&
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.125),  # Hihat on 2&
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.125),   # Hihat on 3&
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.125)   # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
