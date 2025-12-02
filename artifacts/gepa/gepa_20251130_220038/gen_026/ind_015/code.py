
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

drum_notes = [
    # Bar 1
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.0, 0.1875),  # Hihat on 1
    (42, 0.1875, 0.1875),  # Hihat on &
    (42, 0.375, 0.1875),  # Hihat on 2
    (42, 0.5625, 0.1875),  # Hihat on &
    (42, 0.75, 0.1875),  # Hihat on 3
    (42, 0.9375, 0.1875),  # Hihat on &
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.125, 0.1875),  # Hihat on 3
    (42, 1.3125, 0.1875),  # Hihat on &
    (38, 1.5, 0.375),  # Snare on 4
    (42, 1.5, 0.1875),  # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# BASS: Walking line in F, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (45, 1.5, 0.375),  # F
    (46, 1.875, 0.375),  # G
    (44, 2.25, 0.375),  # E
    (45, 2.625, 0.375),  # F
    # Bar 3 (3.0 - 4.5s)
    (48, 3.0, 0.375),  # A
    (47, 3.375, 0.375),  # G#
    (46, 3.75, 0.375),  # G
    (48, 4.125, 0.375),  # A
    # Bar 4 (4.5 - 6.0s)
    (45, 4.5, 0.375),  # F
    (47, 4.875, 0.375),  # G#
    (44, 5.25, 0.375),  # E
    (45, 5.625, 0.375),  # F
]

for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# PIANO: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (50, 1.5, 0.375),  # F7: F, A, C, E
    (53, 1.5, 0.375),
    (55, 1.5, 0.375),
    (57, 1.5, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (53, 3.0, 0.375),  # F7 again
    (55, 3.0, 0.375),
    (57, 3.0, 0.375),
    (50, 3.0, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (50, 4.5, 0.375),  # F7
    (53, 4.5, 0.375),
    (55, 4.5, 0.375),
    (57, 4.5, 0.375),
]

for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# SAX: Your motif — short, singable, leaves it hanging
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375),  # G (F7)
    (64, 1.875, 0.375),  # A
    (62, 2.25, 0.375),  # G
    (60, 2.625, 0.375),  # F
    # Bar 3 (3.0 - 4.5s)
    (62, 3.0, 0.375),  # G (again)
    (64, 3.375, 0.375),  # A
    (62, 3.75, 0.375),  # G
    (65, 4.125, 0.375),  # Bb
    # Bar 4 (4.5 - 6.0s)
    (62, 4.5, 0.375),  # G
    (64, 4.875, 0.375),  # A
    (62, 5.25, 0.375),  # G
    (60, 5.625, 0.375),  # F
]

for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums continue for bars 2-4
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.5, 0.1875),  # Hihat on 1
    (42, 1.6875, 0.1875),  # Hihat on &
    (42, 1.875, 0.1875),  # Hihat on 2
    (42, 2.0625, 0.1875),  # Hihat on &
    (42, 2.25, 0.1875),  # Hihat on 3
    (42, 2.4375, 0.1875),  # Hihat on &
    (36, 2.625, 0.375),  # Kick on 3
    (42, 2.625, 0.1875),  # Hihat on 3
    (42, 2.8125, 0.1875),  # Hihat on &
    (38, 3.0, 0.375),  # Snare on 4
    (42, 3.0, 0.1875),  # Hihat on 4
    # Bar 3 (3.0 - 4.5s)
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.0, 0.1875),  # Hihat on 1
    (42, 3.1875, 0.1875),  # Hihat on &
    (42, 3.375, 0.1875),  # Hihat on 2
    (42, 3.5625, 0.1875),  # Hihat on &
    (42, 3.75, 0.1875),  # Hihat on 3
    (42, 3.9375, 0.1875),  # Hihat on &
    (36, 4.125, 0.375),  # Kick on 3
    (42, 4.125, 0.1875),  # Hihat on 3
    (42, 4.3125, 0.1875),  # Hihat on &
    (38, 4.5, 0.375),  # Snare on 4
    (42, 4.5, 0.1875),  # Hihat on 4
    # Bar 4 (4.5 - 6.0s)
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.5, 0.1875),  # Hihat on 1
    (42, 4.6875, 0.1875),  # Hihat on &
    (42, 4.875, 0.1875),  # Hihat on 2
    (42, 5.0625, 0.1875),  # Hihat on &
    (42, 5.25, 0.1875),  # Hihat on 3
    (42, 5.4375, 0.1875),  # Hihat on &
    (36, 5.625, 0.375),  # Kick on 3
    (42, 5.625, 0.1875),  # Hihat on 3
    (42, 5.8125, 0.1875),  # Hihat on &
    (38, 6.0, 0.375),  # Snare on 4
    (42, 6.0, 0.1875),  # Hihat on 4
]

for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
