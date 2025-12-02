
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (42, 0.1875, 0.1875), (42, 0.375, 0.1875), (42, 0.5625, 0.1875),
    (42, 0.75, 0.1875), (42, 0.9375, 0.1875), (42, 1.125, 0.1875),
    (42, 1.3125, 0.1875),
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (48, 1.5, 0.375), (49, 1.875, 0.375), (50, 2.25, 0.375), (51, 2.625, 0.375),
    (52, 2.875, 0.375), (51, 3.25, 0.375), (50, 3.625, 0.375), (49, 4.0, 0.375),
    (48, 4.375, 0.375), (47, 4.75, 0.375), (46, 5.125, 0.375), (45, 5.5, 0.375)
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (55, 1.875, 0.375), (57, 1.875, 0.375), (60, 1.875, 0.375), (62, 1.875, 0.375),
    # Bar 3
    (55, 3.25, 0.375), (57, 3.25, 0.375), (60, 3.25, 0.375), (62, 3.25, 0.375),
    # Bar 4
    (55, 4.75, 0.375), (57, 4.75, 0.375), (60, 4.75, 0.375), (62, 4.75, 0.375)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (65, 2.25, 0.375),
    (64, 2.625, 0.375), (62, 2.875, 0.375),
    (65, 3.625, 0.375), (67, 3.875, 0.375), (69, 4.125, 0.375),
    (67, 4.5, 0.375), (65, 4.875, 0.375)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: continue for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (42, 1.6875, 0.1875), (42, 1.875, 0.1875), (42, 2.0625, 0.1875),
    (42, 2.25, 0.1875), (42, 2.4375, 0.1875), (42, 2.625, 0.1875),
    (42, 2.8125, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (42, 3.1875, 0.1875), (42, 3.375, 0.1875), (42, 3.5625, 0.1875),
    (42, 3.75, 0.1875), (42, 3.9375, 0.1875), (42, 4.125, 0.1875),
    (42, 4.3125, 0.1875),
    # Bar 3
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (42, 4.6875, 0.1875), (42, 4.875, 0.1875), (42, 5.0625, 0.1875),
    (42, 5.25, 0.1875), (42, 5.4375, 0.1875), (42, 5.625, 0.1875),
    (42, 5.8125, 0.1875),
    # Bar 4
    (36, 6.0, 0.375), (38, 6.375, 0.375), (42, 6.0, 0.1875),
    (42, 6.1875, 0.1875), (42, 6.375, 0.1875), (42, 6.5625, 0.1875),
    (42, 6.75, 0.1875), (42, 6.9375, 0.1875), (42, 7.125, 0.1875),
    (42, 7.3125, 0.1875)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
