
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
kick_times = [bar1_start + 0.375, bar1_start + 1.125]
snare_times = [bar1_start + 0.75, bar1_start + 1.5]
hihat_times = [bar1_start + 0.1875, bar1_start + 0.375, bar1_start + 0.5625, bar1_start + 0.75, bar1_start + 0.9375, bar1_start + 1.125, bar1_start + 1.3125, bar1_start + 1.5]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
# F7 chord: F A C E (root, 3, 5, 7)
# Bass line in F: F, G#, A#, B, C#, D#, E#, F
bass_notes = [
    (1.5, 71),  # F (C4)
    (1.875, 73),  # G#
    (2.25, 75),  # A#
    (2.625, 76),  # B
    (3.0, 78),  # C#
    (3.375, 80),  # D#
    (3.75, 81),  # E#
    (4.125, 71),  # F
    (4.5, 73),  # G#
    (4.875, 75),  # A#
    (5.25, 76),  # B
    (5.625, 78),  # C#
    (6.0, 71)  # F
]
for t, pitch in bass_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.375)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: F7 (F A C E)
# Bar 3: B7 (B D# F# A)
# Bar 4: E7 (E G# B D)
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2: F7 - comp on 2 and 4
piano_notes = [
    (bar2_start + 0.75, 71),  # F
    (bar2_start + 0.75, 74),  # A
    (bar2_start + 0.75, 76),  # C
    (bar2_start + 0.75, 79),  # E
    (bar2_start + 1.5, 71),  # F
    (bar2_start + 1.5, 74),  # A
    (bar2_start + 1.5, 76),  # C
    (bar2_start + 1.5, 79),  # E
]

# Bar 3: B7 - comp on 2 and 4
piano_notes.extend([
    (bar3_start + 0.75, 76),  # B
    (bar3_start + 0.75, 79),  # D#
    (bar3_start + 0.75, 81),  # F#
    (bar3_start + 0.75, 84),  # A
    (bar3_start + 1.5, 76),  # B
    (bar3_start + 1.5, 79),  # D#
    (bar3_start + 1.5, 81),  # F#
    (bar3_start + 1.5, 84),  # A
])

# Bar 4: E7 - comp on 2 and 4
piano_notes.extend([
    (bar4_start + 0.75, 74),  # E
    (bar4_start + 0.75, 77),  # G#
    (bar4_start + 0.75, 79),  # B
    (bar4_start + 0.75, 82),  # D
    (bar4_start + 1.5, 74),  # E
    (bar4_start + 1.5, 77),  # G#
    (bar4_start + 1.5, 79),  # B
    (bar4_start + 1.5, 82),  # D
])

for t, pitch in piano_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=t, end=t + 0.375)
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F, G#, A#, B (F melodic minor)
# Start on beat 1 of bar 2, play F, G#, A#, B (each note for 0.375s)
sax_notes = [
    (bar2_start, 71),   # F
    (bar2_start + 0.375, 73),  # G#
    (bar2_start + 0.75, 75),  # A#
    (bar2_start + 1.125, 76),  # B
    (bar2_start + 1.5, 71),   # F (reprise)
    (bar2_start + 1.875, 73),  # G#
    (bar2_start + 2.25, 75),  # A#
    (bar2_start + 2.625, 76),  # B
]

for t, pitch in sax_notes:
    note = pretty_midi.Note(velocity=110, pitch=pitch, start=t, end=t + 0.375)
    sax.notes.append(note)

# Drums: Continue the pattern for bars 2-4
bar2_start = 1.5
bar3_start = 3.0
bar4_start = 4.5

# Bar 2
kick_times = [bar2_start + 0.375, bar2_start + 1.125]
snare_times = [bar2_start + 0.75, bar2_start + 1.5]
hihat_times = [bar2_start + 0.1875, bar2_start + 0.375, bar2_start + 0.5625, bar2_start + 0.75, bar2_start + 0.9375, bar2_start + 1.125, bar2_start + 1.3125, bar2_start + 1.5]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 3
kick_times = [bar3_start + 0.375, bar3_start + 1.125]
snare_times = [bar3_start + 0.75, bar3_start + 1.5]
hihat_times = [bar3_start + 0.1875, bar3_start + 0.375, bar3_start + 0.5625, bar3_start + 0.75, bar3_start + 0.9375, bar3_start + 1.125, bar3_start + 1.3125, bar3_start + 1.5]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 4
kick_times = [bar4_start + 0.375, bar4_start + 1.125]
snare_times = [bar4_start + 0.75, bar4_start + 1.5]
hihat_times = [bar4_start + 0.1875, bar4_start + 0.375, bar4_start + 0.5625, bar4_start + 0.75, bar4_start + 0.9375, bar4_start + 1.125, bar4_start + 1.3125, bar4_start + 1.5]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in snare_times:
    note = pretty_midi.Note(velocity=110, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)
for t in hihat_times:
    note = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.1)
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
