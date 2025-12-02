
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (38, 1.5, 0.375),  # Snare on 4
    (42, 1.5, 0.1875),  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375),  # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375),  # D#
    (64, 3.0, 0.375),  # E
    (65, 3.375, 0.375),  # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375),  # G
    (68, 4.5, 0.375),  # G#
    (69, 4.875, 0.375),  # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375),  # B
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (60, 1.875, 0.375),  # C7 (C, E, B)
    (64, 1.875, 0.375),
    (67, 1.875, 0.375),
    # Bar 3
    (60, 3.375, 0.375),  # C7
    (64, 3.375, 0.375),
    (67, 3.375, 0.375),
    # Bar 4
    (60, 4.875, 0.375),  # C7
    (64, 4.875, 0.375),
    (67, 4.875, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),  # D
    (64, 1.875, 0.375),  # E
    (60, 2.25, 0.375),  # C
    (62, 2.625, 0.375),  # D
    (64, 3.0, 0.375),  # E
    (60, 3.375, 0.375),  # C
    (62, 3.75, 0.375),  # D
    (64, 4.125, 0.375),  # E
    (60, 4.5, 0.375),  # C
    (62, 4.875, 0.375),  # D
    (64, 5.25, 0.375),  # E
    (60, 5.625, 0.375),  # C
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums continue for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.5, 0.1875),  # Hihat on 1
    (42, 1.6875, 0.1875),  # Hihat on &
    (42, 1.875, 0.1875),  # Hihat on 2
    (42, 2.0625, 0.1875),  # Hihat on &
    (42, 2.25, 0.1875),  # Hihat on 3
    (42, 2.4375, 0.1875),  # Hihat on &
    (36, 2.625, 0.375),  # Kick on 3
    (38, 3.0, 0.375),  # Snare on 4
    (42, 3.0, 0.1875),  # Hihat on 4
    # Bar 3
    (36, 3.375, 0.375),  # Kick on 1
    (38, 3.75, 0.375),  # Snare on 2
    (42, 3.375, 0.1875),  # Hihat on 1
    (42, 3.5625, 0.1875),  # Hihat on &
    (42, 3.75, 0.1875),  # Hihat on 2
    (42, 3.9375, 0.1875),  # Hihat on &
    (42, 4.125, 0.1875),  # Hihat on 3
    (42, 4.3125, 0.1875),  # Hihat on &
    (36, 4.5, 0.375),  # Kick on 3
    (38, 4.875, 0.375),  # Snare on 4
    (42, 4.875, 0.1875),  # Hihat on 4
    # Bar 4
    (36, 5.25, 0.375),  # Kick on 1
    (38, 5.625, 0.375),  # Snare on 2
    (42, 5.25, 0.1875),  # Hihat on 1
    (42, 5.4375, 0.1875),  # Hihat on &
    (42, 5.625, 0.1875),  # Hihat on 2
    (42, 5.8125, 0.1875),  # Hihat on &
    (42, 6.0, 0.1875),  # Hihat on 3
    (42, 6.1875, 0.1875),  # Hihat on &
    (36, 6.375, 0.375),  # Kick on 3
    (38, 6.75, 0.375),  # Snare on 4
    (42, 6.75, 0.1875),  # Hihat on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
