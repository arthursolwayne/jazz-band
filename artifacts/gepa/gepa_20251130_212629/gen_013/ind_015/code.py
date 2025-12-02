
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # 4 bars at 160 BPM
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)
BPM = 160
BEAT_DURATION = 60.0 / BPM  # seconds per beat
BAR_DURATION = BEAT_DURATION * 4  # seconds per bar
SIXTEENTH_NOTE = BEAT_DURATION / 4
EIGHTH_NOTE = BEAT_DURATION / 2
QUARTER_NOTE = BEAT_DURATION
HALF_NOTE = BEAT_DURATION * 2

# D Major Scale: D, E, F#, G, A, B, C#
D = 293.66  # D4
E = 329.63  # E4
F_SHARP = 369.99  # F#4
G = 392.00  # G4
A = 440.00  # A4
B = 493.88  # B4
C_SHARP = 554.37  # C#5

# D Minor Scale (used for tension): D, E, F, G, A, Bb, C
F = 349.23  # F4
B_FLAT = 466.16  # Bb4
C = 523.25  # C5

# Generate a sine wave
def sine_wave(freq, duration, sample_rate=SAMPLE_RATE):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    return wave

# Bar 1: Little Ray on drums (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
def bar_1():
    # Kick on 1 and 3
    kick = np.zeros(TOTAL_SAMPLES)
    kick[int(SAMPLE_RATE * 0.0)] = 0.5  # beat 1
    kick[int(SAMPLE_RATE * 0.75)] = 0.5  # beat 3

    # Snare on 2 and 4
    snare = np.zeros(TOTAL_SAMPLES)
    snare[int(SAMPLE_RATE * 0.5)] = 0.3  # beat 2
    snare[int(SAMPLE_RATE * 1.0)] = 0.3  # beat 4

    # Hihat on every eighth note
    hihat = np.zeros(TOTAL_SAMPLES)
    for i in range(0, int(SAMPLE_RATE * BAR_DURATION), int(SAMPLE_RATE * EIGHTH_NOTE)):
        hihat[i] = 0.1

    return kick + snare + hihat

# Bar 2-4: Full ensemble
def bar_2_4():
    # Bass line (Marcus) – walking line in D minor, chromatic approaches
    bass_notes = [F, F_SHARP, G, A, B_FLAT, B, C, D]  # walking line in D minor
    bass = np.zeros(TOTAL_SAMPLES)
    for i, note in enumerate(bass_notes):
        start = int(SAMPLE_RATE * (i * QUARTER_NOTE))
        end = int(SAMPLE_RATE * ((i + 1) * QUARTER_NOTE))
        bass[start:end] += sine_wave(note, end - start)

    # Piano (Diane) – 7th chords on 2 and 4
    # Dm7: D, F, A, C
    piano_notes = [D, F, A, C]  # Dm7
    piano = np.zeros(TOTAL_SAMPLES)
    # Comp on 2 and 4
    for i, note in enumerate(piano_notes):
        start = int(SAMPLE_RATE * (i * QUARTER_NOTE + 0.5))  # shift to beat 2
        end = int(SAMPLE_RATE * (i * QUARTER_NOTE + 0.5 + 0.25))
        piano[start:end] += sine_wave(note, end - start)

    # Saxophone (Dante) – melody in D minor, with a question at the end
    sax_notes = [D, F, G, B_FLAT]  # short motif
    sax = np.zeros(TOTAL_SAMPLES)
    durations = [0.25, 0.125, 0.25, 0.25]  # vary rhythm: quarter, eighth, quarter, quarter
    for i, note in enumerate(sax_notes):
        start = int(SAMPLE_RATE * (i * 0.5))  # start at 0, 0.5, 1.0, 1.5
        end = start + int(SAMPLE_RATE * durations[i])
        sax[start:end] += sine_wave(note, durations[i])

    # Drums (Little Ray) – same as bar 1, but louder
    kick = np.zeros(TOTAL_SAMPLES)
    kick[int(SAMPLE_RATE * 0.0)] = 0.7  # beat 1
    kick[int(SAMPLE_RATE * 0.75)] = 0.7  # beat 3

    snare = np.zeros(TOTAL_SAMPLES)
    snare[int(SAMPLE_RATE * 0.5)] = 0.4  # beat 2
    snare[int(SAMPLE_RATE * 1.0)] = 0.4  # beat 4

    hihat = np.zeros(TOTAL_SAMPLES)
    for i in range(0, int(SAMPLE_RATE * BAR_DURATION), int(SAMPLE_RATE * EIGHTH_NOTE)):
        hihat[i] = 0.15

    return bass + piano + sax + kick + snare + hihat

# Combine the bars
def compose_piece():
    bar1 = bar_1()
    bar2_4 = bar_2_4()
    piece = np.concatenate([bar1, bar2_4])
    return piece

# Normalize and play
def play_piece(piece):
    piece = piece / np.max(np.abs(piece))  # normalize to [-1, 1]
    write("dante_intro.wav", SAMPLE_RATE, (piece * 32767).astype(np.int16))  # save as 16-bit WAV
    sd.play(piece, SAMPLE_RATE)
    sd.wait()

# Run the composition
piece = compose_piece()
play_piece(piece)
