
import numpy as np
import sounddevice as sd
import time
from scipy.io.wavfile import write

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # 4 bars at 160 BPM, 4/4 time
NUM_SAMPLES = int(SAMPLE_RATE * DURATION)
FREQ_RESOLUTION = SAMPLE_RATE / NUM_SAMPLES

# Key: D minor (D, F, G, A, Bb, C, D)
# Root = D (D2 = 73.416 Hz)
# We'll use a D minor key signature for a haunting, urgent feel.

# Define time points in seconds
bar_length = DURATION / 4
beat_length = bar_length / 4  # 1 beat = 1.5 / 4 = 0.375 seconds

def generate_sine_wave(freq, duration, sample_rate=SAMPLE_RATE):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    return wave

def generate_click(attack=0.01, decay=0.05, sample_rate=SAMPLE_RATE):
    t = np.linspace(0, attack + decay, int(sample_rate * (attack + decay)), False)
    envelope = np.concatenate([
        np.linspace(0, 1, int(sample_rate * attack)),
        np.linspace(1, 0, int(sample_rate * decay))
    ])
    click = envelope * 0.5 * np.sin(2 * np.pi * 2000 * t)
    return click

def generate_drum_pattern(bar_length, sample_rate=SAMPLE_RATE):
    pattern = np.zeros(int(sample_rate * bar_length))
    
    # Kick on 1 and 3
    kick1 = generate_click()
    kick2 = generate_click()
    pattern[0 : len(kick1)] += kick1
    pattern[int(2 * beat_length * sample_rate) : int(2 * beat_length * sample_rate) + len(kick2)] += kick2
    
    # Snare on 2 and 4
    snare1 = generate_click(attack=0.005, decay=0.02)
    snare2 = generate_click(attack=0.005, decay=0.02)
    pattern[int(1 * beat_length * sample_rate) : int(1 * beat_length * sample_rate) + len(snare1)] += snare1
    pattern[int(3 * beat_length * sample_rate) : int(3 * beat_length * sample_rate) + len(snare2)] += snare2
    
    # Hihat on every eighth note
    hihat = generate_click(attack=0.001, decay=0.002, sample_rate=sample_rate)
    for i in range(0, int(bar_length * sample_rate), int(beat_length * sample_rate / 2)):
        pattern[i : i + len(hihat)] += hihat
    
    # Normalize
    pattern = np.clip(pattern / np.max(np.abs(pattern)), -1, 1)
    return pattern

def generate_bass_line(bar_length, sample_rate=SAMPLE_RATE):
    # Walking line: D2, F2, G2, A2, Bb2, C2, D2, D2
    notes = [73.416, 87.307, 98.000, 110.000, 116.541, 130.813, 73.416, 73.416]
    # Add chromatic approaches on roots
    chromatic_approach = [73.416, 78.000, 87.307, 98.000, 110.000, 116.541, 123.471, 130.813]
    
    pattern = np.zeros(int(sample_rate * bar_length))
    for i, freq in enumerate(chromatic_approach):
        start = int(i * beat_length * sample_rate)
        end = start + int(beat_length * sample_rate)
        if end > len(pattern):
            break
        pattern[start:end] += generate_sine_wave(freq, beat_length, sample_rate)
    
    # Normalize
    pattern = np.clip(pattern / np.max(np.abs(pattern)), -1, 1)
    return pattern

def generate_piano_chords(bar_length, sample_rate=SAMPLE_RATE):
    # Open voicings: Dm7, G7, Cm7, F7
    # Each chord for one bar
    chords = [
        [73.416, 98.000, 130.813, 146.832],  # Dm7: D, F, A, C
        [98.000, 130.813, 155.563, 196.000],  # G7: G, B, D, F
        [73.416, 98.000, 130.813, 146.832],  # Cm7: C, Eb, G, Bb
        [73.416, 98.000, 130.813, 174.614]   # F7: F, A, C, E
    ]
    
    pattern = np.zeros(int(sample_rate * bar_length))
    
    for i, chord in enumerate(chords):
        start = int(i * beat_length * sample_rate)
        end = start + int(beat_length * sample_rate)
        if end > len(pattern):
            break
        for freq in chord:
            wave = generate_sine_wave(freq, beat_length, sample_rate)
            pattern[start:end] += wave
    
    # Normalize
    pattern = np.clip(pattern / np.max(np.abs(pattern)), -1, 1)
    return pattern

def generate_sax_melody(bar_length, sample_rate=SAMPLE_RATE):
    # Melody: D, F, G, A, D (sings the motif, leaves it hanging)
    notes = [73.416, 87.307, 98.000, 110.000, 73.416]
    durations = [0.25, 0.25, 0.25, 0.25, 0.25]  # Each note is a quarter note

    pattern = np.zeros(int(sample_rate * bar_length))
    for i, (freq, duration) in enumerate(zip(notes, durations)):
        start = int(i * beat_length * sample_rate)
        end = start + int(duration * sample_rate)
        if end > len(pattern):
            break
        wave = generate_sine_wave(freq, duration, sample_rate)
        pattern[start:end] += wave
    
    # Normalize
    pattern = np.clip(pattern / np.max(np.abs(pattern)), -1, 1)
    return pattern

# Generate each part
drum_pattern = generate_drum_pattern(bar_length)
bass_line = generate_bass_line(bar_length)
piano_chords = generate_piano_chords(bar_length)
sax_melody = generate_sax_melody(bar_length)

# Combine all parts
final_wave = np.zeros(NUM_SAMPLES)
for i in range(4):
    start = int(i * bar_length * sample_rate)
    end = start + int(bar_length * sample_rate)
    final_wave[start:end] += drum_pattern
    final_wave[start:end] += bass_line
    final_wave[start:end] += piano_chords
    final_wave[start:end] += sax_melody

# Normalize the entire wave
final_wave = np.clip(final_wave / np.max(np.abs(final_wave)), -1, 1)

# Export as WAV
write("jazz_intro_4bars.wav", SAMPLE_RATE, final_wave.astype(np.float32))

# Play it
sd.play(final_wave, SAMPLE_RATE)
time.sleep(DURATION)
sd.stop()

print("Generated 4-bar jazz intro. Saved as 'jazz_intro_4bars.wav'.")
