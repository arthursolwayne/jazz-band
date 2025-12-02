
import pretty_midi

# Create the MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

bar1_start = 0.0
bar1_end = 1.5
kick_time = bar1_start + 0.375  # 1
snare_time = bar1_start + 0.75   # 2
hihat_time = bar1_start + 0.1875  # 1&

for i in range(2):
    kick_time = bar1_start + (i * 0.75) + 0.375
    snare_time = bar1_start + (i * 0.75) + 0.75
    hihat_time = bar1_start + (i * 0.75) + 0.1875
    for time in [kick_time, snare_time]:
        note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    for time in range(int(hihat_time), int(hihat_time + 1.5), 1):
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

bar2_start = 1.5
bar2_end = 3.0

# Bass: Walking line, chromatic approaches, no repeats
bass_notes = [
    (bar2_start + 0.0, 84),  # F
    (bar2_start + 0.375, 83),  # E
    (bar2_start + 0.75, 86),  # G
    (bar2_start + 1.125, 85),  # F#
    (bar2_start + 1.5, 84),   # F
    (bar2_start + 1.875, 83),  # E
    (bar2_start + 2.25, 86),  # G
    (bar2_start + 2.625, 85)  # F#
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (bar2_start + 0.75, 84),  # F7 (F, A, C, E)
    (bar2_start + 1.5, 84),
    (bar2_start + 2.25, 84)
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Main motif (F, G#, Bb, C)
# Start at bar2_start (1.5s), play the first two notes (F and G#)

sax_notes = [
    (bar2_start, 84),  # F
    (bar2_start + 0.375, 87),  # G#
    (bar2_start + 1.5, 82),  # Bb
    (bar2_start + 1.875, 87)  # C
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

bar3_start = 3.0
bar3_end = 4.5

# Bass: Walking line
bass_notes = [
    (bar3_start + 0.0, 84),  # F
    (bar3_start + 0.375, 83),  # E
    (bar3_start + 0.75, 86),  # G
    (bar3_start + 1.125, 85),  # F#
    (bar3_start + 1.5, 84),   # F
    (bar3_start + 1.875, 83),  # E
    (bar3_start + 2.25, 86),  # G
    (bar3_start + 2.625, 85)  # F#
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (bar3_start + 0.75, 84),  # F7 again
    (bar3_start + 1.5, 84),
    (bar3_start + 2.25, 84)
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Repeat the motif, but end on C to give it that "hanging" feeling

sax_notes = [
    (bar3_start, 84),  # F
    (bar3_start + 0.375, 87),  # G#
    (bar3_start + 0.75, 82),  # Bb
    (bar3_start + 1.125, 87)  # C
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

bar4_start = 4.5
bar4_end = 6.0

# Bass: Walking line
bass_notes = [
    (bar4_start + 0.0, 84),  # F
    (bar4_start + 0.375, 83),  # E
    (bar4_start + 0.75, 86),  # G
    (bar4_start + 1.125, 85),  # F#
    (bar4_start + 1.5, 84),   # F
    (bar4_start + 1.875, 83),  # E
    (bar4_start + 2.25, 86),  # G
    (bar4_start + 2.625, 85)  # F#
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (bar4_start + 0.75, 84),  # F7
    (bar4_start + 1.5, 84),
    (bar4_start + 2.25, 84)
]

for start, pitch in piano_notes:
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=start, end=start + 0.25)
    piano.notes.append(note)

# Sax: Return to the motif, but this time resolve it
# End on F (root), open it up, leave it hanging

sax_notes = [
    (bar4_start, 84),  # F
    (bar4_start + 0.375, 87),  # G#
    (bar4_start + 0.75, 84),  # F (resolve)
    (bar4_start + 1.125, 84)  # F (linger)
]

for start, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# Drums: Continue kick on 1 and 3, snare on 2 and 4, hihat on every eighth

for i in range(2):
    kick_time = bar4_start + (i * 0.75) + 0.375
    snare_time = bar4_start + (i * 0.75) + 0.75
    hihat_time = bar4_start + (i * 0.75) + 0.1875
    for time in [kick_time, snare_time]:
        note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    for time in range(int(hihat_time), int(hihat_time + 1.5), 1):
        note = pretty_midi.Note(velocity=70, pitch=42, start=time, end=time + 0.1)
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dantes_intro.mid")
