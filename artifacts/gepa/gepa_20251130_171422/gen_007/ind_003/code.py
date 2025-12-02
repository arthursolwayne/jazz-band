
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import librosa

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # seconds
BPM = 160
BEAT = 60 / BPM  # seconds per beat
BAR_DURATION = 4 * BEAT  # 4 beats per bar
TOTAL_SAMPLES = int(SAMPLE_RATE * DURATION)

# Initialize audio arrays
drums = np.zeros(TOTAL_SAMPLES)
bass = np.zeros(TOTAL_SAMPLES)
piano = np.zeros(TOTAL_SAMPLES)
sax = np.zeros(TOTAL_SAMPLES)

# Helper functions
def generate_tone(freq, duration, sample_rate, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave

def map_midi_to_freq(midi):
    return 440 * (2 ** ((midi - 69) / 12))

# Bar 1: Drums (tension and anticipation)
# Open-ended rhythms, avoid predictable patterns
# Kick on 3, snare on 2 and 4, hihat on 6th and 8th notes

# Bar 1: 0 - 1.5 seconds
kick_time = 1.125  # 3rd beat (1.5s bar)
snare_time = [0.75, 1.5]  # 2nd and 4th beats
hihat_time = [0.375, 0.75, 1.125, 1.5]  # 6th and 8th notes

for t in [kick_time]:
    start_idx = int(t * SAMPLE_RATE)
    drums[start_idx:start_idx + 100] += generate_tone(82.41, 0.1, SAMPLE_RATE, 0.7)

for t in snare_time:
    start_idx = int(t * SAMPLE_RATE)
    drums[start_idx:start_idx + 100] += generate_tone(185.00, 0.1, SAMPLE_RATE, 0.6)

for t in hihat_time:
    start_idx = int(t * SAMPLE_RATE)
    drums[start_idx:start_idx + 100] += generate_tone(1550.0, 0.05, SAMPLE_RATE, 0.3)

# Bar 2-4: Everyone in

# Bass (chromatic line, walking in Dm)
# Dm chord: D - F - A - C
# Chromatic approach to each note

# Bar 2: Dm7 (D, F, A, C)
note_d = map_midi_to_freq(62)
note_f = map_midi_to_freq(64)
note_a = map_midi_to_freq(67)
note_c = map_midi_to_freq(60)

# One beat per note, chromatic line from B to D
chromatic_line = [map_midi_to_freq(61), map_midi_to_freq(62), map_midi_to_freq(63), map_midi_to_freq(62)]

for i, note in enumerate(chromatic_line):
    start_time = 1.5 + i * BEAT
    start_idx = int(start_time * SAMPLE_RATE)
    bass[start_idx:start_idx + 100] += generate_tone(note, 0.1, SAMPLE_RATE, 0.5)

# Bar 3: Chromatic approach to F
chromatic_line = [map_midi_to_freq(63), map_midi_to_freq(64), map_midi_to_freq(65), map_midi_to_freq(64)]

for i, note in enumerate(chromatic_line):
    start_time = 1.5 + 1.5 + i * BEAT
    start_idx = int(start_time * SAMPLE_RATE)
    bass[start_idx:start_idx + 100] += generate_tone(note, 0.1, SAMPLE_RATE, 0.5)

# Bar 4: Chromatic approach to A
chromatic_line = [map_midi_to_freq(66), map_midi_to_freq(67), map_midi_to_freq(68), map_midi_to_freq(67)]

for i, note in enumerate(chromatic_line):
    start_time = 1.5 + 3.0 + i * BEAT
    start_idx = int(start_time * SAMPLE_RATE)
    bass[start_idx:start_idx + 100] += generate_tone(note, 0.1, SAMPLE_RATE, 0.5)

# Piano: 7th chords on 2 and 4, supportive, avoiding sax
# Dm7: D, F, A, C
# Chord on beat 2 and 4 of bars 2-4

def play_seventh_chord(root, duration, sample_rate, amplitude=0.3):
    freqs = [root, root + 5, root + 9, root + 10]  # Root, 3rd, 5th, 7th
    chord = np.zeros(int(duration * sample_rate))
    for f in freqs:
        chord += generate_tone(f, duration, sample_rate, amplitude)
    return chord

# Bar 2: Chord on beat 2 (0.75s into bar)
chord_start = 1.5 + 0.75
chord = play_seventh_chord(map_midi_to_freq(62), 0.1, SAMPLE_RATE, 0.3)
start_idx = int(chord_start * SAMPLE_RATE)
piano[start_idx:start_idx + len(chord)] += chord

# Bar 3: Chord on beat 2 (0.75s into bar)
chord_start = 1.5 + 1.5 + 0.75
chord = play_seventh_chord(map_midi_to_freq(62), 0.1, SAMPLE_RATE, 0.3)
start_idx = int(chord_start * SAMPLE_RATE)
piano[start_idx:start_idx + len(chord)] += chord

# Bar 4: Chord on beat 2 (0.75s into bar)
chord_start = 1.5 + 3.0 + 0.75
chord = play_seventh_chord(map_midi_to_freq(62), 0.1, SAMPLE_RATE, 0.3)
start_idx = int(chord_start * SAMPLE_RATE)
piano[start_idx:start_idx + len(chord)] += chord

# Saxophone: Sparse, singable motif — D to F to A to C, with space
# Melody: D (62) - F (64) - A (67) - C (60), with a pause after the first note

note_d = map_midi_to_freq(62)
note_f = map_midi_to_freq(64)
note_a = map_midi_to_freq(67)
note_c = map_midi_to_freq(60)

# Bar 2: D (beat 1)
start_idx = int(1.5 * SAMPLE_RATE)
sax[start_idx:start_idx + 100] += generate_tone(note_d, 0.1, SAMPLE_RATE, 0.5)

# Bar 2: F (beat 2)
start_idx = int(1.5 + 0.75 * SAMPLE_RATE)
sax[start_idx:start_idx + 100] += generate_tone(note_f, 0.1, SAMPLE_RATE, 0.5)

# Bar 3: A (beat 1)
start_idx = int(1.5 + 1.5 * SAMPLE_RATE)
sax[start_idx:start_idx + 100] += generate_tone(note_a, 0.1, SAMPLE_RATE, 0.5)

# Bar 4: C (beat 1), leaving the last beat open
start_idx = int(1.5 + 3.0 * SAMPLE_RATE)
sax[start_idx:start_idx + 100] += generate_tone(note_c, 0.1, SAMPLE_RATE, 0.5)

# Combine all tracks
mix = sax + piano + bass + drums

# Normalize
max_val = np.max(np.abs(mix))
if max_val > 0:
    mix = mix / max_val * 0.8

# Output to file
write("jazz_intro_4_bar.wav", SAMPLE_RATE, mix.astype(np.float32))

# Play it
sd.play(mix, SAMPLE_RATE)
sd.wait()
