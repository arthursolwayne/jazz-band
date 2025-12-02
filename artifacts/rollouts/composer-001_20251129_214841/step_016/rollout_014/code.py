
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    (38, 0.375, 0.375),# Snare on 2
    (42, 0.375, 0.1875),# Hihat on 2&
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3&
    (38, 1.125, 0.375),# Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
bass_notes = [
    (60, 1.5, 0.375), # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375), # D
    (63, 2.625, 0.375), # D#
    (64, 3.0, 0.375), # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375), # F#
    (67, 4.125, 0.375), # G
    (68, 4.5, 0.375), # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375), # A#
    (71, 5.625, 0.375), # B
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano - Diane
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (64, 1.5, 0.375), # C7
    (67, 1.5, 0.375), # E7
    (71, 1.5, 0.375), # B7
    (69, 1.5, 0.375), # G7
    (64, 2.25, 0.375), # C7
    (67, 2.25, 0.375), # E7
    (71, 2.25, 0.375), # B7
    (69, 2.25, 0.375), # G7

    # Bar 3 (3.0 - 4.5s)
    (64, 3.0, 0.375), # C7
    (67, 3.0, 0.375), # E7
    (71, 3.0, 0.375), # B7
    (69, 3.0, 0.375), # G7
    (64, 3.75, 0.375), # C7
    (67, 3.75, 0.375), # E7
    (71, 3.75, 0.375), # B7
    (69, 3.75, 0.375), # G7

    # Bar 4 (4.5 - 6.0s)
    (64, 4.5, 0.375), # C7
    (67, 4.5, 0.375), # E7
    (71, 4.5, 0.375), # B7
    (69, 4.5, 0.375), # G7
    (64, 5.25, 0.375), # C7
    (67, 5.25, 0.375), # E7
    (71, 5.25, 0.375), # B7
    (69, 5.25, 0.375), # G7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax - Dante
sax_notes = [
    (65, 1.5, 0.375), # E
    (67, 1.875, 0.375), # G
    (69, 2.25, 0.375), # A
    (67, 2.625, 0.375), # G
    (65, 3.0, 0.375), # E
    (67, 3.375, 0.375), # G
    (69, 3.75, 0.375), # A
    (67, 4.125, 0.375), # G
    (65, 4.5, 0.375), # E
    (67, 4.875, 0.375), # G
    (69, 5.25, 0.375), # A
    (67, 5.625, 0.375), # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1&
    (38, 1.875, 0.375),# Snare on 2
    (42, 1.875, 0.1875),# Hihat on 2&
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3&
    (38, 2.625, 0.375),# Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4&

    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1&
    (38, 3.375, 0.375),# Snare on 2
    (42, 3.375, 0.1875),# Hihat on 2&
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3&
    (38, 4.125, 0.375),# Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4&

    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1&
    (38, 4.875, 0.375),# Snare on 2
    (42, 4.875, 0.1875),# Hihat on 2&
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3&
    (38, 5.625, 0.375),# Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4&
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
