
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
    (36, 1.125, 0.375), (38, 1.5, 0.375), (42, 1.125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking, chromatic approaches)
bass_notes = [
    # Bar 2
    (20, 1.5, 0.375), (21, 1.875, 0.375), (20, 2.25, 0.375), (19, 2.625, 0.375),
    # Bar 3
    (17, 3.0, 0.375), (18, 3.375, 0.375), (17, 3.75, 0.375), (16, 4.125, 0.375),
    # Bar 4
    (14, 4.5, 0.375), (15, 4.875, 0.375), (14, 5.25, 0.375), (13, 5.625, 0.375)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Diane - Piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2: F7 on 2 and 4
    (42, 1.875, 0.375), (46, 1.875, 0.375), (50, 1.875, 0.375), (53, 1.875, 0.375),
    (42, 2.625, 0.375), (46, 2.625, 0.375), (50, 2.625, 0.375), (53, 2.625, 0.375),
    # Bar 3: Bb7 on 2 and 4
    (46, 3.375, 0.375), (50, 3.375, 0.375), (53, 3.375, 0.375), (57, 3.375, 0.375),
    (46, 4.125, 0.375), (50, 4.125, 0.375), (53, 4.125, 0.375), (57, 4.125, 0.375),
    # Bar 4: Eb7 on 2 and 4
    (49, 4.875, 0.375), (52, 4.875, 0.375), (55, 4.875, 0.375), (58, 4.875, 0.375),
    (49, 5.625, 0.375), (52, 5.625, 0.375), (55, 5.625, 0.375), (58, 5.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
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

# Dante - Tenor Sax (motif: F - Bb - D - Eb, leave it hanging on D)
sax_notes = [
    (53, 1.5, 0.375), (58, 1.875, 0.375), (55, 2.25, 0.375), (52, 2.625, 0.375),
    (55, 3.0, 0.375), (58, 3.375, 0.375), (55, 3.75, 0.375), (52, 4.125, 0.375),
    (55, 4.5, 0.375), (58, 4.875, 0.375), (55, 5.25, 0.375), (52, 5.625, 0.375)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
