
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
track_drums = pretty_midi.Instrument(program=10)  # Drums
track_bass = pretty_midi.Instrument(program=33)   # Double Bass
track_piano = pretty_midi.Instrument(program=0)   # Acoustic Piano
track_sax = pretty_midi.Instrument(program=64)    # Tenor Saxophone

# Time per bar in seconds (160 BPM = 60/160 = 0.375 s per beat, 1.5 s per bar)
time_per_bar = 1.5
time_per_beat = 0.375

# MIDI notes for Fm7 (F, Ab, C, Eb)
Fm7_notes = [65, 68, 72, 69]  # F, Ab, C, Eb

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Little Ray alone
# Kick on beat 1 and 3, hihat on all eighths

# MIDI note numbers for drum kit
kick = 36
snare = 38
hihat = 42

# Bar 1: Drums only
for bar in range(1):
    for beat in [0, 2]:  # Kick on 1 and 3
        time = bar * time_per_bar + beat * time_per_beat
        track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1))
    for beat in [1, 3]:  # Snare on 2 and 4
        time = bar * time_per_bar + beat * time_per_beat
        track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1))
    for eighth in range(8):  # Hihat on every eighth
        time = bar * time_per_bar + eighth * 0.1875
        track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time, end=time + 0.05))

# Bars 2-4: Full ensemble

# Bar 2: Diane on piano (comp on 2 and 4)
for bar in range(1, 4):
    time = bar * time_per_bar
    # 7th chord on beat 2 and 4
    for beat in [1, 3]:
        start_time = time + beat * time_per_beat
        for note in Fm7_notes:
            track_piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start_time, end=start_time + 0.1))

# Marcus on bass: Walking line, chromatic approaches
# Fm7 bass line: F, Eb, D, C, Bb, A, G, F
bass_line = [65, 69, 68, 72, 71, 67, 67, 65]  # F, Eb, D, C, Bb, A, G, F
for bar in range(1, 4):
    time = bar * time_per_bar
    for i in range(8):
        note = bass_line[i % len(bass_line)]
        start = time + i * 0.1875
        end = start + 0.1
        track_bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Little Ray on drums: Full pattern (kick on 1 and 3, snare on 2 and 4, hihat on all eighths)
for bar in range(1, 4):
    time = bar * time_per_bar
    for beat in [0, 2]:  # Kick
        track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=time + beat * time_per_beat, end=time + beat * time_per_beat + 0.1))
    for beat in [1, 3]:  # Snare
        track_drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=time + beat * time_per_beat, end=time + beat * time_per_beat + 0.1))
    for eighth in range(8):
        track_drums.notes.append(pretty_midi.Note(velocity=80, pitch=hihat, start=time + eighth * 0.1875, end=time + eighth * 0.1875 + 0.05))

# You on sax: Short motif, whisper to shout
# Motif: F, Bb, Eb, F (start on beat 2, resolve on beat 4)
sax_notes = [65, 67, 69, 65]  # F, Bb, Eb, F
sax_velocities = [60, 80, 100, 110]  # Quiet to loud

for i in range(len(sax_notes)):
    start_time = 1 * time_per_bar + i * time_per_beat  # Start on beat 2 of bar 2
    track_sax.notes.append(pretty_midi.Note(velocity=sax_velocities[i], pitch=sax_notes[i], start=start_time, end=start_time + 0.25))

# Add instruments to the MIDI file
pm.instruments = [track_drums, track_bass, track_piano, track_sax]

# Save the MIDI file
pm.write("jazz_intro_4_bar_Fm.mid")
