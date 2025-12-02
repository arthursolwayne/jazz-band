
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# C minor walking bass line: C - Bb - B - C - D - Eb - E - D - C - Bb - B - C
bass_notes = [
    (60, 1.5, 0.375), (108, 1.875, 0.375), (109, 2.25, 0.375),
    (60, 2.625, 0.375), (62, 2.999, 0.375), (63, 3.375, 0.375),
    (64, 3.75, 0.375), (62, 4.125, 0.375), (60, 4.5, 0.375),
    (108, 4.875, 0.375), (109, 5.25, 0.375), (60, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
# C7, F7, Bb7, Eb7
piano_notes = [
    # Bar 2
    (60, 1.5, 0.1875), (64, 1.5, 0.1875), (67, 1.5, 0.1875), (71, 1.5, 0.1875),
    (60, 2.25, 0.1875), (64, 2.25, 0.1875), (67, 2.25, 0.1875), (71, 2.25, 0.1875),
    # Bar 3
    (65, 3.0, 0.1875), (69, 3.0, 0.1875), (71, 3.0, 0.1875), (74, 3.0, 0.1875),
    (65, 3.75, 0.1875), (69, 3.75, 0.1875), (71, 3.75, 0.1875), (74, 3.75, 0.1875),
    # Bar 4
    (62, 4.5, 0.1875), (67, 4.5, 0.1875), (71, 4.5, 0.1875), (76, 4.5, 0.1875),
    (62, 5.25, 0.1875), (67, 5.25, 0.1875), (71, 5.25, 0.1875), (76, 5.25, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Same pattern as Bar 1 but starting at 1.5
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 2.999, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax, one short motif, make it sing
# C - Eb - D - C (melodic motif), start at bar 2
sax_notes = [
    (60, 1.5, 0.375),
    (63, 1.875, 0.375),
    (62, 2.25, 0.375),
    (60, 2.625, 0.375),
    # Repeat motif slightly higher
    (62, 3.0, 0.375),
    (65, 3.375, 0.375),
    (64, 3.75, 0.375),
    (62, 4.125, 0.375),
    # End with a slight resolution
    (60, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
