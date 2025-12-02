
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # 6 seconds
BPM = 160
BEAT_DURATION = 60.0 / BPM  # seconds per beat
BAR_DURATION = 4 * BEAT_DURATION  # 4/4 time
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)

# Frequency to note mapping (approximate for melody)
NOTE_FREQUENCIES = {
    'F': 174.61,   # F3
    'G': 195.996,  # G3
    'Ab': 207.65,  # Ab3
    'Bb': 233.08,  # Bb3
    'C': 261.63,   # C4
    'Db': 277.18,  # Db4
    'D': 293.66,   # D4
    'Eb': 311.13,  # Eb4
    'E': 329.63,   # E4
    'F#': 369.99,  # F#4
    'G#': 415.30,  # G#4
    'A': 440.00,   # A4
    'B': 493.88    # B4
}

# Tempo-based timing
BEAT_DURATION_SECONDS = 60.0 / BPM
BAR_DURATION_SECONDS = 4 * BEAT_DURATION_SECONDS

# Generate a blank audio buffer
audio = np.zeros(TOTAL_SAMPLES, dtype=np.float32)

# Define the four bars in a timeline
timeline = []

# Bar 1: Little Ray on drums alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll simulate this with white noise and panning
def add_drums(bar, kick_times, snare_times, hihat_times):
    kick_freq = 75  # low frequency for kick
    snare_freq = 200  # mid-high for snare
    hihat_freq = 2000  # high for hihat
    vol_kick = 0.4
    vol_snare = 0.3
    vol_hihat = 0.2

    for t in kick_times:
        start = int(t * SAMPLE_RATE)
        env = np.linspace(0, 1, int(0.05 * SAMPLE_RATE))  # 50ms attack
        env = np.concatenate([env, np.linspace(1, 0, int(0.1 * SAMPLE_RATE))])  # 100ms decay
        if len(env) > len(audio[start:start + len(env)]):
            env = env[:len(audio[start:start + len(env)])]
        audio[start:start + len(env)] += np.sin(2 * np.pi * kick_freq * np.arange(len(env)) / SAMPLE_RATE) * env * vol_kick

    for t in snare_times:
        start = int(t * SAMPLE_RATE)
        env = np.random.normal(0, 1, int(0.1 * SAMPLE_RATE))
        env = (env - env.min()) / (env.max() - env.min())  # normalize
        env = np.concatenate([env, np.linspace(1, 0, int(0.1 * SAMPLE_RATE))])  # 100ms decay
        if len(env) > len(audio[start:start + len(env)]):
            env = env[:len(audio[start:start + len(env)])]
        audio[start:start + len(env)] += np.sin(2 * np.pi * snare_freq * np.arange(len(env)) / SAMPLE_RATE) * env * vol_snare

    for t in hihat_times:
        start = int(t * SAMPLE_RATE)
        env = np.random.normal(0, 1, int(0.02 * SAMPLE_RATE))
        env = (env - env.min()) / (env.max() - env.min())
        env = np.concatenate([env, np.linspace(1, 0, int(0.05 * SAMPLE_RATE))])
        if len(env) > len(audio[start:start + len(env)]):
            env = env[:len(audio[start:start + len(env)])]
        audio[start:start + len(env)] += np.sin(2 * np.pi * hihat_freq * np.arange(len(env)) / SAMPLE_RATE) * env * vol_hihat

# Bar 1: Drums alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar1_kicks = [0.0, 0.75]
bar1_snare = [0.25, 1.0]
bar1_hihat = np.arange(0.0, 1.0 + 0.125, 0.125)  # every eighth note

add_drums(0, bar1_kicks, bar1_snare, bar1_hihat)

# Bar 2: Bass enters, walking line in Fm
# Fm = F, Ab, Bb, D, Eb, F# (not used), G (not used) — walking bass in Fm
# Free of repetition, chromatic approaches
def add_bass(bar, notes, durations):
    for note, duration in zip(notes, durations):
        freq = NOTE_FREQUENCIES[note]
        start = int(bar * BAR_DURATION_SECONDS + duration[0] * BAR_DURATION_SECONDS)
        length = int(duration[1] * BAR_DURATION_SECONDS * SAMPLE_RATE)
        env = np.linspace(0, 1, int(0.05 * SAMPLE_RATE))  # attack
        env = np.concatenate([env, np.linspace(1, 0, int(0.1 * SAMPLE_RATE))])  # decay
        if len(env) > length:
            env = env[:length]
        audio[start:start + length] += np.sin(2 * np.pi * freq * np.arange(length) / SAMPLE_RATE) * env * 0.3

# Fm walking line in bar 2
# Chromatic approach to F, then to Bb, then to D, then to Eb
bass_notes = ['F', 'F#', 'Bb', 'Bb', 'B', 'D', 'D#', 'Eb']
bass_durations = [(0.0, 0.125), (0.125, 0.125), (0.25, 0.125), (0.375, 0.125),
                  (0.5, 0.125), (0.625, 0.125), (0.75, 0.125), (0.875, 0.125)]

add_bass(1, bass_notes, bass_durations)

# Bar 2-3: Piano enters — 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, D
# Cm7 = C, Eb, F, A
# Fm7 again on 2 and 4
def add_piano(bar, chords):
    for chord in chords:
        # Use root, 7th, 3rd, 5th in a comp
        # Chord: Fm7 = F, Ab, Bb, D
        # Chord: Cm7 = C, Eb, F, A
        # Chord: Fm7 = F, Ab, Bb, D
        # Chord: Dm7 = D, F, Ab, B
        notes = chord
        for note in notes:
            freq = NOTE_FREQUENCIES[note]
            # Randomize start slightly for more human feel
            start = int((bar * BAR_DURATION_SECONDS) + (np.random.rand() * 0.05) + 0.0)
            length = int(0.125 * BAR_DURATION_SECONDS * SAMPLE_RATE)
            env = np.linspace(0, 1, int(0.05 * SAMPLE_RATE))  # attack
            env = np.concatenate([env, np.linspace(1, 0, int(0.1 * SAMPLE_RATE))])  # decay
            if len(env) > length:
                env = env[:length]
            audio[start:start + length] += np.sin(2 * np.pi * freq * np.arange(length) / SAMPLE_RATE) * env * 0.2

# Piano plays on 2 and 4
piano_chords = [
    ['F', 'Ab', 'Bb', 'D'],  # Fm7 on beat 2
    ['C', 'Eb', 'F', 'A'],   # Cm7 on beat 4
    ['F', 'Ab', 'Bb', 'D'],  # Fm7 again on beat 2
    ['D', 'F', 'Ab', 'B']    # Dm7 on beat 4
]

add_piano(1, piano_chords)

# Bar 2-4: Tenor sax enters — one short motif, make it sing
# "F" -> "Ab" -> "Bb" -> rest
# Then "D" -> "C" -> rest -> rest
# Then "Eb" -> "F#"
# Then rest -> rest -> rest -> rest
# Create a sparse, searching motif

def add_sax(bar, notes, durations):
    for note, duration in zip(notes, durations):
        freq = NOTE_FREQUENCIES[note]
        start = int((bar * BAR_DURATION_SECONDS) + duration[0] * BAR_DURATION_SECONDS)
        length = int(duration[1] * BAR_DURATION_SECONDS * SAMPLE_RATE)
        if length == 0:
            continue
        env = np.linspace(0, 1, int(0.05 * SAMPLE_RATE))  # attack
        env = np.concatenate([env, np.linspace(1, 0, int(0.1 * SAMPLE_RATE))])  # decay
        if len(env) > length:
            env = env[:length]
        audio[start:start + length] += np.sin(2 * np.pi * freq * np.arange(length) / SAMPLE_RATE) * env * 0.5

# Sax motif: start with F, then Ab, then Bb — leave it hanging
# Then D, C — another tension
# Then Eb, F# — a pivot
# Then silence — the question

sax_notes = [
    ('F', (0.0, 0.125)),
    ('Ab', (0.125, 0.125)),
    ('Bb', (0.25, 0.125)),
    ('F', (0.375, 0.0)),  # rest
    ('D', (0.5, 0.125)),
    ('C', (0.625, 0.125)),
    ('Eb', (0.75, 0.125)),
    ('F#', (0.875, 0.125)),
    ('', (1.0, 0.0))  # rest
]

add_sax(1, sax_notes, sax_notes)

# Normalize the audio
audio = audio / np.max(np.abs(audio)) if np.max(np.abs(audio)) != 0 else audio

# Play the sound
sd.play(audio, SAMPLE_RATE)
sd.wait()

# Save to file
write('intro.wav', SAMPLE_RATE, audio)
print("Intro saved to 'intro.wav'")
