
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
    (36, bar1_start, 0.375),  # Kick on 1
    (38, bar1_start + 0.375, 0.375),  # Snare on 2
    (42, bar1_start, 0.75),  # Hihat on 1 & 2
    (42, bar1_start + 0.375, 0.75),  # Hihat on 2 & 3
    (36, bar1_start + 0.75, 0.375),  # Kick on 3
    (38, bar1_start + 1.125, 0.375),  # Snare on 4
    (42, bar1_start + 0.75, 1.5),  # Hihat on 3 & 4
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches, D2-G2 (MIDI 38-43)
# Bar 2: Fm7 -> Bb7 -> Eb7 -> Am7
# Bar 3: Fm7 -> Bb7 -> Eb7 -> Am7
# Bar 4: Fm7 -> Bb7 -> Eb7 -> Am7

# Bass line (MIDI 38-43)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2
bass_notes = [
    (38, bar2_start, 0.375),     # F (root)
    (40, bar2_start + 0.375, 0.375),  # Ab (flat 5th)
    (43, bar2_start + 0.75, 0.375),  # Bb (bass approach)
    (43, bar2_start + 1.125, 0.375),  # Bb (chord root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3
bass_notes = [
    (38, bar3_start, 0.375),     # F (root)
    (40, bar3_start + 0.375, 0.375),  # Ab (flat 5th)
    (45, bar3_start + 0.75, 0.375),  # C (approach)
    (45, bar3_start + 1.125, 0.375),  # C (chord root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4
bass_notes = [
    (38, bar4_start, 0.375),     # F (root)
    (40, bar4_start + 0.375, 0.375),  # Ab (flat 5th)
    (48, bar4_start + 0.75, 0.375),  # E (approach)
    (48, bar4_start + 1.125, 0.375),  # E (chord root)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, D, C) -> Bb7 (Bb, D, F, Ab)
# Bar 3: Eb7 (Eb, G, Bb, D) -> Am7 (A, C, E, G)
# Bar 4: Fm7 (F, Ab, D, C) -> Bb7 (Bb, D, F, Ab)

# Bar 2
piano_notes = [
    (53, bar2_start, 0.75),  # F
    (60, bar2_start, 0.75),  # Ab
    (58, bar2_start, 0.75),  # D
    (60, bar2_start, 0.75),  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3
piano_notes = [
    (57, bar3_start, 0.75),  # Eb
    (62, bar3_start, 0.75),  # G
    (60, bar3_start, 0.75),  # Bb
    (65, bar3_start, 0.75),  # D
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4
piano_notes = [
    (53, bar4_start, 0.75),  # F
    (60, bar4_start, 0.75),  # Ab
    (58, bar4_start, 0.75),  # D
    (60, bar4_start, 0.75),  # C
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Motif: F - Eb - D - F
# Start on bar 2, play first three notes, then come back on bar 3 to finish

bar2_start_sax = bar2_start
bar3_start_sax = bar3_start
bar4_start_sax = bar4_start

# Bar 2: Play F, Eb, D
sax_notes = [
    (53, bar2_start_sax, 0.375),  # F
    (57, bar2_start_sax + 0.375, 0.375),  # Eb
    (58, bar2_start_sax + 0.75, 0.375),  # D
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 3: Finish the motif with F
sax_notes = [
    (53, bar3_start_sax + 0.75, 0.375),  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Bar 4: Play a counter-melody to the bass line
# E - D - C - Bb
sax_notes = [
    (58, bar4_start_sax, 0.375),  # E
    (58, bar4_start_sax + 0.375, 0.375),  # D
    (57, bar4_start_sax + 0.75, 0.375),  # C
    (57, bar4_start_sax + 1.125, 0.375),  # Bb
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=start, end=start + duration))

# Add drum fills in bar 2 and 3
# Bar 2
bar2_drum_fill_start = bar2_start
bar2_drum_fill_notes = [
    (36, bar2_drum_fill_start + 1.125, 0.125),  # Kick
    (38, bar2_drum_fill_start + 1.125, 0.125),  # Snare
    (42, bar2_drum_fill_start + 1.125, 0.25),  # Hihat
]
for note, start, duration in bar2_drum_fill_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3
bar3_drum_fill_start = bar3_start
bar3_drum_fill_notes = [
    (36, bar3_drum_fill_start + 1.125, 0.125),  # Kick
    (38, bar3_drum_fill_start + 1.125, 0.125),  # Snare
    (42, bar3_drum_fill_start + 1.125, 0.25),  # Hihat
]
for note, start, duration in bar3_drum_fill_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Finalize
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
