
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    (36, 0.0, 0.25), (36, 1.0, 0.25),
    # Snare on 2 and 4
    (38, 0.5, 0.25), (38, 1.5, 0.25),
    # Hi-hat on every eighth
    (42, 0.0, 0.125), (42, 0.125, 0.125),
    (42, 0.25, 0.125), (42, 0.375, 0.125),
    (42, 0.5, 0.125), (42, 0.625, 0.125),
    (42, 0.75, 0.125), (42, 0.875, 0.125),
    (42, 1.0, 0.125), (42, 1.125, 0.125),
    (42, 1.25, 0.125), (42, 1.375, 0.125),
    (42, 1.5, 0.125)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    (60, 1.5, 1.75),  # C
    (61, 1.75, 2.0),  # C#
    (62, 2.0, 2.25),  # D
    (63, 2.25, 2.5),  # D#
    (64, 2.5, 2.75),  # E
    (65, 2.75, 3.0),  # F
    (66, 3.0, 3.25),  # F#
    (67, 3.25, 3.5),  # G
    (68, 3.5, 3.75),  # G#
    (69, 3.75, 4.0),  # A
    (70, 4.0, 4.25),  # A#
    (71, 4.25, 4.5),  # B
    (72, 4.5, 4.75),  # C
    (73, 4.75, 5.0),  # C#
    (74, 5.0, 5.25),  # D
    (75, 5.25, 5.5),  # D#
    (76, 5.5, 5.75),  # E
    (77, 5.75, 6.0),  # F
]
for note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, B, G)
    (60, 1.5, 1.75), (64, 1.5, 1.75), (67, 1.5, 1.75), (69, 1.5, 1.75),
    # Bar 3: F7 (F, A, E, C)
    (65, 3.0, 3.25), (69, 3.0, 3.25), (64, 3.0, 3.25), (60, 3.0, 3.25),
    # Bar 4: G7 (G, B, F, D)
    (67, 4.5, 4.75), (71, 4.5, 4.75), (66, 4.5, 4.75), (69, 4.5, 4.75)
]
for note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C (60), E (64), B (67), C (60) - start on 1.5s
# Then return and finish on 5.0s
sax_notes = [
    (60, 1.5, 1.75), (64, 1.75, 2.0), (67, 2.0, 2.25), (60, 2.25, 2.5),
    (60, 5.0, 5.25), (64, 5.25, 5.5), (67, 5.5, 5.75), (60, 5.75, 6.0)
]
for note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

# Drums: continue in bars 2-4
drum_notes = [
    # Kick on 1 and 3 (bar 2)
    (36, 1.5, 1.75), (36, 2.5, 2.75),
    # Snare on 2 and 4 (bar 2)
    (38, 2.0, 2.25), (38, 3.0, 3.25),
    # Hi-hat on every eighth (bar 2)
    (42, 1.5, 1.625), (42, 1.625, 1.75),
    (42, 1.75, 1.875), (42, 1.875, 2.0),
    (42, 2.0, 2.125), (42, 2.125, 2.25),
    (42, 2.25, 2.375), (42, 2.375, 2.5),
    (42, 2.5, 2.625), (42, 2.625, 2.75),
    (42, 2.75, 2.875), (42, 2.875, 3.0),

    # Kick on 1 and 3 (bar 3)
    (36, 3.0, 3.25), (36, 4.0, 4.25),
    # Snare on 2 and 4 (bar 3)
    (38, 3.5, 3.75), (38, 4.5, 4.75),
    # Hi-hat on every eighth (bar 3)
    (42, 3.0, 3.125), (42, 3.125, 3.25),
    (42, 3.25, 3.375), (42, 3.375, 3.5),
    (42, 3.5, 3.625), (42, 3.625, 3.75),
    (42, 3.75, 3.875), (42, 3.875, 4.0),
    (42, 4.0, 4.125), (42, 4.125, 4.25),

    # Kick on 1 and 3 (bar 4)
    (36, 4.5, 4.75), (36, 5.5, 5.75),
    # Snare on 2 and 4 (bar 4)
    (38, 5.0, 5.25), (38, 6.0, 6.25),
    # Hi-hat on every eighth (bar 4)
    (42, 4.5, 4.625), (42, 4.625, 4.75),
    (42, 4.75, 4.875), (42, 4.875, 5.0),
    (42, 5.0, 5.125), (42, 5.125, 5.25),
    (42, 5.25, 5.375), (42, 5.375, 5.5),
    (42, 5.5, 5.625), (42, 5.625, 5.75)
]
for note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note[0], start=note[1], end=note[2]))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
