
import numpy as np
import sounddevice as sd
import time
from scipy.io.wavfile import write

# Parameters
sample_rate = 44100
duration = 6.0  # 6 seconds for 4 bars at 160 BPM
channels = 1
bits_per_sample = 16

# Synthesize the audio
def generate_intro():
    # Initialize audio buffer
    audio = np.zeros(int(sample_rate * duration), dtype=np.float32)

    # Define the key: Dm (D, F, A)
    root = 62  # D4
    fifth = 67  # A4
    minor_third = 64  # F4
    low_root = 47  # D3

    # Function to play a note (frequency, start, duration)
    def play_note(freq, start, duration):
        t = np.linspace(start, start + duration, int(duration * sample_rate), False)
        wave = np.sin(2 * np.pi * freq * t)
        audio[int(start * sample_rate):int((start + duration) * sample_rate)] += wave

    # Drums (Little Ray)
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    for bar in range(4):
        for beat in [0, 2]:  # 1 and 3 in 0-indexed
            kick_time = bar * 1.5 + beat * 0.375
            play_note(65.41, kick_time, 0.1)

        for beat in [1, 3]:  # 2 and 4
            snare_time = bar * 1.5 + beat * 0.375
            play_note(185.00, snare_time, 0.1)

        for eighth in range(8):
            hihat_time = bar * 1.5 + eighth * 0.1875
            play_note(2500.0, hihat_time, 0.05)

    # Bass (Marcus)
    # Walking line: D2-G2, roots and fifths with chromatic approaches
    bass_notes = [
        47,  # D3
        48,  # D#3 (chromatic approach)
        50,  # F3
        52,  # G3
        57,  # Bb3
        59,  # B3 (chromatic)
        62,  # D4
        64,  # F4
        67,  # A4
        69,  # B4 (chromatic)
        72,  # D5
        74,  # E5 (chromatic)
        76,  # F#5
        79,  # A5
        81,  # B5 (chromatic)
        84   # D6
    ]

    # Distribute bass notes across the 6 seconds, roughly every 0.375s
    for i, note in enumerate(bass_notes):
        time_point = i * 0.375
        play_note(2 ** ((note - 69) / 12) * 440.0, time_point, 0.1)

    # Piano (Diane)
    # Open voicings, different chord each bar, resolve on the last
    # Bar 1: Dm7 (D, F, A, C)
    # Bar 2: Dm7 -> Gm7
    # Bar 3: Am7
    # Bar 4: Dm7 (resolve)
    def play_chord(chord_notes, start_time):
        for note in chord_notes:
            freq = 2 ** ((note - 69) / 12) * 440.0
            play_note(freq, start_time, 0.2)

    # Bar 1: Dm7 (D, F, A, C)
    play_chord([62, 64, 67, 69], 0)

    # Bar 2: Gm7 (G, Bb, D, F)
    play_chord([67, 69, 72, 64], 1.5)

    # Bar 3: Am7 (A, C, E, G)
    play_chord([69, 72, 76, 67], 3.0)

    # Bar 4: Dm7 (resolve)
    play_chord([62, 64, 67, 69], 4.5)

    # Tenor Sax (You)
    # One short motif, simple but with a twist
    # Start on D (62), then F (64), then A (67), then rest
    # Then come back on D (62) and hold

    # First motif: D, F, A
    play_note(2 ** ((62 - 69) / 12) * 440.0, 0, 0.2)
    play_note(2 ** ((64 - 69) / 12) * 440.0, 0.375, 0.2)
    play_note(2 ** ((67 - 69) / 12) * 440.0, 0.75, 0.2)

    # Rest for tension
    # Then come back on D, hold for the rest of the bar
    play_note(2 ** ((62 - 69) / 12) * 440.0, 1.5, 0.6)

    # Normalize
    audio = audio / np.max(np.abs(audio))

    return audio

# Generate the audio
audio = generate_intro()

# Write to file
write("jazz_intro.wav", sample_rate, audio.astype(np.int16))

# Play the audio
sd.play(audio, sample_rate)
sd.wait()

print("Intro generated and played. Let the legend hear it.")
