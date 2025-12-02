
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Constants
SAMPLE_RATE = 44100
DURATION = 6.0  # seconds for 4 bars at 160 BPM
TOTAL_FRAMES = int(SAMPLE_RATE * DURATION)
FREQ_F = 349.23  # Frequency of F (concert pitch)
SEMITONE_RATIO = 2 ** (1 / 12)

# Tempo and Timing
BEAT_DURATION = 0.375  # 160 BPM, 60/160 = 0.375s per beat
BAR_DURATION = 1.5  # 4 beats per bar
FREQ_RESOLUTION = 0.001  # For precise frequency control

# Tone generator
def generate_tone(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    tone = np.sin(2 * np.pi * freq * t)
    return tone

# Drum pattern (snare, kick, hihat)
def generate_drum_pattern(sample_rate, duration, kick_on, snare_on, hihat_on):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    kick = np.zeros_like(t)
    snare = np.zeros_like(t)
    hihat = np.zeros_like(t)
    
    for i in kick_on:
        kick[int(i * sample_rate)] = 1.0
    for i in snare_on:
        snare[int(i * sample_rate)] = 1.0
    for i in hihat_on:
        hihat[int(i * sample_rate)] = 1.0
    
    return kick, snare, hihat

# Bass line (chromatic walking)
def generate_bass_line(sample_rate, duration, start_freq, chromatic_steps):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    bass = np.zeros_like(t)
    
    for i, step in enumerate(chromatic_steps):
        freq = start_freq * (SEMITONE_RATIO ** step)
        start = int(i * sample_rate * (duration / len(chromatic_steps)))
        end = int((i + 1) * sample_rate * (duration / len(chromatic_steps)))
        bass[start:end] = generate_tone(freq, duration / len(chromatic_steps), sample_rate)
    
    return bass

# Piano chords (7th chords, comp on 2 and 4)
def generate_piano_chords(sample_rate, duration, chord_freqs, timing):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    piano = np.zeros_like(t)
    
    for chord, times in zip(chord_freqs, timing):
        for time in times:
            start = int(time * sample_rate)
            end = start + int(sample_rate * 0.1)  # 100ms chords
            chord_wave = sum(generate_tone(freq, 0.1, sample_rate) for freq in chord)
            piano[start:end] = chord_wave
    
    return piano

# Saxophone melody (short motif, leave it hanging)
def generate_sax_melody(sample_rate, duration, motif_freqs, motif_durations):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    sax = np.zeros_like(t)
    
    current_time = 0
    for freq, dur in zip(motif_freqs, motif_durations):
        start = int(current_time * sample_rate)
        end = int(current_time * sample_rate + dur * sample_rate)
        sax[start:end] = generate_tone(freq, dur, sample_rate)
        current_time += dur
    
    return sax

# Main composition
def compose_piece():
    # Bar 1: Little Ray alone
    kick_on = [0.0]  # Kick on 1
    snare_on = [0.25]  # Snare on 3
    hihat_on = [0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875]  # Hihat on every eighth
    kick, snare, hihat = generate_drum_pattern(SAMPLE_RATE, BAR_DURATION, kick_on, snare_on, hihat_on)
    
    # Bar 2: Everyone in
    # Bass line: F, Bb, B, C (chromatic walking)
    bass_start_freq = FREQ_F
    chromatic_steps = [0, 1, 2, 3]  # F, F#, G, G# (but we use Bb, B, C for chromatic effect)
    bass_line = generate_bass_line(SAMPLE_RATE, BAR_DURATION * 3, bass_start_freq, chromatic_steps)
    
    # Piano chords: 7th chords on 2 and 4 (F7, Bb7)
    chord_freqs = [
        [FREQ_F, FREQ_F * SEMITONE_RATIO**2, FREQ_F * SEMITONE_RATIO**4, FREQ_F * SEMITONE_RATIO**6],  # F7
        [FREQ_F * SEMITONE_RATIO**2, FREQ_F * SEMITONE_RATIO**4, FREQ_F * SEMITONE_RATIO**6, FREQ_F * SEMITONE_RATIO**8],  # Bb7
    ]
    timing = [0.5, 1.0]  # On 2 and 4
    piano = generate_piano_chords(SAMPLE_RATE, BAR_DURATION * 3, chord_freqs, timing)
    
    # Saxophone motif: F to Bb to C (hanging on the last note)
    motif_freqs = [FREQ_F, FREQ_F * SEMITONE_RATIO**1, FREQ_F * SEMITONE_RATIO**2]
    motif_durations = [0.15, 0.15, 0.3]  # Short, short, lingering
    sax = generate_sax_melody(SAMPLE_RATE, BAR_DURATION * 3, motif_freqs, motif_durations)
    
    # Combine all tracks
    audio = (
        (0.2 * kick) +
        (0.2 * snare) +
        (0.4 * hihat) +
        (0.2 * bass_line) +
        (0.2 * piano) +
        (0.3 * sax)
    )
    
    # Normalize
    audio = audio / np.max(np.abs(audio))
    
    # Play the audio
    sd.play(audio, SAMPLE_RATE)
    sd.wait()
    
    # Save to file
    write("dante_opening.wav", SAMPLE_RATE, audio.astype(np.float32))
    print("Composition saved to 'dante_opening.wav'")

# Run the composition
compose_piece()
