
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Parameters
sample_rate = 44100
duration_per_bar = 1.5  # seconds per bar
total_duration = 6.0  # 4 bars
num_samples = int(total_duration * sample_rate)

# Frequencies
D4 = 293.66  # D4 (concert D)
G4 = 392.0   # G4
B4 = 493.88  # B4
F5 = 698.46  # F5
A4 = 440.0   # A4 (tuning reference)
C5 = 523.25  # C5

# Rhythm Section (MIDI-like representation with amplitude levels)
def generate_rhythm_section(num_samples, bpm, bar_length, sample_rate):
    # Time per beat in seconds
    beat_length = 60.0 / bpm

    # Create an array of zeros for the rhythm section
    rhythm = np.zeros(num_samples)

    # Marcus - Walking bass line
    # Simple walking line in D minor: D - F - A - B (chromatic approach to B)
    # Every 4 beats
    bass_notes = [D4, F4, A4, B4]
    bass_pattern = [0.2, 0.3, 0.25, 0.2]
    for i in range(0, num_samples, int(beat_length * sample_rate)):
        for j in range(4):
            if i + j * int(beat_length * sample_rate) < num_samples:
                rhythm[i + j * int(beat_length * sample_rate)] = bass_pattern[j] * 0.5

    # Diane - Piano comping on 2 & 4 (7th chords, Dm7)
    # Dm7: D, F, A, C
    # Play on beat 2 and 4 of each bar
    piano_notes = [D4, F4, A4, C5]
    piano_pattern = [0.2, 0.3, 0.25, 0.2]
    for i in range(0, num_samples, int(beat_length * sample_rate)):
        for j in range(2, 5, 2):  # beat 2 and beat 4
            if i + j * int(beat_length * sample_rate) < num_samples:
                rhythm[i + j * int(beat_length * sample_rate)] = 0.4 * np.mean(piano_pattern)  # Harmonic comping

    # Little Ray - Drums
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    kick = [0.5, 0.0, 0.5, 0.0]  # Kick on 1 and 3
    snare = [0.0, 0.6, 0.0, 0.6]  # Snare on 2 and 4
    hihat = [0.15, 0.15, 0.15, 0.15]  # Hihat on every eighth

    for i in range(0, num_samples, int(beat_length * sample_rate)):
        for j in range(4):
            kick_sample = kick[j] * 0.3 if i + j * int(beat_length * sample_rate) < num_samples else 0
            snare_sample = snare[j] * 0.2 if i + j * int(beat_length * sample_rate) < num_samples else 0
            hihat_sample = hihat[j] * 0.1 if i + j * int(beat_length * sample_rate) < num_samples else 0
            rhythm[i + j * int(beat_length * sample_rate)] = kick_sample + snare_sample + hihat_sample

    return rhythm

# Saxophone Motif
def generate_saxophone(num_samples, sample_rate):
    sax = np.zeros(num_samples)
    t = np.linspace(0, total_duration, num_samples)

    # Start of the motif
    # D4 -> B4 -> G4 -> silence -> repeat
    # Tension, a question: is the answer the same or different?
    # Start at 0.5 seconds, play for 1.0 seconds
    start = int(0.5 * sample_rate)
    end = int(1.5 * sample_rate)

    # D4 for 0.3s
    sax[start:start + int(0.3 * sample_rate)] = 0.6 * np.sin(2 * np.pi * D4 * t[start:start + int(0.3 * sample_rate)])
    # B4 for 0.3s
    sax[start + int(0.3 * sample_rate):start + int(0.6 * sample_rate)] = 0.6 * np.sin(2 * np.pi * B4 * t[start + int(0.3 * sample_rate):start + int(0.6 * sample_rate)])
    # G4 for 0.3s
    sax[start + int(0.6 * sample_rate):start + int(0.9 * sample_rate)] = 0.6 * np.sin(2 * np.pi * G4 * t[start + int(0.6 * sample_rate):start + int(0.9 * sample_rate)])
    # Silence for 0.3s, then repeat
    sax[start + int(0.9 * sample_rate):start + int(1.2 * sample_rate)] = 0.0
    sax[start + int(1.2 * sample_rate):end] = sax[start:start + int(0.3 * sample_rate)]  # repeat the D4

    return sax

# Generate all tracks
rhythm_section = generate_rhythm_section(num_samples, 160, duration_per_bar, sample_rate)
saxophone = generate_saxophone(num_samples, sample_rate)

# Combine tracks
mix = rhythm_section + saxophone

# Normalize to avoid clipping
mix = mix / np.max(np.abs(mix))

# Play the audio
sd.play(mix, sample_rate)
time.sleep(total_duration)
sd.stop()

# Optional: Save the output as a WAV file
write("dante_intro.wav", sample_rate, mix.astype(np.float32))

print("Done. Wayne is leaning forward.")
