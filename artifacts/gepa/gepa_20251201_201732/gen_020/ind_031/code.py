
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

# Parameters
sample_rate = 44100
duration = 6.0  # 6 seconds for 4 bars
total_samples = int(sample_rate * duration)

# Key: F minor (F, Gb, Ab, Bb, C, Db, Eb)
# We'll use F minor as the key center
# Set tempo to 160 BPM, 4/4 time
# Bar 1: Little Ray (drums) only
# Bars 2-4: Full ensemble

# 1. Define the timing grid
bars = 4
beats_per_bar = 4
bpm = 160
beat_duration = 60.0 / bpm  # seconds per beat
bar_duration = beat_duration * beats_per_bar  # 6.0 seconds for 4 bars

# 2. Define the time points for each beat
time_ticks = np.arange(0, total_samples) / sample_rate
time_beats = np.arange(0, duration, beat_duration)

# 3. Define drum pattern (Little Ray) — Bar 1 only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: 0-1.5 seconds
def generate_drum_pattern(start, duration, sample_rate):
    samples = np.zeros(int(duration * sample_rate))
    # Kick
    kick_times = [0.0, 0.75]  # beat 1 and 3
    for t in kick_times:
        samples[int((start + t) * sample_rate)] = 1.0
    # Snare
    snare_times = [0.5, 1.25]  # beat 2 and 4
    for t in snare_times:
        samples[int((start + t) * sample_rate)] = 0.8
    # Hihat
    hihat_times = [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1.0, 1.125, 1.25, 1.375, 1.5]
    for t in hihat_times:
        samples[int((start + t) * sample_rate)] = 0.3
    return samples

# 4. Define Marcus's walking bass line (Fm7 - Bb7 - Eb7 - Ab7)
# In F minor, roots: F, Bb, Eb, Ab
# Walking line: roots and fifths with chromatic approaches
# Duration: 6 seconds, 160 BPM == 64 beats per 6 seconds (16 beats per bar)
def generate_bass_line():
    bass = np.zeros(total_samples)
    # Fm7 - bar 2
    root = 69  # F4
    fifth = 76  # C5
    chromatic = 70  # F#4
    duration_per_beat = 1.5  # seconds per beat
    for i in range(4):  # 4 bars
        for j in range(4):  # 4 beats per bar
            beat_start = i * 4 * duration_per_beat + j * duration_per_beat
            if i == 0:
                # Bar 1: no bass
                pass
            else:
                if j % 2 == 0:
                    # Root and chromatic (resolve)
                    bass[int(beat_start * sample_rate)] = 0.3
                    bass[int((beat_start + 0.15) * sample_rate)] = 0.3
                else:
                    # Fifth
                    bass[int(beat_start * sample_rate)] = 0.3
                    bass[int((beat_start + 0.15) * sample_rate)] = 0.3
    return bass

# 5. Diane's piano: Open voicings, one chord per bar, resolve on last
# Chords: Fm7 (bar 2), Bb7 (bar 3), Eb7 (bar 4), Ab7 (bar 4)
# Open voicings: root, 7th, 9th, 13th
def generate_piano_line():
    piano = np.zeros(total_samples)
    # Bar 2: Fm7 (F, Ab, C, Eb)
    # Bar 3: Bb7 (Bb, D, F, Ab)
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    # Bar 4: Ab7 (Ab, C, Eb, Gb)
    # Each chord on downbeat, 1.5s per bar
    for i in range(4):
        bar_start = i * 1.5
        if i == 0:
            # No piano in bar 1
            continue
        # Chord durations: 0.2s
        chord_start = bar_start
        if i == 1:
            # Fm7
            # F4 (69), Ab4 (71), C5 (72), Eb5 (74)
            piano[int(chord_start * sample_rate)] = 0.5
            piano[int((chord_start + 0.1) * sample_rate)] = 0.5
            piano[int((chord_start + 0.2) * sample_rate)] = 0.5
        elif i == 2:
            # Bb7
            # Bb4 (71), D5 (74), F5 (77), Ab5 (78)
            piano[int(chord_start * sample_rate)] = 0.5
            piano[int((chord_start + 0.1) * sample_rate)] = 0.5
            piano[int((chord_start + 0.2) * sample_rate)] = 0.5
        elif i == 3:
            # Eb7
            # Eb5 (74), G5 (76), Bb5 (77), Db6 (78)
            piano[int(chord_start * sample_rate)] = 0.5
            piano[int((chord_start + 0.1) * sample_rate)] = 0.5
            piano[int((chord_start + 0.2) * sample_rate)] = 0.5
            # Final resolve on Ab7 (Ab5, C6, Eb6, Gb6)
            # Ab5 (78), C6 (81), Eb6 (83), Gb6 (84)
            piano[int((chord_start + 0.3) * sample_rate)] = 0.5
            piano[int((chord_start + 0.4) * sample_rate)] = 0.5
            piano[int((chord_start + 0.5) * sample_rate)] = 0.5
    return piano

# 6. Your saxophone: a short, haunting motif
# Let's go for a motif from the Fm scale, with chromatic tension
# Start on Gb (F#) over Fm, then resolve to Eb (diminished) and end on F
def generate_sax_line():
    sax = np.zeros(total_samples)
    # Bar 2: Start motif
    bar_start = 1.5  # bar 2 starts at 1.5s
    # Motif: F, Gb, Eb, F
    # Frequencies: F4 (349.23), Gb4 (369.99), Eb4 (311.13), F4
    # Use a sawtooth wave for a gritty, emotional sound
    for i in range(4):
        bar_start = i * 1.5
        if i == 0:
            # No sax in bar 1
            continue
        # Duration of note: 0.6s
        if i == 1:
            # Start motif: F -> Gb
            # F (349.23 Hz)
            note_freq = 349.23
            note_duration = 0.3
            note_start = bar_start
            t = np.arange(0, note_duration, 1/sample_rate)
            wave = (np.sin(2 * np.pi * note_freq * t) + 0.5) * 0.3
            sax[int(note_start * sample_rate):int((note_start + note_duration) * sample_rate)] += wave
            # Gb (369.99 Hz)
            note_freq = 369.99
            note_duration = 0.3
            note_start = bar_start + 0.3
            t = np.arange(0, note_duration, 1/sample_rate)
            wave = (np.sin(2 * np.pi * note_freq * t) + 0.5) * 0.3
            sax[int(note_start * sample_rate):int((note_start + note_duration) * sample_rate)] += wave
        elif i == 2:
            # Eb (311.13 Hz)
            note_freq = 311.13
            note_duration = 0.3
            note_start = bar_start
            t = np.arange(0, note_duration, 1/sample_rate)
            wave = (np.sin(2 * np.pi * note_freq * t) + 0.5) * 0.3
            sax[int(note_start * sample_rate):int((note_start + note_duration) * sample_rate)] += wave
        elif i == 3:
            # F (349.23 Hz)
            note_freq = 349.23
            note_duration = 0.4
            note_start = bar_start
            t = np.arange(0, note_duration, 1/sample_rate)
            wave = (np.sin(2 * np.pi * note_freq * t) + 0.5) * 0.5
            sax[int(note_start * sample_rate):int((note_start + note_duration) * sample_rate)] += wave
    return sax

# 7. Combine all parts
drum = generate_drum_pattern(0.0, 1.5, sample_rate)
bass = generate_bass_line()
piano = generate_piano_line()
sax = generate_sax_line()

# Sum all parts
audio = drum + bass + piano + sax
audio = np.clip(audio, -1.0, 1.0)

# Normalize
audio = audio / np.max(np.abs(audio))

# Play and save
sd.play(audio, sample_rate)
sd.wait()

write("jazz_intro.wav", sample_rate, audio.astype(np.float32))

# Optional: Plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(time_ticks[:10000], audio[:10000])
plt.title("Jazz Intro in Fm")
plt.xlabel("Time (samples)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
