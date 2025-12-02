
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# Parameters
sample_rate = 44100
duration = 6.0  # seconds
num_samples = int(sample_rate * duration)
BPM = 160
beat = 60.0 / BPM  # seconds per beat
bar_length = beat * 4  # 4 beats per bar
bar_samples = int(sample_rate * bar_length)

# Frequencies and durations
# F minor scale: F, Gb, Ab, A, Bb, C, Db
# We'll use F, Ab, Bb, C, Db as the backbone for the motif

# Define the motif: F - Ab - Bb - C (descending 3rd, then 2nd, then 2nd)
# This is a short, haunting motif – a question in the dark
motif_freqs = [174.61, 116.54, 92.50, 130.81]  # F, Ab, Bb, C
note_durations = [0.3, 0.3, 0.3, 0.3]  # One note per beat

# Synth function (simple sine wave)
def generate_sine(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    return wave

# Drum pattern (snare on 2 and 4, kick on 1 and 3)
def generate_drums(bar_length, sample_rate):
    samples = np.zeros(int(sample_rate * bar_length))
    # Kick on beat 1 and 3
    kick_pos = [0.0, 1.5]
    for pos in kick_pos:
        start = int(pos * sample_rate)
        samples[start:start+100] += 0.5 * np.sin(2 * np.pi * 60 * np.linspace(0, 1, 100))
    # Snare on beat 2 and 4
    snare_pos = [0.75, 2.25]
    for pos in snare_pos:
        start = int(pos * sample_rate)
        samples[start:start+50] += 0.7 * np.sin(2 * np.pi * 200 * np.linspace(0, 1, 50))
    # Hi-hat on every eighth note
    for i in range(8):
        pos = i * (bar_length / 8)
        start = int(pos * sample_rate)
        samples[start:start+20] += 0.3 * np.sin(2 * np.pi * 1000 * np.linspace(0, 1, 20))
    return samples

# Bass line: walking line in Fm (chromatic approach on the 3rd and 7th)
def generate_bass(bar_length, sample_rate):
    # Fm scale: F, Gb, Ab, A, Bb, C, Db
    # Walking line: F - Gb - Ab - A - Bb - C - Db - F
    # Add chromatic approaches on Ab and Bb
    bass_notes = [174.61, 155.56, 116.54, 110.00, 92.50, 130.81, 123.47, 174.61]
    durations = [0.5]*len(bass_notes)
    samples = np.zeros(int(sample_rate * bar_length))
    for i, freq in enumerate(bass_notes):
        start = int(i * (bar_length / len(bass_notes)) * sample_rate)  # Even spacing
        duration = durations[i] * sample_rate
        wave = generate_sine(freq, durations[i], sample_rate)
        samples[start:start+int(duration)] += wave
    return samples

# Piano: 7th chords on 2 and 4, comping with rich voicings
def generate_piano(bar_length, sample_rate):
    # F7 (F, A, C, Eb) - on beat 2
    # Db7 (Db, F, Ab, Bb) - on beat 4
    # Each chord is a 0.5s chord sound
    samples = np.zeros(int(sample_rate * bar_length))
    # F7 chord: F, A, C, Eb
    f7 = [174.61, 220.00, 130.81, 155.56]
    # Db7 chord: Db, F, Ab, Bb
    db7 = [123.47, 174.61, 116.54, 92.50]
    # Play F7 at 0.75s, db7 at 2.25s
    for freq in f7:
        start = int(0.75 * sample_rate)
        wave = generate_sine(freq, 0.5, sample_rate)
        samples[start:start+int(0.5*sample_rate)] += wave
    for freq in db7:
        start = int(2.25 * sample_rate)
        wave = generate_sine(freq, 0.5, sample_rate)
        samples[start:start+int(0.5*sample_rate)] += wave
    return samples

# Saxophone motif: F -> Ab -> Bb -> C (one note per beat, sustained)
def generate_sax(bar_length, sample_rate):
    samples = np.zeros(int(sample_rate * bar_length))
    for i, freq in enumerate(motif_freqs):
        start = int(i * (bar_length / len(motif_freqs)) * sample_rate)
        duration = bar_length / len(motif_freqs)
        wave = generate_sine(freq, duration, sample_rate)
        samples[start:start+int(duration*sample_rate)] += wave
    # Add some vibrato at the end to make it haunting
    vibrato = 0.1 * np.sin(2 * np.pi * 5 * np.linspace(0, 1, len(samples)))
    samples += vibrato
    return samples

# Generate all tracks
drums = generate_drums(bar_length, sample_rate)
bass = generate_bass(bar_length, sample_rate)
piano = generate_piano(bar_length, sample_rate)
sax = generate_sax(bar_length, sample_rate)

# Combine all tracks
mix = (drums + bass + piano + sax) / 4.0  # Normalize

# Normalize to -1 to 1
mix = mix / np.max(np.abs(mix))

# Save to WAV file
write("dante_intro.wav", sample_rate, (mix * 32767).astype(np.int16))

# Play the audio
sd.play(mix, sample_rate)
sd.wait()

print("Intro composed and played. It's a question in the dark — and it's for Wayne.")
