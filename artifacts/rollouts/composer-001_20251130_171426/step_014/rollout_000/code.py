
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
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    (62, 1.5, 0.375),  # D (root)
    (61, 1.875, 0.375),  # C (chromatic approach)
    (63, 2.25, 0.375),  # Eb (3rd)
    (60, 2.625, 0.375),  # C (chromatic approach)
    (62, 3.0, 0.375),  # D
    (61, 3.375, 0.375),  # C
    (63, 3.75, 0.375),  # Eb
    (60, 4.125, 0.375),  # C
    (62, 4.5, 0.375),  # D
    (61, 4.875, 0.375),  # C
    (63, 5.25, 0.375),  # Eb
    (60, 5.625, 0.375)   # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    (64, 1.5, 0.125),  # F7: F, A, C, Eb
    (69, 1.5, 0.125),
    (67, 1.5, 0.125),
    (65, 1.5, 0.125),
    (69, 1.875, 0.125),  # Dm7: D, F, A, C
    (64, 1.875, 0.125),
    (67, 1.875, 0.125),
    (62, 1.875, 0.125),
    # Bar 3
    (64, 2.25, 0.125),  # F7
    (69, 2.25, 0.125),
    (67, 2.25, 0.125),
    (65, 2.25, 0.125),
    (69, 2.625, 0.125),  # Dm7
    (64, 2.625, 0.125),
    (67, 2.625, 0.125),
    (62, 2.625, 0.125),
    # Bar 4
    (64, 3.0, 0.125),  # F7
    (69, 3.0, 0.125),
    (67, 3.0, 0.125),
    (65, 3.0, 0.125),
    (69, 3.375, 0.125),  # Dm7
    (64, 3.375, 0.125),
    (67, 3.375, 0.125),
    (62, 3.375, 0.125),
    (64, 3.75, 0.125),  # F7
    (69, 3.75, 0.125),
    (67, 3.75, 0.125),
    (65, 3.75, 0.125),
    (69, 4.125, 0.125),  # Dm7
    (64, 4.125, 0.125),
    (67, 4.125, 0.125),
    (62, 4.125, 0.125),
    (64, 4.5, 0.125),  # F7
    (69, 4.5, 0.125),
    (67, 4.5, 0.125),
    (65, 4.5, 0.125),
    (69, 4.875, 0.125),  # Dm7
    (64, 4.875, 0.125),
    (67, 4.875, 0.125),
    (62, 4.875, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1 of bar 2
    (42, 1.5, 0.375),  # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.375),  # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4
    (36, 3.0, 0.375),  # Kick on 1 of bar 3
    (42, 3.0, 0.375),  # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.375),  # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4
    (36, 4.5, 0.375),  # Kick on 1 of bar 4
    (42, 4.5, 0.375),  # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.375),  # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Saxophone motif (start on 1.5s)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs.
sax_notes = [
    (67, 1.5, 0.375),  # Dm7: D
    (69, 2.25, 0.375),  # F (chromatic approach)
    (67, 3.0, 0.375),  # D
    (69, 3.75, 0.375),  # F
    (67, 4.5, 0.375),  # D
    (69, 5.25, 0.375)   # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=105, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_4_bar_intro.mid")
