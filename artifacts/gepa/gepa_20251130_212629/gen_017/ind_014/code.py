
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
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (42, 0.0, 0.375),  # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.375),  # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice. Dm7 -> Gm7 -> Am7 -> Dm7
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.5, 0.375),  # D
    (61, 1.875, 0.375),  # C
    (63, 2.25, 0.375),  # Eb
    (62, 2.625, 0.375),  # D

    # Bar 3 (3.0 - 4.5s)
    (60, 3.0, 0.375),  # G
    (59, 3.375, 0.375),  # F
    (61, 3.75, 0.375),  # G
    (60, 4.125, 0.375),  # G

    # Bar 4 (4.5 - 6.0s)
    (57, 4.5, 0.375),  # A
    (58, 4.875, 0.375),  # Bb
    (57, 5.25, 0.375),  # A
    (62, 5.625, 0.375),  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4. Dm7 -> Gm7 -> Am7 -> Dm7
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (62, 1.875, 0.25),  # D
    (67, 1.875, 0.25),  # Bb
    (69, 1.875, 0.25),  # C
    (71, 1.875, 0.25),  # D

    # Bar 3 (3.0 - 4.5s)
    (60, 3.375, 0.25),  # G
    (65, 3.375, 0.25),  # D
    (67, 3.375, 0.25),  # F
    (69, 3.375, 0.25),  # G

    # Bar 4 (4.5 - 6.0s)
    (57, 4.875, 0.25),  # A
    (60, 4.875, 0.25),  # C
    (62, 4.875, 0.25),  # D
    (64, 4.875, 0.25),  # E
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4

    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4

    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375),  # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm7 -> Gm7 -> Am7 -> Dm7
# Motif notes: D, F, G, Bb (Dm7) -> G, Bb, C, D (Gm7) -> A, C, D, E (Am7) -> D, F, G, Bb (Dm7)
# Duration: 0.5s per note
sax_notes = [
    (62, 1.5, 0.5),     # D
    (64, 2.0, 0.5),     # F
    (67, 2.5, 0.5),     # G
    (67, 3.0, 0.5),     # Bb (Gm7)
    (60, 3.5, 0.5),     # G
    (62, 4.0, 0.5),     # Bb
    (64, 4.5, 0.5),     # C
    (67, 5.0, 0.5),     # D (Am7)
    (57, 5.5, 0.5),     # A
    (62, 6.0, 0.5),     # D (Dm7)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
