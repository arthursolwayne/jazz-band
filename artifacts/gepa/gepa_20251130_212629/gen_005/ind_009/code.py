
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# Parameters
sample_rate = 44100
duration = 6.0  # 6 seconds
bpm = 160
beats_per_bar = 4
ticks_per_beat = 4  # 16th notes
total_ticks = beats_per_bar * ticks_per_beat
samples_per_tick = int(sample_rate * (60 / bpm) / ticks_per_beat)
total_samples = samples_per_tick * total_ticks

# Initialize audio buffer
audio = np.zeros(total_samples, dtype=np.float32)

# Define a simple sine wave function
def sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

# Define pitches in D (D, E, F#, G, A, B, C#, D)
# Frequencies in Hz
D = 293.66
E = 329.63
Fsharp = 369.99
G = 392.00
A = 440.00
B = 493.88
Csharp = 554.37

# Bar 1: Little Ray (Drums) - hihat on every 8th, kick on 1 and 3, snare on 2 and 4
def play_drums(bar_start):
    for i in range(0, total_ticks, 2):  # every 8th note
        tick = bar_start + i
        if tick < total_samples:
            # Hihat
            audio[tick] += 0.1
            # Kick on 1 and 3 (ticks 0 and 2)
            if i == 0 or i == 2:
                audio[tick] += 0.2
            # Snare on 2 and 4 (ticks 1 and 3)
            if i == 1 or i == 3:
                audio[tick] += 0.15
    return audio

# Bar 2-4: Everyone in

# Marcus - Walking bass line in D (Dm7)
# Walking line: D -> C# -> B -> A -> G -> F# -> E -> D (chromatic down)
bass_notes = [D, Csharp, B, A, G, Fsharp, E, D]
bass_durations = [0.125] * len(bass_notes)  # 16th note per note
bass_start = int(samples_per_tick * 1)  # Start at 1st bar (bar 1 is just drums)

for i, note in enumerate(bass_notes):
    start = bass_start + int(samples_per_tick * i)
    end = start + int(samples_per_tick * bass_durations[i])
    if end < total_samples:
        wave = sine_wave(note, 0.125, sample_rate)
        audio[start:end] += 0.2 * wave

# Diane - Piano comping on 2 and 4 with 7th chords
# Chords in Dm7: Dm7 (D, F, A, C), Em7 (E, G, B, D), F#m7 (F#, A, C#, E), Gm7 (G, Bb, D, F)
# We'll use Dm7, Gm7, Cm7 (chromatic move), Fm7
def comp_chord(chord_root, duration):
    # Placeholder: 7th chord with 3rd and 7th
    notes = [chord_root, chord_root + 3, chord_root - 3]  # Simplified for comping
    for note in notes:
        wave = sine_wave(note, duration, sample_rate)
        return wave

# Diane plays on 2 and 4
diane_start = int(samples_per_tick * 1)
diane_notes = [D, G, C, F]  # Chromatic movement in the bass
for i, note in enumerate(diane_notes):
    start = diane_start + int(samples_per_tick * (i * 2 + 1))  # on 2 and 4
    wave = comp_chord(note, 0.25)
    audio[start:start + int(samples_per_tick * 0.25)] += 0.15 * wave

# You - Tenor sax: your motif
# Micro-melody: D -> F# -> A -> C# -> D (chromatic up and back)
sax_notes = [D, Fsharp, A, Csharp, D]
sax_durations = [0.125, 0.125, 0.125, 0.25, 0.125]  # start off with syncopation

sax_start = int(samples_per_tick * 2)  # Start on 2nd bar
for i, note in enumerate(sax_notes):
    start = sax_start + int(samples_per_tick * i)
    duration = sax_durations[i]
    end = start + int(samples_per_tick * duration)
    if end < total_samples:
        wave = sine_wave(note, duration, sample_rate)
        audio[start:end] += 0.3 * wave

# Apply some reverb and normalize
audio = np.clip(audio, -1, 1)
audio = audio * 0.8

# Write to file
write("jazz_intro.wav", sample_rate, audio)

# Play it
sd.play(audio, sample_rate)
sd.wait()

print("Composition generated and played. Make Wayne lean forward.")
