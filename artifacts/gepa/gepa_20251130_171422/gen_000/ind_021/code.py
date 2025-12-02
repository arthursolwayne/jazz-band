
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
    (36, 0.0, 0.375),   # Kick on 1
    (42, 0.375, 0.125), # Hihat on &1
    (38, 0.75, 0.375),  # Snare on 2
    (42, 0.875, 0.125), # Hihat on &2
    (36, 1.125, 0.375), # Kick on 3
    (42, 1.5, 0.125),   # Hihat on &3
    (38, 1.875, 0.375), # Snare on 4
    (42, 2.0, 0.125)    # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking, chromatic approaches
bass_notes = [
    (45, 1.5, 0.375),   # D
    (46, 1.875, 0.375), # Eb
    (47, 2.25, 0.375),  # E
    (48, 2.625, 0.375), # F
    (49, 2.75, 0.375),  # F#
    (50, 3.125, 0.375), # G
    (51, 3.5, 0.375),   # G#
    (52, 3.875, 0.375), # A
    (53, 4.25, 0.375),  # A#
    (54, 4.625, 0.375), # B
    (55, 4.75, 0.375),  # B#
    (56, 5.125, 0.375), # C
    (57, 5.5, 0.375),   # C#
    (58, 5.875, 0.375)  # D
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 1.875, 0.375), # G7 (G, B, D, F)
    (52, 1.875, 0.375),
    (53, 1.875, 0.375),
    (55, 1.875, 0.375),
    (50, 2.625, 0.375), # G7
    (52, 2.625, 0.375),
    (53, 2.625, 0.375),
    (55, 2.625, 0.375),
    (57, 3.5, 0.375),   # B7
    (59, 3.5, 0.375),
    (60, 3.5, 0.375),
    (62, 3.5, 0.375),
    (57, 4.375, 0.375), # B7
    (59, 4.375, 0.375),
    (60, 4.375, 0.375),
    (62, 4.375, 0.375)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: full bar
drum_notes = [
    (36, 1.5, 0.375),    # Kick on 1
    (42, 1.5, 0.125),    # Hihat on &1
    (38, 1.875, 0.375),  # Snare on 2
    (42, 1.875, 0.125),  # Hihat on &2
    (36, 2.25, 0.375),   # Kick on 3
    (42, 2.25, 0.125),   # Hihat on &3
    (38, 2.625, 0.375),  # Snare on 4
    (42, 2.625, 0.125),  # Hihat on &4
    (36, 3.0, 0.375),    # Kick on 1
    (42, 3.0, 0.125),    # Hihat on &1
    (38, 3.375, 0.375),  # Snare on 2
    (42, 3.375, 0.125),  # Hihat on &2
    (36, 3.75, 0.375),   # Kick on 3
    (42, 3.75, 0.125),   # Hihat on &3
    (38, 4.125, 0.375),  # Snare on 4
    (42, 4.125, 0.125),  # Hihat on &4
    (36, 4.5, 0.375),    # Kick on 1
    (42, 4.5, 0.125),    # Hihat on &1
    (38, 4.875, 0.375),  # Snare on 2
    (42, 4.875, 0.125),  # Hihat on &2
    (36, 5.25, 0.375),   # Kick on 3
    (42, 5.25, 0.125),   # Hihat on &3
    (38, 5.625, 0.375),  # Snare on 4
    (42, 5.625, 0.125)   # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (62, 1.5, 0.375),  # B
    (64, 1.875, 0.375), # D
    (62, 2.25, 0.375),  # B
    (64, 2.625, 0.375), # D
    (66, 2.75, 0.375),  # E
    (64, 3.125, 0.375), # D
    (62, 3.5, 0.375),   # B
    (64, 3.875, 0.375), # D
    (66, 4.25, 0.375),  # E
    (64, 4.625, 0.375), # D
    (62, 4.75, 0.375),  # B
    (64, 5.125, 0.375), # D
    (66, 5.5, 0.375),   # E
    (64, 5.875, 0.375)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
