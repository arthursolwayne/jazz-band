
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
    (42, 0.0, 0.1875), # Hihat on 1
    (38, 0.375, 0.375), # Snare on 2
    (42, 0.375, 0.1875), # Hihat on 2
    (36, 0.75, 0.375),  # Kick on 3
    (42, 0.75, 0.1875), # Hihat on 3
    (38, 1.125, 0.375), # Snare on 4
    (42, 1.125, 0.1875) # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Fm7 -> Bb7 -> Eb7 -> Am7 (Fm key)
# Marcus: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (Fm7)
    (53, 1.5, 0.375),  # F (root)
    (58, 1.875, 0.375), # C (fifth)
    (52, 2.25, 0.375),  # Eb (chromatic approach)
    (53, 2.625, 0.375), # F (resolve)

    # Bar 3 (Bb7)
    (57, 3.0, 0.375),  # Bb
    (62, 3.375, 0.375), # F (fifth)
    (56, 3.75, 0.375),  # Ab (chromatic approach)
    (57, 4.125, 0.375), # Bb

    # Bar 4 (Eb7)
    (55, 4.5, 0.375),  # Eb
    (60, 4.875, 0.375), # B (fifth)
    (54, 5.25, 0.375),  # G (chromatic approach)
    (55, 5.625, 0.375), # Eb
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    (53, 1.5, 1.5),   # F
    (60, 1.5, 1.5),   # C
    (57, 1.5, 1.5),   # Ab
    (58, 1.5, 1.5),   # D

    # Bar 3: Bb7 (Bb, D, F, Ab)
    (57, 3.0, 1.5),   # Bb
    (65, 3.0, 1.5),   # D
    (53, 3.0, 1.5),   # F
    (57, 3.0, 1.5),   # Ab

    # Bar 4: Eb7 (Eb, G, Bb, D)
    (55, 4.5, 1.5),   # Eb
    (62, 4.5, 1.5),   # G
    (57, 4.5, 1.5),   # Bb
    (60, 4.5, 1.5),   # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm scale: F, Gb, G, Ab, A, Bb, B, C
sax_notes = [
    (53, 1.5, 0.375),  # F
    (55, 1.875, 0.375), # G
    (53, 2.25, 0.375),  # F (hanging)
    (53, 3.0, 0.375),   # F (return)
    (58, 3.375, 0.375), # C
    (53, 3.75, 0.375),  # F (resolve)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    (36, 1.5, 0.375),  # Kick on 1
    (42, 1.5, 0.1875), # Hihat on 1
    (38, 1.875, 0.375), # Snare on 2
    (42, 1.875, 0.1875), # Hihat on 2
    (36, 2.25, 0.375),  # Kick on 3
    (42, 2.25, 0.1875), # Hihat on 3
    (38, 2.625, 0.375), # Snare on 4
    (42, 2.625, 0.1875), # Hihat on 4

    # Bar 3
    (36, 3.0, 0.375),  # Kick on 1
    (42, 3.0, 0.1875), # Hihat on 1
    (38, 3.375, 0.375), # Snare on 2
    (42, 3.375, 0.1875), # Hihat on 2
    (36, 3.75, 0.375),  # Kick on 3
    (42, 3.75, 0.1875), # Hihat on 3
    (38, 4.125, 0.375), # Snare on 4
    (42, 4.125, 0.1875), # Hihat on 4

    # Bar 4
    (36, 4.5, 0.375),  # Kick on 1
    (42, 4.5, 0.1875), # Hihat on 1
    (38, 4.875, 0.375), # Snare on 2
    (42, 4.875, 0.1875), # Hihat on 2
    (36, 5.25, 0.375),  # Kick on 3
    (42, 5.25, 0.1875), # Hihat on 3
    (38, 5.625, 0.375), # Snare on 4
    (42, 5.625, 0.1875), # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
