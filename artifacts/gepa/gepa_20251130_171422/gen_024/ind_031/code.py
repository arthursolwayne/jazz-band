
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import matplotlib.pyplot as plt

# Parameters
sample_rate = 44100
duration = 6.0  # seconds
num_samples = int(sample_rate * duration)
fs = 160  # beats per minute
beat_duration = 60.0 / fs  # seconds per beat
bar_duration = beat_duration * 4  # seconds per bar

# Frequencies for F major scale: F, G, A, Bb, C, D, E
frequencies = [349.23, 392.00, 440.00, 466.16, 523.25, 587.33, 659.25]

# Generate a time axis
t = np.linspace(0, duration, num_samples, False)

# Initialize output signal
signal = np.zeros(num_samples)

# Function to generate a sine wave
def sine_wave(frequency, duration, sample_rate):
    return np.sin(2 * np.pi * frequency * t[:int(duration * sample_rate)])

# Function to apply ADSR envelope
def adsr_envelope(signal, attack=0.02, decay=0.2, sustain=0.5, release=0.5, sample_rate=44100):
    envelope = np.zeros(len(signal))
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    sustain_samples = int(sustain * sample_rate)
    release_samples = int(release * sample_rate)

    # Attack
    envelope[:attack_samples] = np.linspace(0, 1, attack_samples)

    # Decay
    envelope[attack_samples:attack_samples + decay_samples] = np.linspace(1, sustain, decay_samples)

    # Sustain
    envelope[attack_samples + decay_samples : attack_samples + decay_samples + sustain_samples] = sustain

    # Release
    envelope[attack_samples + decay_samples + sustain_samples:] = np.linspace(sustain, 0, release_samples)

    return signal * envelope

# Bar 1: Little Ray alone - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
print("Bar 1: Little Ray - Kick, snare, hihat")

# Kick on 1 and 3
kick1 = sine_wave(60, beat_duration, sample_rate)  # C2
kick1 = adsr_envelope(kick1, attack=0.05, decay=0.1, sustain=0.1, release=0.2)
kick1_start = int(0 * sample_rate)
signal[kick1_start : kick1_start + len(kick1)] += kick1

kick2 = sine_wave(60, beat_duration, sample_rate)
kick2 = adsr_envelope(kick2, attack=0.05, decay=0.1, sustain=0.1, release=0.2)
kick2_start = int(2 * beat_duration * sample_rate)
signal[kick2_start : kick2_start + len(kick2)] += kick2

# Snare on 2 and 4
snare1 = sine_wave(220, beat_duration, sample_rate)  # A3
snare1 = adsr_envelope(snare1, attack=0.02, decay=0.1, sustain=0.1, release=0.1)
snare1_start = int(1 * beat_duration * sample_rate)
signal[snare1_start : snare1_start + len(snare1)] += snare1

snare2 = sine_wave(220, beat_duration, sample_rate)
snare2 = adsr_envelope(snare2, attack=0.02, decay=0.1, sustain=0.1, release=0.1)
snare2_start = int(3 * beat_duration * sample_rate)
signal[snare2_start : snare2_start + len(snare2)] += snare2

# Hihat on every eighth note
hihat = sine_wave(1000, beat_duration / 2, sample_rate)  # High-pitched tone
hihat = adsr_envelope(hihat, attack=0.01, decay=0.01, sustain=0.01, release=0.01)
hihat_start = int(0 * beat_duration * sample_rate)
for i in range(8):
    signal[hihat_start + i * int(beat_duration / 2) : hihat_start + i * int(beat_duration / 2) + len(hihat)] += hihat

# Bar 2: All in. Diane on piano, Marcus on bass, Dante on saxophone

# Diane: 7th chords, comp on 2 and 4
print("Bar 2: Diane on piano - 7th chords on 2 and 4")

# C7 chord (C, E, G, Bb) - root on beat 2
c7 = [261.63, 329.63, 392.00, 466.16]
c7_duration = beat_duration / 2
c7_notes = [sine_wave(f, c7_duration, sample_rate) for f in c7]
c7_volume = 0.3
for note in c7_notes:
    signal[int(1 * beat_duration * sample_rate) : int(1 * beat_duration * sample_rate) + len(note)] += note * c7_volume

# F7 chord (F, A, C, Eb) - root on beat 4
f7 = [349.23, 440.00, 523.25, 311.13]
f7_notes = [sine_wave(f, c7_duration, sample_rate) for f in f7]
for note in f7_notes:
    signal[int(3 * beat_duration * sample_rate) : int(3 * beat_duration * sample_rate) + len(note)] += note * c7_volume

# Marcus: Walking line, chromatic approaches
print("Bar 2: Marcus on bass - Walking line")

# Bassline: F, Gb, G, A, Bb, B, C, Db
bass_notes = [349.23, 311.13, 392.00, 440.00, 466.16, 493.88, 523.25, 554.37]
bass_duration = beat_duration / 4
for note in bass_notes:
    bass_tone = sine_wave(note, bass_duration, sample_rate)
    bass_tone = adsr_envelope(bass_tone, attack=0.01, decay=0.05, sustain=0.1, release=0.05)
    signal[int(bass_notes.index(note) * bass_duration * sample_rate) : int(bass_notes.index(note) * bass_duration * sample_rate) + len(bass_tone)] += bass_tone

# Dante: Tenor saxophone - Motif that suggests a memory or question
print("Bar 2: Dante on tenor sax - Motif starts")

# Motif: F (F), G (G), Bb (Bb), F (F) — but with rhythmic and dynamic variation
motif = [349.23, 392.00, 466.16, 349.23]

# Apply dynamic variation
motif_dynamics = [0.5, 0.6, 0.3, 0.4]  # Whisper, cry, question, memory
motif_lengths = [beat_duration / 3, beat_duration / 4, beat_duration / 4, beat_duration / 3]

for i in range(len(motif)):
    note = sine_wave(motif[i], motif_lengths[i], sample_rate)
    note = adsr_envelope(note, attack=0.01, decay=0.1, sustain=0.2, release=0.1)
    note *= motif_dynamics[i]
    signal[int(i * (beat_duration / 4) * sample_rate) : int(i * (beat_duration / 4) * sample_rate) + len(note)] += note

# Bar 3: Continue the motif, layer in tension
print("Bar 3: Continue motif and add tension")

# Motif continuation: D (D), C (C), Ab (Ab), Bb (Bb) — more tension
motif2 = [587.33, 523.25, 415.30, 466.16]
motif2_dynamics = [0.4, 0.5, 0.3, 0.6]
motif2_lengths = [beat_duration / 4, beat_duration / 4, beat_duration / 4, beat_duration / 4]

for i in range(len(motif2)):
    note = sine_wave(motif2[i], motif2_lengths[i], sample_rate)
    note = adsr_envelope(note, attack=0.01, decay=0.1, sustain=0.2, release=0.1)
    note *= motif2_dynamics[i]
    signal[int(i * (beat_duration / 4) * sample_rate + 2 * beat_duration * sample_rate) : int(i * (beat_duration / 4) * sample_rate + 2 * beat_duration * sample_rate) + len(note)] += note

# Add Diane's comping again — similar to bar 2
for note in c7_notes:
    signal[int(1 * beat_duration * sample_rate + 2 * beat_duration * sample_rate) : int(1 * beat_duration * sample_rate + 2 * beat_duration * sample_rate) + len(note)] += note * c7_volume

for note in f7_notes:
    signal[int(3 * beat_duration * sample_rate + 2 * beat_duration * sample_rate) : int(3 * beat_duration * sample_rate + 2 * beat_duration * sample_rate) + len(note)] += note * c7_volume

# Bar 4: Resolution with tension
print("Bar 4: Resolution with tension")

# Motif resolution: F (F), Eb (Eb), D (D), C (C) — a memory, a question
motif3 = [349.23, 311.13, 587.33, 523.25]
motif3_dynamics = [0.6, 0.3, 0.4, 0.5]
motif3_lengths = [beat_duration / 4, beat_duration / 4, beat_duration / 4, beat_duration / 4]

for i in range(len(motif3)):
    note = sine_wave(motif3[i], motif3_lengths[i], sample_rate)
    note = adsr_envelope(note, attack=0.01, decay=0.1, sustain=0.2, release=0.1)
    note *= motif3_dynamics[i]
    signal[int(i * (beat_duration / 4) * sample_rate + 3 * beat_duration * sample_rate) : int(i * (beat_duration / 4) * sample_rate + 3 * beat_duration * sample_rate) + len(note)] += note

# Diane: Resolve with a C7 chord on beat 4
c7_notes = [sine_wave(f, beat_duration / 2, sample_rate) for f in [261.63, 329.63, 392.00, 466.16]]
for note in c7_notes:
    signal[int(3 * beat_duration * sample_rate) : int(3 * beat_duration * sample_rate) + len(note)] += note * c7_volume

# Marcus: Walking line resolution
bass_notes = [349.23, 392.00, 440.00, 466.16]
for note in bass_notes:
    bass_tone = sine_wave(note, bass_duration, sample_rate)
    bass_tone = adsr_envelope(bass_tone, attack=0.01, decay=0.05, sustain=0.1, release=0.05)
    signal[int(bass_notes.index(note) * bass_duration * sample_rate + 3 * beat_duration * sample_rate) : int(bass_notes.index(note) * bass_duration * sample_rate + 3 * beat_duration * sample_rate) + len(bass_tone)] += bass_tone

# Add Little Ray for bar 4
hihat = sine_wave(1000, beat_duration / 2, sample_rate)
hihat = adsr_envelope(hihat, attack=0.01, decay=0.01, sustain=0.01, release=0.01)
hihat_start = int(3 * beat_duration * sample_rate)
for i in range(8):
    signal[hihat_start + i * int(beat_duration / 2) : hihat_start + i * int(beat_duration / 2) + len(hihat)] += hihat

# Normalize the signal
signal = signal / np.max(np.abs(signal))

# Play the audio
sd.play(signal, sample_rate)
sd.wait()

# Save as a WAV file
write("jazz_intro.wav", sample_rate, signal.astype(np.float32))

print("Audio saved as jazz_intro.wav.")
