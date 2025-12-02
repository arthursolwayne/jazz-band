
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 0.375),  # Kick on 1
    (38, 0.75, 0.375), # Snare on 2
    (42, 0.0, 0.1875), # Hihat on 1
    (42, 0.1875, 0.1875), # Hihat on &1
    (42, 0.375, 0.1875), # Hihat on 2
    (42, 0.5625, 0.1875), # Hihat on &2
    (42, 0.75, 0.1875), # Hihat on 3
    (42, 0.9375, 0.1875), # Hihat on &3
    (42, 1.125, 0.1875), # Hihat on 4
    (42, 1.3125, 0.1875), # Hihat on &4
    (36, 1.5, 0.375),  # Kick on 3
    (38, 1.5, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line, chromatic approaches
bass_notes = [
    (60, 1.5, 0.375),  # C
    (61, 1.875, 0.375), # C#
    (62, 2.25, 0.375),  # D
    (63, 2.625, 0.375), # D#
    (64, 3.0, 0.375),   # E
    (65, 3.375, 0.375), # F
    (66, 3.75, 0.375),  # F#
    (67, 4.125, 0.375), # G
    (68, 4.5, 0.375),   # G#
    (69, 4.875, 0.375), # A
    (70, 5.25, 0.375),  # A#
    (71, 5.625, 0.375), # B
    (72, 6.0, 0.375),   # C
]

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    (60, 1.5, 0.375),  # C7 (C, E, B)
    (64, 1.5, 0.375),
    (67, 1.5, 0.375),
    (69, 1.5, 0.375),
    (60, 2.25, 0.375),  # C7
    (64, 2.25, 0.375),
    (67, 2.25, 0.375),
    (69, 2.25, 0.375),
    (60, 3.0, 0.375),  # C7
    (64, 3.0, 0.375),
    (67, 3.0, 0.375),
    (69, 3.0, 0.375),
    (60, 3.75, 0.375),  # C7
    (64, 3.75, 0.375),
    (67, 3.75, 0.375),
    (69, 3.75, 0.375),
]

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 1.5, 0.375),  # Kick on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.5, 0.1875), # Hihat on 1
    (42, 1.6875, 0.1875), # Hihat on &1
    (42, 1.875, 0.1875), # Hihat on 2
    (42, 2.0625, 0.1875), # Hihat on &2
    (42, 2.25, 0.1875), # Hihat on 3
    (42, 2.4375, 0.1875), # Hihat on &3
    (42, 2.625, 0.1875), # Hihat on 4
    (42, 2.8125, 0.1875), # Hihat on &4
    (36, 3.0, 0.375),  # Kick on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.0, 0.1875), # Hihat on 1
    (42, 3.1875, 0.1875), # Hihat on &1
    (42, 3.375, 0.1875), # Hihat on 2
    (42, 3.5625, 0.1875), # Hihat on &2
    (42, 3.75, 0.1875), # Hihat on 3
    (42, 3.9375, 0.1875), # Hihat on &3
    (42, 4.125, 0.1875), # Hihat on 4
    (42, 4.3125, 0.1875), # Hihat on &4
    (36, 4.5, 0.375),  # Kick on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.5, 0.1875), # Hihat on 1
    (42, 4.6875, 0.1875), # Hihat on &1
    (42, 4.875, 0.1875), # Hihat on 2
    (42, 5.0625, 0.1875), # Hihat on &2
    (42, 5.25, 0.1875), # Hihat on 3
    (42, 5.4375, 0.1875), # Hihat on &3
    (42, 5.625, 0.1875), # Hihat on 4
    (42, 5.8125, 0.1875), # Hihat on &4
    (36, 6.0, 0.375),  # Kick on 3
    (38, 6.0, 0.375),  # Snare on 4
]

for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Melody: C (60), D (62), F (65), G (67), C (60)
# Start at 1.5s, end at 2.25s
sax_notes = [
    (60, 1.5, 0.375),  # C
    (62, 1.875, 0.375),  # D
    (65, 2.25, 0.375),  # F
    (67, 2.625, 0.375),  # G
    (60, 3.0, 0.375),   # C
    (62, 3.375, 0.375),  # D
    (65, 3.75, 0.375),  # F
    (67, 4.125, 0.375),  # G
    (60, 4.5, 0.375),   # C
    (62, 4.875, 0.375),  # D
    (65, 5.25, 0.375),  # F
    (67, 5.625, 0.375),  # G
    (60, 6.0, 0.375),   # C
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
