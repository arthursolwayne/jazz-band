
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
    (42, 0.375, 0.75), # Hihat on 2
    (36, 0.75, 1.125), # Kick on 3
    (42, 1.125, 1.5)   # Hihat on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking line, chromatic approaches)
bass_notes = [
    (62, 1.5, 1.625), # D (root)
    (63, 1.625, 1.75), # Eb (chromatic)
    (60, 1.75, 1.875), # Bb (3rd)
    (62, 1.875, 2.0), # D (root)

    (64, 2.0, 2.125), # F (5th)
    (63, 2.125, 2.25), # Eb (chromatic)
    (61, 2.25, 2.375), # C (7th)
    (62, 2.375, 2.5), # D (root)

    (65, 2.5, 2.625), # G (extension)
    (64, 2.625, 2.75), # F (chromatic)
    (62, 2.75, 2.875), # D (root)
    (60, 2.875, 3.0), # Bb (3rd)

    (62, 3.0, 3.125), # D (root)
    (63, 3.125, 3.25), # Eb (chromatic)
    (60, 3.25, 3.375), # Bb (3rd)
    (62, 3.375, 3.5), # D (root)
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    (60, 1.625, 1.75), # C (Dm7)
    (64, 1.625, 1.75), # F
    (62, 1.625, 1.75), # D
    (67, 1.625, 1.75), # Bb

    (60, 2.25, 2.375), # C (Dm7)
    (64, 2.25, 2.375), # F
    (62, 2.25, 2.375), # D
    (67, 2.25, 2.375), # Bb

    (60, 3.0, 3.125), # C (Dm7)
    (64, 3.0, 3.125), # F
    (62, 3.0, 3.125), # D
    (67, 3.0, 3.125), # Bb
]
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    # Bar 2
    (36, 1.5, 1.875),   # Kick on 1
    (42, 1.5, 1.75),    # Hihat on 1
    (42, 1.75, 2.0),    # Hihat on 2
    (38, 1.75, 2.0),    # Snare on 2
    (42, 2.0, 2.25),    # Hihat on 3
    (36, 2.0, 2.375),   # Kick on 3
    (42, 2.25, 2.5),    # Hihat on 4
    (38, 2.25, 2.5),    # Snare on 4

    # Bar 3
    (36, 2.5, 2.875),   # Kick on 1
    (42, 2.5, 2.75),    # Hihat on 1
    (42, 2.75, 3.0),    # Hihat on 2
    (38, 2.75, 3.0),    # Snare on 2
    (42, 3.0, 3.25),    # Hihat on 3
    (36, 3.0, 3.375),   # Kick on 3
    (42, 3.25, 3.5),    # Hihat on 4
    (38, 3.25, 3.5),    # Snare on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Dante - Sax (melody - one short motif, make it sing)
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 1.75),    # D
    (64, 1.75, 2.0),    # F
    (62, 2.0, 2.125),   # D
    (60, 2.125, 2.375), # Bb

    (62, 3.0, 3.125),   # D
    (64, 3.125, 3.375), # F
    (62, 3.375, 3.5),   # D
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
