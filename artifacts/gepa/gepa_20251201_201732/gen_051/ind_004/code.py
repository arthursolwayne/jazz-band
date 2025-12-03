
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (36, 0.0, 1.0),    # Kick on beat 1
    (38, 0.5, 1.0),    # Snare on beat 2
    (42, 0.0, 1.0),    # Hihat on 1
    (42, 0.25, 1.0),   # Hihat on 2
    (42, 0.5, 1.0),    # Hihat on 3
    (42, 0.75, 1.0),   # Hihat on 4
    (36, 1.0, 1.0),    # Kick on beat 3
    (38, 1.5, 1.0),    # Snare on beat 4
    (42, 1.0, 1.0),    # Hihat on 3
    (42, 1.25, 1.0),   # Hihat on 4
    (42, 1.5, 1.0),    # Hihat on 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 1.5, 0.375),  # D2 (root)
    (40, 1.875, 0.375), # F#2 (chromatic approach)
    (43, 2.25, 0.375),  # A2 (fifth)
    (41, 2.625, 0.375), # G#2 (chromatic approach)
    (43, 2.625, 0.375),  # A2 (fifth)
    (45, 3.0, 0.375),   # C3 (chromatic approach)
    (47, 3.375, 0.375), # D3 (root)
    (49, 3.75, 0.375),  # F#3 (chromatic approach)
    (52, 4.125, 0.375), # A3 (fifth)
    (50, 4.5, 0.375),   # G#3 (chromatic approach)
    (52, 4.5, 0.375),   # A3 (fifth)
    (54, 4.875, 0.375), # C4 (chromatic approach)
    (56, 5.25, 0.375),  # D4 (root)
    (58, 5.625, 0.375), # F#4 (chromatic approach)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C#)
piano_notes = [
    (50, 1.5, 0.375),  # D
    (53, 1.5, 0.375),  # F#
    (57, 1.5, 0.375),  # A
    (60, 1.5, 0.375),  # C#
    (55, 2.0, 0.375),  # B
    (57, 2.0, 0.375),  # A
    (60, 2.0, 0.375),  # C#
    (62, 2.0, 0.375),  # D
    (50, 2.5, 0.375),  # D
    (53, 2.5, 0.375),  # F#
    (57, 2.5, 0.375),  # A
    (60, 2.5, 0.375),  # C#
    (55, 3.0, 0.375),  # B
    (57, 3.0, 0.375),  # A
    (60, 3.0, 0.375),  # C#
    (62, 3.0, 0.375),  # D
    (50, 3.5, 0.375),  # D
    (53, 3.5, 0.375),  # F#
    (57, 3.5, 0.375),  # A
    (60, 3.5, 0.375),  # C#
    (55, 4.0, 0.375),  # B
    (57, 4.0, 0.375),  # A
    (60, 4.0, 0.375),  # C#
    (62, 4.0, 0.375),  # D
    (50, 4.5, 0.375),  # D
    (53, 4.5, 0.375),  # F#
    (57, 4.5, 0.375),  # A
    (60, 4.5, 0.375),  # C#
    (55, 5.0, 0.375),  # B
    (57, 5.0, 0.375),  # A
    (60, 5.0, 0.375),  # C#
    (62, 5.0, 0.375),  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (E) -> F# -> A -> D (end on D)
sax_notes = [
    (50, 1.5, 0.375),  # D
    (52, 1.875, 0.375), # E
    (53, 2.25, 0.375),  # F#
    (57, 2.625, 0.375), # A
    (50, 3.0, 0.375),  # D
    (50, 4.125, 0.375), # D (rest)
    (50, 5.25, 0.375),  # D
    (52, 5.625, 0.375), # E
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on beat 1
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 1.0))
    # Snare on beat 2
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.5, end=bar_start + 0.5 + 1.0))
    # Hihat on every eighth
    for i in range(0, 8):
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.375))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
