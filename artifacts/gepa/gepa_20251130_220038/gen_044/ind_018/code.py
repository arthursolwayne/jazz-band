
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
    (42, 0.375, 0.125),  # Hihat on & 1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.875, 0.125),  # Hihat on & 2
    (36, 1.125, 0.375),  # Kick on 3
    (42, 1.5, 0.125)     # Hihat on & 3
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    (48, 1.5, 0.375),   # F
    (49, 1.875, 0.375), # Gb
    (50, 2.25, 0.375),  # G
    (51, 2.625, 0.375), # Ab
    (53, 2.875, 0.375), # Bb
    (55, 3.25, 0.375),  # B
    (57, 3.625, 0.375), # C
    (58, 4.0, 0.375),   # C#
    (59, 4.375, 0.375), # D
    (60, 4.75, 0.375),  # D#
    (62, 5.125, 0.375), # F
    (63, 5.5, 0.375)    # F#
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.5, 0.375),    # F7 (F, A, C, Eb)
    (65, 1.5, 0.375),
    (64, 1.5, 0.375),
    (62, 1.5, 0.375),
    (65, 1.875, 0.375),  # F7
    (60, 1.875, 0.375),
    (64, 1.875, 0.375),
    (62, 1.875, 0.375),
    (60, 2.25, 0.375),   # F7
    (65, 2.25, 0.375),
    (64, 2.25, 0.375),
    (62, 2.25, 0.375),
    (65, 2.625, 0.375),  # F7
    (60, 2.625, 0.375),
    (64, 2.625, 0.375),
    (62, 2.625, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.125),  # Hihat on & 1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.125),  # Hihat on & 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.125),  # Hihat on & 3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.125),  # Hihat on & 4
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.125),  # Hihat on & 1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.125),  # Hihat on & 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.125),  # Hihat on & 3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.125),  # Hihat on & 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.125),  # Hihat on & 1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.125),  # Hihat on & 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.125),  # Hihat on & 3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.125)   # Hihat on & 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),     # G
    (64, 1.875, 0.375),   # A
    (65, 2.25, 0.375),    # Bb
    (62, 2.625, 0.375),   # G
    (60, 3.0, 0.375),     # F
    (62, 3.375, 0.375),   # G
    (64, 3.75, 0.375),    # A
    (65, 4.125, 0.375),   # Bb
    (62, 4.5, 0.375),     # G
    (60, 4.875, 0.375),   # F
    (62, 5.25, 0.375),    # G
    (64, 5.625, 0.375)    # A
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_shorter_intro.mid")
