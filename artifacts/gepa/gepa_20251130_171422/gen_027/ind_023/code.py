
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write

# Parameters
sample_rate = 44100
duration = 6.0  # 6 seconds
num_samples = int(sample_rate * duration)
fs = 160.0  # 160 BPM
tempo = 60.0 / fs  # seconds per beat
bar_length = 4 * tempo  # seconds per bar
sample_length = int(sample_rate * bar_length)

# Frequencies
Fm = 17.32  # Fm (F minor) tonic frequency (approximated for harmonic context)
Cm = 26.0  # Cm (chromatic approach)
Ab = 41.20  # Ab (7th degree of Fm)
G = 39.20  # G (chromatic approach)
D = 58.27  # D (chromatic approach)
E = 65.41  # E (chromatic approach)
Bb = 23.12  # Bb (chromatic approach)

# Time array
t = np.linspace(0, duration, num_samples, False)

# Initialize audio signal
audio = np.zeros(num_samples)

# Bar 1: Little Ray (drums)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def play_drums(bar_length, sample_rate):
    kick_times = [0, 0.5]  # 1 and 3
    snare_times = [0.25, 0.75]  # 2 and 4
    hihat_times = np.arange(0, bar_length, 0.125)  # every 8th note

    kick = np.zeros(num_samples)
    for t_kick in kick_times:
        kick[int(t_kick * sample_rate)] = 0.8

    snare = np.zeros(num_samples)
    for t_snare in snare_times:
        snare[int(t_snare * sample_rate)] = 0.6

    hihat = np.zeros(num_samples)
    for t_hihat in hihat_times:
        hihat[int(t_hihat * sample_rate)] = 0.3

    return kick + snare + hihat

# Bar 1: Drums only
drum_part = play_drums(bar_length, sample_rate)
audio[:sample_length] += drum_part

# Bar 2-4: Full ensemble
# Marcus (bass): Walking line, chromatic approaches
def bass_line(bar_length, sample_rate):
    # Walking line in Fm: F, Gb, Ab, A, Bb, B, C, Db, etc.
    bass_notes = [Fm, Cm, Ab, G, D, E, Bb, D]
    durations = [tempo / 8] * 8
    bass = np.zeros(num_samples)
    for i, freq in enumerate(bass_notes):
        start = int(i * durations[i] * sample_rate)
        end = int((i + 1) * durations[i] * sample_rate)
        bass[start:end] = np.sin(2 * np.pi * freq * t[start:end])
    return bass

# Diane (piano): 7th chords on 2 and 4
def piano_part(bar_length, sample_rate):
    # Fm7 on beat 2, Ab7 on beat 4
    Fm7 = [Fm, Ab, C, Db]
    Ab7 = [Ab, Bb, Db, Eb]
    chord_durations = [tempo / 2, tempo / 2]
    piano = np.zeros(num_samples)
    for i, chord in enumerate([Fm7, Ab7]):
        start = int((i + 1) * tempo / 2 * sample_rate)
        end = int((i + 2) * tempo / 2 * sample_rate)
        for freq in chord:
            piano[start:end] += np.sin(2 * np.pi * freq * t[start:end])
    return piano

# You (tenor sax): Short motif, start it, leave it hanging
def sax_part(bar_length, sample_rate):
    # Motif: Fm - Ab - Bb - D
    notes = [Fm, Ab, Bb, D]
    durations = [tempo / 4, tempo / 4, tempo / 4, tempo / 4]
    sax = np.zeros(num_samples)
    for i, freq in enumerate(notes):
        start = int(i * durations[i] * sample_rate)
        end = int((i + 1) * durations[i] * sample_rate)
        sax[start:end] = np.sin(2 * np.pi * freq * t[start:end])
    return sax

# Add parts for bars 2-4
bass = bass_line(bar_length, sample_rate)
piano = piano_part(bar_length, sample_rate)
sax = sax_part(bar_length, sample_rate)

audio[sample_length:] += bass + piano + sax

# Normalize and play
audio = audio / np.max(np.abs(audio))
sd.play(audio, sample_rate)
sd.wait()

# Save as WAV
write("jazz_intro.wav", sample_rate, audio.astype(np.float32))
