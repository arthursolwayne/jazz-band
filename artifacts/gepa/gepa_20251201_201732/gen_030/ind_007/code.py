
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # 6 seconds for 4 bars
FREQ_A4 = 440.0
F_NOTE_FREQ = 174.61  # Frequency of F (F4)
F_SHARP_FREQ = 185.00  # F#
G_NOTE_FREQ = 196.00  # G
A_NOTE_FREQ = 220.00  # A
B_FLAT_FREQ = 233.08  # Bb
B_NOTE_FREQ = 246.94  # B
C_NOTE_FREQ = 261.63  # C
D_NOTE_FREQ = 293.66  # D
E_NOTE_FREQ = 329.63  # E

# Time per beat (160 BPM = 0.375 seconds per beat)
BEAT_DURATION = 0.375
BAR_DURATION = 1.5  # 4 beats per bar
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)

# Initialize the audio array
audio = np.zeros(TOTAL_SAMPLES, dtype=np.float32)

# Helper function to generate a sine wave tone
def generate_sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    return wave

# Bar 1: Little Ray on drums (Kick on 1 and 3, snare on 2 and 4)
print("Bar 1: Little Ray (Drums) - Kick on 1 and 3, snare on 2 and 4")

# Kick on 1
audio[int(0 * SAMPLE_RATE * BEAT_DURATION):int(0.1 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(60, 0.1, SAMPLE_RATE) * 0.2
# Snare on 2
audio[int(1 * SAMPLE_RATE * BEAT_DURATION):int(1.1 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(200, 0.1, SAMPLE_RATE) * 0.2
# Kick on 3
audio[int(2 * SAMPLE_RATE * BEAT_DURATION):int(2.1 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(60, 0.1, SAMPLE_RATE) * 0.2
# Snare on 4
audio[int(3 * SAMPLE_RATE * BEAT_DURATION):int(3.1 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(200, 0.1, SAMPLE_RATE) * 0.2

# Bar 2: Diane on piano (Open voicings, different chord each bar, comp on 2 and 4)
print("Bar 2: Diane (Piano) - Open voicings, chord: F7 (F A C E♭)")

# F7 chord (F A C Eb) - open voicing with some tension
# We'll simulate this with a chord sound (approximate)
chord_sample = generate_sine_wave(F_NOTE_FREQ, 0.2, SAMPLE_RATE) * 0.3
chord_sample += generate_sine_wave(A_NOTE_FREQ, 0.2, SAMPLE_RATE) * 0.2
chord_sample += generate_sine_wave(C_NOTE_FREQ, 0.2, SAMPLE_RATE) * 0.2
chord_sample += generate_sine_wave(B_FLAT_FREQ, 0.2, SAMPLE_RATE) * 0.2

# Place the chord on beat 2 and 4
audio[int(1 * SAMPLE_RATE * BEAT_DURATION):int(1.2 * SAMPLE_RATE * BEAT_DURATION)] += chord_sample
audio[int(3 * SAMPLE_RATE * BEAT_DURATION):int(3.2 * SAMPLE_RATE * BEAT_DURATION)] += chord_sample

# Bar 3: Marcus on bass (Walking line, roots and fifths with chromatic approaches)
print("Bar 3: Marcus (Bass) - Walking line: F (root), G (fifth), F# (chromatic approach), E (fifth again)")

# F (root)
audio[int(2 * SAMPLE_RATE * BEAT_DURATION):int(2.1 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(F_NOTE_FREQ, 0.1, SAMPLE_RATE) * 0.5
# G (fifth)
audio[int(3 * SAMPLE_RATE * BEAT_DURATION):int(3.1 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(G_NOTE_FREQ, 0.1, SAMPLE_RATE) * 0.5
# F# (chromatic)
audio[int(4 * SAMPLE_RATE * BEAT_DURATION):int(4.1 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(F_SHARP_FREQ, 0.1, SAMPLE_RATE) * 0.5
# E (fifth movement)
audio[int(5 * SAMPLE_RATE * BEAT_DURATION):int(5.1 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(E_NOTE_FREQ, 0.1, SAMPLE_RATE) * 0.5

# Bar 4: Dante on tenor sax (Motif: short, singable, leaves it hanging)
print("Bar 4: Dante (Tenor Sax) - Motif: F A Bb F (melody that lingers)")

# F
audio[int(2 * SAMPLE_RATE * BEAT_DURATION):int(2.2 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(F_NOTE_FREQ, 0.2, SAMPLE_RATE) * 0.5
# A
audio[int(2.5 * SAMPLE_RATE * BEAT_DURATION):int(2.7 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(A_NOTE_FREQ, 0.2, SAMPLE_RATE) * 0.5
# Bb
audio[int(3 * SAMPLE_RATE * BEAT_DURATION):int(3.2 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(B_FLAT_FREQ, 0.2, SAMPLE_RATE) * 0.5
# F (return to start, but don't resolve)
audio[int(3.5 * SAMPLE_RATE * BEAT_DURATION):int(3.7 * SAMPLE_RATE * BEAT_DURATION)] += generate_sine_wave(F_NOTE_FREQ, 0.2, SAMPLE_RATE) * 0.5

# Normalize and apply a soft envelope
audio = np.clip(audio / np.max(np.abs(audio)), -1, 1)

# Write to a WAV file
write("dante_intro.wav", SAMPLE_RATE, audio)

# Play the audio
sd.play(audio, SAMPLE_RATE)
sd.wait()

print("Composition complete. The intro is ready. Wayne is listening.")
