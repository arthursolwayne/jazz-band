
import numpy as np
import soundfile as sf
from scipy.io.wavfile import write
import midiutil

# Set parameters
sample_rate = 44100
duration = 6.0  # 6 seconds for 4 bars at 160 BPM
tempo = 160
time_signature = (4, 4)
key = 'F'  # F major

# Convert tempo to beats per second
bpm_to_bps = tempo / 60
bar_length = 4 * (60 / tempo)  # seconds per bar
beat_length = bar_length / 4  # seconds per beat
note_length = beat_length / 4  # 16th note

# Define the instruments
# 0: Drums (Little Ray)
# 1: Bass (Marcus)
# 2: Piano (Diane)
# 3: Tenor Sax (Dante)

# Generate a mono audio track for each instrument and mix them together

# Drum pattern (Bar 1: Alone, Bar 2-4: Full)
def generate_drums():
    samples = np.zeros(int(sample_rate * duration))
    # Bar 1: Kick on 1, Snare on 3
    kick = 0.5 * np.sin(2 * np.pi * 100 * np.linspace(0, 1, int(sample_rate * beat_length)))
    snare = 0.6 * np.sin(2 * np.pi * 200 * np.linspace(0, 1, int(sample_rate * beat_length)))
    samples[int(beat_length * sample_rate)] += kick
    samples[int(3 * beat_length * sample_rate)] += snare

    # Bar 2: Kick on 1, Snare on 3
    samples[int(beat_length * sample_rate * 4)] += kick
    samples[int(3 * beat_length * sample_rate * 4)] += snare

    # Bar 3: Kick on 1, Snare on 3
    samples[int(beat_length * sample_rate * 8)] += kick
    samples[int(3 * beat_length * sample_rate * 8)] += snare

    # Bar 4: Kick on 1, Snare on 3
    samples[int(beat_length * sample_rate * 12)] += kick
    samples[int(3 * beat_length * sample_rate * 12)] += snare

    # Hihat on every 8th note
    for i in range(1, 13):
        start = i * beat_length * sample_rate
        hihat = 0.2 * np.sin(2 * np.pi * 1200 * np.linspace(0, 1, int(sample_rate * note_length)))
        samples[int(start):int(start + note_length * sample_rate)] += hihat

    return samples

# Bass line (Marcus)
def generate_bass():
    samples = np.zeros(int(sample_rate * duration))
    # Bar 1: Walk F7 chord
    # F7 = F, A, C, E♭
    # Walk down chromatically
    notes = [79, 77, 76, 74, 79, 77, 76, 74]  # F, E♭, D, C, F, E♭, D, C
    for i, note in enumerate(notes):
        start = i * note_length * sample_rate
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.3 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(note_length * sample_rate)))
        samples[int(start):int(start + note_length * sample_rate)] += wave

    # Bar 2: Keep walking
    for i, note in enumerate(notes):
        start = (i + 8) * note_length * sample_rate
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.3 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(note_length * sample_rate)))
        samples[int(start):int(start + note_length * sample_rate)] += wave

    # Bar 3: Walk up chromatically
    notes = [74, 76, 77, 79, 74, 76, 77, 79]  # C, D, E♭, F
    for i, note in enumerate(notes):
        start = (i + 16) * note_length * sample_rate
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.3 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(note_length * sample_rate)))
        samples[int(start):int(start + note_length * sample_rate)] += wave

    # Bar 4: Walk back down
    for i, note in enumerate(notes):
        start = (i + 24) * note_length * sample_rate
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.3 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(note_length * sample_rate)))
        samples[int(start):int(start + note_length * sample_rate)] += wave

    return samples

# Piano chords (Diane)
def generate_piano():
    samples = np.zeros(int(sample_rate * duration))
    # Bar 1: Rest
    pass

    # Bar 2: F7 on 2 and 4
    notes = [79, 77, 76, 74]  # F7
    for i, note in enumerate(notes):
        start = (i + 1) * beat_length * sample_rate  # 2nd beat
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.3 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(beat_length * sample_rate)))
        samples[int(start):int(start + beat_length * sample_rate)] += wave

    # Bar 3: F7 again
    for i, note in enumerate(notes):
        start = (i + 1) * beat_length * sample_rate + 8 * beat_length * sample_rate
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.3 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(beat_length * sample_rate)))
        samples[int(start):int(start + beat_length * sample_rate)] += wave

    # Bar 4: F7
    for i, note in enumerate(notes):
        start = (i + 1) * beat_length * sample_rate + 16 * beat_length * sample_rate
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.3 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(beat_length * sample_rate)))
        samples[int(start):int(start + beat_length * sample_rate)] += wave

    return samples

# Tenor sax melody (Dante)
def generate_tenor():
    samples = np.zeros(int(sample_rate * duration))
    # Bar 1: Rest
    pass

    # Bar 2: Start the motif
    # F (79) on beat 1, G (81) on beat 3, rest on beat 2, F on beat 4
    # Motif: F - G - rest - F
    # Bar 2:
    for i, note in enumerate([79, 81, 79]):
        start = i * beat_length * sample_rate + 4 * beat_length * sample_rate
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.5 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(beat_length * sample_rate)))
        samples[int(start):int(start + beat_length * sample_rate)] += wave

    # Bar 3: Continue motif
    # G - A - rest - G
    for i, note in enumerate([81, 83, 81]):
        start = i * beat_length * sample_rate + 8 * beat_length * sample_rate
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.5 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(beat_length * sample_rate)))
        samples[int(start):int(start + beat_length * sample_rate)] += wave

    # Bar 4: Resolution
    # G - F - rest - F
    for i, note in enumerate([81, 79, 79]):
        start = i * beat_length * sample_rate + 12 * beat_length * sample_rate
        freq = 440 * 2 ** ((note - 69) / 12)
        wave = 0.5 * np.sin(2 * np.pi * freq * np.linspace(0, 1, int(beat_length * sample_rate)))
        samples[int(start):int(start + beat_length * sample_rate)] += wave

    return samples

# Generate tracks
drums = generate_drums()
bass = generate_bass()
piano = generate_piano()
tenor = generate_tenor()

# Mix the tracks
mix = (drums + bass + piano + tenor) / 4.0

# Normalize the mix
max_val = np.max(np.abs(mix))
if max_val > 0:
    mix = mix / max_val * 0.8  # leave some headroom

# Save the file
write("four_bar_intro.wav", sample_rate, mix.astype(np.float32))

print("Generated 4-bar intro in F at 160 BPM. Saved as 'four_bar_intro.wav'.")
