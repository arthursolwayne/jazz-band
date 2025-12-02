
import numpy as np
import sounddevice as sd
import time
from scipy.io.wavfile import write

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # 6 seconds for 4 bars at 160 BPM
DURATION_SAMPLES = int(SAMPLE_RATE * DURATION)
BPM = 160
BEAT_DURATION = 60.0 / BPM
BAR_DURATION = 4 * BEAT_DURATION  # In seconds
BAR_SAMPLES = int(SAMPLE_RATE * BAR_DURATION)

# Frequencies in Dm (D, F, A, C, etc.) using just intonation
D = 293.66
F = 349.23
A = 440.00
C = 261.63
Eb = 311.13
G = 392.00
Bb = 233.08
B = 246.94
Db = 277.18
Fsharp = 369.99
Gsharp = 415.30
Csharp = 277.18
Ab = 220.00
E = 329.63
Dsharp = 311.13

# All instruments will be generated as separate tracks and mixed

# Generate Little Ray's drum track (Bar 1 only, kick on 1 and 3, snare on 2 and 4)
def generate_little_ray_drums(bar_samples):
    kick = np.zeros(bar_samples)
    snare = np.zeros(bar_samples)
    hihat = np.zeros(bar_samples)

    # Kick on 1 and 3
    kick[int(0.1 * SAMPLE_RATE)] = 1.0
    kick[int(0.75 * SAMPLE_RATE)] = 1.0

    # Snare on 2 and 4
    snare[int(0.5 * SAMPLE_RATE)] = 0.8
    snare[int(1.0 * SAMPLE_RATE)] = 0.8

    # Hihat on every eighth note
    for i in range(0, bar_samples, int(SAMPLE_RATE * 0.25)):
        hihat[i] = 0.5

    # Normalize and mix
    drums = kick + snare + hihat
    drums /= np.max(np.abs(drums))
    return drums

# Generate Marcus's bass line (walking line in Dm, D2-G2, using roots and fifths with chromatic approaches)
def generate_marcus_bass():
    # Dm root is D2 (73.42 Hz), fifth is A2 (110 Hz)
    # We'll walk down chromatically on the beat
    # D2, C2, Bb2, B2, A2, G2, F2, E2, D2
    # But we'll use D2, C, Bb, B, A, G, F, E, D

    notes = [D, C, Bb, B, A, G, F, E, D]
    note_durations = [0.125] * 8  # 8 notes over 1 bar (4 beats, 2 notes per beat)
    note_durations.append(0.125)  # last note

    bass = np.zeros(DURATION_SAMPLES)
    for i, freq in enumerate(notes):
        start = int(i * note_durations[i] * SAMPLE_RATE)
        end = int((i + 1) * note_durations[i] * SAMPLE_RATE)
        bass[start:end] = np.sin(2 * np.pi * freq * np.arange(end - start) / SAMPLE_RATE)
    bass /= np.max(np.abs(bass))
    return bass

# Generate Diane's piano chords (open voicings, resolve on the last bar)
def generate_diane_piano():
    # Dm -> Gm -> Cm -> Fm (each bar)
    # Chords: Dm (D, F, A), Gm (G, Bb, D), Cm (C, Eb, G), Fm (F, Ab, C)
    # Open voicings, comp on 2 and 4 of each bar

    # Dm: D, F, A
    # Gm: G, Bb, D
    # Cm: C, Eb, G
    # Fm: F, Ab, C

    # Chord durations: on 2 and 4 of each bar
    # Bar 1: Dm on beat 2 and 4
    # Bar 2: Gm on beat 2 and 4
    # Bar 3: Cm on beat 2 and 4
    # Bar 4: Fm on beat 2 and 4

    piano = np.zeros(DURATION_SAMPLES)
    for bar in range(4):
        beat = bar * 4
        # Beats 1-4
        # Comp on beat 2 and 4 (0.5 and 1.0 seconds)
        for comp_beat in [0.5, 1.0]:
            start = int((bar * BAR_DURATION) + comp_beat * SAMPLE_RATE)
            end = start + int(0.1 * SAMPLE_RATE)
            if bar == 0:
                # Dm: D, F, A
                freqs = [D, F, A]
            elif bar == 1:
                # Gm: G, Bb, D
                freqs = [G, Bb, D]
            elif bar == 2:
                # Cm: C, Eb, G
                freqs = [C, Eb, G]
            elif bar == 3:
                # Fm: F, Ab, C
                freqs = [F, Ab, C]

            # Mix together with volume balance
            for f in freqs:
                tone = np.sin(2 * np.pi * f * np.arange(end - start) / SAMPLE_RATE)
                piano[start:end] += tone * 0.2

    piano /= np.max(np.abs(piano))
    return piano

# Generate Dante's tenor sax melody: one short motif, starting, leaving, returning
def generate_dante_sax():
    # Motif: D - F - A - C (Dm scale), but with rhythm and space
    # Start on beat 1, leave on beat 3, return on beat 4
    # D, F, A, C
    # D on beat 1 (0.0), F on beat 2 (0.5), A on beat 3 (0.75), C on beat 4 (1.0)

    sax = np.zeros(DURATION_SAMPLES)
    # D on beat 1
    start = 0
    end = int(0.1 * SAMPLE_RATE)
    sax[start:end] = np.sin(2 * np.pi * D * np.arange(end - start) / SAMPLE_RATE)

    # F on beat 2
    start = int(0.5 * SAMPLE_RATE)
    end = int(0.6 * SAMPLE_RATE)
    sax[start:end] = np.sin(2 * np.pi * F * np.arange(end - start) / SAMPLE_RATE)

    # A on beat 3
    start = int(0.75 * SAMPLE_RATE)
    end = int(0.85 * SAMPLE_RATE)
    sax[start:end] = np.sin(2 * np.pi * A * np.arange(end - start) / SAMPLE_RATE)

    # C on beat 4
    start = int(1.0 * SAMPLE_RATE)
    end = int(1.1 * SAMPLE_RATE)
    sax[start:end] = np.sin(2 * np.pi * C * np.arange(end - start) / SAMPLE_RATE)

    # Add a small, mysterious note after the motif (a tritone or a quarter note off)
    # D# or F# on beat 4.5
    start = int(1.5 * SAMPLE_RATE)
    end = int(1.6 * SAMPLE_RATE)
    sax[start:end] = np.sin(2 * np.pi * Fsharp * np.arange(end - start) / SAMPLE_RATE)

    sax /= np.max(np.abs(sax))
    return sax

# Generate and mix all tracks
def generate_jazz_piece():
    drums = generate_little_ray_drums(BAR_SAMPLES)
    bass = generate_marcus_bass()
    piano = generate_diane_piano()
    sax = generate_dante_sax()

    # Mix the tracks with appropriate volume levels
    mix = (drums * 0.3) + (bass * 0.4) + (piano * 0.3) + (sax * 0.6)

    # Normalize
    mix = np.clip(mix, -1.0, 1.0)

    # Write to file
    write("dante_intro.wav", SAMPLE_RATE, (mix * 32767).astype(np.int16))

    # Play it back
    sd.play(mix, SAMPLE_RATE)
    sd.wait()

# Run the composition
generate_jazz_piece()
