
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
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.1875), # Hihat on 1&
    (42, 0.1875, 0.1875), # Hihat on 2&
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2&
    (42, 0.5625, 0.1875), # Hihat on 3&
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3&
    (42, 0.9375, 0.1875), # Hihat on 4&
    (38, 1.125, 0.375),  # Snare on 4
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass line (Marcus): Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375),  # D
    (63, 1.875, 0.375), # Eb
    (62, 2.25, 0.375),  # D
    (60, 2.625, 0.375), # C
    # Bar 3
    (62, 3.0, 0.375),  # D
    (63, 3.375, 0.375), # Eb
    (62, 3.75, 0.375),  # D
    (60, 4.125, 0.375), # C
    # Bar 4
    (62, 4.5, 0.375),  # D
    (63, 4.875, 0.375), # Eb
    (62, 5.25, 0.375),  # D
    (60, 5.625, 0.375), # C
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note[0], start=note[1], end=note[2]))

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (72, 1.875, 0.375),  # C7 (C, E, Bb, D)
    (76, 1.875, 0.375),
    (79, 1.875, 0.375),
    (74, 1.875, 0.375),
    # Bar 3
    (74, 3.375, 0.375),  # D7 (D, F#, C, E)
    (78, 3.375, 0.375),
    (81, 3.375, 0.375),
    (76, 3.375, 0.375),
    # Bar 4
    (72, 4.875, 0.375),  # C7 again
    (76, 4.875, 0.375),
    (79, 4.875, 0.375),
    (74, 4.875, 0.375),
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax (Dante): One short motif, make it sing
sax_notes = [
    (62, 1.5, 0.375),  # D
    (66, 1.875, 0.375), # F
    (67, 2.25, 0.375),  # F#
    (64, 2.625, 0.375), # E
    (62, 3.0, 0.375),  # D
    (66, 3.375, 0.375), # F
    (67, 3.75, 0.375),  # F#
    (64, 4.125, 0.375), # E
    (62, 4.5, 0.375),  # D
    (66, 4.875, 0.375), # F
    (67, 5.25, 0.375),  # F#
    (64, 5.625, 0.375), # E
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note[0], start=note[1], end=note[2]))

# Drums for bars 2-4
drum_notes_2_4 = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1&
    (42, 1.6875, 0.1875), # Hihat on 2&
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2&
    (42, 2.0625, 0.1875), # Hihat on 3&
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3&
    (42, 2.4375, 0.1875), # Hihat on 4&
    (38, 2.625, 0.375),  # Snare on 4
    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1&
    (42, 3.1875, 0.1875), # Hihat on 2&
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2&
    (42, 3.5625, 0.1875), # Hihat on 3&
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3&
    (42, 3.9375, 0.1875), # Hihat on 4&
    (38, 4.125, 0.375),  # Snare on 4
    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1&
    (42, 4.6875, 0.1875), # Hihat on 2&
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2&
    (42, 5.0625, 0.1875), # Hihat on 3&
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3&
    (42, 5.4375, 0.1875), # Hihat on 4&
    (38, 5.625, 0.375),  # Snare on 4
]
for note in drum_notes_2_4:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
