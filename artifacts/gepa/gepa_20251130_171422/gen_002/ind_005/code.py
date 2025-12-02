
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

# Parameters
sample_rate = 44100
duration = 6.0  # seconds
total_samples = int(sample_rate * duration)
tempo = 160  # BPM
beat_duration = 60.0 / tempo  # seconds per beat
bar_duration = beat_duration * 4  # seconds per bar

# Time array
t = np.linspace(0, duration, total_samples, endpoint=False)

# Frequency constants
F = 69.30  # F4 in Hz
Bb = 62.23  # Bb4 in Hz
C = 65.41  # C5 in Hz
Eb = 73.42  # Eb5 in Hz
G = 82.41  # G4 in Hz
A = 88.00  # A4 in Hz
D = 73.42  # D5 in Hz (same as Eb for now, chromatic)

# Duration constants in seconds
beat = beat_duration
half_beat = beat / 2
quarter_beat = beat / 4
eighth_beat = beat / 8

# Generate sine wave
def sine_wave(freq, duration, sample_rate):
    return np.sin(2 * np.pi * freq * t[:int(duration * sample_rate)])

# Generate noise for drum hits
def noise(duration, sample_rate):
    return np.random.normal(0, 0.1, int(duration * sample_rate))

# Drums (Little Ray)
drums = np.zeros(total_samples)
drums[round(0 * sample_rate)] = noise(0.05, sample_rate)  # Kick on beat 1
drums[round(1.5 * sample_rate)] = noise(0.05, sample_rate)  # Snare on beat 2
drums[round(3 * sample_rate)] = noise(0.05, sample_rate)   # Kick on beat 3
drums[round(4.5 * sample_rate)] = noise(0.05, sample_rate)  # Snare on beat 4
drums[round(2.25 * sample_rate)] = noise(0.025, sample_rate) # Hihat on & 2
drums[round(3.75 * sample_rate)] = noise(0.025, sample_rate) # Hihat on & 4

# Bass (Marcus) - walking line in F minor
bass_frequencies = [
    F,     # F4 - beat 1
    Bb,    # Bb4 - & 1
    C,     # C5 - beat 2
    Eb,    # Eb5 - & 2
    G,     # G4 - beat 3
    A,     # A4 - & 3
    D,     # D5 - beat 4
    Bb     # Bb4 - & 4
]
bass = np.zeros(total_samples)
bass_positions = [i * sample_rate * beat for i in np.linspace(0, 1, len(bass_frequencies))]
for i, pos in enumerate(bass_positions):
    start = int(pos)
    end = int(pos + 0.05 * sample_rate)
    if end > total_samples:
        end = total_samples
    bass[start:end] += sine_wave(bass_frequencies[i], 0.05, sample_rate)

# Piano (Diane) - chords on 2 and 4, 7th chords
# F7 (F A C Eb)
# Bb7 (Bb D F Ab)
piano = np.zeros(total_samples)
chord_duration = 0.4  # seconds
chord1_start = int(1.5 * sample_rate)
chord1_end = int(1.5 * sample_rate + chord_duration)
chord2_start = int(3.5 * sample_rate)
chord2_end = int(3.5 * sample_rate + chord_duration)

# F7 chord (F, A, C, Eb)
chord1 = np.zeros(int(chord_duration * sample_rate))
chord1 += sine_wave(F, chord_duration, sample_rate)
chord1 += sine_wave(A, chord_duration, sample_rate)
chord1 += sine_wave(C, chord_duration, sample_rate)
chord1 += sine_wave(Eb, chord_duration, sample_rate)

# Bb7 chord (Bb, D, F, Ab)
chord2 = np.zeros(int(chord_duration * sample_rate))
chord2 += sine_wave(Bb, chord_duration, sample_rate)
chord2 += sine_wave(D, chord_duration, sample_rate)
chord2 += sine_wave(F, chord_duration, sample_rate)
chord2 += sine_wave(A, chord_duration, sample_rate)  # Ab = G#; using A as a substitute for effect

piano[chord1_start:chord1_end] += chord1
piano[chord2_start:chord2_end] += chord2

# Saxophone (Dante Russo) - 4-note motif, open-ended
sax = np.zeros(total_samples)
sax_notes = [F, Bb, C, Eb]  # Simple, questioning motif in F minor
note_durations = [0.4, 0.3, 0.2, 0.1]  # decreasing for tension

for i in range(4):
    start = int(i * 0.4 * sample_rate)
    duration = note_durations[i]
    end = start + int(duration * sample_rate)
    if end > total_samples:
        end = total_samples
    sax[start:end] += sine_wave(sax_notes[i], duration, sample_rate)

# Combine all tracks
mix = (drums + bass + piano + sax) / 4  # Normalize
mix = np.clip(mix, -1, 1)

# Play the sound
sd.play(mix, sample_rate)
sd.wait()

# Save the sound as a WAV file
write("jazz_intro.wav", sample_rate, mix.astype(np.float32))
