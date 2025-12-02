
import pretty_midi

# Create the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# Time in seconds per bar (160 BPM, 4/4 time)
bar_length = 1.5  # 60 / 160 * 4 = 1.5s per bar

# Bar 1: Little Ray (Drums) alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_start = 0.0
bar1_end = bar_length

# Hihat every eighth note
for i in range(0, 8):
    time = bar1_start + (i * bar_length / 8)
    note = pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=time, end=time + 0.05)
    drums.notes.append(note)

# Kick on 1 and 3 (beat 0 and 2)
for beat in [0, 2]:
    time = bar1_start + (beat * bar_length / 4)
    note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4 (beat 1 and 3)
for beat in [1, 3]:
    time = bar1_start + (beat * bar_length / 4)
    note = pretty_midi.Note(velocity=110, pitch=drum_notes['snare'], start=time, end=time + 0.1)
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in Fm (F, Ab, D, Eb, etc.)
# Roots and fifths with chromatic approaches
# Key: Fm (F, Ab, Bb, Db)
# Walking line: F (D), Ab (G), Bb (A), Db (C), F (D), Ab (G), Bb (A), Db (C)
bass_notes = [
    (0.0, 53, 90),  # F (D chromatic approach)
    (0.375, 67, 90),  # Ab (G chromatic approach)
    (0.75, 55, 90),  # Bb (A chromatic approach)
    (1.125, 50, 90),  # Db (C chromatic approach)
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=bar1_end + time, end=bar1_end + time + 0.25)
    bass.notes.append(note)

# Diane: Open voicings, different chords each bar, resolve on last
# Bar 2: Fm7
# Fm7: F, Ab, Bb, D
note_times = [0.0, 0.25, 0.5, 0.75]
for i, pitch in enumerate([53, 67, 55, 60]):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bar1_end + note_times[i], end=bar1_end + note_times[i] + 0.5)
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar2_start = bar1_end
bar2_end = bar1_end + bar_length

# Hihat
for i in range(0, 8):
    time = bar2_start + (i * bar_length / 8)
    note = pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=time, end=time + 0.05)
    drums.notes.append(note)

# Kick and snare
for beat in [0, 2]:
    time = bar2_start + (beat * bar_length / 4)
    note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
    drums.notes.append(note)

for beat in [1, 3]:
    time = bar2_start + (beat * bar_length / 4)
    note = pretty_midi.Note(velocity=110, pitch=drum_notes['snare'], start=time, end=time + 0.1)
    drums.notes.append(note)

# Dante: Sax motif — short, singable, leave it hanging
# Fm: F, Ab, Bb, Db
# Motif: F -> Ab -> Bb -> (Db) — end on Bb, leave it hanging

# Note durations: 0.25, 0.25, 0.25, 0.25
sax_notes = [
    (0.0, 53, 95),
    (0.25, 67, 95),
    (0.5, 55, 95),
    (0.75, 55, 95),  # Bb again, leave it hanging
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=bar1_end + time, end=bar1_end + time + 0.25)
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Fm7 -> Gm7 -> Am7 -> Bm7
# Walking bass: F, G, A, B (F, G, A, B) chromatic approaches
bass_notes = [
    (0.0, 53, 90),  # F
    (0.375, 60, 90),  # G
    (0.75, 65, 90),  # A
    (1.125, 67, 90),  # B
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=bar2_end + time, end=bar2_end + time + 0.25)
    bass.notes.append(note)

# Diane: Gm7
# Gm7: G, Bb, D, F
note_times = [0.0, 0.25, 0.5, 0.75]
for i, pitch in enumerate([60, 55, 67, 53]):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bar2_end + note_times[i], end=bar2_end + note_times[i] + 0.5)
    piano.notes.append(note)

# Little Ray: Same pattern as before
bar3_start = bar2_end
bar3_end = bar2_end + bar_length

# Hihat
for i in range(0, 8):
    time = bar3_start + (i * bar_length / 8)
    note = pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=time, end=time + 0.05)
    drums.notes.append(note)

# Kick and snare
for beat in [0, 2]:
    time = bar3_start + (beat * bar_length / 4)
    note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
    drums.notes.append(note)

for beat in [1, 3]:
    time = bar3_start + (beat * bar_length / 4)
    note = pretty_midi.Note(velocity=110, pitch=drum_notes['snare'], start=time, end=time + 0.1)
    drums.notes.append(note)

# Dante: Repeat motif, but with a slight variation
sax_notes = [
    (0.0, 53, 95),
    (0.25, 67, 95),
    (0.5, 55, 95),
    (0.75, 58, 95),  # Db chromatic approach to F
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=bar2_end + time, end=bar2_end + time + 0.25)
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Am7 -> Bm7 -> Cm7 -> Dm7
# Walking bass: A, B, C, D
bass_notes = [
    (0.0, 65, 90),  # A
    (0.375, 67, 90),  # B
    (0.75, 69, 90),  # C
    (1.125, 71, 90),  # D
]
for time, pitch, velocity in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=bar3_end + time, end=bar3_end + time + 0.25)
    bass.notes.append(note)

# Diane: Am7
# Am7: A, C, E, G
note_times = [0.0, 0.25, 0.5, 0.75]
for i, pitch in enumerate([65, 60, 67, 59]):
    note = pretty_midi.Note(velocity=90, pitch=pitch, start=bar3_end + note_times[i], end=bar3_end + note_times[i] + 0.5)
    piano.notes.append(note)

# Little Ray: Same pattern
bar4_start = bar3_end
bar4_end = bar3_end + bar_length

# Hihat
for i in range(0, 8):
    time = bar4_start + (i * bar_length / 8)
    note = pretty_midi.Note(velocity=90, pitch=drum_notes['hihat'], start=time, end=time + 0.05)
    drums.notes.append(note)

# Kick and snare
for beat in [0, 2]:
    time = bar4_start + (beat * bar_length / 4)
    note = pretty_midi.Note(velocity=100, pitch=drum_notes['kick'], start=time, end=time + 0.1)
    drums.notes.append(note)

for beat in [1, 3]:
    time = bar4_start + (beat * bar_length / 4)
    note = pretty_midi.Note(velocity=110, pitch=drum_notes['snare'], start=time, end=time + 0.1)
    drums.notes.append(note)

# Dante: Resolution of the motif — F, Ab, Bb, F
sax_notes = [
    (0.0, 53, 95),
    (0.25, 67, 95),
    (0.5, 55, 95),
    (0.75, 53, 95),  # F again — resolution
]
for time, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=bar3_end + time, end=bar3_end + time + 0.25)
    sax.notes.append(note)

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_jazz_intro.mid")
