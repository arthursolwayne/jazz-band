
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
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line (F2 - C3)
bass_notes = [
    (38, 1.5, 0.375),    # F2 (root) on 1
    (40, 1.875, 0.375),  # G2 (fifth) on 2
    (37, 2.25, 0.375),   # E2 (chromatic approach) on 3
    (38, 2.625, 0.375),  # F2 (root) on 4
    (43, 3.0, 0.375),    # C3 (root) on 1
    (45, 3.375, 0.375),  # D3 (fifth) on 2
    (44, 3.75, 0.375),   # C#3 (chromatic approach) on 3
    (43, 4.125, 0.375),  # C3 (root) on 4
    (48, 4.5, 0.375),    # G3 (root) on 1
    (50, 4.875, 0.375),  # A3 (fifth) on 2
    (49, 5.25, 0.375),   # G#3 (chromatic approach) on 3
    (48, 5.625, 0.375)   # G3 (root) on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    (53, 1.5, 0.375),    # F
    (58, 1.5, 0.375),    # A
    (60, 1.5, 0.375),    # C
    (64, 1.5, 0.375),    # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (50, 2.25, 0.375),   # Bb
    (55, 2.25, 0.375),   # D
    (60, 2.25, 0.375),   # F
    (57, 2.25, 0.375),   # Ab
    # Bar 4: Cm7 (C, Eb, G, Bb)
    (60, 3.0, 0.375),    # C
    (63, 3.0, 0.375),    # Eb
    (67, 3.0, 0.375),    # G
    (67, 3.0, 0.375)     # Bb (duplicate G for harmony)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.375),    # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.375),   # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4

    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.375),    # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.375),   # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4

    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.375),    # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.375),   # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (60), G (62), F (60), E (59)
# Play the first two notes, hold the last note, then return to finish it on the last bar
sax_notes = [
    (60, 1.5, 0.375),    # F on 1
    (62, 1.875, 0.375),  # G on 2
    (60, 2.25, 0.375),   # F on 3
    (59, 2.625, 0.375),  # E on 4
    (60, 4.5, 0.375),    # F on 1 (return)
    (62, 4.875, 0.375),  # G on 2
    (60, 5.25, 0.375),   # F on 3
    (59, 5.625, 0.375)   # E on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo.mid")
