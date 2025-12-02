
import numpy as np
import sounddevice as sd
import time

# Parameters
sample_rate = 44100
duration = 6.0  # 6 seconds
total_samples = int(sample_rate * duration)
buffer = np.zeros(total_samples, dtype=np.float32)

# Tempo: 160 BPM, 4/4 time
# Bar = 1.5 seconds, beat = 0.375 seconds
# Time mapping: 0.0 - 1.5s = Bar 1, 1.5-3.0s = Bar 2, etc.

# Define the key: Fm (F, Ab, Bb, C, Eb, F, Gb)
# We'll use F minor as the key. Some references (no modulation)

# Frequencies for Fm scale (F, Gb, Ab, Bb, C, Db, Eb)
# Let's map the notes to frequencies (approximate 12-TET)
# Using A4 = 440Hz as reference
note_freq = {
    'F': 349.23,
    'Gb': 369.99,
    'Ab': 392.00,
    'Bb': 415.30,
    'C': 523.25,
    'Db': 554.37,
    'Eb': 587.33,
    'F': 349.23,  # Repeat for octave
    'Gb': 369.99,
    'Ab': 392.00
}

# GUI-like note names for readability
note_names = ['F', 'Gb', 'Ab', 'Bb', 'C', 'Db', 'Eb', 'F', 'Gb', 'Ab']

# Define the motif: simple, emotionally charged, with space and tension
# The motif will be your tenor sax line — we'll model it with simple sinusoids
# We'll use a few notes with dynamic variation and rests

# Bar 1: Little Ray on drums — just hihat on every eighth, fill the bar
# Let's simulate that with a hihat pattern (clicks)
hihat_freq = 1000.0
hihat_volume = 0.2
hihat_interval = 0.1875  # 0.375 sec per beat, 1/2 beat per hihat

# Bar 2–4: Full ensemble — melody, bass, piano, drums

# Melody (your tenor sax): start with a motif, leave it hanging
# Notes: F (beat 1), Eb (beat 2), Ab (beat 3), rest (beat 4)
# Then return later in the piece (but not here)
melody_notes = [
    note_freq['F'],  # beat 1
    note_freq['Eb'], # beat 2
    note_freq['Ab'], # beat 3
    0.0             # rest
]

# Bass line: Marcus — chromatic walking line, no repeats
bass_notes = [
    note_freq['F'],     # beat 1
    note_freq['Gb'],    # beat 2
    note_freq['Ab'],    # beat 3
    note_freq['Bb'],    # beat 4
    note_freq['C'],     # beat 1 (bar 2)
    note_freq['Db'],    # beat 2
    note_freq['Eb'],    # beat 3
    note_freq['F'],     # beat 4
    note_freq['Gb'],    # beat 1 (bar 3)
    note_freq['Ab'],    # beat 2
    note_freq['Bb'],    # beat 3
    note_freq['C'],     # beat 4
    note_freq['Db'],    # beat 1 (bar 4)
    note_freq['Eb'],    # beat 2
    note_freq['F'],     # beat 3
    note_freq['Gb']     # beat 4
]

# Piano: Diane — 7th chords, comp on 2 and 4
piano_notes = [
    note_freq['F'] + note_freq['Ab'],  # F7 (beat 2)
    note_freq['Bb'] + note_freq['Db'], # Bb7 (beat 4)
    note_freq['F'] + note_freq['Ab'],  # F7 (beat 2)
    note_freq['Bb'] + note_freq['Db'], # Bb7 (beat 4)
    note_freq['F'] + note_freq['Ab'],  # F7 (beat 2)
    note_freq['Bb'] + note_freq['Db'], # Bb7 (beat 4)
    note_freq['F'] + note_freq['Ab'],  # F7 (beat 2)
    note_freq['Bb'] + note_freq['Db'], # Bb7 (beat 4)
]

# Drums: Little Ray — kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_volume = 0.5
snare_volume = 0.4
hihat_volume = 0.3

# Create the buffers for each part

# Hihat (Bar 1)
hihat_time = 0.0
while hihat_time < 1.5:
    start = int(hihat_time * sample_rate)
    end = start + int(0.01 * sample_rate)  # short click
    buffer[start:end] += np.sin(2 * np.pi * hihat_freq * np.linspace(0, 1, end - start)) * hihat_volume
    hihat_time += hihat_interval

# Kick (Bars 2–4)
kick_times = [1.5, 2.25, 3.0, 3.75, 4.5, 5.25, 6.0]
for t in kick_times:
    start = int(t * sample_rate)
    end = start + int(0.01 * sample_rate)
    buffer[start:end] += np.sin(2 * np.pi * 100.0 * np.linspace(0, 1, end - start)) * kick_volume

# Snare (Bars 2–4)
snare_times = [1.875, 2.625, 3.375, 4.125, 4.875, 5.625]
for t in snare_times:
    start = int(t * sample_rate)
    end = start + int(0.01 * sample_rate)
    buffer[start:end] += np.sin(2 * np.pi * 200.0 * np.linspace(0, 1, end - start)) * snare_volume

# Melody (Bar 2)
melody_start = 1.5
note_durations = [0.375, 0.375, 0.375, 0.375]  # 1 beat each
for i, freq in enumerate(melody_notes):
    if freq == 0:
        continue
    start = int((melody_start + i * 0.375) * sample_rate)
    end = start + int(0.375 * sample_rate)
    envelope = np.linspace(0.2, 1.0, end - start)
    buffer[start:end] += np.sin(2 * np.pi * freq * np.linspace(0, 1, end - start)) * envelope * 0.7

# Bass (Bars 2–4)
bass_start = 1.5
for i, freq in enumerate(bass_notes):
    start = int((bass_start + i * 0.375) * sample_rate)
    end = start + int(0.01 * sample_rate)
    buffer[start:end] += np.sin(2 * np.pi * freq * np.linspace(0, 1, end - start)) * 0.2

# Piano (Bars 2–4)
piano_start = 1.5
for i, freq in enumerate(piano_notes):
    start = int((piano_start + i * 0.75) * sample_rate)
    end = start + int(0.1 * sample_rate)
    buffer[start:end] += np.sin(2 * np.pi * freq * np.linspace(0, 1, end - start)) * 0.3

# Normalize
buffer /= np.max(np.abs(buffer)) * 1.2

# Play it
sd.play(buffer, sample_rate)
time.sleep(6.0)
sd.stop()
