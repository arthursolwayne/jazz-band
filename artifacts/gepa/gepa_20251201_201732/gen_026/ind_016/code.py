
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    (36, 0.0, 0.375),       # Kick on 1
    (42, 0.0, 0.1875),      # Hihat on 1
    (38, 0.375, 0.375),     # Snare on 2
    (42, 0.375, 0.1875),    # Hihat on 2
    (36, 0.75, 0.375),      # Kick on 3
    (42, 0.75, 0.1875),     # Hihat on 3
    (38, 1.125, 0.375),     # Snare on 4
    (42, 1.125, 0.1875)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in F (F2-G2-A2-Bb2-C3-D3-Eb3-F3)
bass_notes = [
    (38, 1.5, 0.375),       # F2 on 1
    (40, 1.875, 0.375),     # G2 on 2
    (41, 2.25, 0.375),      # A2 on 3
    (42, 2.625, 0.375),     # Bb2 on 4
    (44, 3.0, 0.375),       # C3 on 1
    (45, 3.375, 0.375),     # D3 on 2
    (46, 3.75, 0.375),      # Eb3 on 3
    (47, 4.125, 0.375),     # F3 on 4
    (42, 4.5, 0.375),       # Bb2 on 1
    (44, 4.875, 0.375),     # C3 on 2
    (45, 5.25, 0.375),      # D3 on 3
    (47, 5.625, 0.375)      # F3 on 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar
# Bar 2: F7 (F, A, C, E)
piano_notes = [
    (65, 1.5, 0.5),  # F
    (68, 1.5, 0.5),  # A
    (72, 1.5, 0.5),  # C
    (74, 1.5, 0.5),  # E
    # Bar 3: Bb7 (Bb, D, F, Ab)
    (62, 2.25, 0.5), # Bb
    (67, 2.25, 0.5), # D
    (72, 2.25, 0.5), # F
    (69, 2.25, 0.5), # Ab
    # Bar 4: C7 (C, E, G, B)
    (72, 3.0, 0.5),  # C
    (74, 3.0, 0.5),  # E
    (76, 3.0, 0.5),  # G
    (79, 3.0, 0.5)   # B
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
drum_notes = [
    (36, 1.5, 0.375),       # Kick on 1
    (42, 1.5, 0.1875),      # Hihat on 1
    (38, 1.875, 0.375),     # Snare on 2
    (42, 1.875, 0.1875),    # Hihat on 2
    (36, 2.25, 0.375),      # Kick on 3
    (42, 2.25, 0.1875),     # Hihat on 3
    (38, 2.625, 0.375),     # Snare on 4
    (42, 2.625, 0.1875),    # Hihat on 4
    (36, 3.0, 0.375),       # Kick on 1
    (42, 3.0, 0.1875),      # Hihat on 1
    (38, 3.375, 0.375),     # Snare on 2
    (42, 3.375, 0.1875),    # Hihat on 2
    (36, 3.75, 0.375),      # Kick on 3
    (42, 3.75, 0.1875),     # Hihat on 3
    (38, 4.125, 0.375),     # Snare on 4
    (42, 4.125, 0.1875),    # Hihat on 4
    (36, 4.5, 0.375),       # Kick on 1
    (42, 4.5, 0.1875),      # Hihat on 1
    (38, 4.875, 0.375),     # Snare on 2
    (42, 4.875, 0.1875),    # Hihat on 2
    (36, 5.25, 0.375),      # Kick on 3
    (42, 5.25, 0.1875),     # Hihat on 3
    (38, 5.625, 0.375),     # Snare on 4
    (42, 5.625, 0.1875)     # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax solo: One short motif, start it, leave it hanging, come back and finish it
# Melody: F (65), Ab (69), Bb (62), C (72)
sax_notes = [
    (65, 1.5, 0.375),       # F on 1
    (69, 1.875, 0.375),     # Ab on 2
    (62, 2.25, 0.375),      # Bb on 3
    (72, 2.625, 0.375),     # C on 4
    (65, 3.0, 0.375),       # F on 1
    (69, 3.375, 0.375),     # Ab on 2
    (62, 3.75, 0.375),      # Bb on 3
    (72, 4.125, 0.375),     # C on 4
    (65, 4.5, 0.375),       # F on 1
    (69, 4.875, 0.375),     # Ab on 2
    (62, 5.25, 0.375),      # Bb on 3
    (72, 5.625, 0.375)      # C on 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
