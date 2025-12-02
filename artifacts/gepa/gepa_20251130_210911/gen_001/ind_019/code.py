
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Parameters
sample_rate = 44100
duration = 6.0  # 6 seconds
num_samples = int(duration * sample_rate)
fs = sample_rate
bpm = 160
beat_duration = 60.0 / bpm  # seconds per beat
bar_duration = beat_duration * 4  # 4 beats per bar
note_duration = beat_duration / 4  # 16th note

# Define key: Dm (D Dorian)
# Dm scale: D, E, F, G, A, Bb, C
# Chords: Dm7, G7, Cm7, F7 (if modulating, but we stick to Dm)
# We're in Dm, no modulation.

# Tuning: A4 = 440Hz
note_freqs = {
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'Bb': 466.16,
    'C': 523.25
}

# Bar 1: Little Ray (drums)
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
def generate_bar1():
    samples = np.zeros(num_samples)
    beat = 0
    for i in range(0, num_samples, int(beat_duration * sample_rate)):
        tick = beat % 4
        if tick == 0 or tick == 2:
            # Kick on 1 and 3
            samples[i:i+int(0.05*sample_rate)] += 0.5 * np.sin(2 * np.pi * 60 * np.linspace(0, 1, int(0.05*sample_rate)))
        if tick == 1 or tick == 3:
            # Snare on 2 and 4
            samples[i:i+int(0.05*sample_rate)] += 0.5 * np.sin(2 * np.pi * 150 * np.linspace(0, 1, int(0.05*sample_rate)))
        # Hi-Hat on every 8th
        if tick % 2 == 0:
            samples[i:i+int(0.025*sample_rate)] += 0.1 * np.sin(2 * np.pi * 1000 * np.linspace(0, 1, int(0.025*sample_rate)))
        beat += 1
    return samples

# Bar 2-4: Full band
# - Marcus: Walking bass line in Dm, chromatic approach
# - Diane: 7th chords, comp on 2 and 4
# - Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
# - You: Tenor sax, motif: D -> E -> F -> G (but leave it hanging on F)

def generate_bar2_4():
    samples = np.zeros(num_samples)
    
    # Marcus: Walking bass line in Dm
    # Chromatic approach on 2 and 4 (1 and 3 are root or 5)
    # Dm: D, F, A
    bass_notes = [note_freqs['D'], note_freqs['F'], note_freqs['A'], note_freqs['E'], note_freqs['F'], note_freqs['A'], note_freqs['Bb'], note_freqs['A']]
    for i, note in enumerate(bass_notes):
        start = int(i * beat_duration * sample_rate)
        samples[start:start+int(0.25*sample_rate)] += 0.2 * np.sin(2 * np.pi * note * np.linspace(0, 1, int(0.25*sample_rate)))

    # Diane: 7th chords, comp on 2 and 4
    chord_freqs = {
        'Dm7': [note_freqs['D'], note_freqs['F'], note_freqs['A'], note_freqs['C']],
        'G7': [note_freqs['G'], note_freqs['B'], note_freqs['D'], note_freqs['F']],
        'Cm7': [note_freqs['C'], note_freqs['Eb'], note_freqs['G'], note_freqs['Bb']],
        'F7': [note_freqs['F'], note_freqs['A'], note_freqs['C'], note_freqs['Eb']]
    }
    for beat in range(4):
        pos = int(beat * beat_duration * sample_rate)
        if beat % 2 == 1:  # Comp on 2 and 4
            chord = chord_freqs['Dm7'] if beat == 1 else chord_freqs['G7']
            for note in chord:
                samples[pos:pos+int(0.25*sample_rate)] += 0.1 * np.sin(2 * np.pi * note * np.linspace(0, 1, int(0.25*sample_rate)))

    # Little Ray: same as bar 1
    for i in range(0, num_samples, int(beat_duration * sample_rate)):
        tick = (i // (int(beat_duration * sample_rate))) % 4
        if tick == 0 or tick == 2:
            # Kick
            samples[i:i+int(0.05*sample_rate)] += 0.5 * np.sin(2 * np.pi * 60 * np.linspace(0, 1, int(0.05*sample_rate)))
        if tick == 1 or tick == 3:
            # Snare
            samples[i:i+int(0.05*sample_rate)] += 0.5 * np.sin(2 * np.pi * 150 * np.linspace(0, 1, int(0.05*sample_rate)))
        # Hi-Hat on every 8th
        if tick % 2 == 0:
            samples[i:i+int(0.025*sample_rate)] += 0.1 * np.sin(2 * np.pi * 1000 * np.linspace(0, 1, int(0.025*sample_rate)))

    # You: Tenor sax motif
    # D -> E -> F -> G -> (leave on F)
    notes = [note_freqs['D'], note_freqs['E'], note_freqs['F'], note_freqs['G']]
    for i, note in enumerate(notes):
        start = int((i * note_duration) * sample_rate)
        if i < 3:  # Play first 3 notes
            samples[start:start+int(note_duration*sample_rate)] += 0.3 * np.sin(2 * np.pi * note * np.linspace(0, 1, int(note_duration*sample_rate)))
        else:  # Leave on F
            samples[start:start+int(note_duration*sample_rate)] += 0.3 * np.sin(2 * np.pi * note_freqs['F'] * np.linspace(0, 1, int(note_duration*sample_rate)))
    
    return samples

# Combine the bars
intro = generate_bar1()[:int(bar_duration * sample_rate)]  # First bar
intro = np.concatenate((intro, generate_bar2_4()))  # Bars 2-4

# Normalize
intro = intro / np.max(np.abs(intro))

# Save as WAV file
write('jazz_intro.wav', fs, intro.astype(np.float32))

# Play the sound
sd.play(intro, fs)
time.sleep(duration)
sd.stop()

print("Intro saved as 'jazz_intro.wav' and played.")
