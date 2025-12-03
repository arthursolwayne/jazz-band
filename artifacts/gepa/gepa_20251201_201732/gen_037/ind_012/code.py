
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
    (36, 0.0, 0.375),    # Kick on 1
    (42, 0.375, 0.75),   # Hihat on 2
    (36, 0.75, 1.125),   # Kick on 3
    (42, 1.125, 1.5),    # Hihat on 4
]
for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (F2-C2, MIDI 53-58)
# Roots and fifths with chromatic approaches
bass_notes = [
    (53, 1.5, 1.75),     # F2
    (55, 1.75, 2.0),     # G2 (F2 chromatic up)
    (58, 2.0, 2.25),     # C3
    (56, 2.25, 2.5),     # Bb2 (C3 chromatic down)
    (53, 2.5, 2.75),     # F2
    (55, 2.75, 3.0),     # G2
    (58, 3.0, 3.25),     # C3
    (56, 3.25, 3.5),     # Bb2
    (53, 3.5, 3.75),     # F2
    (55, 3.75, 4.0),     # G2
    (58, 4.0, 4.25),     # C3
    (56, 4.25, 4.5),     # Bb2
    (53, 4.5, 4.75),     # F2
    (55, 4.75, 5.0),     # G2
    (58, 5.0, 5.25),     # C3
    (56, 5.25, 5.5),     # Bb2
]
for note, start, end in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    (53, 1.5, 2.0),      # F
    (60, 1.5, 2.0),      # Ab
    (58, 1.5, 2.0),      # C
    (62, 1.5, 2.0),      # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    (57, 2.0, 2.5),      # Bb
    (65, 2.0, 2.5),      # D
    (58, 2.0, 2.5),      # F
    (60, 2.0, 2.5),      # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    (58, 2.5, 3.0),      # C
    (61, 2.5, 3.0),      # Eb
    (62, 2.5, 3.0),      # G
    (57, 2.5, 3.0),      # Bb
])
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes.extend([
    (53, 3.0, 3.5),      # F
    (60, 3.0, 3.5),      # Ab
    (58, 3.0, 3.5),      # C
    (62, 3.0, 3.5),      # D
])
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    (57, 3.5, 4.0),      # Bb
    (65, 3.5, 4.0),      # D
    (58, 3.5, 4.0),      # F
    (60, 3.5, 4.0),      # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    (58, 4.0, 4.5),      # C
    (61, 4.0, 4.5),      # Eb
    (62, 4.0, 4.5),      # G
    (57, 4.0, 4.5),      # Bb
])
for note, start, end in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    drum_notes.append((36, bar_start + 0.0, bar_start + 0.375))
    drum_notes.append((36, bar_start + 0.75, bar_start + 1.125))
    # Snare on 2 and 4
    drum_notes.append((38, bar_start + 0.375, bar_start + 0.75))
    drum_notes.append((38, bar_start + 1.125, bar_start + 1.5))
    # Hihat on every eighth
    for i in range(8):
        drum_notes.append((42, bar_start + i*0.375, bar_start + i*0.375 + 0.1875))

for note, start, end in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Dante: Motif (F, G, Bb, C), short and singable
# Start on 1.5, end on 2.0
sax_notes = [
    (53, 1.5, 1.75),     # F
    (55, 1.75, 2.0),     # G
    (57, 2.0, 2.25),     # Bb
    (58, 2.25, 2.5),     # C
    (53, 2.5, 2.75),     # F
    (55, 2.75, 3.0),     # G
    (57, 3.0, 3.25),     # Bb
    (58, 3.25, 3.5),     # C
    (53, 3.5, 3.75),     # F
    (55, 3.75, 4.0),     # G
    (57, 4.0, 4.25),     # Bb
    (58, 4.25, 4.5),     # C
    (53, 4.5, 4.75),     # F
    (55, 4.75, 5.0),     # G
    (57, 5.0, 5.25),     # Bb
    (58, 5.25, 5.5),     # C
]
for note, start, end in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=end))

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
