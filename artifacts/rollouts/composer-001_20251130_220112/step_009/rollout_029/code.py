
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875), (42, 0.1875, 0.1875),
    (42, 0.375, 0.1875), (42, 0.5625, 0.1875), (36, 0.75, 0.375), (38, 1.125, 0.375),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875), (42, 1.3125, 0.1875)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    (62, 1.5, 0.375), (63, 1.875, 0.375), (61, 2.25, 0.375), (60, 2.625, 0.375),
    # Bar 3
    (62, 3.0, 0.375), (63, 3.375, 0.375), (64, 3.75, 0.375), (62, 4.125, 0.375),
    # Bar 4
    (63, 4.5, 0.375), (62, 4.875, 0.375), (60, 5.25, 0.375), (61, 5.625, 0.375)
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (66, 1.5, 0.375), (69, 1.5, 0.375), (71, 1.5, 0.375), (72, 1.5, 0.375),
    # Bar 3
    (66, 3.0, 0.375), (69, 3.0, 0.375), (71, 3.0, 0.375), (72, 3.0, 0.375),
    # Bar 4
    (66, 4.5, 0.375), (69, 4.5, 0.375), (71, 4.5, 0.375), (72, 4.5, 0.375)
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: One short motif, make it sing
# Start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375),
    # Bar 3
    (62, 3.0, 0.375), (65, 3.375, 0.375),
    # Bar 4
    (67, 4.5, 0.375), (65, 4.875, 0.375), (62, 5.25, 0.375)
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875), (42, 1.6875, 0.1875),
    (42, 1.875, 0.1875), (42, 2.0625, 0.1875), (36, 2.25, 0.375), (38, 2.625, 0.375),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875), (42, 2.8125, 0.1875),
    # Bar 3
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875), (42, 3.1875, 0.1875),
    (42, 3.375, 0.1875), (42, 3.5625, 0.1875), (36, 3.75, 0.375), (38, 4.125, 0.375),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875), (42, 4.3125, 0.1875),
    # Bar 4
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875), (42, 4.6875, 0.1875),
    (42, 4.875, 0.1875), (42, 5.0625, 0.1875), (36, 5.25, 0.375), (38, 5.625, 0.375),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875), (42, 5.8125, 0.1875)
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
