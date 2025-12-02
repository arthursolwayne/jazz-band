
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

# Marcus: Walking line, chromatic approaches, never the same note twice
# Dm7 -> G7 -> Cm7 -> F7
# Walking bass line in D Dorian (D, E, F, G, A, B, C)
bass_notes = [
    (50, 1.5, 0.375), (51, 1.875, 0.375), (50, 2.25, 0.375), (49, 2.625, 0.375),

    (52, 3.0, 0.375), (53, 3.375, 0.375), (52, 3.75, 0.375), (51, 4.125, 0.375),

    (50, 4.5, 0.375), (51, 4.875, 0.375), (50, 5.25, 0.375), (49, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
# Dm7, G7, Cm7, F7
piano_notes = [
    # Bar 2 (Dm7)
    (62, 1.875, 0.1875), (64, 1.875, 0.1875), (67, 1.875, 0.1875), (69, 1.875, 0.1875),
    # Bar 3 (G7)
    (67, 3.375, 0.1875), (69, 3.375, 0.1875), (71, 3.375, 0.1875), (74, 3.375, 0.1875),
    # Bar 4 (Cm7)
    (60, 4.875, 0.1875), (62, 4.875, 0.1875), (64, 4.875, 0.1875), (67, 4.875, 0.1875)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Dante: Tenor sax, one short motif, start it, leave it hanging. Come back and finish it.
# Dm7 -> G7 -> Cm7 -> F7
# Motif: D - F - G - Bb (Dm7) with a slight chromatic twist

# Bar 2: Start the motif
sax_notes = [
    (62, 1.5, 0.375), (64, 1.875, 0.375), (67, 2.25, 0.375), (69, 2.625, 0.375),
    # Bar 3: Repeat the motif
    (62, 3.0, 0.375), (64, 3.375, 0.375), (67, 3.75, 0.375), (69, 4.125, 0.375),
    # Bar 4: Repeat the motif again, ending on the tonic (D)
    (62, 4.5, 0.375), (64, 4.875, 0.375), (67, 5.25, 0.375), (62, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
