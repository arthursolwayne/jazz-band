
"""
Dante Russo - "The Cellar Intro" (4-bar jazz intro in Fm)
Generated for Wayne Shorter, 2am at The Cellar, Montclair

Time signature: 4/4
Tempo: 160 BPM
Key: F minor
Bar duration: 1.5 seconds
Beat duration: 0.375 seconds
"""

import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Parameters
sample_rate = 44100
duration = 6.0  # 4 bars at 160 BPM = 6 seconds
num_samples = int(duration * sample_rate)
buffer = np.zeros(num_samples, dtype=np.float32)

# Define frequencies for the notes in F minor (F, G, Ab, Bb, C, Db, Eb)
# MIDI note numbers for F3 = 65, G3 = 67, Ab3 = 68, Bb3 = 69, C4 = 72, Db4 = 73, Eb4 = 74
note_frequencies = {
    'F3': 174.61,
    'G3': 196.00,
    'Ab3': 207.65,
    'Bb3': 212.00,
    'C4': 261.63,
    'Db4': 277.18,
    'Eb4': 293.66
}

# Define the motif (Dante's sax line)
# Bar 1 (Ray's intro): Just cymbal swish on beat 1
# Bar 2: Sax plays a simple motif that feels unresolved
# Bar 3: Bass enters with walking line, piano comps
# Bar 4: Sax returns, ends on a lingering note

# Function to generate a sine wave
def generate_sine(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return np.sin(2 * np.pi * freq * t)

# Bar 1: Little Ray - cymbal swish on beat 1
# Simulate cymbal swish with a short high-pitched sine wave
cymbal_freq = 1000.0
cymbal_duration = 0.05
cymbal_start = int(0.375 * sample_rate)  # on beat 1
cymbal = generate_sine(cymbal_freq, cymbal_duration, sample_rate)
buffer[cymbal_start:cymbal_start+len(cymbal)] += cymbal

# Bar 2: Saxophone (Dante) - motif starts
# Simple motif: F3 -> G3 -> Ab3 -> Bb3
# Starts on beat 1, ends on the "and" of beat 4
# Each note is 0.5 seconds long, space between them
motif = []
motif_start = int(0.375 * sample_rate)  # beat 1

for note in ['F3', 'G3', 'Ab3', 'Bb3']:
    note_freq = note_frequencies[note]
    note_duration = 0.5
    note_samples = generate_sine(note_freq, note_duration, sample_rate)
    note_start = motif_start + int((note.index(note) * 0.5) * sample_rate)
    buffer[note_start:note_start+len(note_samples)] += note_samples

# Bar 3: Marcus (Bass) - walking line in Fm
# Fm -> G -> Ab -> Bb -> C -> Db -> Eb -> F
# Bass line: F3 -> G3 -> Ab3 -> Bb3 -> C3 -> Db3 -> Eb3 -> F3
bass_line = ['F3', 'G3', 'Ab3', 'Bb3', 'C3', 'Db3', 'Eb3', 'F3']
bass_freqs = [note_frequencies[note] for note in bass_line]
bass_duration = 0.375  # Each beat is 0.375 seconds

bass_start = int(1.5 * sample_rate)  # start of bar 3 (beat 1 of bar 3)
for i, freq in enumerate(bass_freqs):
    bass_note = generate_sine(freq, bass_duration, sample_rate)
    start = bass_start + int(i * bass_duration * sample_rate)
    buffer[start:start + len(bass_note)] += bass_note

# Bar 3: Diane (Piano) - 7th chords on 2 and 4
# Fm7 -> Bb7 (on beat 2), Fm7 -> Bb7 (on beat 4)
# Use simple 7th chords: F - Ab - Bb - C - F (root, minor 3rd, 5th, 7th)

# Fm7 frequencies: F3, Ab3, Bb3, C4
fm7_freqs = [note_frequencies['F3'], note_frequencies['Ab3'], note_frequencies['Bb3'], note_frequencies['C4']]
# Bb7 frequencies: Bb3, Db4, F4, Ab4
bb7_freqs = [note_frequencies['Bb3'], note_frequencies['Db4'], note_frequencies['F4'], note_frequencies['Ab4']]

# Piano: volume is low, comp on 2 and 4
piano_volume = 0.3

# On beat 2 of bar 3 (second half of bar 3) play Fm7
piano_start = int(1.5 * sample_rate) + int(0.75 * sample_rate)
piano_note = generate_sine(note_frequencies['F3'], 0.1, sample_rate)
piano_note += generate_sine(note_frequencies['Ab3'], 0.1, sample_rate)
piano_note += generate_sine(note_frequencies['Bb3'], 0.1, sample_rate)
piano_note += generate_sine(note_frequencies['C4'], 0.1, sample_rate)
piano_note *= piano_volume
buffer[piano_start:piano_start + len(piano_note)] += piano_note

# On beat 4 of bar 3 (end of bar 3) play Bb7
piano_start = int(1.5 * sample_rate) + int(1.5 * sample_rate)
piano_note = generate_sine(note_frequencies['Bb3'], 0.1, sample_rate)
piano_note += generate_sine(note_frequencies['Db4'], 0.1, sample_rate)
piano_note += generate_sine(note_frequencies['F4'], 0.1, sample_rate)
piano_note += generate_sine(note_frequencies['Ab4'], 0.1, sample_rate)
piano_note *= piano_volume
buffer[piano_start:piano_start + len(piano_note)] += piano_note

# Bar 4: Saxophone returns, ends on a lingering note
# F3, G3, Ab3, Bb3 again, but ends with a space on the last note
# Use a short decay on the Bb3
end_motif = []
end_motif_start = int(1.5 * sample_rate) + int(0.375 * sample_rate)  # on beat 1 of bar 4
for note in ['F3', 'G3', 'Ab3', 'Bb3']:
    note_freq = note_frequencies[note]
    note_duration = 0.5
    note_samples = generate_sine(note_freq, note_duration, sample_rate)
    note_start = end_motif_start + int((note.index(note) * 0.5) * sample_rate)
    buffer[note_start:note_start+len(note_samples)] += note_samples

# Drums: Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: Only cymbal
# Bar 2: Kick on 1, snare on 2, hihat on 1, 2, 3, 4
# Bar 3: Kick on 1, snare on 2, hihat on every eighth
# Bar 4: Kick on 1, snare on 2, hihat on every eighth, with end cymbal on 4

# Kick sound (low sine wave)
kick_freq = 60.0
kick_duration = 0.1
kick_volume = 0.4

# Snare sound (higher sine wave, with a sharp attack)
snare_freq = 200.0
snare_duration = 0.1
snare_volume = 0.3

# Hi-hat (high-pitched sine wave)
hihat_freq = 1200.0
hihat_duration = 0.05
hihat_volume = 0.3

# Bar 2: Kick on 1, snare on 2, hihat on 1, 2, 3, 4
bar2_start = int(0.375 * sample_rate)
bar2_kick = generate_sine(kick_freq, kick_duration, sample_rate)
bar2_kick *= kick_volume
buffer[bar2_start:bar2_start + len(bar2_kick)] += bar2_kick

bar2_snare = generate_sine(snare_freq, snare_duration, sample_rate)
bar2_snare *= snare_volume
buffer[bar2_start + int(0.375 * sample_rate):bar2_start + int(0.375 * sample_rate) + len(bar2_snare)] += bar2_snare

# Hihat on every eighth
for i in range(0, 4):
    hihat_start = bar2_start + int(i * 0.1875 * sample_rate)
    hihat = generate_sine(hihat_freq, hihat_duration, sample_rate)
    hihat *= hihat_volume
    buffer[hihat_start:hihat_start + len(hihat)] += hihat

# Bar 3: Kick on 1, snare on 2, hihat on every eighth
bar3_start = int(1.5 * sample_rate)
bar3_kick = generate_sine(kick_freq, kick_duration, sample_rate)
bar3_kick *= kick_volume
buffer[bar3_start:bar3_start + len(bar3_kick)] += bar3_kick

bar3_snare = generate_sine(snare_freq, snare_duration, sample_rate)
bar3_snare *= snare_volume
buffer[bar3_start + int(0.375 * sample_rate):bar3_start + int(0.375 * sample_rate) + len(bar3_snare)] += bar3_snare

for i in range(0, 4):
    hihat_start = bar3_start + int(i * 0.1875 * sample_rate)
    hihat = generate_sine(hihat_freq, hihat_duration, sample_rate)
    hihat *= hihat_volume
    buffer[hihat_start:hihat_start + len(hihat)] += hihat

# Bar 4: Kick on 1, snare on 2, hihat on every eighth, cymbal on 4
bar4_start = int(3.0 * sample_rate)
bar4_kick = generate_sine(kick_freq, kick_duration, sample_rate)
bar4_kick *= kick_volume
buffer[bar4_start:bar4_start + len(bar4_kick)] += bar4_kick

bar4_snare = generate_sine(snare_freq, snare_duration, sample_rate)
bar4_snare *= snare_volume
buffer[bar4_start + int(0.375 * sample_rate):bar4_start + int(0.375 * sample_rate) + len(bar4_snare)] += bar4_snare

for i in range(0, 4):
    hihat_start = bar4_start + int(i * 0.1875 * sample_rate)
    hihat = generate_sine(hihat_freq, hihat_duration, sample_rate)
    hihat *= hihat_volume
    buffer[hihat_start:hihat_start + len(hihat)] += hihat

# End cymbal on beat 4 of bar 4
end_cymbal = generate_sine(1000.0, 0.05, sample_rate)
end_cymbal *= 0.3
buffer[bar4_start + int(1.5 * sample_rate):bar4_start + int(1.5 * sample_rate) + len(end_cymbal)] += end_cymbal

# Normalize and play
buffer = np.clip(buffer / np.max(np.abs(buffer)), -1, 1)
sd.play(buffer, sample_rate)
sd.wait()

# Save as WAV
write('the_cellar_intro.wav', sample_rate, buffer)
print("Intro saved to 'the_cellar_intro.wav' — Wayne, lean forward.")
