
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# 160 BPM, 4/4 time => each beat is 0.375 seconds
# Total duration: 6 seconds (4 bars)

# Sampling rate
SR = 44100

# Time per bar (6 seconds)
BAR_DURATION = 6.0
NUM_BARS = 4
BEAT_DURATION = 0.375  # 160 BPM
BAR_SAMPLES = int(BAR_DURATION * SR)

# Function to generate a sine wave
def sinewave(freq, duration, amp=0.5, phase=0):
    t = np.linspace(0, duration, int(duration * SR), False)
    wave = amp * np.sin(2 * np.pi * freq * t + phase)
    return wave

# Function to generate a percussive kick
def kick(freq, duration, decay=0.1, amp=0.6):
    t = np.linspace(0, duration, int(duration * SR), False)
    envelope = np.exp(-t / decay)
    wave = amp * np.sin(2 * np.pi * freq * t) * envelope
    return wave

# Function to generate a snare-like sound
def snare(duration, amp=0.3):
    t = np.linspace(0, duration, int(duration * SR), False)
    # Combination of white noise and a sine wave
    noise = np.random.normal(0, 0.1, len(t))
    sine = amp * np.sin(2 * np.pi * 2000 * t)
    return (noise + sine) * 0.5

# Function to generate hihat
def hihat(duration, density=0.8):
    t = np.linspace(0, duration, int(duration * SR), False)
    # High frequency noise
    noise = np.random.normal(0, 0.05, len(t))
    # Amplitude envelope
    envelope = np.linspace(0, 1, len(t))
    # Random spikes
    spikes = np.zeros(len(t))
    spike_positions = np.random.choice(len(t), int(len(t) * density), replace=False)
    spikes[spike_positions] = 1
    return noise * envelope * spikes

# Function to generate bass line (walking line with chromatic approaches)
def generate_bass_line():
    # Dm7 chord: D, F, A, C
    # Walking bass with chromatic approaches
    notes = [
        'C', 'D', 'Eb', 'F', 'F#', 'G', 'A', 'Bb', 'B', 'C'
    ]
    note_freqs = {
        'C': 146.83,
        'C#': 155.56,
        'D': 164.81,
        'Eb': 174.61,
        'E': 185.00,
        'F': 196.00,
        'F#': 207.65,
        'G': 220.00,
        'Ab': 233.08,
        'A': 246.94,
        'Bb': 261.63,
        'B': 277.18
    }

    # Bass line with chromatic approaches
    bass_notes = ['C', 'F', 'Bb', 'F', 'C', 'F', 'Bb', 'F', 'C', 'F', 'Bb', 'F', 'C']
    bass_line = [note_freqs[note] for note in bass_notes]
    bass_line_durations = [BEAT_DURATION] * len(bass_line)

    # Generate bass track
    bass = np.zeros(int(BAR_DURATION * SR))
    for i, (freq, dur) in enumerate(zip(bass_line, bass_line_durations)):
        start = int(i * BEAT_DURATION * SR)
        end = start + int(dur * SR)
        segment = sinewave(freq, dur, amp=0.3)
        bass[start:end] += segment
    return bass

# Function to generate piano comping (7th chords, comp on 2 and 4)
def generate_piano_comp():
    # Dm7 chord: D, F, A, C
    # 7th chords: Dm7, G7, Cm7, F7
    # Comp on beats 2 and 4
    chords = {
        'Dm7': [293.66, 349.23, 440.00, 523.25],  # D, F, A, C
        'G7': [392.00, 493.88, 587.33, 698.46],   # G, B, D, F#
        'Cm7': [261.63, 311.13, 392.00, 523.25],  # C, Eb, G, Bb
        'F7': [349.23, 415.30, 493.88, 659.25],   # F, A, C, E
    }

    chord_times = [1.25, 1.75, 2.25, 2.75]  # Beats 2 and 4 in each bar
    chord_indices = [0, 1, 0, 1]  # Dm7 on beat 2, G7 on beat 4, etc.

    # Generate piano comp
    piano = np.zeros(int(BAR_DURATION * SR))
    for t, idx in zip(chord_times, chord_indices):
        start = int(t * SR)
        chord = chords['Dm7'] if idx == 0 else chords['G7']
        chord_waves = [sinewave(freq, 0.05, amp=0.1) for freq in chord]
        chord_signal = sum(chord_waves)
        piano[start:start + int(0.05 * SR)] += chord_signal
    return piano

# Function to generate drum track (kick, snare, hihat)
def generate_drums():
    # Kicks on 1 and 3
    kick_times = [0.0, 1.5, 3.0, 4.5]
    # Snares on 2 and 4
    snare_times = [1.0, 2.5, 4.0, 5.5]
    # Hihat on every eighth
    hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625,
                   3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]

    # Generate kick
    kicks = np.zeros(int(BAR_DURATION * SR))
    for t in kick_times:
        if t < BAR_DURATION:
            kicks[int(t * SR):int(t * SR)+int(0.05 * SR)] += kick(60, 0.05)

    # Generate snare
    snares = np.zeros(int(BAR_DURATION * SR))
    for t in snare_times:
        if t < BAR_DURATION:
            snares[int(t * SR):int(t * SR)+int(0.05 * SR)] += snare(0.05)

    # Generate hihat
    hihats = np.zeros(int(BAR_DURATION * SR))
    for t in hihat_times:
        if t < BAR_DURATION:
            hihats[int(t * SR):int(t * SR)+int(0.025 * SR)] += hihat(0.025)

    # Combine all
    drums = kicks + snares + hihats
    return drums

# Function to generate tenor sax melody (short motif with space and tension)
def generate_tenor_melody():
    # Dm7 chord: D, F, A, C
    # Melody: D, Eb, F, C (a fragment that lingers)
    notes = ['D', 'Eb', 'F', 'C']
    note_freqs = {
        'D': 164.81,
        'Eb': 174.61,
        'F': 196.00,
        'C': 146.83
    }

    # Melody durations (with rests)
    melody_durations = [0.25, 0.25, 0.25, 0.25, 0.5]  # 4 notes + rest
    melody_freqs = [note_freqs[note] for note in notes] + [0.0]  # rest

    tenor = np.zeros(int(BAR_DURATION * SR))
    for i, (freq, dur) in enumerate(zip(melody_freqs, melody_durations)):
        start = int(i * 0.25 * SR)
        if i == 4:
            continue  # skip rest
        segment = sinewave(freq, dur, amp=0.5, phase=0.25 * np.pi)
        tenor[start:start + int(dur * SR)] += segment
    return tenor

# Generate all tracks
bass = generate_bass_line()
piano = generate_piano_comp()
drums = generate_drums()
tenor = generate_tenor_melody()

# Combine all tracks
mix = bass + piano + drums + tenor

# Normalize
mix = mix / np.max(np.abs(mix))

# Write to file
write("dante_russo_intro.wav", SR, (mix * 32767).astype(np.int16))

# Play the sound
sd.play(mix, SR)
sd.wait()

print("4-bar intro written to 'dante_russo_intro.wav'")
print("The music begins with a question — a motive that lingers just out of reach.")
print("The drums set the tension, the bass walks with purpose, the piano compes with fire, and the tenor saxophone searches for an answer.")
print("Wayne Shorter is listening — and he hears something he hasn't heard before.")
