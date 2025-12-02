
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
    (36, 0.75, 0.375), (38, 1.125, 0.375), (42, 0.75, 0.1875),
    (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: walking line in Fm, chromatic approaches
bass_notes = [
    (44, 1.5, 0.375), (45, 1.875, 0.375), (43, 2.25, 0.375), (42, 2.625, 0.375),  # Bar 2
    (44, 3.0, 0.375), (45, 3.375, 0.375), (43, 3.75, 0.375), (42, 4.125, 0.375),  # Bar 3
    (44, 4.5, 0.375), (45, 4.875, 0.375), (43, 5.25, 0.375), (42, 5.625, 0.375)   # Bar 4
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane on piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (42, 2.25, 0.375), (46, 2.25, 0.375), (49, 2.25, 0.375), (53, 2.25, 0.375),  # Fm7
    (45, 2.625, 0.375), (49, 2.625, 0.375), (52, 2.625, 0.375), (56, 2.625, 0.375),  # Ab7
    # Bar 3
    (42, 3.75, 0.375), (46, 3.75, 0.375), (49, 3.75, 0.375), (53, 3.75, 0.375),  # Fm7
    (45, 4.125, 0.375), (49, 4.125, 0.375), (52, 4.125, 0.375), (56, 4.125, 0.375),  # Ab7
    # Bar 4
    (42, 5.25, 0.375), (46, 5.25, 0.375), (49, 5.25, 0.375), (53, 5.25, 0.375),  # Fm7
    (45, 5.625, 0.375), (49, 5.625, 0.375), (52, 5.625, 0.375), (56, 5.625, 0.375)   # Ab7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray on drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875),
    (36, 5.25, 0.375), (38, 5.625, 0.375), (42, 5.25, 0.1875),
    (42, 6.0, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (61, 1.5, 0.375), (62, 1.875, 0.375), (60, 2.25, 0.375),  # Fm -> Gb -> E
    (61, 3.0, 0.375), (62, 3.375, 0.375), (60, 3.75, 0.375),  # Repeat
    (61, 4.5, 0.375), (62, 4.875, 0.375), (60, 5.25, 0.375)   # Finish
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
