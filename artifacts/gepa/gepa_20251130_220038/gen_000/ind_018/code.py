
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    (36, 0.0, 0.375),     # Kick on 1
    (42, 0.0, 0.1875),    # Hihat on 1
    (38, 0.375, 0.375),   # Snare on 2
    (42, 0.375, 0.1875),  # Hihat on 2
    (36, 0.75, 0.375),    # Kick on 3
    (42, 0.75, 0.1875),   # Hihat on 3
    (38, 1.125, 0.375),   # Snare on 4
    (42, 1.125, 0.1875)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Walking bass line in F
bass_notes = [
    (45, 1.5, 0.375),  # F
    (47, 1.875, 0.375), # G
    (46, 2.25, 0.375),  # Ab
    (48, 2.625, 0.375), # Bb
    (50, 3.0, 0.375),   # C
    (52, 3.375, 0.375), # D
    (51, 3.75, 0.375),  # Eb
    (53, 4.125, 0.375), # E
    (55, 4.5, 0.375),   # F
    (57, 4.875, 0.375), # G
    (56, 5.25, 0.375),  # Ab
    (58, 5.625, 0.375)  # Bb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane - 7th chords on 2 and 4, comp
piano_notes = [
    (57, 1.5, 0.1875),  # F7 on 1
    (59, 1.5, 0.1875),  # A
    (60, 1.5, 0.1875),  # C
    (62, 1.5, 0.1875),  # Eb

    (60, 2.25, 0.1875),  # F7 on 2
    (62, 2.25, 0.1875),  # A
    (63, 2.25, 0.1875),  # C
    (65, 2.25, 0.1875),  # Eb

    (57, 3.0, 0.1875),  # F7 on 3
    (59, 3.0, 0.1875),  # A
    (60, 3.0, 0.1875),  # C
    (62, 3.0, 0.1875),  # Eb

    (60, 3.75, 0.1875),  # F7 on 4
    (62, 3.75, 0.1875),  # A
    (63, 3.75, 0.1875),  # C
    (65, 3.75, 0.1875),  # Eb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),     # Kick on 1
    (42, 1.5, 0.1875),    # Hihat on 1
    (38, 1.875, 0.375),   # Snare on 2
    (42, 1.875, 0.1875),  # Hihat on 2
    (36, 2.25, 0.375),    # Kick on 3
    (42, 2.25, 0.1875),   # Hihat on 3
    (38, 2.625, 0.375),   # Snare on 4
    (42, 2.625, 0.1875),  # Hihat on 4

    (36, 3.0, 0.375),     # Kick on 1
    (42, 3.0, 0.1875),    # Hihat on 1
    (38, 3.375, 0.375),   # Snare on 2
    (42, 3.375, 0.1875),  # Hihat on 2
    (36, 3.75, 0.375),    # Kick on 3
    (42, 3.75, 0.1875),   # Hihat on 3
    (38, 4.125, 0.375),   # Snare on 4
    (42, 4.125, 0.1875),  # Hihat on 4

    (36, 4.5, 0.375),     # Kick on 1
    (42, 4.5, 0.1875),    # Hihat on 1
    (38, 4.875, 0.375),   # Snare on 2
    (42, 4.875, 0.1875),  # Hihat on 2
    (36, 5.25, 0.375),    # Kick on 3
    (42, 5.25, 0.1875),   # Hihat on 3
    (38, 5.625, 0.375),   # Snare on 4
    (42, 5.625, 0.1875)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - Tenor sax melody
sax_notes = [
    (62, 1.5, 0.25),    # Bb
    (64, 1.75, 0.25),   # D
    (65, 2.0, 0.25),    # Eb
    (62, 2.25, 0.25),   # Bb
    (67, 2.5, 0.25),    # F
    (69, 2.75, 0.25),   # G
    (67, 3.0, 0.25),    # F
    (65, 3.25, 0.25),   # Eb
    (64, 3.5, 0.25),    # D
    (62, 3.75, 0.25),   # Bb
    (60, 4.0, 0.25),    # A
    (62, 4.25, 0.25),   # Bb
    (64, 4.5, 0.25),    # D
    (65, 4.75, 0.25),   # Eb
    (67, 5.0, 0.25),    # F
    (69, 5.25, 0.25)    # G
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
