
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
    (36, 0.0, 0.375),  # kick on 1
    (42, 0.0, 0.375),  # hihat on 1
    (38, 0.375, 0.375),  # snare on 2
    (42, 0.375, 0.375),  # hihat on 2
    (36, 0.75, 0.375),  # kick on 3
    (42, 0.75, 0.375),  # hihat on 3
    (38, 1.125, 0.375),  # snare on 4
    (42, 1.125, 0.375),  # hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = [
    (19, 1.5, 0.375),  # Fm root (F)
    (21, 1.875, 0.375),  # Bb
    (20, 2.25, 0.375),  # Ab (chromatic approach)
    (19, 2.625, 0.375),  # F
    (22, 3.0, 0.375),  # Cm root (C)
    (24, 3.375, 0.375),  # Eb
    (23, 3.75, 0.375),  # D (chromatic approach)
    (22, 4.125, 0.375),  # C
    (25, 4.5, 0.375),  # Gm root (G)
    (27, 4.875, 0.375),  # B
    (26, 5.25, 0.375),  # A (chromatic approach)
    (25, 5.625, 0.375),  # G
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano (Diane): 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    (47, 1.5, 0.375),  # F7 (F, A, C, Eb)
    (50, 1.5, 0.375),
    (52, 1.5, 0.375),
    (55, 1.5, 0.375),
    (50, 2.25, 0.375),  # Cm7 (C, Eb, G, Bb)
    (53, 2.25, 0.375),
    (55, 2.25, 0.375),
    (57, 2.25, 0.375),
    # Bar 3 (3.0 - 4.5s)
    (47, 3.0, 0.375),  # F7
    (50, 3.0, 0.375),
    (52, 3.0, 0.375),
    (55, 3.0, 0.375),
    (50, 3.75, 0.375),  # Cm7
    (53, 3.75, 0.375),
    (55, 3.75, 0.375),
    (57, 3.75, 0.375),
    # Bar 4 (4.5 - 6.0s)
    (47, 4.5, 0.375),  # F7
    (50, 4.5, 0.375),
    (52, 4.5, 0.375),
    (55, 4.5, 0.375),
    (50, 5.25, 0.375),  # Cm7
    (53, 5.25, 0.375),
    (55, 5.25, 0.375),
    (57, 5.25, 0.375),
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax (Dante): short motif, make it sing
sax_notes = [
    (47, 1.5, 0.375),  # F
    (49, 1.875, 0.375),  # A
    (47, 2.25, 0.375),  # F (left hanging)
    (49, 2.625, 0.375),  # A (come back)
    (47, 3.0, 0.375),  # F
    (49, 3.375, 0.375),  # A
    (52, 3.75, 0.375),  # C
    (55, 4.125, 0.375),  # Eb
    (52, 4.5, 0.375),  # C
    (55, 4.875, 0.375),  # Eb
    (57, 5.25, 0.375),  # G
    (55, 5.625, 0.375),  # Eb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4 (Little Ray)
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # kick on 1
    (42, 1.5, 0.375),  # hihat on 1
    (38, 1.875, 0.375),  # snare on 2
    (42, 1.875, 0.375),  # hihat on 2
    (36, 2.25, 0.375),  # kick on 3
    (42, 2.25, 0.375),  # hihat on 3
    (38, 2.625, 0.375),  # snare on 4
    (42, 2.625, 0.375),  # hihat on 4
    # Bar 3
    (36, 3.0, 0.375),  # kick on 1
    (42, 3.0, 0.375),  # hihat on 1
    (38, 3.375, 0.375),  # snare on 2
    (42, 3.375, 0.375),  # hihat on 2
    (36, 3.75, 0.375),  # kick on 3
    (42, 3.75, 0.375),  # hihat on 3
    (38, 4.125, 0.375),  # snare on 4
    (42, 4.125, 0.375),  # hihat on 4
    # Bar 4
    (36, 4.5, 0.375),  # kick on 1
    (42, 4.5, 0.375),  # hihat on 1
    (38, 4.875, 0.375),  # snare on 2
    (42, 4.875, 0.375),  # hihat on 2
    (36, 5.25, 0.375),  # kick on 3
    (42, 5.25, 0.375),  # hihat on 3
    (38, 5.625, 0.375),  # snare on 4
    (42, 5.625, 0.375),  # hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
