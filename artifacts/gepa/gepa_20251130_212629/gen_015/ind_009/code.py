
import numpy as np
import sounddevice as sd
import time
from scipy.io.wavfile import write

# Sampling rate and duration
sample_rate = 44100
duration = 6.0  # 6 seconds for 4 bars at 160 BPM
num_samples = int(sample_rate * duration)

# Generate a blank audio buffer
audio = np.zeros(num_samples, dtype=np.float32)

# Key: F Major
# Scale degrees: F (1), G (2), A (3), Bb (4), C (5), D (6), E (7)
# Frequencies in Hz for F Major scale (approximate)
# F = 349.23, G = 392.00, A = 440.00, Bb = 466.16, C = 523.25, D = 587.33, E = 659.25

# Frequency map
freq_map = {
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'Bb': 466.16,
    'C': 523.25,
    'D': 587.33,
    'E': 659.25
}

# Time per beat (160 BPM = 60 / 160 = 0.375 seconds per beat)
beat_time = 0.375
bar_time = beat_time * 4  # 1.5 seconds per bar

# Function to generate a tone
def generate_tone(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(2 * np.pi * freq * t)
    return tone

# Function to play a note at a certain time
def play_note(note, start_time, duration=0.1):
    freq = freq_map[note]
    samples = generate_tone(freq, duration, sample_rate)
    start_sample = int(start_time * sample_rate)
    end_sample = start_sample + len(samples)
    if end_sample < len(audio):
        audio[start_sample:end_sample] += samples

# Function to generate a walking bass line
def generate_bass_line(start_time=0):
    bass_notes = ['F', 'G', 'Ab', 'A', 'Bb', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'G', 'Ab', 'A', 'Bb', 'C']
    for i, note in enumerate(bass_notes):
        play_note(note, start_time + i * beat_time, duration=0.1)

# Function to generate piano chords
def generate_piano_chords(start_time=0):
    chords = ['F7', 'Bb7', 'E7', 'Am7']
    for i, chord in enumerate(chords):
        if chord == 'F7':
            notes = ['F', 'A', 'C', 'E']
        elif chord == 'Bb7':
            notes = ['Bb', 'D', 'F', 'Ab']
        elif chord == 'E7':
            notes = ['E', 'G', 'B', 'D']
        elif chord == 'Am7':
            notes = ['A', 'C', 'E', 'G']
        for j, note in enumerate(notes):
            play_note(note, start_time + i * beat_time + j * 0.05, duration=0.05)

# Function to generate drum pattern
def generate_drum_pattern(start_time=0):
    # Kick on 1 and 3
    play_note('kick', start_time + 0, duration=0.05)
    play_note('kick', start_time + 2, duration=0.05)
    # Snare on 2 and 4
    play_note('snare', start_time + 1, duration=0.05)
    play_note('snare', start_time + 3, duration=0.05)
    # Hi-hat on every eighth
    for i in range(0, 4):
        play_note('hihat', start_time + i * 0.1875, duration=0.05)
        play_note('hihat', start_time + i * 0.1875 + 0.09375, duration=0.05)

# Function to generate saxophone motif
def generate_sax_motif(start_time=0):
    # Motif: F - Bb - D - Bb (rest for 0.5s) - F - Bb - D - E
    # Represented as: [F, Bb, D, Bb] -> rest -> [F, Bb, D, E]
    notes = ['F', 'Bb', 'D', 'Bb', 'F', 'Bb', 'D', 'E']
    for i, note in enumerate(notes):
        if i < 4:
            play_note(note, start_time + i * 0.25, duration=0.1)
        else:
            play_note(note, start_time + 1.5 + (i - 4) * 0.25, duration=0.1)

# Generate the intro
generate_drum_pattern(0)  # Bar 1: Drums only
generate_bass_line(0)     # Bass starts from bar 1
generate_piano_chords(0)  # Piano starts from bar 1

generate_sax_motif(1.5)  # Sax enters at bar 2

# Normalize audio
audio = audio / np.max(np.abs(audio))

# Play audio
sd.play(audio, sample_rate)
sd.wait()

# Save as WAV file
write("jazz_intro.wav", sample_rate, audio)
print("Generated 'jazz_intro.wav'")
