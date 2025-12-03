
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
from scipy.signal import savgol_filter

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # seconds
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)
BPM = 160
BEAT_DURATION = 60.0 / BPM  # seconds per beat
BAR_DURATION = 4 * BEAT_DURATION  # seconds per bar
TWO_BAR_DURATION = 2 * BEAT_DURATION  # seconds for 2 bars
THREE_BAR_DURATION = 3 * BEAT_DURATION  # for the intro build-up
FOUR_BAR_DURATION = BAR_DURATION  # 6.0 seconds total

# Frequencies for Dm scale (D, Eb, F, G, Ab, Bb, C)
# MIDI note numbers: D2=37, Eb2=38, F2=39, G2=40, Ab2=41, Bb2=42, C3=43
# Using Dm as the key (D minor, Dm7 = D, F, Ab, C)

# Generate a sine wave function
def sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return np.sin(2 * np.pi * freq * t)

# Generate a drum pattern for Little Ray
def generate_drums(duration, beat_duration):
    samples = np.zeros(int(duration * SAMPLE_RATE))
    for i in range(int(duration / beat_duration)):
        # Kick on 1 and 3
        if i % 2 == 0:
            kick_freq = 60  # low C
            samples[int(i * beat_duration * SAMPLE_RATE) : int((i + 0.05) * beat_duration * SAMPLE_RATE)] += sine_wave(kick_freq, 0.05, SAMPLE_RATE)
        # Snare on 2 and 4
        if i % 2 == 1:
            snare_freq = 200  # snare-like pitch
            samples[int(i * beat_duration * SAMPLE_RATE) : int((i + 0.03) * beat_duration * SAMPLE_RATE)] += sine_wave(snare_freq, 0.03, SAMPLE_RATE)
        # Hi-hat on every eighth
        for j in range(2):
            hat_freq = 500
            samples[int((i * beat_duration + j * 0.5) * SAMPLE_RATE) : int((i * beat_duration + j * 0.5 + 0.01) * SAMPLE_RATE)] += sine_wave(hat_freq, 0.01, SAMPLE_RATE)
    return samples

# Generate bass line for Marcus (D2-G2, with chromatic approaches)
def generate_bass_line(duration, beat_duration):
    samples = np.zeros(int(duration * SAMPLE_RATE))
    # Bass line in Dm7: D, F, Ab, C (MIDI 37, 39, 41, 43)
    # Walking line with chromatic approaches
    bass_notes = [37, 38, 39, 40, 41, 42, 43, 41, 40, 39, 38, 37, 39, 40, 41, 43]
    for i, note in enumerate(bass_notes):
        freq = 440 * (2 ** ((note - 69) / 12))  # Convert MIDI to frequency
        start = int(i * beat_duration * SAMPLE_RATE)
        end = int((i + 0.25) * beat_duration * SAMPLE_RATE)
        samples[start:end] += sine_wave(freq, 0.25, SAMPLE_RATE)
    return samples

# Generate piano comping for Diane (open voicings, one chord per bar)
def generate_piano(duration, beat_duration):
    samples = np.zeros(int(duration * SAMPLE_RATE))
    # Dm7: D, F, Ab, C
    # D minor 7th chord - open voicings, one chord per bar
    chords = [
        [37, 39, 41, 43],  # Dm7
        [39, 41, 43, 45],  # F7 (substitute)
        [40, 42, 44, 46],  # Gm7
        [37, 39, 41, 43]   # Dm7 (resolve)
    ]
    for i, chord in enumerate(chords):
        chord_samples = np.zeros(int(duration * SAMPLE_RATE))
        for note in chord:
            freq = 440 * (2 ** ((note - 69) / 12))
            start = int(i * beat_duration * SAMPLE_RATE)
            end = int((i + 0.5) * beat_duration * SAMPLE_RATE)
            chord_samples[start:end] += sine_wave(freq, 0.5, SAMPLE_RATE)
        # Apply a soft decay to simulate piano dynamics
        chord_samples = savgol_filter(chord_samples, 101, 3)
        samples += chord_samples
    return samples

# Generate saxophone melody for Dante (unique, emotive, Dm mode with a twist)
def generate_sax_melody(duration, beat_duration):
    samples = np.zeros(int(duration * SAMPLE_RATE))
    # Melody in Dm, but with a twist (chromaticism and emotional inflection)
    # Dm mode: D, Eb, F, G, Ab, Bb, C
    # Melody: D (start), Eb, F, G, Ab, Bb, C, Ab, G, F, Eb, D
    # Notes (MIDI): 37, 38, 39, 40, 41, 42, 43, 41, 40, 39, 38, 37
    # Play the motif, leave it hanging, return
    notes = [37, 38, 39, 40, 41, 42, 43, 41, 40, 39, 38, 37]
    for i, note in enumerate(notes):
        freq = 440 * (2 ** ((note - 69) / 12))
        start = int(i * (beat_duration / 2) * SAMPLE_RATE)
        end = int((i + 0.25) * (beat_duration / 2) * SAMPLE_RATE)
        samples[start:end] += sine_wave(freq, 0.25, SAMPLE_RATE)
    return samples

# Generate full track
def generate_intro():
    total_audio = np.zeros(TOTAL_SAMPLES)
    
    # Add drums
    total_audio += generate_drums(FOUR_BAR_DURATION, BEAT_DURATION)
    
    # Add bass
    total_audio += generate_bass_line(FOUR_BAR_DURATION, BEAT_DURATION)
    
    # Add piano
    total_audio += generate_piano(FOUR_BAR_DURATION, BEAT_DURATION)
    
    # Add sax
    total_audio += generate_sax_melody(FOUR_BAR_DURATION, BEAT_DURATION)
    
    # Normalize and limit to prevent clipping
    total_audio = total_audio / np.max(np.abs(total_audio)) * 0.5

    return total_audio

# Generate and save the audio
intro_audio = generate_intro()
write("dante_intro.wav", SAMPLE_RATE, intro_audio.astype(np.float32))

print("Intro saved as 'dante_intro.wav'")
