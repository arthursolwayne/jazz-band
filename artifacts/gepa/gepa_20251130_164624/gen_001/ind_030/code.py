
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
    (36, 0.0, 0.375), (38, 0.375, 0.375), (42, 0.0, 0.1875),
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches
bass_notes = [
    (37, 1.5, 0.375), (38, 1.875, 0.375), (36, 2.25, 0.375), (35, 2.625, 0.375),  # Bar 2
    (37, 3.0, 0.375), (38, 3.375, 0.375), (36, 3.75, 0.375), (35, 4.125, 0.375),  # Bar 3
    (37, 4.5, 0.375), (38, 4.875, 0.375), (36, 5.25, 0.375), (35, 5.625, 0.375)   # Bar 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (65, 1.875, 0.1875), (67, 1.875, 0.1875), (72, 1.875, 0.1875), (71, 1.875, 0.1875),
    (65, 2.625, 0.1875), (67, 2.625, 0.1875), (72, 2.625, 0.1875), (71, 2.625, 0.1875),
    # Bar 3: Bb7 on 2 and 4
    (62, 3.375, 0.1875), (64, 3.375, 0.1875), (67, 3.375, 0.1875), (66, 3.375, 0.1875),
    (62, 4.125, 0.1875), (64, 4.125, 0.1875), (67, 4.125, 0.1875), (66, 4.125, 0.1875),
    # Bar 4: Eb7 on 2 and 4
    (60, 4.875, 0.1875), (62, 4.875, 0.1875), (65, 4.875, 0.1875), (64, 4.875, 0.1875),
    (60, 5.625, 0.1875), (62, 5.625, 0.1875), (65, 5.625, 0.1875), (64, 5.625, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Drums: continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65) -> Bb (62) -> D (67) -> F (65) -> Bb (62) -> D (67)
# First two notes in bar 2, last four in bar 4
sax_notes = [
    (65, 1.5, 0.375), (62, 1.875, 0.375),  # Bar 2
    (67, 4.5, 0.375), (65, 4.875, 0.375), (62, 5.25, 0.375), (67, 5.625, 0.375)  # Bar 4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
