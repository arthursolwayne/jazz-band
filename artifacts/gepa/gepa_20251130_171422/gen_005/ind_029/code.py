
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Parameters
sample_rate = 44100
duration = 6.0  # 6 seconds for 4 bars
total_samples = int(sample_rate * duration)
buffer_size = 1024
channels = 1

# Key: D Major
# Scale degrees: D (0), E (2), F# (4), G (5), A (7), B (9), C# (11)

# Frequencies for D Major (approximate for tuning purposes)
# D = 293.66, E = 329.63, F# = 369.99, G = 392.00, A = 440.00, B = 493.88, C# = 554.37

# Time signature: 4/4
# Tempo: 160 BPM
# Each beat is 0.375 seconds
# Each bar is 1.5 seconds
# 4 bars total = 6 seconds

# Bar 1: Drums only - tight, precise, anticipation
# Bar 2-4: Full band, melody on tenor sax, bass walking, piano comping, drums driving

def generate_sine_tone(frequency, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    waveform = 0.5 * np.sin(2 * np.pi * frequency * t)
    return waveform

def generate_drums(bar_number, sample_rate):
    # Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on eighths
    # Bar 2-4: Same pattern, but with more energy
    bar_length = 1.5
    beat = 0.375
    samples_per_beat = int(sample_rate * beat)
    
    if bar_number == 1:
        volume = 0.3
    else:
        volume = 0.5

    # Kick on 1 and 3
    kick = generate_sine_tone(60, beat, sample_rate)
    kick = np.tile(kick, 2)
    kick = np.pad(kick, (0, int(sample_rate * bar_length) - len(kick)), 'constant')
    
    # Snare on 2 and 4
    snare = generate_sine_tone(120, beat, sample_rate)
    snare = np.tile(snare, 2)
    snare = np.pad(snare, (0, int(sample_rate * bar_length) - len(snare)), 'constant')
    
    # Hihat on every eighth
    hihat = generate_sine_tone(300, beat/2, sample_rate)
    hihat = np.tile(hihat, 4)
    hihat = np.pad(hihat, (0, int(sample_rate * bar_length) - len(hihat)), 'constant')
    
    hihat *= 0.3
    kick *= volume
    snare *= volume

    return kick + snare + hihat

def generate_piano(bar_number, sample_rate):
    # Diane's piano: 7th chords, offbeat comping, angry energy
    # Bar 1: No piano
    if bar_number == 1:
        return np.zeros(int(sample_rate * 1.5))
    
    # Bar 2-4: 7th chords on offbeats, playing with tension
    bar_length = 1.5
    beat = 0.375

    # F#7 (F#, A, C#, E) on beat 2 and 4
    # D7 (D, F#, A, C#) on beat 1 and 3
    notes = [369.99, 440.00, 554.37, 493.88]  # F#7
    comping = generate_sine_tone(notes[0], beat/2, sample_rate)
    comping += generate_sine_tone(notes[1], beat/2, sample_rate)
    comping += generate_sine_tone(notes[2], beat/2, sample_rate)
    comping += generate_sine_tone(notes[3], beat/2, sample_rate)
    
    comping = np.tile(comping, 2)  # 2 comping hits per bar
    comping = np.pad(comping, (0, int(sample_rate * bar_length) - len(comping)), 'constant')
    comping *= 0.4
    return comping

def generate_bass(bar_number, sample_rate):
    # Marcus's bass: walking chromatic line, never repeating a note
    if bar_number == 1:
        return np.zeros(int(sample_rate * 1.5))
    
    bar_length = 1.5
    beat = 0.375

    # Chromatic line: D, D#, E, F, F#, G, G#, A, B, C, C#, D (for D key)
    # Walking bass line: D -> D# -> E -> F -> F# -> G -> G# -> A -> B -> C -> C# -> D
    bass_notes = [293.66, 311.13, 329.63, 349.23, 369.99, 392.00, 415.30, 440.00, 493.88, 523.25, 554.37, 587.33]
    bass_line = []
    for note in bass_notes:
        bass_line.append(generate_sine_tone(note, beat, sample_rate))
    bass_line = np.hstack(bass_line)
    bass_line = np.pad(bass_line, (0, int(sample_rate * bar_length) - len(bass_line)), 'constant')
    bass_line *= 0.3
    return bass_line

def generate_tenor_sax(bar_number, sample_rate):
    # Dante's tenor sax: One short, expressive motif
    if bar_number != 2:
        return np.zeros(int(sample_rate * 1.5))
    
    # Motif: D -> A -> F# -> D
    # D (293.66), A (440.00), F# (369.99), D (293.66)
    # Each note for 0.375 seconds
    notes = [293.66, 440.00, 369.99, 293.66]
    motif = []
    for note in notes:
        motif.append(generate_sine_tone(note, 0.375, sample_rate))
    motif = np.hstack(motif)
    motif = np.pad(motif, (0, int(sample_rate * 1.5) - len(motif)), 'constant')
    motif *= 0.6  # Slightly louder
    return motif

def generate_intro():
    audio = np.zeros(total_samples)
    
    for bar in range(1, 5):
        start = int(sample_rate * (bar - 1) * 1.5)
        end = int(sample_rate * bar * 1.5)
        if bar == 1:
            audio[start:end] = generate_drums(bar, sample_rate)
        else:
            # All instruments in
            drums = generate_drums(bar, sample_rate)
            piano = generate_piano(bar, sample_rate)
            bass = generate_bass(bar, sample_rate)
            sax = generate_tenor_sax(bar, sample_rate)
            audio[start:end] = drums + piano + bass + sax

    # Normalize
    audio = audio / np.max(np.abs(audio))
    return audio

def play_audio(audio, sample_rate):
    sd.play(audio, sample_rate)
    sd.wait()

def save_audio(audio, sample_rate, filename="jazz_intro.wav"):
    write(filename, sample_rate, audio.astype(np.float32))

# Generate and play the intro
intro_audio = generate_intro()
play_audio(intro_audio, sample_rate)
save_audio(intro_audio, sample_rate)
