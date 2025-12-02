
import numpy as np
import simpleaudio as sa
import sounddevice as sd
from scipy.io.wavfile import write

# Sample rate and duration
SAMPLE_RATE = 44100
BAR_DURATION = 1.5  # 6 seconds for 4 bars
DURATION = BAR_DURATION * 4
NUM_SAMPLES = int(SAMPLE_RATE * DURATION)

# Create a blank audio array
audio = np.zeros(NUM_SAMPLES, dtype=np.float32)

# Define a simple sine wave function
def sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

# Dm7 chord tones (D, F, A, C)
# Frequencies in Hz (approximate equal temperament)
D4 = 293.66
F4 = 349.23
A4 = 440.00
C5 = 523.25

# Define 4 bars with the structure:
# Bar 1: Little Ray (drums) on 1 and 3 (kick), 2 and 4 (snare), hihat on every eighth
# Bar 2-4: Full ensemble, tenor sax melody with rests and dynamics

# Bar 1: Drums
# Kick on beats 1 and 3
# Snare on beats 2 and 4
# Hihat on every eighth note

# Kick sound (low bass)
kick_freq = 60  # Hz
kick_amp = 0.3
kick_start = 0

# Snare sound (higher, with a bit of distortion)
snare_freq = 150  # Hz
snare_amp = 0.4
snare_start = 0

# Hihat sound (high, short)
hihat_freq = 1200  # Hz
hihat_amp = 0.2
hihat_start = 0

# Bar 1 - Duration: 1.5 seconds
bar1_start = 0
bar1_end = 1.5

# Kick on beat 1 and 3 (0.0s and 0.75s)
kick_times = [0.0, 0.75]
for t in kick_times:
    start_idx = int(t * SAMPLE_RATE)
    wave = sine_wave(kick_freq, 0.05, SAMPLE_RATE) * kick_amp
    audio[start_idx:start_idx + len(wave)] += wave

# Snare on beat 2 and 4 (0.375s and 1.125s)
snare_times = [0.375, 1.125]
for t in snare_times:
    start_idx = int(t * SAMPLE_RATE)
    wave = sine_wave(snare_freq, 0.05, SAMPLE_RATE) * snare_amp
    audio[start_idx:start_idx + len(wave)] += wave

# Hihat on every eighth note (0.0, 0.375, 0.75, 1.125, 1.5)
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5]
for t in hihat_times:
    start_idx = int(t * SAMPLE_RATE)
    wave = sine_wave(hihat_freq, 0.02, SAMPLE_RATE) * hihat_amp
    audio[start_idx:start_idx + len(wave)] += wave

# Bar 2-4: Full Ensemble - Tenor Sax Melody in Dm
# Dm7: D, F, A, C
# Simple motif: D - F - A - rest (D -> F -> A -> silence)
# Start at bar 2 (1.5s)
start_bar2 = 1.5
note_duration = 0.25  # quarter note at 160 BPM

# Tenor sax melody (D, F, A, rest)
# Frequencies: D4, F4, A4, rest
note_frequencies = [D4, F4, A4, 0]  # 0 = rest
note_amp = 0.5

# Melody starts at bar 2, beat 1
note_times = [start_bar2 + 0.0, start_bar2 + 0.375, start_bar2 + 0.75, start_bar2 + 1.125]

# Generate the melody
for t, freq in zip(note_times, note_frequencies):
    start_idx = int(t * SAMPLE_RATE)
    if freq != 0:
        wave = sine_wave(freq, note_duration, SAMPLE_RATE) * note_amp
        audio[start_idx:start_idx + len(wave)] += wave

# Bass line: Marcus - walking line on Dm7
# Chromatic approach to D (C#), then D, F, A
# Dm7 bass line: C#, D, F, A (chromatic approach, then D, F, A)
bass_freqs = [C5 + 10, D4, F4, A4]  # C#4 approx 277.18 + 10 = 287.18, D4 = 293.66
bass_amp = 0.4
bass_duration = 0.25  # quarter note

# Bass starts at bar 2, beat 1
bass_times = [start_bar2 + 0.0, start_bar2 + 0.375, start_bar2 + 0.75, start_bar2 + 1.125]

for t, freq in zip(bass_times, bass_freqs):
    start_idx = int(t * SAMPLE_RATE)
    if freq != 0:
        wave = sine_wave(freq, bass_duration, SAMPLE_RATE) * bass_amp
        audio[start_idx:start_idx + len(wave)] += wave

# Piano: Diane - 7th chords on 2 and 4
# Dm7 = D, F, A, C
# Play on beat 2 and beat 4 of each bar (bar 2 and bar 3)

# Bar 2, beat 2: 0.375s from start_bar2 = 1.5 + 0.375 = 1.875s
# Bar 2, beat 4: 1.125s from start_bar2 = 1.5 + 1.125 = 2.625s
# Bar 3, beat 2: 1.5 + 1.5 + 0.375 = 3.375s
# Bar 3, beat 4: 1.5 + 1.5 + 1.125 = 4.125s

piano_times = [1.875, 2.625, 3.375, 4.125]
piano_amp = 0.1

for t in piano_times:
    start_idx = int(t * SAMPLE_RATE)
    # Play Dm7 chord as a chord sound (sum of four sine waves)
    chord = sine_wave(D4, 0.25, SAMPLE_RATE) * 0.25
    chord += sine_wave(F4, 0.25, SAMPLE_RATE) * 0.25
    chord += sine_wave(A4, 0.25, SAMPLE_RATE) * 0.25
    chord += sine_wave(C5, 0.25, SAMPLE_RATE) * 0.25
    audio[start_idx:start_idx + len(chord)] += chord * piano_amp

# Normalize to prevent clipping
audio = np.clip(audio / np.max(np.abs(audio)), -1, 1)

# Play the sound
sd.play(audio, SAMPLE_RATE)
sd.wait()

# Save the audio as a WAV file
write("jazz_intro.wav", SAMPLE_RATE, audio)
