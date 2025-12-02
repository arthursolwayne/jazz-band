
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
    (36, bar1_start + 0.0, 0.375),  # Kick on 1
    (38, bar1_start + 0.375, 0.375), # Snare on 2
    (42, bar1_start + 0.0, 0.75),   # Hihat on 1 & 2
    (42, bar1_start + 0.375, 0.75),
    (36, bar1_start + 0.75, 0.375),  # Kick on 3
    (38, bar1_start + 1.125, 0.375), # Snare on 4
    (42, bar1_start + 0.75, 0.75),   # Hihat on 3 & 4
    (42, bar1_start + 1.125, 0.75)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (F2 - C3), roots and fifths with chromatic approaches
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2: Fm7 -> Bbm7
# Roots: F2 (38), Bb2 (35)
# Fifths: C3 (40), F3 (44)
# Chromatic approaches: E2 (33) to F2, A2 (39) to Bb2
bass_notes = [
    (33, bar2_start + 0.0, 0.25), # E2 (approach to F2)
    (38, bar2_start + 0.25, 0.25), # F2
    (40, bar2_start + 0.5, 0.25),  # C3 (fifth of F)
    (35, bar2_start + 0.75, 0.25), # Bb2
    (39, bar2_start + 1.0, 0.25),  # A2 (approach to Bb2)
    (44, bar2_start + 1.25, 0.25), # F3 (fifth of Bb)
    (35, bar2_start + 1.5, 0.25),  # Bb2
    (40, bar2_start + 1.75, 0.25), # C3
    (38, bar2_start + 2.0, 0.25),  # F2
    (44, bar2_start + 2.25, 0.25), # F3
]

# Bar 3: Ab7 -> Dm7
# Roots: Ab2 (32), D2 (37)
# Fifths: Eb3 (43), A3 (47)
# Chromatic approaches: G2 (37) to Ab2, C2 (34) to D2
bass_notes.extend([
    (37, bar3_start + 0.0, 0.25), # G2 (approach to Ab2)
    (32, bar3_start + 0.25, 0.25), # Ab2
    (43, bar3_start + 0.5, 0.25),  # Eb3 (fifth of Ab)
    (37, bar3_start + 0.75, 0.25), # D2
    (34, bar3_start + 1.0, 0.25),  # C2 (approach to D2)
    (47, bar3_start + 1.25, 0.25), # A3 (fifth of D)
    (37, bar3_start + 1.5, 0.25),  # D2
    (43, bar3_start + 1.75, 0.25), # Eb3
    (32, bar3_start + 2.0, 0.25),  # Ab2
    (47, bar3_start + 2.25, 0.25), # A3
])

# Bar 4: Cm7 -> Fm7
# Roots: C2 (36), F2 (38)
# Fifths: G3 (46), C4 (48)
# Chromatic approaches: B2 (34) to C2, E2 (33) to F2
bass_notes.extend([
    (34, bar4_start + 0.0, 0.25), # B2 (approach to C2)
    (36, bar4_start + 0.25, 0.25), # C2
    (46, bar4_start + 0.5, 0.25),  # G3 (fifth of C)
    (38, bar4_start + 0.75, 0.25), # F2
    (33, bar4_start + 1.0, 0.25),  # E2 (approach to F2)
    (48, bar4_start + 1.25, 0.25), # C4 (fifth of F)
    (38, bar4_start + 1.5, 0.25),  # F2
    (46, bar4_start + 1.75, 0.25), # G3
    (36, bar4_start + 2.0, 0.25),  # C2
    (48, bar4_start + 2.25, 0.25), # C4
])

for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    (53, bar2_start + 0.0, 0.75), # F
    (58, bar2_start + 0.0, 0.75), # Ab
    (59, bar2_start + 0.0, 0.75), # C
    (60, bar2_start + 0.0, 0.75)  # Eb
]

# Bar 3: Ab7 (Ab, C, Eb, G)
piano_notes.extend([
    (55, bar3_start + 0.0, 0.75), # Ab
    (59, bar3_start + 0.0, 0.75), # C
    (60, bar3_start + 0.0, 0.75), # Eb
    (62, bar3_start + 0.0, 0.75)  # G
])

# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    (60, bar4_start + 0.0, 0.75), # C
    (60, bar4_start + 0.0, 0.75), # Eb
    (62, bar4_start + 0.0, 0.75), # G
    (61, bar4_start + 0.0, 0.75)  # Bb
])

for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_drums = [
    (36, bar2_start + 0.0, 0.375), # Kick on 1
    (38, bar2_start + 0.375, 0.375), # Snare on 2
    (42, bar2_start + 0.0, 0.75), # Hihat on 1 & 2
    (42, bar2_start + 0.375, 0.75),
    (36, bar2_start + 0.75, 0.375), # Kick on 3
    (38, bar2_start + 1.125, 0.375), # Snare on 4
    (42, bar2_start + 0.75, 0.75), # Hihat on 3 & 4
    (42, bar2_start + 1.125, 0.75)
]
for note, start, duration in bar2_drums:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

bar3_drums = [
    (36, bar3_start + 0.0, 0.375), # Kick on 1
    (38, bar3_start + 0.375, 0.375), # Snare on 2
    (42, bar3_start + 0.0, 0.75), # Hihat on 1 & 2
    (42, bar3_start + 0.375, 0.75),
    (36, bar3_start + 0.75, 0.375), # Kick on 3
    (38, bar3_start + 1.125, 0.375), # Snare on 4
    (42, bar3_start + 0.75, 0.75), # Hihat on 3 & 4
    (42, bar3_start + 1.125, 0.75)
]
for note, start, duration in bar3_drums:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

bar4_drums = [
    (36, bar4_start + 0.0, 0.375), # Kick on 1
    (38, bar4_start + 0.375, 0.375), # Snare on 2
    (42, bar4_start + 0.0, 0.75), # Hihat on 1 & 2
    (42, bar4_start + 0.375, 0.75),
    (36, bar4_start + 0.75, 0.375), # Kick on 3
    (38, bar4_start + 1.125, 0.375), # Snare on 4
    (42, bar4_start + 0.75, 0.75), # Hihat on 3 & 4
    (42, bar4_start + 1.125, 0.75)
]
for note, start, duration in bar4_drums:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# You: Tenor sax - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm7 chord
sax_notes = [
    (66, bar2_start + 0.0, 0.5),   # F
    (71, bar2_start + 0.5, 0.5),   # Ab
    (66, bar2_start + 1.0, 0.5),   # F
    (69, bar2_start + 1.5, 0.5),   # G
    (66, bar2_start + 2.0, 0.5),   # F
    (71, bar2_start + 2.5, 0.5),   # Ab
    (72, bar2_start + 3.0, 0.5),   # A
    (69, bar2_start + 3.5, 0.5),   # G
    (66, bar2_start + 4.0, 0.5),   # F
    (71, bar2_start + 4.5, 0.5)    # Ab
]

for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])
midi.write('fm_intro.mid')
