
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
bar_length = 1.5
for i in range(4):  # 4 beats
    start = i * bar_length / 4
    # Kick on 1 and 3
    if i == 0 or i == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    if i == 1 or i == 3:
        note = pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for j in range(2):
        note = pretty_midi.Note(velocity=90, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.05)
        drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bar 2: Start of the melody
bar_start = 1.5

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    (38, 0.0),         # D2
    (41, 0.25),        # F#2 (chromatic approach)
    (43, 0.5),         # A2 (fifth of D)
    (41, 0.75),        # F#2
    (38, 1.0),         # D2
    (40, 1.25),        # E2 (chromatic approach)
    (43, 1.5),         # A2
    (40, 1.75),        # E2
    (38, 2.0),         # D2
    (41, 2.25),        # F#2
    (43, 2.5),         # A2
    (41, 2.75),        # F#2
    (38, 3.0),         # D2
    (40, 3.25),        # E2
    (43, 3.5),         # A2
    (40, 3.75),        # E2
]

for pitch, time in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=bar_start + time, end=bar_start + time + 0.25)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7sus4 (D, G, C#)
# Bar 3: G7sus4 (G, C, F)
# Bar 4: C7sus4 (C, F, Bb)
piano_notes = [
    # Bar 2: D7sus4
    (62, 1.5), (67, 1.5), (66, 1.5),  # D, G, C#
    # Bar 3: G7sus4
    (67, 3.0), (72, 3.0), (71, 3.0),  # G, C, F
    # Bar 4: C7sus4
    (60, 4.5), (65, 4.5), (64, 4.5),  # C, F, Bb
]

for pitch, time in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> F# (66) -> A (69) -> D (62) -> F# (66)
sax_notes = [
    (62, 1.5),  # D
    (66, 1.6),  # F#
    (69, 1.7),  # A
    (62, 2.0),  # D
    (66, 2.1),  # F#
    (69, 2.2),  # A
    (62, 2.5),  # D
    (66, 2.6),  # F#
    (69, 2.7),  # A
    (62, 3.0),  # D
]

for pitch, time in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=time, end=time + 0.1)
    sax.notes.append(note)

# Drums for bars 2-4
for i in range(4):  # 4 beats per bar for 3 bars = 12 beats
    start = bar_start + (i % 4) * bar_length / 4
    # Kick on 1 and 3
    if i % 4 == 0 or i % 4 == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    if i % 4 == 1 or i % 4 == 3:
        note = pretty_midi.Note(velocity=110, pitch=38, start=start, end=start + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    for j in range(2):
        note = pretty_midi.Note(velocity=90, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.05)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
