
import numpy as np
import soundfile as sf
from scipy.io.wavfile import write
from matplotlib import pyplot as plt
import mido
from mido import MidiFile, MidiTrack, Message

# Parameters
BPM = 160
tempo = 60 / BPM  # seconds per beat
duration = 4 * tempo  # 4 bars
sample_rate = 44100
num_samples = int(duration * sample_rate)

# Generate a 4-bar intro in Dm (Dm7 -> G7 -> Cm7 -> F7)
# Key: Dm (D, F, A, C)
# Chord progression: Dm7 - G7 - Cm7 - F7 (ii - V - i - IV)

# Frequencies for the key of Dm (D, F, A, C)
D = 293.66
F = 349.23
A = 440.00
C = 261.63

# Time signature: 4/4, 160 BPM
# Each bar is 6 seconds (4 bars = 24 seconds)
# Each beat is 0.375 seconds
# Each eighth note is 0.1875 seconds
# Each sixteenth note is 0.09375 seconds

# Generate bass line (Marcus) - walking line in Dm7
# Bass notes: D, F, A, C, D, F, A, C, D, F, A, C, D, F, A, C
bass_notes = [D, F, A, C] * 4
bass_times = [i * tempo / 4 for i in range(16)]  # Each beat is 1/4 note
bass_durations = [tempo / 4] * 16

# Diane's piano chords - open voicings, one chord per bar
# Bar 1: Dm7 (D, F, A, C)
# Bar 2: G7 (G, B, D, F)
# Bar 3: Cm7 (C, Eb, G, Bb) — use C, E, G, B (approximate for simplicity)
# Bar 4: F7 (F, A, C, Eb) — use F, A, C, E (approximate)
chords = [
    [D, F, A, C],
    [392.00, 493.88, 293.66, 349.23],
    [261.63, 329.63, 392.00, 493.88],
    [349.23, 440.00, 261.63, 392.00]
]
chord_times = [i * tempo for i in range(4)]
chord_durations = [tempo] * 4

# Little Ray's drums - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Kick on beats 1 and 3 (every 2 beats)
# Snare on 2 and 4
# Hihat on every eighth note
kick_times = [i * tempo for i in range(0, 16, 2)]
snare_times = [i * tempo for i in range(1, 16, 2)]
hihat_times = [i * tempo / 2 for i in range(16)]

# You, the tenor sax - short motif: D -> F -> A -> D (quarter notes, 1 bar)
# Then on bar 2: F -> A -> C -> F
# Then on bar 3: A -> C -> D -> A
# Then on bar 4: C -> D -> F -> C
# Start with D, leave it hanging, come back with the full motif
sax_notes = [
    D, 0, 0, 0,  # Bar 1: D, rest
    F, A, C, F,  # Bar 2: F, A, C, F
    A, C, D, A,  # Bar 3: A, C, D, A
    C, D, F, C   # Bar 4: C, D, F, C
]
sax_times = [i * tempo / 4 for i in range(16)]
sax_durations = [tempo / 4] * 16

# Generate the audio
audio = np.zeros(num_samples)

# Generate bass line
for note, start, duration in zip(bass_notes, bass_times, bass_durations):
    samples = int(duration * sample_rate)
    freq = note
    t = np.linspace(0, duration, samples, False)
    wave = 0.3 * np.sin(2 * np.pi * freq * t)
    audio[int(start * sample_rate):int(start * sample_rate) + samples] += wave

# Generate piano chords
for chord in chords:
    start = chord_times[chords.index(chord)]
    for note in chord:
        samples = int(chord_durations[chords.index(chord)] * sample_rate)
        freq = note
        t = np.linspace(0, chord_durations[chords.index(chord)], samples, False)
        wave = 0.2 * np.sin(2 * np.pi * freq * t)
        audio[int(start * sample_rate):int(start * sample_rate) + samples] += wave

# Generate drums
for time in kick_times:
    samples = int(0.1 * sample_rate)
    wave = 0.4 * np.sin(2 * np.pi * 100 * np.linspace(0, 0.1, samples))
    audio[int(time * sample_rate):int(time * sample_rate) + samples] += wave

for time in snare_times:
    samples = int(0.1 * sample_rate)
    wave = 0.4 * np.sin(2 * np.pi * 200 * np.linspace(0, 0.1, samples))
    audio[int(time * sample_rate):int(time * sample_rate) + samples] += wave

for time in hihat_times:
    samples = int(0.05 * sample_rate)
    wave = 0.2 * np.sin(2 * np.pi * 1000 * np.linspace(0, 0.05, samples))
    audio[int(time * sample_rate):int(time * sample_rate) + samples] += wave

# Generate saxophone line
for note, start, duration in zip(sax_notes, sax_times, sax_durations):
    if note == 0:
        continue
    samples = int(duration * sample_rate)
    freq = note
    t = np.linspace(0, duration, samples, False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    audio[int(start * sample_rate):int(start * sample_rate) + samples] += wave

# Normalize audio
audio = audio / np.max(np.abs(audio))

# Save as WAV
write("dante_intro.wav", sample_rate, audio.astype(np.float32))

print("Generated 'dante_intro.wav' — a 4-bar jazz intro in Dm for Wayne.")
