
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Parameters
SAMPLE_RATE = 44100
DURATION = 6.0  # 6 seconds for 4 bars
BPM = 160
BAR_DURATION = DURATION / 4  # 1.5 seconds per bar
BEAT_DURATION = BAR_DURATION / 4  # 0.375 seconds per beat

# Key: F major
F_MAJOR_SCALE = [69, 71, 72, 74, 76, 77, 79]  # MIDI notes for F major (F, G, A, Bb, B, C, D)
F_MAJOR_INTERVALS = [0, 2, 3, 5, 7, 8, 10]  # Intervals in semitones from F

# Frequencies for each instrument
def get_frequency(note):
    return 440 * (2 ** ((note - 69) / 12))

# Create a silence
def silence(duration):
    return np.zeros(int(duration * SAMPLE_RATE), dtype=np.float32)

# Create a sine wave
def sine_wave(freq, duration, amplitude=0.5):
    t = np.linspace(0, duration, int(duration * SAMPLE_RATE), False)
    return amplitude * np.sin(2 * np.pi * freq * t)

# Create a percussive click
def click(duration):
    t = np.linspace(0, duration, int(duration * SAMPLE_RATE), False)
    return np.sin(2 * np.pi * 1000 * t) * np.exp(-t * 1000)

# Create a walking bass line (Marcus)
def walking_bass_line(num_beats):
    notes = [72, 74, 76, 77]  # C, D, E, F
    line = []
    for _ in range(num_beats):
        note = notes[_ % len(notes)]
        line.append(sine_wave(get_frequency(note), BEAT_DURATION/2, 0.1))
    return np.concatenate(line)

# Create piano comp (Diane) - 7th chords on 2 and 4
def piano_comp(num_beats):
    chords = [
        [69, 76, 77, 81],  # F7 (F, A, Bb, D)
        [71, 78, 79, 83],  # G7 (G, B, C, E)
    ]
    comp = silence(BAR_DURATION)
    for beat in range(num_beats):
        if beat % 2 == 1:  # on 2 and 4
            chord = chords[beat % 2]
            for note in chord:
                comp += sine_wave(get_frequency(note), BEAT_DURATION/2, 0.05)
    return comp

# Create drum pattern (Little Ray)
def drum_pattern(num_beats):
    kick = click(BEAT_DURATION/2)
    snare = click(BEAT_DURATION/2)
    hihat = sine_wave(1000, BEAT_DURATION/2, 0.1)

    pattern = silence(BAR_DURATION)
    for beat in range(num_beats):
        if beat % 2 == 0:  # Kicks on 1 and 3
            pattern += kick
        if beat % 2 == 1:  # Snares on 2 and 4
            pattern += snare
        pattern += hihat
    return pattern

# Create tenor sax melody (Dante)
def sax_melody():
    # Your motif: F (69) -> Bb (74) -> C (72) -> F (69) -> rest
    notes = [69, 74, 72, 69]
    durations = [BEAT_DURATION * 0.75, BEAT_DURATION * 0.5, BEAT_DURATION * 0.5, BEAT_DURATION * 0.5]
    melody = silence(BAR_DURATION)
    for i, note in enumerate(notes):
        melody += sine_wave(get_frequency(note), durations[i], 0.6)
    return melody

# BAR 1: Little Ray alone
bar1 = drum_pattern(4)

# BAR 2: All in
bar2 = (
    walking_bass_line(4) +
    piano_comp(4) +
    drum_pattern(4) +
    sax_melody()
)

# BAR 3: All in
bar3 = (
    walking_bass_line(4) +
    piano_comp(4) +
    drum_pattern(4) +
    sax_melody()
)

# BAR 4: All in
bar4 = (
    walking_bass_line(4) +
    piano_comp(4) +
    drum_pattern(4) +
    sax_melody()
)

# Combine all bars
intro = np.concatenate([bar1, bar2, bar3, bar4])

# Normalize and convert to 16-bit
intro = intro / np.max(np.abs(intro))
intro = np.int16(intro * 32767)

# Write to file
write("jazz_intro.wav", SAMPLE_RATE, intro)

# Play it (if you want)
# sd.play(intro, SAMPLE_RATE)
# sd.wait()

print("Intro written to 'jazz_intro.wav'. Time to make Wayne lean forward.")
