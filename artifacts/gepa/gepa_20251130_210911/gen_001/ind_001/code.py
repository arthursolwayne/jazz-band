
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # 6 seconds for 4 bars at 160 BPM
FPS = SAMPLE_RATE
TONE_DURATION = 0.1  # In seconds
REST_DURATION = 0.05
VOLUME = 0.3

# Scale (D Dorian)
D_DORIAN = [D, E, F, G, A, B, C]  # Represented as note frequencies using MIDI
NOTE_FREQUENCIES = {
    'C': 261.63,
    'C#': 277.18,
    'D': 293.66,
    'D#': 311.13,
    'E': 329.63,
    'F': 349.23,
    'F#': 369.99,
    'G': 392.00,
    'G#': 415.30,
    'A': 440.00,
    'A#': 466.16,
    'B': 493.88
}

# Define the melody (tenor sax)
# Melody: D, F#, A, D (Dorian scale, simple motif)
melody_notes = ['D', 'F#', 'A', 'D']

# Define the bass line (Marcus)
# Walking bass line in D Dorian: D, E, F, G, A, B, C, D
bass_line = ['D', 'E', 'F', 'G', 'A', 'B', 'C', 'D']

# Define the piano chords (Diane) - 7th chords on 2 and 4
piano_chords = {
    'D7': [D, F#, A, C],  # D7 chord
    'F#7': [F#, A#, C#, E],  # F#7 chord
    'A7': [A, C#, E, G],  # A7 chord
    'D7': [D, F#, A, C]   # D7 chord
}

# Define the drum pattern (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_pattern = [
    ('kick', 0.0), ('hihat', 0.125), ('hihat', 0.25),
    ('snare', 0.375), ('hihat', 0.5), ('hihat', 0.625),
    ('kick', 0.75), ('hihat', 0.875), ('hihat', 1.0),
    ('snare', 1.125), ('hihat', 1.25), ('hihat', 1.375)
]

def generate_tone(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    tone = np.sin(frequency * t * 2 * np.pi)
    return tone

def generate_rest(duration, sample_rate):
    return np.zeros(int(duration * sample_rate))

def play_note(note, duration, sample_rate):
    freq = NOTE_FREQUENCIES[note]
    return generate_tone(freq, duration, sample_rate)

def generate_drums(drum_pattern, sample_rate):
    audio = np.zeros(int(DURATION * sample_rate))
    for event in drum_pattern:
        type_, time = event
        if type_ == 'kick':
            kick = generate_tone(60, 0.1, sample_rate)
            start_idx = int(time * sample_rate)
            audio[start_idx:start_idx + len(kick)] += kick
        elif type_ == 'snare':
            snare = generate_tone(150, 0.05, sample_rate)
            start_idx = int(time * sample_rate)
            audio[start_idx:start_idx + len(snare)] += snare
        elif type_ == 'hihat':
            hihat = generate_tone(1000, 0.02, sample_rate)
            start_idx = int(time * sample_rate)
            audio[start_idx:start_idx + len(hihat)] += hihat
    return audio

def generate_intro():
    audio = np.zeros(int(DURATION * SAMPLE_RATE))
    time_elapsed = 0.0

    # Bar 1: Little Ray alone
    # Kick and snare only
    # Kick on 1 (0.0), 3 (0.75)
    # Snare on 2 (0.375), 4 (1.125)
    drum_bar1 = [
        ('kick', 0.0), ('snare', 0.375),
        ('kick', 0.75), ('snare', 1.125)
    ]
    audio += generate_drums(drum_bar1, SAMPLE_RATE)
    time_elapsed += 1.5  # 1.5 seconds for bar 1

    # Bar 2: Everyone in
    # Melody (tenor sax)
    for note in melody_notes:
        audio[int(time_elapsed * SAMPLE_RATE):] += play_note(note, TONE_DURATION, SAMPLE_RATE)
        time_elapsed += TONE_DURATION
        # Rest between notes
        audio[int(time_elapsed * SAMPLE_RATE):] += generate_rest(REST_DURATION, SAMPLE_RATE)
        time_elapsed += REST_DURATION

    # Bass line (Marcus)
    for note in bass_line:
        audio[int(time_elapsed * SAMPLE_RATE):] += play_note(note, TONE_DURATION, SAMPLE_RATE)
        time_elapsed += TONE_DURATION
        # Rest between notes
        audio[int(time_elapsed * SAMPLE_RATE):] += generate_rest(REST_DURATION, SAMPLE_RATE)
        time_elapsed += REST_DURATION

    # Piano chords (Diane)
    # Play on 2 and 4
    for chord in piano_chords.values():
        for note in chord:
            audio[int(time_elapsed * SAMPLE_RATE):] += play_note(note, TONE_DURATION, SAMPLE_RATE)
            time_elapsed += TONE_DURATION
            # Rest between notes
            audio[int(time_elapsed * SAMPLE_RATE):] += generate_rest(REST_DURATION, SAMPLE_RATE)
            time_elapsed += REST_DURATION

    # Final bar: Everyone wraps up
    # Bass line again
    for note in bass_line:
        audio[int(time_elapsed * SAMPLE_RATE):] += play_note(note, TONE_DURATION, SAMPLE_RATE)
        time_elapsed += TONE_DURATION
        # Rest between notes
        audio[int(time_elapsed * SAMPLE_RATE):] += generate_rest(REST_DURATION, SAMPLE_RATE)
        time_elapsed += REST_DURATION

    # Normalize audio
    audio = np.clip(audio * VOLUME, -1, 1)
    return audio

# Generate the intro
intro_audio = generate_intro()

# Play it
sd.play(intro_audio, SAMPLE_RATE)
sd.wait()

# Save to a WAV file
write("jazz_intro.wav", SAMPLE_RATE, intro_audio)
print("Intro saved to 'jazz_intro.wav'")
