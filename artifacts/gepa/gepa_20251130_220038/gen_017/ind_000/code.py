
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
    (36, 0.0, 0.375), (38, 0.375, 0.375),
    (36, 0.75, 0.375), (38, 1.125, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches
bass_notes = [
    (40, 1.5, 0.375), (41, 1.875, 0.375), (39, 2.25, 0.375), (38, 2.625, 0.375),
    (40, 2.625, 0.375), (41, 3.0, 0.375), (39, 3.375, 0.375), (38, 3.75, 0.375),
    (40, 4.125, 0.375), (41, 4.5, 0.375), (39, 4.875, 0.375), (38, 5.25, 0.375),
    (40, 5.625, 0.375), (41, 6.0, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (48, 1.5, 0.375), (50, 1.5, 0.375), (53, 1.5, 0.375), (59, 1.5, 0.375),
    (50, 1.875, 0.375), (52, 1.875, 0.375), (57, 1.875, 0.375), (62, 1.875, 0.375),
    # Bar 3
    (48, 2.25, 0.375), (50, 2.25, 0.375), (53, 2.25, 0.375), (59, 2.25, 0.375),
    (50, 2.625, 0.375), (52, 2.625, 0.375), (57, 2.625, 0.375), (62, 2.625, 0.375),
    # Bar 4
    (48, 3.0, 0.375), (50, 3.0, 0.375), (53, 3.0, 0.375), (59, 3.0, 0.375),
    (50, 3.375, 0.375), (52, 3.375, 0.375), (57, 3.375, 0.375), (62, 3.375, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375),
    (36, 2.25, 0.375), (38, 2.625, 0.375),
    (36, 3.0, 0.375), (38, 3.375, 0.375),
    (36, 3.75, 0.375), (38, 4.125, 0.375),
    (36, 4.5, 0.375), (38, 4.875, 0.375),
    (36, 5.25, 0.375), (38, 5.625, 0.375)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Fm7 -> Ab -> Bb -> D
sax_notes = [
    (40, 1.5, 0.375), (43, 1.875, 0.375), (44, 2.25, 0.375), (47, 2.625, 0.375),
    (40, 3.0, 0.375), (43, 3.375, 0.375), (44, 3.75, 0.375), (47, 4.125, 0.375),
    (40, 4.5, 0.375), (43, 4.875, 0.375), (44, 5.25, 0.375), (47, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
