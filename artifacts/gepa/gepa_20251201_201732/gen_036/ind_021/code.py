
import numpy as np
import sounddevice as sd
import time
from scipy.io.wavfile import write

# Set parameters
sample_rate = 44100
duration = 6.0  # seconds
num_samples = int(duration * sample_rate)
buffer = np.zeros(num_samples, dtype=np.float32)

# Tempo and time
bpm = 160
bar_length = 6.0 / 4  # 6 seconds for 4 bars
beat_length = bar_length / 4  # 1.5 seconds per beat
sample_per_beat = int(beat_length * sample_rate)

# TONE GENERATOR FUNCTION
def tone(freq, duration, sample_rate, amplitude=0.3):
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    return amplitude * np.sin(2 * np.pi * freq * t)

# --- BASS (Marcus) ---
# Walking line in Fm: F, Ab, Bb, D, etc. with chromatic approaches
# Convert to frequencies using A4 = 440 Hz

note_freqs = {
    'F2': 87.31,
    'F#2': 92.50,
    'G2': 98.00,
    'Ab2': 103.83,  # chromatic approach
    'A2': 110.00,
    'Bb2': 116.54,
    'B2': 123.47,
    'C3': 130.81,
    'Db3': 138.59,  # chromatic approach
    'D3': 146.83
}

bass_notes = [
    note_freqs['F2'],  # Root
    note_freqs['Ab2'],  # Chromatic approach
    note_freqs['Bb2'],  # 5th
    note_freqs['D2'],  # 7th
]

for i in range(4):
    start = i * sample_per_beat
    end = start + sample_per_beat
    # Walking rhythm: on beats 1, 2, 3, 4, but spaced
    for j in range(4):
        if j in [0, 2]:  # Beat 1 and 3
            freq = bass_notes[j % 4]
            note = tone(freq, beat_length, sample_rate)
            buffer[start + j * int(sample_per_beat / 2):end + j * int(sample_per_beat / 2)] += note

# --- PIANO (Diane) ---
# Open voicings with tension, different chord each bar
# Fm7, G7#9, Bbmaj7, Cm7

def chord_voicing(freqs, duration):
    # Simple additive synthesis
    return np.sum([tone(freq, duration, sample_rate, 0.1) for freq in freqs], axis=0)

# Chord voicings per bar (Fm7, G7#9, Bbmaj7, Cm7)
chord1 = [note_freqs['F2'], note_freqs['Ab2'], note_freqs['C3'], note_freqs['Eb3']]  # Fm7
chord2 = [note_freqs['G2'], note_freqs['Bb2'], note_freqs['D3'], note_freqs['F#3']]  # G7#9
chord3 = [note_freqs['Bb2'], note_freqs['D3'], note_freqs['F3'], note_freqs['A3']]  # Bbmaj7
chord4 = [note_freqs['C2'], note_freqs['Eb2'], note_freqs['G3'], note_freqs['Bb3']]  # Cm7

# Diane plays on beats 2 and 4
for i in range(4):
    start = i * sample_per_beat
    end = start + sample_per_beat
    if i % 2 == 1:  # Beat 2 and 4
        chord = [chord1, chord2, chord3, chord4][i]
        note = chord_voicing(chord, beat_length)
        buffer[start + int(beat_length * sample_rate / 2):end + int(beat_length * sample_rate / 2)] += note

# --- DRUMS (Little Ray) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
kick_freq = 60.0  # Hz
snare_freq = 200.0
hihat_freq = 1000.0

for i in range(4):
    start = i * sample_per_beat
    end = start + sample_per_beat
    # Kick on 1 and 3
    for j in [0, 2]:
        note = tone(kick_freq, 0.05, sample_rate)
        buffer[start + j * int(sample_per_beat / 2):start + j * int(sample_per_beat / 2) + len(note)] += note
    # Snare on 2 and 4
    for j in [1, 3]:
        note = tone(snare_freq, 0.05, sample_rate)
        buffer[start + j * int(sample_per_beat / 2):start + j * int(sample_per_beat / 2) + len(note)] += note
    # Hihat on every 8th
    for j in range(8):
        note = tone(hihat_freq, 0.02, sample_rate)
        buffer[start + j * int(sample_per_beat / 4):start + j * int(sample_per_beat / 4) + len(note)] += note

# --- TENOR SAX (Dante) ---
# Short motif: Fm, start it, leave it hanging, return to finish

motif = [note_freqs['F3'], note_freqs['Ab3'], note_freqs['Bb3'], note_freqs['D3']]
offsets = [0, 0.25, 0.5, 0.75]  # Place notes on the first beat (first bar), staggered

for i in range(4):
    start = i * sample_per_beat
    end = start + sample_per_beat
    for j, freq in enumerate(motif):
        if j == 0:  # Start the motif on beat 1
            note = tone(freq, 0.25, sample_rate)  # Play the first note
            buffer[start + int(beat_length * sample_rate / 4):start + int(beat_length * sample_rate / 4) + len(note)] += note
        elif j == 3:  # Finish the motif on beat 4 of the 4th bar
            note = tone(freq, 0.25, sample_rate)
            buffer[start + int(beat_length * sample_rate * 3 / 4):start + int(beat_length * sample_rate * 3 / 4) + len(note)] += note

# Normalize and play the sound
buffer = buffer / np.max(np.abs(buffer))
sd.play(buffer, sample_rate)
sd.wait()

# Save the audio file if needed
write("intro_4_bar.wav", sample_rate, buffer)
