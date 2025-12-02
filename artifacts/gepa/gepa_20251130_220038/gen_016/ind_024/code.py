
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
    (42, bar1_start + 0.0, 0.75),    # Hihat on 1 & 2
    (42, bar1_start + 0.375, 0.75),
    (36, bar1_start + 0.75, 0.375),  # Kick on 3
    (38, bar1_start + 1.125, 0.375), # Snare on 4
    (42, bar1_start + 0.75, 0.75),   # Hihat on 3 & 4
    (42, bar1_start + 1.125, 0.75)
]
for note, start, duration in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Bass: Walking line in F, chromatic approaches
bass_notes = [
    (37, bar2_start + 0.0, 0.375),  # F (37)
    (38, bar2_start + 0.375, 0.375), # Gb (38)
    (39, bar2_start + 0.75, 0.375),  # G (39)
    (40, bar2_start + 1.125, 0.375)  # Ab (40)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (45, bar2_start + 0.375, 0.375),  # F7 (45=7th)
    (48, bar2_start + 0.375, 0.375),  # A (48)
    (50, bar2_start + 0.375, 0.375),  # C (50)
    (48, bar2_start + 1.125, 0.375),  # A (48)
    (50, bar2_start + 1.125, 0.375),  # C (50)
    (45, bar2_start + 1.125, 0.375)   # F7 (45)
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif on F, start it, leave it hanging
sax_notes = [
    (66, bar2_start + 0.0, 0.375),  # F (66)
    (68, bar2_start + 0.375, 0.375), # G (68)
    (67, bar2_start + 0.75, 0.375),  # F# (67)
    (66, bar2_start + 1.125, 0.375)  # F (66)
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue in bar 2
bar2_drum_notes = [
    (36, bar2_start + 0.0, 0.375),   # Kick on 1
    (38, bar2_start + 0.375, 0.375),  # Snare on 2
    (42, bar2_start + 0.0, 0.75),     # Hihat on 1 & 2
    (42, bar2_start + 0.375, 0.75),
    (36, bar2_start + 0.75, 0.375),   # Kick on 3
    (38, bar2_start + 1.125, 0.375),  # Snare on 4
    (42, bar2_start + 0.75, 0.75),    # Hihat on 3 & 4
    (42, bar2_start + 1.125, 0.75)
]
for note, start, duration in bar2_drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Bass: Walking line with chromatic approach
bass_notes = [
    (41, bar3_start + 0.0, 0.375),   # Bb (41)
    (42, bar3_start + 0.375, 0.375),  # B (42)
    (43, bar3_start + 0.75, 0.375),   # C (43)
    (44, bar3_start + 1.125, 0.375)   # C# (44)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (45, bar3_start + 0.375, 0.375),  # F7
    (48, bar3_start + 0.375, 0.375),  # A
    (50, bar3_start + 0.375, 0.375),  # C
    (48, bar3_start + 1.125, 0.375),  # A
    (50, bar3_start + 1.125, 0.375),  # C
    (45, bar3_start + 1.125, 0.375)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Motif continuation, leave it hanging
sax_notes = [
    (66, bar3_start + 0.0, 0.375),  # F
    (68, bar3_start + 0.375, 0.375), # G
    (67, bar3_start + 0.75, 0.375),  # F#
    (66, bar3_start + 1.125, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: continue in bar 3
bar3_drum_notes = [
    (36, bar3_start + 0.0, 0.375),   # Kick on 1
    (38, bar3_start + 0.375, 0.375),  # Snare on 2
    (42, bar3_start + 0.0, 0.75),     # Hihat on 1 & 2
    (42, bar3_start + 0.375, 0.75),
    (36, bar3_start + 0.75, 0.375),   # Kick on 3
    (38, bar3_start + 1.125, 0.375),  # Snare on 4
    (42, bar3_start + 0.75, 0.75),    # Hihat on 3 & 4
    (42, bar3_start + 1.125, 0.75)
]
for note, start, duration in bar3_drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Bass: Walking line with chromatic approach
bass_notes = [
    (45, bar4_start + 0.0, 0.375),   # D (45)
    (46, bar4_start + 0.375, 0.375),  # Eb (46)
    (47, bar4_start + 0.75, 0.375),   # E (47)
    (48, bar4_start + 1.125, 0.375)   # F (48)
]
for note, start, duration in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=start + duration))

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (45, bar4_start + 0.375, 0.375),  # F7
    (48, bar4_start + 0.375, 0.375),  # A
    (50, bar4_start + 0.375, 0.375),  # C
    (48, bar4_start + 1.125, 0.375),  # A
    (50, bar4_start + 1.125, 0.375),  # C
    (45, bar4_start + 1.125, 0.375)   # F7
]
for note, start, duration in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + duration))

# Sax: Finish the motif
sax_notes = [
    (66, bar4_start + 0.0, 0.375),  # F
    (68, bar4_start + 0.375, 0.375), # G
    (67, bar4_start + 0.75, 0.375),  # F#
    (66, bar4_start + 1.125, 0.375)  # F
]
for note, start, duration in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

# Drums: final bar
bar4_drum_notes = [
    (36, bar4_start + 0.0, 0.375),   # Kick on 1
    (38, bar4_start + 0.375, 0.375),  # Snare on 2
    (42, bar4_start + 0.0, 0.75),     # Hihat on 1 & 2
    (42, bar4_start + 0.375, 0.75),
    (36, bar4_start + 0.75, 0.375),   # Kick on 3
    (38, bar4_start + 1.125, 0.375),  # Snare on 4
    (42, bar4_start + 0.75, 0.75),    # Hihat on 3 & 4
    (42, bar4_start + 1.125, 0.75)
]
for note, start, duration in bar4_drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration))

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
