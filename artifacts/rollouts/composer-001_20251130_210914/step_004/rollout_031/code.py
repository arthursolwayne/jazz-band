
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.0, 0.375),    # Hihat on 1
    (38, 0.375, 0.375),  # Snare on 2
    (42, 0.375, 0.375),  # Hihat on 2
    (36, 0.75, 0.375),   # Kick on 3
    (42, 0.75, 0.375),   # Hihat on 3
    (38, 1.125, 0.375),  # Snare on 4
    (42, 1.125, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass (walking line, chromatic approaches)
bass_notes = [
    # Bar 2
    (48, 1.5, 0.375),    # F
    (49, 1.875, 0.375),  # Gb
    (50, 2.25, 0.375),   # G
    (51, 2.625, 0.375),  # Ab

    # Bar 3
    (52, 3.0, 0.375),    # A
    (53, 3.375, 0.375),  # Bb
    (54, 3.75, 0.375),   # B
    (55, 4.125, 0.375),  # C

    # Bar 4
    (55, 4.5, 0.375),    # C
    (54, 4.875, 0.375),  # B
    (53, 5.25, 0.375),   # Bb
    (52, 5.625, 0.375)   # A
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Diane - Piano (7th chords on 2 and 4)
piano_notes = [
    # Bar 2
    (57, 1.875, 0.375),  # F7 - F
    (60, 1.875, 0.375),  # F7 - A
    (62, 1.875, 0.375),  # F7 - C
    (64, 1.875, 0.375),  # F7 - E

    # Bar 3
    (57, 3.375, 0.375),  # F7 - F
    (60, 3.375, 0.375),  # F7 - A
    (62, 3.375, 0.375),  # F7 - C
    (64, 3.375, 0.375),  # F7 - E

    # Bar 4
    (57, 4.875, 0.375),  # F7 - F
    (60, 4.875, 0.375),  # F7 - A
    (62, 4.875, 0.375),  # F7 - C
    (64, 4.875, 0.375)   # F7 - E
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray - Drums (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.375),    # Hihat on 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.375),  # Hihat on 2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.375),   # Hihat on 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.375),  # Hihat on 4

    # Bar 3
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.375),    # Hihat on 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.375),  # Hihat on 2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.375),   # Hihat on 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.375),  # Hihat on 4

    # Bar 4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.375),    # Hihat on 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.375),  # Hihat on 2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.375),   # Hihat on 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.375)   # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante - Saxophone (motif)
sax_notes = [
    # Bar 2 - Motif: F, G, Ab, Bb
    (65, 1.5, 0.375),    # F
    (67, 1.875, 0.375),  # G
    (69, 2.25, 0.375),   # Ab
    (70, 2.625, 0.375),  # Bb

    # Bar 3 - Repeat motif
    (65, 3.0, 0.375),    # F
    (67, 3.375, 0.375),  # G
    (69, 3.75, 0.375),   # Ab
    (70, 4.125, 0.375),  # Bb

    # Bar 4 - End with a rest, leave it hanging
    (65, 4.5, 0.375),    # F
    (67, 4.875, 0.375),  # G
    (69, 5.25, 0.375),   # Ab
    (70, 5.625, 0.375)   # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("the_cellar_intro.mid")
