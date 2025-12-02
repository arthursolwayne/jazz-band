
from playsound import playsound
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Configuration
SAMPLE_RATE = 44100
DURATION = 6.0  # 6 seconds for 4 bars at 160 BPM
DURATION_SAMPLES = int(SAMPLE_RATE * DURATION)
CHANNELS = 1

# Dm7 chord: D F A C
# Frequencies in Hz (approx.)
D = 293.66
F = 349.23
A = 440.00
C = 523.25

# Synth parameters
DAMPING = 0.995
ATTACK = 0.005
DECAY = 0.1
SUSTAIN = 0.2
RELEASE = 0.1

def generate_sine_wave(freq, duration, sample_rate, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave

def envelope_attack_decay_release(length, attack, decay, release, sample_rate):
    t = np.linspace(0, 1, length)
    envelope = np.zeros_like(t)
    attack_len = int(attack * sample_rate)
    decay_len = int(decay * sample_rate)
    release_len = int(release * sample_rate)
    
    # Attack
    envelope[:attack_len] = t[:attack_len] / attack
    # Decay
    envelope[attack_len:attack_len+decay_len] = 1 - (t[attack_len:attack_len+decay_len] - attack) / decay
    # Sustain
    envelope[attack_len+decay_len:-release_len] = 1 - (t[attack_len+decay_len:-release_len] - attack - decay) / (1 - attack - decay - release)
    # Release
    envelope[-release_len:] = 1 - t[-release_len:] / release
    return envelope

def generate_note(freq, duration, sample_rate, envelope):
    wave = generate_sine_wave(freq, duration, sample_rate)
    return wave * envelope

def generate_synth_note(freq, sample_rate, duration, attack, decay, release):
    envelope = envelope_attack_decay_release(int(duration * sample_rate), attack, decay, release, sample_rate)
    return generate_note(freq, duration, sample_rate, envelope)

def generate_part(part, sample_rate):
    audio = np.zeros(DURATION_SAMPLES)
    for note in part:
        freq, start, duration, volume = note
        if volume == 0:
            continue
        note_samples = generate_synth_note(freq, sample_rate, duration, ATTACK, DECAY, RELEASE)
        start_idx = int(start * sample_rate)
        end_idx = start_idx + len(note_samples)
        audio[start_idx:end_idx] += note_samples * volume
    return audio

# Generate the four bars
# Bar 1: Little Ray on drums (snare on 2 and 4, hihat on every 8th)
# Bar 2-4: Full band in

# Bar 1: Drums only
bar1 = [
    # Snare on 2 and 4
    (554.37, 0.5, 0.05, 0.5),  # Snare on beat 2 (0.5s)
    (554.37, 1.0, 0.05, 0.5),  # Snare on beat 4 (1.0s)
    # Hihat on every eighth
    (207.65, 0.0, 0.03, 0.3),  # Hihat on beat 1
    (207.65, 0.25, 0.03, 0.3), # Hihat on beat 1+
    (207.65, 0.5, 0.03, 0.3),  # Hihat on beat 2
    (207.65, 0.75, 0.03, 0.3), # Hihat on beat 2+
    (207.65, 1.0, 0.03, 0.3),  # Hihat on beat 3
    (207.65, 1.25, 0.03, 0.3), # Hihat on beat 3+
    (207.65, 1.5, 0.03, 0.3),  # Hihat on beat 4
]

# Bar 2: Full band in
# Diane's chords on 2 and 4 (Dm7: D, F, A, C)
diane_part = [
    (293.66, 0.75, 0.1, 0.6),  # D on beat 2 (start at 0.75s)
    (349.23, 0.75, 0.1, 0.6),  # F on beat 2
    (440.00, 0.75, 0.1, 0.6),  # A on beat 2
    (523.25, 0.75, 0.1, 0.6),  # C on beat 2
    (293.66, 1.25, 0.1, 0.6),  # D on beat 4
    (349.23, 1.25, 0.1, 0.6),  # F on beat 4
    (440.00, 1.25, 0.1, 0.6),  # A on beat 4
    (523.25, 1.25, 0.1, 0.6),  # C on beat 4
]

# Marcus' walking bass (chromatic line)
# Dm7 chromatic walking line: D, Eb, E, F, G, Ab, A, Bb, B, C, D, Eb, etc.
# Duration: 2 bars (3 seconds), 16 notes (approx 0.1875s each)
chromatic_notes = [293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 440.00, 466.16, 493.88, 523.25, 554.37, 587.33]
chromatic_part = [
    (chromatic_notes[i], 0.0 + i * 0.1875, 0.05, 0.4) for i in range(len(chromatic_notes))
]

# Your tenor sax: melody (your motif)
# Dm7 melody (starting on D, with a half-step chromatic approach, then resolving)
# Dm7 melody: D, Eb, C, B, A, G, F, D
melody_notes = [293.66, 311.13, 523.25, 493.88, 440.00, 392.00, 349.23, 293.66]
melody_durations = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
melody_part = [
    (melody_notes[i], 0.0 + i * 0.25, melody_durations[i], 0.7) for i in range(len(melody_notes))
]

# Combine all parts
bar2 = diane_part + chromatic_part + melody_part

# Bar 3: Diane comps, Marcus walks, Ray continues
# Diane comps on 2 and 4 again
diane_part_bar3 = [
    (293.66, 1.75, 0.1, 0.6),
    (349.23, 1.75, 0.1, 0.6),
    (440.00, 1.75, 0.1, 0.6),
    (523.25, 1.75, 0.1, 0.6),
    (293.66, 2.25, 0.1, 0.6),
    (349.23, 2.25, 0.1, 0.6),
    (440.00, 2.25, 0.1, 0.6),
    (523.25, 2.25, 0.1, 0.6),
]
# Marcus continues walking (same chromatic line)
chromatic_part_bar3 = [
    (chromatic_notes[i], 1.5 + i * 0.1875, 0.05, 0.4) for i in range(len(chromatic_notes))
]

# Bar 3: No melody — it lingers

# Bar 4: Diane comps, Marcus walks, Ray continues
diane_part_bar4 = [
    (293.66, 2.75, 0.1, 0.6),
    (349.23, 2.75, 0.1, 0.6),
    (440.00, 2.75, 0.1, 0.6),
    (523.25, 2.75, 0.1, 0.6),
    (293.66, 3.25, 0.1, 0.6),
    (349.23, 3.25, 0.1, 0.6),
    (440.00, 3.25, 0.1, 0.6),
    (523.25, 3.25, 0.1, 0.6),
]
chromatic_part_bar4 = [
    (chromatic_notes[i], 3.0 + i * 0.1875, 0.05, 0.4) for i in range(len(chromatic_notes))
]

# Final bar: pause, leave it hanging
# Silence for 0.5 seconds at end
silence = np.zeros(int(0.5 * SAMPLE_RATE))

# Combine all parts
bar1_audio = generate_part(bar1, SAMPLE_RATE)
bar2_audio = generate_part(bar2, SAMPLE_RATE)
bar3_audio = generate_part(diane_part_bar3 + chromatic_part_bar3, SAMPLE_RATE)
bar4_audio = generate_part(diane_part_bar4 + chromatic_part_bar4, SAMPLE_RATE)

# Combine everything
full_audio = np.concatenate([
    bar1_audio,
    bar2_audio,
    bar3_audio,
    bar4_audio,
    silence
])

# Normalize
full_audio = full_audio / np.max(np.abs(full_audio))

# Write to file
write("intro.wav", SAMPLE_RATE, full_audio.astype(np.float32))

# Play the audio
playsound("intro.wav")

print("The intro is done. Let the silence linger.")
