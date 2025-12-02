
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
# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),   # D2 (root)
    (40, 1.875, 0.375), # Eb2 (chromatic approach)
    (43, 2.25, 0.375),  # G2 (fifth)
    (41, 2.625, 0.375), # Ab2 (chromatic approach)
    (38, 3.0, 0.375),   # D2 (root)
    (40, 3.375, 0.375), # Eb2 (chromatic approach)
    (43, 3.75, 0.375),  # G2 (fifth)
    (41, 4.125, 0.375), # Ab2 (chromatic approach)
    (38, 4.5, 0.375),   # D2 (root)
    (40, 4.875, 0.375), # Eb2 (chromatic approach)
    (43, 5.25, 0.375),  # G2 (fifth)
    (41, 5.625, 0.375)  # Ab2 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    (50, 1.5, 0.125), # D
    (53, 1.5, 0.125), # F
    (57, 1.5, 0.125), # A
    (60, 1.5, 0.125), # C

    # Bar 3: G7 (G-B-D-F)
    (55, 2.25, 0.125), # G
    (58, 2.25, 0.125), # B
    (62, 2.25, 0.125), # D
    (65, 2.25, 0.125), # F

    # Bar 4: Cm7 (C-Eb-G-Bb)
    (60, 3.0, 0.125), # C
    (63, 3.0, 0.125), # Eb
    (67, 3.0, 0.125), # G
    (70, 3.0, 0.125)  # Bb
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Bar 2
    # Kick on 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    # Hihat on &1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5))
    # Snare on 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125))
    # Hihat on &2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.875, end=bar_start + 1.0))
    # Kick on 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5))
    # Hihat on &3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.5, end=bar_start + 1.625))
    # Snare on 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.25))
    # Hihat on &4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 2.0, end=bar_start + 2.125))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (50), F (53), A (57), D (50)
sax_notes = [
    (50, 1.5, 0.125), # D
    (53, 1.625, 0.125), # F
    (57, 1.75, 0.125), # A
    (50, 1.875, 0.125), # D
    (50, 3.0, 0.125), # D
    (53, 3.125, 0.125), # F
    (57, 3.25, 0.125), # A
    (50, 3.375, 0.125)  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
