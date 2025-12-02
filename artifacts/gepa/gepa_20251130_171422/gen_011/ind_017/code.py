
import numpy as np
import soundfile as sf
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

# Constants
SAMPLE_RATE = 44100
DURATIONS = [1.5, 1.5, 1.5, 1.5]  # 4 bars, 1.5 seconds each (6 seconds total)
BPM = 160
BEAT_DURATION = 60 / BPM  # 0.375 seconds per beat
N_BARS = 4
N_BEATS_PER_BAR = 4
N_SAMPLES_PER_BEAT = int(SAMPLE_RATE * BEAT_DURATION)
N_SAMPLES_PER_BAR = N_SAMPLES_PER_BEAT * N_BEATS_PER_BAR
TOTAL_SAMPLES = int(SAMPLE_RATE * sum(DURATIONS))

# Define the key of D major
D_MAJOR_SCALE = [2, 2, 1, 2, 2, 2, 1]  # D, E, F#, G, A, B, C#, D
NOTES = {
    'D': 293.66,
    'E': 329.63,
    'F#': 369.99,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88,
    'C#': 329.63  # C# is same as D in this case, just a chromatic approach
}

# Generate sine waves
def generate_sine(freq, duration, sample_rate=SAMPLE_RATE):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    return wave

# Bar 1: Little Ray (Drums) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def bar1():
    audio = np.zeros(int(SAMPLE_RATE * 1.5))
    # Kick on 1 and 3
    for beat in [0, 2]:
        start = beat * N_SAMPLES_PER_BEAT
        kick = generate_sine(60, 0.1, SAMPLE_RATE)  # Low bass kick
        audio[start:start + len(kick)] += kick
    # Snare on 2 and 4
    for beat in [1, 3]:
        start = beat * N_SAMPLES_PER_BEAT
        snare = generate_sine(200, 0.1, SAMPLE_RATE)  # High-pitched snare
        audio[start:start + len(snare)] += snare
    # Hi-hat on every eighth
    for i in range(0, N_SAMPLES_PER_BAR, N_SAMPLES_PER_BEAT // 2):
        hihat = generate_sine(1000, 0.02, SAMPLE_RATE)  # High-pitched hihat
        audio[i:i + len(hihat)] += hihat
    return audio

# Bar 2: Everyone in - Diane (Piano) comps on 2 and 4
def bar2():
    audio = np.zeros(int(SAMPLE_RATE * 1.5))
    # Piano comping (7th chords on 2 and 4)
    # Bar 2: D7 (D, F#, A, C#)
    # D: 293.66, F#: 369.99, A: 440.00, C#: 329.63
    chord = [NOTES['D'], NOTES['F#'], NOTES['A'], NOTES['C#']]
    for note in chord:
        comp = generate_sine(note, 0.3, SAMPLE_RATE) * 0.1
        audio[600:600 + len(comp)] += comp  # 2nd beat
    return audio

# Bar 3: You (Tenor Sax) - Motif
def bar3():
    audio = np.zeros(int(SAMPLE_RATE * 1.5))
    # Motif: D -> A -> F# -> rest -> repeat
    motif = [NOTES['D'], NOTES['A'], NOTES['F#']]
    for i, note in enumerate(motif):
        duration = 0.4 if i < 2 else 0.2  # First two notes longer, third shorter
        start = i * int(SAMPLE_RATE * 0.4)
        sax = generate_sine(note, duration, SAMPLE_RATE) * 0.3
        audio[start:start + len(sax)] += sax
    return audio

# Bar 4: Marcus (Bass) - Walking line with chromatic approach
def bar4():
    audio = np.zeros(int(SAMPLE_RATE * 1.5))
    # Bass line: D -> C# -> D -> E (chromatic)
    for note in [NOTES['D'], NOTES['C#'], NOTES['D'], NOTES['E']]:
        bass = generate_sine(note, 0.3, SAMPLE_RATE) * 0.2
        audio[0:0 + len(bass)] += bass
    return audio

# Main composition
def compose_intro():
    audio = np.zeros(TOTAL_SAMPLES)
    audio[:len(bar1())] += bar1()
    audio[len(bar1()):len(bar1()) + len(bar2())] += bar2()
    audio[len(bar1()) + len(bar2()):len(bar1()) + len(bar2()) + len(bar3())] += bar3()
    audio[len(bar1()) + len(bar2()) + len(bar3()):] += bar4()
    return audio

# Normalize and save
intro = compose_intro()
intro = intro / np.max(np.abs(intro))  # Normalize to -1 to 1
write("jazz_intro.wav", SAMPLE_RATE, intro.astype(np.float32))

print("Intro saved to 'jazz_intro.wav'. Play it loud for Wayne.")
