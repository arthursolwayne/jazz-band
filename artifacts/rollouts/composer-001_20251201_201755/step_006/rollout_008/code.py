
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5
drum_notes = [
    # Kick on 1 and 3
    (36, bar1_start, 0.375),
    (36, bar1_start + 0.75, 0.375),
    # Snare on 2 and 4
    (38, bar1_start + 0.375, 0.375),
    (38, bar1_start + 1.125, 0.375),
    # Hihat on every eighth
    (42, bar1_start, 0.1875),
    (42, bar1_start + 0.1875, 0.1875),
    (42, bar1_start + 0.375, 0.1875),
    (42, bar1_start + 0.5625, 0.1875),
    (42, bar1_start + 0.75, 0.1875),
    (42, bar1_start + 0.9375, 0.1875),
    (42, bar1_start + 1.125, 0.1875),
    (42, bar1_start + 1.3125, 0.1875)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, roots and fifths with chromatic approaches
# Dm7: D, F, A, C
# Dm: D, F, A, C
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2: Dm (D, F, A, C)
# Root (D2), chromatic approach (C#2), root (D2), fifth (A2)
bass_notes = [
    (38, bar2_start, 0.375),   # D2
    (37, bar2_start + 0.1875, 0.1875),  # C#2
    (38, bar2_start + 0.375, 0.375),   # D2
    (45, bar2_start + 0.75, 0.375)     # A2
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: F7 (F, A, C, E)
# Root (F2), chromatic approach (E#2), root (F2), fifth (C3)
bass_notes = [
    (41, bar3_start, 0.375),   # F2
    (40, bar3_start + 0.1875, 0.1875),  # E#2
    (41, bar3_start + 0.375, 0.375),   # F2
    (48, bar3_start + 0.75, 0.375)     # C3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Gm7 (G, Bb, D, F)
# Root (G2), chromatic approach (F#2), root (G2), fifth (D3)
bass_notes = [
    (43, bar4_start, 0.375),   # G2
    (42, bar4_start + 0.1875, 0.1875),  # F#2
    (43, bar4_start + 0.375, 0.375),   # G2
    (50, bar4_start + 0.75, 0.375)     # D3
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, each bar a different chord, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    (50, bar2_start, 0.375),   # D3
    (53, bar2_start, 0.375),   # F3
    (57, bar2_start, 0.375),   # A3
    (60, bar2_start, 0.375)    # C4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: F7 (F, A, C, E)
piano_notes = [
    (55, bar3_start, 0.375),   # F3
    (58, bar3_start, 0.375),   # A3
    (60, bar3_start, 0.375),   # C4
    (64, bar3_start, 0.375)    # E4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Gm7 (G, Bb, D, F)
piano_notes = [
    (55, bar4_start, 0.375),   # G3
    (57, bar4_start, 0.375),   # Bb3
    (62, bar4_start, 0.375),   # D4
    (65, bar4_start, 0.375)    # F4
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: Motif, start it, leave it hanging, finish it
# Dm scale: D, Eb, F, G, A, Bb, C, D
# Motif: D, Eb, F, G (4 notes), leave it on G, come back and finish with A, Bb, C

# Bar 2: D, Eb, F, G
sax_notes = [
    (62, bar2_start, 0.375),   # D4
    (63, bar2_start + 0.375, 0.375),  # Eb4
    (64, bar2_start + 0.75, 0.375),   # F4
    (65, bar2_start + 1.125, 0.375)   # G4
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: rest
# Bar 4: A, Bb, C, D
sax_notes = [
    (67, bar4_start, 0.375),   # A4
    (69, bar4_start + 0.375, 0.375),  # Bb4
    (71, bar4_start + 0.75, 0.375),   # C5
    (72, bar4_start + 1.125, 0.375)   # D5
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar1_end + (bar - 2) * 1.5
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.125, end=bar_start + 1.125 + 0.375))
    # Hihat on every eighth
    for i in range(8):
        start = bar_start + i * 0.1875
        drums.notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 0.1875))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
