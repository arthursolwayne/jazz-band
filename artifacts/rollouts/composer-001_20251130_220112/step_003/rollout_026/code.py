
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.1875),    # Hihat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hihat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.1875)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    (45, 1.5, 0.375),     # F
    (46, 1.875, 0.375),   # G
    (44, 2.25, 0.375),    # E
    (43, 2.625, 0.375),   # D
    (45, 3.0, 0.375),     # F
    (47, 3.375, 0.375),   # A
    (46, 3.75, 0.375),    # G
    (44, 4.125, 0.375),   # E
    (45, 4.5, 0.375),     # F
    (48, 4.875, 0.375),   # Bb
    (47, 5.25, 0.375),    # A
    (46, 5.625, 0.375)    # G
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Diane - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (50, 1.875, 0.1875),  # F7 chord: F, A, C, Eb (50, 53, 55, 57)
    (53, 1.875, 0.1875),
    (55, 1.875, 0.1875),
    (57, 1.875, 0.1875),
    # Bar 3
    (50, 3.375, 0.1875),
    (53, 3.375, 0.1875),
    (55, 3.375, 0.1875),
    (57, 3.375, 0.1875),
    # Bar 4
    (50, 4.875, 0.1875),
    (53, 4.875, 0.1875),
    (55, 4.875, 0.1875),
    (57, 4.875, 0.1875)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.1875),    # Hihat on 1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.875, 0.1875),  # Hihat on 2
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.25, 0.1875),   # Hihat on 3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.625, 0.1875),  # Hihat on 4

    # Bar 3
    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.1875),    # Hihat on 1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.375, 0.1875),  # Hihat on 2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.75, 0.1875),   # Hihat on 3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.125, 0.1875),  # Hihat on 4

    # Bar 4
    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.1875),    # Hihat on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.1875),  # Hihat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.1875),   # Hihat on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.625, 0.1875)   # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Dante
sax_notes = [
    (62, 1.5, 0.375),     # D (F7 chord)
    (66, 1.875, 0.375),   # G
    (60, 2.25, 0.375),    # C
    (62, 2.625, 0.375),   # D
    (67, 3.0, 0.1875),    # G#
    (69, 3.1875, 0.1875), # Bb
    (62, 3.375, 0.375),   # D
    (66, 3.75, 0.375),    # G
    (60, 4.125, 0.375),   # C
    (62, 4.5, 0.375),     # D
    (67, 4.875, 0.1875),  # G#
    (69, 5.0625, 0.1875), # Bb
    (62, 5.25, 0.375),    # D
    (66, 5.625, 0.375)    # G
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
