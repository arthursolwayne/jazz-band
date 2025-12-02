
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

# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    (41, 1.5, 0.375), (40, 1.875, 0.375), (39, 2.25, 0.375), (37, 2.625, 0.375),
    (41, 3.0, 0.375), (40, 3.375, 0.375), (39, 3.75, 0.375), (37, 4.125, 0.375),
    (41, 4.5, 0.375), (40, 4.875, 0.375), (39, 5.25, 0.375), (37, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (48, 2.0, 0.375), (50, 2.0, 0.375), (53, 2.0, 0.375), (55, 2.0, 0.375),  # F7 on 2
    (48, 3.0, 0.375), (50, 3.0, 0.375), (53, 3.0, 0.375), (55, 3.0, 0.375),  # F7 on 4
    (48, 4.0, 0.375), (50, 4.0, 0.375), (53, 4.0, 0.375), (55, 4.0, 0.375)   # F7 on 4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Dante: Tenor sax solo (your moment)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, Ab, A, Bb, B, Db
sax_notes = [
    (44, 1.5, 0.375), (46, 1.875, 0.375), (47, 2.25, 0.375),  # F, Gb, Ab
    (44, 2.625, 0.375), (46, 3.0, 0.375), (47, 3.375, 0.375),  # F, Gb, Ab
    (44, 3.75, 0.375), (46, 4.125, 0.375), (47, 4.5, 0.375),   # F, Gb, Ab
    (44, 4.875, 0.375), (46, 5.25, 0.375), (47, 5.625, 0.375)  # F, Gb, Ab
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
