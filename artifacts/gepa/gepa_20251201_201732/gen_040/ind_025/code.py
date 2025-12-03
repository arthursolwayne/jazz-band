
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # seconds
BPM = 160
BEATS_PER_BAR = 4
NOTES_PER_BAR = 4  # 4/4 time
BAR_DURATION = (60.0 / BPM) * BEATS_PER_BAR  # 1.5 seconds per bar
SAMPLES_PER_BAR = int(SAMPLE_RATE * BAR_DURATION)
SAMPLES_PER_BEAT = int(SAMPLE_RATE * (60.0 / BPM))
SAMPLES_PER_NOTE = int(SAMPLE_RATE * (60.0 / BPM) / NOTES_PER_BAR)  # 1.5 / 4 = 0.375s per note

# Key: D minor (D, Eb, F, G, Ab, Bb, C)
# Notes in Hz
note_freqs = {
    'D2': 73.416,
    'Eb2': 77.782,
    'F2': 82.407,
    'G2': 98.0,
    'Ab2': 103.826,
    'Bb2': 116.541,
    'C3': 130.813,
    'D3': 146.832,
    'Eb3': 155.563,
    'F3': 164.814,
    'G3': 196.0,
    'Ab3': 207.652,
    'Bb3': 233.082,
    'C4': 261.626,
    'D4': 293.665,
    'Eb4': 311.127,
    'F4': 329.628,
    'G4': 392.0,
    'Ab4': 415.305,
    'Bb4': 466.164,
    'C5': 523.251,
    'D5': 587.330,
    'Eb5': 622.254,
    'F5': 659.255,
    'G5': 783.991,
}

def generate_sine_wave(freq, duration, sample_rate=SAMPLE_RATE):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    return wave

def generate_envelope(wave, attack=0.05, decay=0.2, sustain=0.5, release=0.1):
    envelope = np.zeros_like(wave)
    attack_samples = int(attack * SAMPLE_RATE)
    decay_samples = int(decay * SAMPLE_RATE)
    sustain_samples = int(sustain * SAMPLE_RATE)
    release_samples = int(release * SAMPLE_RATE)
    
    # Attack
    envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
    # Decay
    envelope[attack_samples:attack_samples+decay_samples] = np.linspace(1, sustain, decay_samples)
    # Sustain
    envelope[attack_samples+decay_samples:attack_samples+decay_samples+sustain_samples] = sustain
    # Release
    envelope[attack_samples+decay_samples+sustain_samples:] = np.linspace(sustain, 0, release_samples)
    return envelope * wave

# Initialize audio buffer
audio = np.zeros(int(SAMPLE_RATE * DURATION))

# ---------------------------
# Bar 1: Little Ray - Rhythm and Tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Build anticipation, use space, let it breathe
# ---------------------------

# Kick on 1 and 3
kick_samples = generate_sine_wave(60, 0.1)  # 60 Hz is sub-bass
kick_attack = 0.02
kick_decay = 0.05
kick_envelope = generate_envelope(kick_samples, kick_attack, kick_decay)

# Snare on 2 and 4
snare_samples = generate_sine_wave(200, 0.1)  # 200 Hz for snare
snare_attack = 0.02
snare_decay = 0.05
snare_envelope = generate_envelope(snare_samples, snare_attack, snare_decay)

# Hihat on every eighth note
hihat_samples = generate_sine_wave(1000, 0.02)  # 1000 Hz for hihat
hihat_envelope = generate_envelope(hihat_samples, 0.01, 0.01)

# Bar 1 timing
bar_1_start = 0
kick_1 = bar_1_start
kick_3 = bar_1_start + int(0.75 * SAMPLE_RATE)  # 3/4 of the bar
snare_2 = bar_1_start + int(0.5 * SAMPLE_RATE)  # 2/4 of the bar
snare_4 = bar_1_start + int(1.0 * SAMPLE_RATE)  # 4/4 of the bar
hihat = bar_1_start + int(0.125 * SAMPLE_RATE)  # 1/8 note increments

for i in range(8):  # 8 eighth notes in a bar
    hihat_pos = bar_1_start + int(i * 0.125 * SAMPLE_RATE)
    audio[hihat_pos:hihat_pos + len(hihat_envelope)] += hihat_envelope

audio[kick_1:kick_1 + len(kick_envelope)] += kick_envelope
audio[kick_3:kick_3 + len(kick_envelope)] += kick_envelope
audio[snare_2:snare_2 + len(snare_envelope)] += snare_envelope
audio[snare_4:snare_4 + len(snare_envelope)] += snare_envelope

# ---------------------------
# Bar 2: Diane (Piano) - Open voicings, different chord each bar
# Resolve on the last note of the bar
# ---------------------------

# Bar 2 chords (Dm7 - G7 - Cm7 - F7)
# Dm7: D, F, A, C
# G7: G, B, D, F
# Cm7: C, Eb, G, Bb
# F7: F, A, C, Eb

def generate_chord(freqs, duration, sample_rate=SAMPLE_RATE):
    waves = []
    for freq in freqs:
        wave = generate_sine_wave(freq, duration)
        envelope = generate_envelope(wave)
        waves.append(envelope)
    return sum(waves)

# Dm7
Dm7 = [note_freqs['D3'], note_freqs['F3'], note_freqs['A3'], note_freqs['C4']]
chord_dmin7 = generate_chord(Dm7, 0.15)
chord_dmin7_start = bar_1_start + int(0.5 * SAMPLE_RATE)

# G7
G7 = [note_freqs['G3'], note_freqs['B3'], note_freqs['D4'], note_freqs['F4']]
chord_g7 = generate_chord(G7, 0.15)
chord_g7_start = bar_1_start + int(1.0 * SAMPLE_RATE)

# Cm7
Cm7 = [note_freqs['C4'], note_freqs['Eb4'], note_freqs['G4'], note_freqs['Bb4']]
chord_cm7 = generate_chord(Cm7, 0.15)
chord_cm7_start = bar_1_start + int(1.5 * SAMPLE_RATE)

# F7
F7 = [note_freqs['F4'], note_freqs['A4'], note_freqs['C5'], note_freqs['Eb5']]
chord_f7 = generate_chord(F7, 0.15)
chord_f7_start = bar_1_start + int(2.0 * SAMPLE_RATE)

audio[chord_dmin7_start:chord_dmin7_start + len(chord_dmin7)] += chord_dmin7
audio[chord_g7_start:chord_g7_start + len(chord_g7)] += chord_g7
audio[chord_cm7_start:chord_cm7_start + len(chord_cm7)] += chord_cm7
audio[chord_f7_start:chord_f7_start + len(chord_f7)] += chord_f7

# ---------------------------
# Bar 3: Marcus (Bass) - Walking line (D2-G2, roots and fifths with chromatic approaches)
# ---------------------------

# Walking line in D minor: D2 (root), F2 (minor 3rd), G2 (fifth), Ab2 (chromatic approach)
# One walking note per beat, each with a short attack and decay

bass_notes = [
    note_freqs['D2'],
    note_freqs['F2'],
    note_freqs['G2'],
    note_freqs['Ab2'],
]

for i, note in enumerate(bass_notes):
    start = bar_1_start + int(i * 0.375 * SAMPLE_RATE)
    bass_wave = generate_sine_wave(note, 0.1)
    bass_envelope = generate_envelope(bass_wave, attack=0.01, decay=0.05)
    audio[start:start + len(bass_envelope)] += bass_envelope

# ---------------------------
# Bar 4: You (Tenor Sax) - One short motif, make it sing. Start it, leave it hanging.
# ---------------------------

# Tenor sax motif: D4 (start), F4 (chromatic approach), G4 (resolve), D4 (echo)
# Make it a question, not an answer

motif_notes = [
    note_freqs['D4'],
    note_freqs['F4'],
    note_freqs['G4'],
    note_freqs['D4'],
]

motif_wave = []
for note in motif_notes:
    wave = generate_sine_wave(note, 0.1)
    envelope = generate_envelope(wave, attack=0.01, decay=0.05)
    motif_wave.append(envelope)

motif = sum(motif_wave)
motif_start = bar_1_start + int(2.5 * SAMPLE_RATE)  # Start on the "and" of 1

# Play the first three notes, leave the last one hanging
audio[motif_start:motif_start + len(motif_wave[0]) + len(motif_wave[1]) + len(motif_wave[2])] += motif_wave[0] + motif_wave[1] + motif_wave[2]

# ---------------------------
# Output the audio
# ---------------------------

# Normalize
audio = audio / np.max(np.abs(audio))

# Play the audio
sd.play(audio, SAMPLE_RATE)
sd.wait()

# Save as a WAV file
write('dante_intro.wav', SAMPLE_RATE, audio)
print("Intro saved as 'dante_intro.wav'.")
print("The question is out there. Now it's up to Wayne.")
