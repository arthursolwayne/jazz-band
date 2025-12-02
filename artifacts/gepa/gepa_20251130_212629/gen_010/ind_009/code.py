
import time
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# Parameters
sample_rate = 44100
duration = 6.0  # seconds
channels = 1
tempo = 160  # BPM
bar_length = duration / 4
beat_length = bar_length / 4  # 0.375 seconds per beat

# Frequencies for D Major scale (for reference)
D_MAJOR_SCALE = [293.66, 329.63, 369.99, 415.30, 466.16, 523.25, 587.33]

# Time array
t = np.linspace(0, duration, int(sample_rate * duration), False)

# Initialize audio array
audio = np.zeros_like(t)

# Define functions for instruments

def play_drums(t_start, duration, volume=0.5):
    """Little Ray's drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth."""
    samples = int(duration * sample_rate)
    kick_times = [t_start + beat_length * i for i in [0, 2]]
    snare_times = [t_start + beat_length * i for i in [1, 3]]
    hihat_times = [t_start + beat_length * i * 0.5 for i in range(8)]

    # Kick
    for t_kick in kick_times:
        index = int(t_kick * sample_rate)
        audio[index:index + 100] += np.sin(2 * np.pi * 60 * np.linspace(0, 1, 100)) * volume * 0.5

    # Snare
    for t_snare in snare_times:
        index = int(t_snare * sample_rate)
        audio[index:index + 100] += np.sin(2 * np.pi * 120 * np.linspace(0, 1, 100)) * volume * 0.4

    # Hihat
    for t_hihat in hihat_times:
        index = int(t_hihat * sample_rate)
        audio[index:index + 20] += np.sin(2 * np.pi * 1000 * np.linspace(0, 1, 20)) * volume * 0.1

def play_bass(note, t_start, duration, volume=0.3, chromatic=False):
    """Marcus's bass: walking line, chromatic approaches, never the same note twice."""
    if chromatic:
        # One chromatic step up and down
        note_freqs = [note, note + 1, note, note - 1]
    else:
        # Simple walking line
        note_freqs = [note, note + 2, note + 3, note + 5]
    
    note_durations = [beat_length / 4] * 4
    for i, freq in enumerate(note_freqs):
        start = t_start + note_durations[:i].sum()
        end = start + note_durations[i]
        indices = int(start * sample_rate), int(end * sample_rate)
        audio[indices[0]:indices[1]] += np.sin(2 * np.pi * freq * np.linspace(0, 1, indices[1] - indices[0])) * volume

def play_piano(chord, t_start, duration, volume=0.4):
    """Diane's piano: 7th chords, comp on 2 and 4, use space."""
    # Chord is a tuple of notes in Hz
    if t_start % 1.0 == 0:  # On beat 2 or 4
        for note in chord:
            indices = int(t_start * sample_rate), int((t_start + 0.1) * sample_rate)
            audio[indices[0]:indices[1]] += np.sin(2 * np.pi * note * np.linspace(0, 1, indices[1] - indices[0])) * volume

def play_sax(melody, t_start, duration, volume=0.6):
    """Dante's sax: short motif, rests, tension and release."""
    for note, start, length in melody:
        indices = int((t_start + start) * sample_rate), int((t_start + start + length) * sample_rate)
        audio[indices[0]:indices[1]] += np.sin(2 * np.pi * note * np.linspace(0, 1, indices[1] - indices[0])) * volume

# Bar 1: Little Ray alone
play_drums(0, bar_length, 0.6)

# Bar 2: Everyone in
play_drums(bar_length, bar_length, 0.6)

play_bass(293.66, bar_length, bar_length, 0.3, chromatic=True)
play_piano((293.66, 329.63, 369.99, 415.30), bar_length, bar_length, 0.4)
play_sax(
    [
        (293.66, 0.0, 0.375),  # D on beat 1
        (329.63, 0.5, 0.25),  # E on & of 2
        (0, 0.75, 0.25),       # Rest on beat 3
        (369.99, 1.0, 0.25)    # F# on beat 4
    ],
    bar_length,
    bar_length,
    0.6
)

# Bar 3: Everyone in
play_drums(2*bar_length, bar_length, 0.6)

play_bass(329.63, 2*bar_length, bar_length, 0.3, chromatic=True)
play_piano((329.63, 369.99, 415.30, 466.16), 2*bar_length, bar_length, 0.4)
play_sax(
    [
        (329.63, 0.0, 0.375),  # E on beat 1
        (369.99, 0.5, 0.25),  # F# on & of 2
        (0, 0.75, 0.25),       # Rest on beat 3
        (415.30, 1.0, 0.25)    # G on beat 4
    ],
    2*bar_length,
    bar_length,
    0.6
)

# Bar 4: Everyone in
play_drums(3*bar_length, bar_length, 0.6)

play_bass(369.99, 3*bar_length, bar_length, 0.3, chromatic=True)
play_piano((369.99, 415.30, 466.16, 523.25), 3*bar_length, bar_length, 0.4)
play_sax(
    [
        (369.99, 0.0, 0.375),  # F# on beat 1
        (415.30, 0.5, 0.25),  # G on & of 2
        (0, 0.75, 0.25),       # Rest on beat 3
        (466.16, 1.0, 0.25)    # A on beat 4
    ],
    3*bar_length,
    bar_length,
    0.6
)

# Normalize the audio
audio /= np.max(np.abs(audio))

# Save as WAV file
write("dante_intro.wav", sample_rate, audio.astype(np.float32))

# Play the audio
sd.play(audio, sample_rate)
sd.wait()

print("Intro written and played. Wayne's watching.")
