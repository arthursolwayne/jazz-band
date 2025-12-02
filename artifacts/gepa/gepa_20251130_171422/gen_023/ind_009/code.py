
import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # 6 seconds for 4 bars at 160 BPM
FRAME_COUNT = int(SAMPLE_RATE * DURATION)

# Function to generate a sine wave
def sine_wave(freq, duration, sample_rate, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave

# Function to generate a note with dynamics
def generate_note(freq, duration, sample_rate, amplitude, attack=0.05, release=0.05):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    envelope = np.zeros_like(t)
    attack_idx = int(attack * sample_rate)
    release_idx = int((duration - release) * sample_rate)
    envelope[:attack_idx] = np.linspace(0, 1, attack_idx)
    envelope[attack_idx:release_idx] = 1.0
    envelope[release_idx:] = np.linspace(1, 0, int(release * sample_rate))
    wave = sine_wave(freq, duration, sample_rate, amplitude)
    return wave * envelope

# Bar 1: Drums only
def bar1():
    # Kick on 1 and 3
    kick1 = generate_note(65.41, 0.1, SAMPLE_RATE, 0.6)
    kick3 = generate_note(65.41, 0.1, SAMPLE_RATE, 0.6)
    # Snare on 2 and 4
    snare2 = generate_note(185.00, 0.1, SAMPLE_RATE, 0.7)
    snare4 = generate_note(185.00, 0.1, SAMPLE_RATE, 0.7)
    # Hi-hat on every eighth
    hihat = np.zeros(FRAME_COUNT)
    for i in range(0, FRAME_COUNT, int(SAMPLE_RATE * 0.125)):
        hihat[i:i+int(SAMPLE_RATE * 0.05)] = 0.2 * np.random.rand(int(SAMPLE_RATE * 0.05))
    # Combine
    bar = np.zeros(FRAME_COUNT)
    bar[:len(kick1)] += kick1
    bar[int(SAMPLE_RATE * 0.25):int(SAMPLE_RATE * 0.25)+len(kick1)] += kick3
    bar[int(SAMPLE_RATE * 0.5):int(SAMPLE_RATE * 0.5)+len(snare2)] += snare2
    bar[int(SAMPLE_RATE * 0.75):int(SAMPLE_RATE * 0.75)+len(snare4)] += snare4
    bar += hihat
    return bar

# Bar 2: All instruments
def bar2():
    # Bass line: D, F#, A, B, D (chromatic approach)
    bass_notes = [73.42, 82.41, 92.50, 97.99, 73.42]
    bass = np.zeros(FRAME_COUNT)
    for i, note in enumerate(bass_notes):
        start = int(SAMPLE_RATE * (i * 0.25))
        duration = 0.25
        bass[start:start+int(SAMPLE_RATE * duration)] += generate_note(note, duration, SAMPLE_RATE, 0.4)
    # Piano: 7th chords on 2 and 4
    # D7 = D, F#, A, C#
    # Bm7 = B, D, F#, A
    piano_notes = [73.42, 82.41, 92.50, 116.54]  # D7
    piano = np.zeros(FRAME_COUNT)
    for note in piano_notes:
        piano[int(SAMPLE_RATE * 0.5):int(SAMPLE_RATE * 0.5) + int(SAMPLE_RATE * 0.25)] += generate_note(note, 0.25, SAMPLE_RATE, 0.3)
    # Drums
    drums = bar1()
    # Sax: Motif - D, F#, A, Bb, D
    sax_notes = [73.42, 82.41, 92.50, 98.83, 73.42]
    sax = np.zeros(FRAME_COUNT)
    for i, note in enumerate(sax_notes):
        start = int(SAMPLE_RATE * (i * 0.2))
        duration = 0.2
        sax[start:start+int(SAMPLE_RATE * duration)] += generate_note(note, duration, SAMPLE_RATE, 0.8)
    # Combine
    bar = bass + piano + drums + sax
    return bar

# Bar 3: All instruments
def bar3():
    # Bass line: D, C#, B, A, D
    bass_notes = [73.42, 69.30, 65.41, 58.27, 73.42]
    bass = np.zeros(FRAME_COUNT)
    for i, note in enumerate(bass_notes):
        start = int(SAMPLE_RATE * (i * 0.25))
        duration = 0.25
        bass[start:start+int(SAMPLE_RATE * duration)] += generate_note(note, duration, SAMPLE_RATE, 0.4)
    # Piano: Bm7 on 2 and 4
    piano_notes = [116.54, 73.42, 82.41, 92.50]
    piano = np.zeros(FRAME_COUNT)
    for note in piano_notes:
        piano[int(SAMPLE_RATE * 0.5):int(SAMPLE_RATE * 0.5) + int(SAMPLE_RATE * 0.25)] += generate_note(note, 0.25, SAMPLE_RATE, 0.3)
    # Drums
    drums = bar1()
    # Sax: Motif variation - D, Bb, A, F#, D
    sax_notes = [73.42, 98.83, 92.50, 82.41, 73.42]
    sax = np.zeros(FRAME_COUNT)
    for i, note in enumerate(sax_notes):
        start = int(SAMPLE_RATE * (i * 0.2))
        duration = 0.2
        sax[start:start+int(SAMPLE_RATE * duration)] += generate_note(note, duration, SAMPLE_RATE, 0.8)
    # Combine
    bar = bass + piano + drums + sax
    return bar

# Bar 4: All instruments
def bar4():
    # Bass line: D, A, B, D
    bass_notes = [73.42, 58.27, 65.41, 73.42]
    bass = np.zeros(FRAME_COUNT)
    for i, note in enumerate(bass_notes):
        start = int(SAMPLE_RATE * (i * 0.25))
        duration = 0.25
        bass[start:start+int(SAMPLE_RATE * duration)] += generate_note(note, duration, SAMPLE_RATE, 0.4)
    # Piano: D7 on 2 and 4
    piano_notes = [73.42, 82.41, 92.50, 116.54]
    piano = np.zeros(FRAME_COUNT)
    for note in piano_notes:
        piano[int(SAMPLE_RATE * 0.5):int(SAMPLE_RATE * 0.5) + int(SAMPLE_RATE * 0.25)] += generate_note(note, 0.25, SAMPLE_RATE, 0.3)
    # Drums
    drums = bar1()
    # Sax: Motif resolution - D, A, Bb, D
    sax_notes = [73.42, 92.50, 98.83, 73.42]
    sax = np.zeros(FRAME_COUNT)
    for i, note in enumerate(sax_notes):
        start = int(SAMPLE_RATE * (i * 0.25))
        duration = 0.25
        sax[start:start+int(SAMPLE_RATE * duration)] += generate_note(note, duration, SAMPLE_RATE, 0.9)
    # Combine
    bar = bass + piano + drums + sax
    return bar

# Combine all bars
audio = np.zeros(FRAME_COUNT)
audio[:FRAME_COUNT] += bar1()
audio[:FRAME_COUNT] += bar2()
audio[:FRAME_COUNT] += bar3()
audio[:FRAME_COUNT] += bar4()

# Normalize the audio
audio = audio / np.max(np.abs(audio))

# Play the audio
sd.play(audio, SAMPLE_RATE)
sd.wait()

# Save the audio to a file
write("jazz_intro.wav", SAMPLE_RATE, audio.astype(np.float32))
