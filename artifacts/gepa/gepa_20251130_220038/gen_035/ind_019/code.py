
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

# Bass line: walking line with chromatic approaches
bass_notes = [
    (53, 1.5, 0.375),   # Fm7 root (F)
    (50, 1.875, 0.375),  # Eb (chromatic)
    (51, 2.25, 0.375),   # D (chromatic)
    (49, 2.625, 0.375),  # C (chromatic)
    (53, 2.75, 0.375),   # F
    (57, 3.125, 0.375),  # Ab
    (58, 3.5, 0.375),    # A
    (56, 3.875, 0.375),  # G
    (53, 4.25, 0.375),   # F
    (50, 4.625, 0.375),  # Eb
    (51, 5.0, 0.375),    # D
    (49, 5.375, 0.375)   # C
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, 2.25, 0.125),  # Eb7 (Eb, G, Bb, D)
    (48, 2.25, 0.125),
    (52, 2.25, 0.125),
    (55, 2.25, 0.125),
    (50, 3.0, 0.125),   # Eb7
    (48, 3.0, 0.125),
    (52, 3.0, 0.125),
    (55, 3.0, 0.125),
    (50, 3.75, 0.125),  # Eb7
    (48, 3.75, 0.125),
    (52, 3.75, 0.125),
    (55, 3.75, 0.125)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    (36, 1.5, 0.375),   # Kick on 1
    (42, 1.875, 0.125), # Hihat on &1
    (38, 2.25, 0.375),  # Snare on 2
    (42, 2.375, 0.125), # Hihat on &2
    (36, 2.625, 0.375), # Kick on 3
    (42, 2.75, 0.125),  # Hihat on &3
    (38, 3.0, 0.375),   # Snare on 4
    (42, 3.125, 0.125), # Hihat on &4
    (36, 3.5, 0.375),   # Kick on 1
    (42, 3.875, 0.125), # Hihat on &1
    (38, 4.25, 0.375),  # Snare on 2
    (42, 4.375, 0.125), # Hihat on &2
    (36, 4.625, 0.375), # Kick on 3
    (42, 4.75, 0.125),  # Hihat on &3
    (38, 5.0, 0.375),   # Snare on 4
    (42, 5.125, 0.125)  # Hihat on &4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax melody: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    (55, 1.5, 0.375),   # Fm7 (F, Ab, C, Eb) - first note: A (55)
    (53, 1.875, 0.375),  # E
    (50, 2.25, 0.25),    # D (leave it hanging)
    (53, 2.625, 0.375),  # E (come back)
    (55, 3.0, 0.375),    # A
    (53, 3.375, 0.375),  # E
    (50, 3.75, 0.375),   # D
    (55, 4.125, 0.375),  # A
    (58, 4.5, 0.375),    # C (next beat)
    (55, 4.875, 0.375),  # A
    (53, 5.25, 0.375),   # E
    (50, 5.625, 0.375)   # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
