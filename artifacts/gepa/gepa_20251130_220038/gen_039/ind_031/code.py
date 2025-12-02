
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
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
# Dm7 = D, F, A, C
bass_notes = [
    (62, 1.5, 0.375), (61, 1.875, 0.375), (60, 2.25, 0.375), (63, 2.625, 0.375),  # D, C, B, D#
    (62, 2.625, 0.375), (61, 2.625, 0.375), (60, 2.625, 0.375), (63, 2.625, 0.375),  # D, C, B, D#
    (63, 3.0, 0.375), (62, 3.375, 0.375), (64, 3.75, 0.375), (62, 4.125, 0.375),  # D#, D, E, D
    (63, 4.125, 0.375), (62, 4.125, 0.375), (64, 4.125, 0.375), (62, 4.125, 0.375),  # D#, D, E, D
    (62, 4.5, 0.375), (61, 4.875, 0.375), (60, 5.25, 0.375), (63, 5.625, 0.375)    # D, C, B, D#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4, comp on beat 2 and 4
# Dm7 = D, F, A, C
# F7 = F, A, C, E
# Bm7b5 = B, D, F, A
# G7 = G, B, D, F
piano_notes = [
    # Bar 2
    (62, 1.5, 0.1875), (65, 1.5, 0.1875), (67, 1.5, 0.1875), (60, 1.5, 0.1875),  # Dm7
    (66, 2.25, 0.1875), (69, 2.25, 0.1875), (71, 2.25, 0.1875), (64, 2.25, 0.1875),  # F7
    # Bar 3
    (67, 3.0, 0.1875), (69, 3.0, 0.1875), (71, 3.0, 0.1875), (64, 3.0, 0.1875),  # Bm7b5
    (71, 3.75, 0.1875), (74, 3.75, 0.1875), (76, 3.75, 0.1875), (69, 3.75, 0.1875),  # G7
    # Bar 4
    (62, 4.5, 0.1875), (65, 4.5, 0.1875), (67, 4.5, 0.1875), (60, 4.5, 0.1875),  # Dm7
    (66, 5.25, 0.1875), (69, 5.25, 0.1875), (71, 5.25, 0.1875), (64, 5.25, 0.1875)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> F (65) -> A (67) -> C (60) -> G (67) -> B (69) -> D (62)
sax_notes = [
    (62, 1.5, 0.375), (65, 1.875, 0.375), (67, 2.25, 0.375), (60, 2.625, 0.375),
    (67, 3.0, 0.375), (69, 3.375, 0.375), (62, 3.75, 0.375),
    (62, 4.125, 0.375), (65, 4.5, 0.375), (67, 4.875, 0.375), (60, 5.25, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums: Continue the fill
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375), (38, 1.875, 0.375), (42, 1.5, 0.1875),
    (36, 2.25, 0.375), (38, 2.625, 0.375), (42, 2.25, 0.1875),
    (36, 3.0, 0.375), (38, 3.375, 0.375), (42, 3.0, 0.1875),
    (36, 3.75, 0.375), (38, 4.125, 0.375), (42, 3.75, 0.1875),
    (36, 4.5, 0.375), (38, 4.875, 0.375), (42, 4.5, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
