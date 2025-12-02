
import pretty_midi
import numpy as np

# Create a MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
track_drums = pretty_midi.Instrument(program=10)  # Acoustic Drums
track_bass = pretty_midi.Instrument(program=33)   # Double Bass
track_piano = pretty_midi.Instrument(program=0)   # Acoustic Piano
track_sax = pretty_midi.Instrument(program=64)    # Alto Saxophone

pm.instruments = [track_drums, track_bass, track_piano, track_sax]

# Define note values and durations
QUARTER_NOTE = 1.0
EIGHTH_NOTE = 0.5
SIXTEENTH_NOTE = 0.25
BAR_DURATION = 6.0  # seconds for 4 bars at 160 BPM
BEAT_DURATION = BAR_DURATION / 4  # 1.5 seconds per beat

# Drums: Bar 1 only, varied rhythm
# Kick on 1, snare on 3, hihat on all eighths
# With rests and subtle velocity variation

# Bar 1: Drums
for i in range(0, 4):  # 4 beats
    time = i * BEAT_DURATION

    # Kicks on beat 1
    if i == 0:
        track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + SIXTEENTH_NOTE))

    # Snares on beat 3
    if i == 2:
        track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + SIXTEENTH_NOTE))

    # Hihat on all eighths with slight velocity variation
    track_drums.notes.append(pretty_midi.Note(velocity=np.random.randint(60, 90), pitch=42, start=time, end=time + EIGHTH_NOTE))

# Bass: Walking line in Fm with chromatic approaches
# Fm: F, Ab, C, Eb
# Use chromatic passing tones, no repeated notes

bass_notes = [
    # Bar 2: F (root), Ab (flatted 3rd), C (perfect 5th), Eb (flatted 7th)
    # Bar 3: chromatic passing between Ab and C
    # Bar 4: chromatic passing between C and F
    # Bar 5: Eb
    # Bar 6: F (root)
    [65, 67, 69, 64],  # F, Ab, C, Eb
    [66, 68, 69, 65],  # chromatic between Ab and C
    [69, 70, 71, 66],  # chromatic between C and F
    [64, 65, 66, 67],  # chromatic leading to F
    [64, 65, 66, 67],  # chromatic leading to F
    [65, 67, 69, 64],  # F, Ab, C, Eb
]

# Assign each note to a time
for bar in range(2, 6):  # 4 bars starting at bar 2
    for note_idx, note in enumerate(bass_notes[bar - 2]):
        time = bar * BEAT_DURATION + note_idx * EIGHTH_NOTE
        track_bass.notes.append(pretty_midi.Note(velocity=75, pitch=note, start=time, end=time + EIGHTH_NOTE))

# Piano: 7th chords on beat 2 and 4
# Fm7: F, Ab, C, Eb
# Bb7: Bb, D, F, Ab
# C7: C, E, G, Bb
# D7: D, F, A, C
# Fm7, Bb7, C7, D7 — descending 7th chords

piano_chords = [
    # Bar 2: Fm7 on beat 2
    [65, 67, 69, 64],  # F, Ab, C, Eb
    # Bar 3: Bb7 on beat 2
    [71, 74, 65, 67],  # Bb, D, F, Ab
    # Bar 4: C7 on beat 2
    [69, 72, 76, 71],  # C, E, G, Bb
    # Bar 5: D7 on beat 2
    [62, 65, 71, 69],  # D, F, A, C
]

# Assign each chord to beat 2 and 4 of each bar
for bar in range(2, 6):  # 4 bars starting at bar 2
    for beat in [1, 3]:  # beats 2 and 4
        chord = piano_chords[bar - 2]
        time = bar * BEAT_DURATION + beat * BEAT_DURATION
        for pitch in chord:
            track_piano.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + EIGHTH_NOTE))

# Saxophone: Your motif — one phrase, 4 notes, at the start of bar 2

# Motif: F (65), Ab (67), C (69), Eb (64)
# Play on beats 2 and 4 of bar 2
# Play first two notes on beat 2, then rest on beat 3, then finish on beat 4

sax_notes = [
    (65, 0.0),     # F on beat 2
    (67, 0.5),     # Ab on beat 2.5
    (69, 0.0),     # C on beat 3 (rest)
    (64, 0.5)      # Eb on beat 3.5
]

# Bar 2 starts at time 1.5s, so 2nd bar is at time 1.5s
bar_start = 1.5
for idx, (pitch, offset) in enumerate(sax_notes):
    time = bar_start + offset
    track_sax.notes.append(pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + EIGHTH_NOTE))

# Export the MIDI
pm.write("jazz_intro_in_fm.mid")
print("MIDI file 'jazz_intro_in_fm.mid' has been created.")
