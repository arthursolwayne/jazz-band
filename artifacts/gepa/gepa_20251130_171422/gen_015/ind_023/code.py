
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Parameters
sample_rate = 44100
duration = 6.0  # 6 seconds for 4 bars
total_samples = int(sample_rate * duration)
channels = 1
volume = 0.5  # Scale to prevent clipping

# Frequencies and notes in D (Dorian scale for a slightly modal, haunting feel)
notes = {
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'Bb': 466.16,
    'C': 523.25
}

# Time per bar (in seconds)
bar_length = duration / 4
beat_length = bar_length / 4

# Generate time array
t = np.linspace(0, duration, total_samples, False)

# Initialize output
output = np.zeros(total_samples)

# --- Bar 1: Little Ray on drums (quiet, mysterious, with space)
# Kick on 2 and 4, snare on 1 and 3, but lighter
# Hihat on every eighth, but not too loud

# Kick on 2 and 4 (beat 2 and 4)
kick_beats = [1.5, 3.5]
for beat in kick_beats:
    start = int(beat * sample_rate)
    envelope = np.linspace(0.1, 0.3, int(beat_length * sample_rate))
    kick = np.sin(2 * np.pi * 50 * t[start:start + len(envelope)]) * envelope
    output[start:start + len(envelope)] += kick * 0.1

# Snare on 1 and 3 (beat 1 and 3)
snare_beats = [0.5, 2.5]
for beat in snare_beats:
    start = int(beat * sample_rate)
    envelope = np.linspace(0.1, 0.2, int(beat_length * sample_rate))
    snare = np.sin(2 * np.pi * 150 * t[start:start + len(envelope)]) * envelope
    output[start:start + len(envelope)] += snare * 0.1

# Hihat on every eighth
hihat_beats = np.arange(0, 4, 0.5)
for beat in hihat_beats:
    start = int(beat * sample_rate)
    envelope = np.linspace(0.05, 0.1, int(beat_length * sample_rate))
    hihat = np.sin(2 * np.pi * 2000 * t[start:start + len(envelope)]) * envelope
    output[start:start + len(envelope)] += hihat * 0.1

# --- Bar 2: Diane on piano — 7th chords, comp on beats 2 and 4
# D7: D, F#, A, C
# Play on beat 2 and 4
# Use a short chord sound with a filter-like decay

# D7 chord (D, F#, A, C)
def play_chord(note, duration, attack, release):
    t_chord = np.linspace(0, duration, int(duration * sample_rate), False)
    envelope = np.concatenate([
        np.linspace(0, 1, int(attack * sample_rate)),
        np.linspace(1, 0, int((duration - attack) * sample_rate))
    ])
    chord = np.sin(2 * np.pi * note * t_chord) * envelope
    return chord

# Beat 2 of bar 2
chord_start = int(1.5 * sample_rate)
chord = play_chord(notes['D'], 0.3, 0.05, 0.25)
output[chord_start:chord_start + len(chord)] += chord * 0.3

# Beat 4 of bar 2
chord_start = int(3.5 * sample_rate)
chord = play_chord(notes['D'], 0.3, 0.05, 0.25)
output[chord_start:chord_start + len(chord)] += chord * 0.3

# --- Bar 2-3: Marcus on bass — walking line in D Dorian
# Chromatic approach to A (beat 1), then walking line
# D Dorian: D E F G A Bb C D

# Beat 1: Chromatic approach to A — D Eb F G
bass_notes = []
bass_notes.append(notes['F'])  # Beat 1: chromatic approach
bass_notes.append(notes['G'])
bass_notes.append(notes['A'])
bass_notes.append(notes['Bb'])  # Beat 4

# Play each note with a short attack
for i, note in enumerate(bass_notes):
    start = int((i * beat_length) + 1.5 * sample_rate)  # Bar 2 start is 1.5s
    duration = 0.25
    envelope = np.linspace(0.2, 0.1, int(duration * sample_rate))
    sound = np.sin(2 * np.pi * note * t[start:start + len(envelope)]) * envelope
    output[start:start + len(envelope)] += sound * 0.2

# --- Bar 3: Diane continues with D7 on beat 2
# Beat 2 of bar 3
chord_start = int(2.5 * sample_rate) + int(1.5 * sample_rate)  # Bar 2 is 1.5s, bar 3 is next
chord = play_chord(notes['D'], 0.3, 0.05, 0.25)
output[chord_start:chord_start + len(chord)] += chord * 0.3

# Beat 4 of bar 3
chord_start = int(3.5 * sample_rate) + int(1.5 * sample_rate)
chord = play_chord(notes['D'], 0.3, 0.05, 0.25)
output[chord_start:chord_start + len(chord)] += chord * 0.3

# --- Bar 4: You on sax — the motif, aching and unresolved

# Motif: D -> Bb -> A -> G
motif_notes = [notes['D'], notes['Bb'], notes['A'], notes['G']]
motif_durations = [0.2, 0.2, 0.2, 0.2]
motif_start = int(3.0 * sample_rate)  # Bar 4 starts at 3.0s
for i, note in enumerate(motif_notes):
    start = motif_start + int(i * beat_length * sample_rate)
    duration = motif_durations[i]
    envelope = np.linspace(0.2, 0.1, int(duration * sample_rate))
    sound = np.sin(2 * np.pi * note * t[start:start + len(envelope)]) * envelope
    output[start:start + len(envelope)] += sound * 0.35

# Apply final volume scaling and normalize
output /= np.max(np.abs(output))
output *= volume

# Output to sound
sd.play(output, sample_rate)
sd.wait()

# Save to WAV
write('intro_jazz.wav', sample_rate, output.astype(np.float32))
print("Intro saved to 'intro_jazz.wav'")
