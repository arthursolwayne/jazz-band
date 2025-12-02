
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
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.5, 0.1875)   # Hihat fill
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),   # D2 (root)
    (40, 1.875, 0.375),  # F (chromatic approach)
    (43, 2.25, 0.375),   # A (fifth)
    (41, 2.625, 0.375),  # G (chromatic approach)
    (38, 3.0, 0.375),    # D2 (root)
    (40, 3.375, 0.375),  # F (chromatic approach)
    (43, 3.75, 0.375),   # A (fifth)
    (41, 4.125, 0.375),  # G (chromatic approach)
    (38, 4.5, 0.375),    # D2 (root)
    (40, 4.875, 0.375),  # F (chromatic approach)
    (43, 5.25, 0.375),   # A (fifth)
    (41, 5.625, 0.375)   # G (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane on piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 -> F6/9
piano_notes = [
    (62, 1.5, 0.375),   # F
    (67, 1.5, 0.375),   # A
    (69, 1.5, 0.375),   # C
    (72, 1.5, 0.375),   # D
    (76, 1.5, 0.375),   # F
    (79, 1.5, 0.375),   # A
    (81, 1.5, 0.375),   # C
    (84, 1.5, 0.375),   # D
    (72, 1.5, 0.375),   # D (resolve)
    # Bar 3: G7 -> Cm7
    (78, 2.25, 0.375),  # G
    (81, 2.25, 0.375),  # B
    (83, 2.25, 0.375),  # D
    (76, 2.25, 0.375),  # F
    (84, 2.25, 0.375),  # C
    (87, 2.25, 0.375),  # E
    (89, 2.25, 0.375),  # G
    (82, 2.25, 0.375),  # B
    (76, 2.25, 0.375),  # F (resolve)
    # Bar 4: Cm7 -> Dm7
    (72, 3.0, 0.375),   # C
    (76, 3.0, 0.375),   # E
    (79, 3.0, 0.375),   # G
    (82, 3.0, 0.375),   # B
    (62, 3.0, 0.375),   # F
    (67, 3.0, 0.375),   # A
    (69, 3.0, 0.375),   # C
    (72, 3.0, 0.375),   # D
    (72, 3.0, 0.375),   # C (resolve)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F (65), G (67), D (62)
# First phrase: 1.5 - 2.25s
# Second phrase: 3.75 - 4.5s
# Third phrase: 5.25 - 6.0s

sax_notes = [
    (62, 1.5, 0.375),   # D
    (65, 1.875, 0.375),  # F
    (67, 2.25, 0.375),   # G
    (62, 3.75, 0.375),   # D
    (65, 4.125, 0.375),  # F
    (67, 4.5, 0.375),    # G
    (62, 5.25, 0.375),   # D
    (65, 5.625, 0.375),  # F
    (67, 6.0, 0.375)     # G (end on G)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4
    (42, 3.0, 0.1875),  # Hihat fill

    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4
    (42, 4.5, 0.1875),  # Hihat fill

    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
