
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = 1.5
bar1_beat = 0.375
drum_notes = [
    (kick, bar1_start + 0.0, bar1_beat),  # Kick on 1
    (snare, bar1_start + bar1_beat, bar1_beat),  # Snare on 2
    (hihat, bar1_start + 0.0, bar1_beat / 2),  # Hihat on 1
    (hihat, bar1_start + bar1_beat / 2, bar1_beat / 2),  # Hihat on &
    (kick, bar1_start + bar1_beat * 2, bar1_beat),  # Kick on 3
    (snare, bar1_start + bar1_beat * 3, bar1_beat),  # Snare on 4
    (hihat, bar1_start + bar1_beat * 2, bar1_beat / 2),  # Hihat on 3
    (hihat, bar1_start + bar1_beat * 2.5, bar1_beat / 2),  # Hihat on &
    (hihat, bar1_start + bar1_beat * 3, bar1_beat / 2),  # Hihat on 4
    (hihat, bar1_start + bar1_beat * 3.5, bar1_beat / 2),  # Hihat on &
]

for note, start, duration in drum_notes:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

# Bar 2: Full quartet (1.5 - 3.0s)
bar2_start = 1.5
bar2_end = 3.0

# Bass line: Fm7 -> Bb7 -> Eb7 -> Ab7
bass_notes = [
    (53, bar2_start + 0.0, 0.375),  # F
    (50, bar2_start + 0.375, 0.375),  # Ab
    (48, bar2_start + 0.75, 0.375),  # Bb
    (51, bar2_start + 1.125, 0.375),  # D
    (49, bar2_start + 1.5, 0.375),  # Eb
    (46, bar2_start + 1.875, 0.375),  # G
    (45, bar2_start + 2.25, 0.375),  # Ab
    (48, bar2_start + 2.625, 0.375),  # Bb
]

for note, start, duration in bass_notes:
    bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (50, bar2_start + 0.375, 0.375),  # Bb7 (root)
    (53, bar2_start + 0.375, 0.375),  # F7 (7th)
    (55, bar2_start + 0.375, 0.375),  # Ab7 (9th)
    (57, bar2_start + 0.375, 0.375),  # C7 (11th)
    (50, bar2_start + 1.875, 0.375),  # Eb7 (root)
    (53, bar2_start + 1.875, 0.375),  # F7 (7th)
    (55, bar2_start + 1.875, 0.375),  # Ab7 (9th)
    (57, bar2_start + 1.875, 0.375),  # C7 (11th)
]

for note, start, duration in piano_notes:
    piano_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Motif in Fm
# Fm: F, Ab, Bb, Db
# Motif: F -> Db -> Bb -> Ab
sax_notes = [
    (53, bar2_start, 0.375),  # F
    (48, bar2_start + 0.75, 0.375),  # Db
    (50, bar2_start + 1.125, 0.375),  # Bb
    (51, bar2_start + 1.5, 0.375),  # Ab
]

for note, start, duration in sax_notes:
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 3: Full quartet (3.0 - 4.5s)
bar3_start = 3.0
bar3_end = 4.5

# Bass line: Fm7 -> Bb7 -> Eb7 -> Ab7 (repeating the pattern)
for i, note in enumerate(bass_notes):
    start = bar3_start + (note[1] - bar2_start)
    duration = note[2]
    bass_note = pretty_midi.Note(velocity=100, pitch=note[0], start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
for i, note in enumerate(piano_notes):
    start = bar3_start + (note[1] - bar2_start)
    duration = note[2]
    piano_note = pretty_midi.Note(velocity=100, pitch=note[0], start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Motif repeated
for i, note in enumerate(sax_notes):
    start = bar3_start + (note[1] - bar2_start)
    duration = note[2]
    sax_note = pretty_midi.Note(velocity=100, pitch=note[0], start=start, end=start + duration)
    sax.notes.append(sax_note)

# Bar 4: Full quartet (4.5 - 6.0s)
bar4_start = 4.5
bar4_end = 6.0

# Bass line: Fm7 -> Bb7 -> Eb7 -> Ab7 (repeating the pattern)
for i, note in enumerate(bass_notes):
    start = bar4_start + (note[1] - bar2_start)
    duration = note[2]
    bass_note = pretty_midi.Note(velocity=100, pitch=note[0], start=start, end=start + duration)
    bass.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
for i, note in enumerate(piano_notes):
    start = bar4_start + (note[1] - bar2_start)
    duration = note[2]
    piano_note = pretty_midi.Note(velocity=100, pitch=note[0], start=start, end=start + duration)
    piano.notes.append(piano_note)

# Sax: Motif repeated
for i, note in enumerate(sax_notes):
    start = bar4_start + (note[1] - bar2_start)
    duration = note[2]
    sax_note = pretty_midi.Note(velocity=100, pitch=note[0], start=start, end=start + duration)
    sax.notes.append(sax_note)

# Drums: same pattern in bar 3 and 4
bar3_drums = [
    (kick, bar3_start + 0.0, bar1_beat),  # Kick on 1
    (snare, bar3_start + bar1_beat, bar1_beat),  # Snare on 2
    (hihat, bar3_start + 0.0, bar1_beat / 2),  # Hihat on 1
    (hihat, bar3_start + bar1_beat / 2, bar1_beat / 2),  # Hihat on &
    (kick, bar3_start + bar1_beat * 2, bar1_beat),  # Kick on 3
    (snare, bar3_start + bar1_beat * 3, bar1_beat),  # Snare on 4
    (hihat, bar3_start + bar1_beat * 2, bar1_beat / 2),  # Hihat on 3
    (hihat, bar3_start + bar1_beat * 2.5, bar1_beat / 2),  # Hihat on &
    (hihat, bar3_start + bar1_beat * 3, bar1_beat / 2),  # Hihat on 4
    (hihat, bar3_start + bar1_beat * 3.5, bar1_beat / 2),  # Hihat on &
]

for note, start, duration in bar3_drums:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

bar4_drums = [
    (kick, bar4_start + 0.0, bar1_beat),  # Kick on 1
    (snare, bar4_start + bar1_beat, bar1_beat),  # Snare on 2
    (hihat, bar4_start + 0.0, bar1_beat / 2),  # Hihat on 1
    (hihat, bar4_start + bar1_beat / 2, bar1_beat / 2),  # Hihat on &
    (kick, bar4_start + bar1_beat * 2, bar1_beat),  # Kick on 3
    (snare, bar4_start + bar1_beat * 3, bar1_beat),  # Snare on 4
    (hihat, bar4_start + bar1_beat * 2, bar1_beat / 2),  # Hihat on 3
    (hihat, bar4_start + bar1_beat * 2.5, bar1_beat / 2),  # Hihat on &
    (hihat, bar4_start + bar1_beat * 3, bar1_beat / 2),  # Hihat on 4
    (hihat, bar4_start + bar1_beat * 3.5, bar1_beat / 2),  # Hihat on &
]

for note, start, duration in bar4_drums:
    drum_note = pretty_midi.Note(velocity=100, pitch=note, start=start, end=start + duration)
    drums.notes.append(drum_note)

midi.instruments.extend([sax, bass, piano, drums])
