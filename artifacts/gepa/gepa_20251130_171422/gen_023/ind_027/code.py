
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Parameters
sample_rate = 44100
duration_per_bar = 1.5  # seconds per bar
total_duration = 6.0  # 4 bars at 1.5 seconds each
channels = 1
volume = 0.5

# Frequencies for Dm7: D, F, A, C
# Frequencies in Hz
d = 293.66  # D4
f = 349.23  # F4
a = 440.00  # A4
c = 261.63  # C4

# Time array for the entire piece
t = np.linspace(0, total_duration, int(total_duration * sample_rate), False)

# Initialize audio signal
audio = np.zeros(len(t))

# Function to generate a sine wave
def sine_wave(freq, duration, phase_offset=0):
    return np.sin(2 * np.pi * freq * t + phase_offset)

# BAR 1: Little Ray – solo snare and hihat
# Rhythmic drive, with subtle variation
def bar1():
    # Snare on 2 and 4 (simpler for bar 1)
    snare_beat = 0.5 * 0.375  # offset for snare
    for i in range(0, 160 * 1.5, int(160 * 0.375 * 2)):  # every 2 beats
        snare = sine_wave(200, 0.05, phase_offset=snare_beat)
        audio[i:i+len(snare)] += snare * volume * 0.4  # lower volume for subtlety

    # Hihat on every eighth
    hihat_beat = 0.0
    for i in range(0, int(160 * 1.5), int(160 * 0.125)):
        hihat = sine_wave(4000, 0.01, phase_offset=hihat_beat)
        audio[i:i+len(hihat)] += hihat * volume * 0.3  # high frequency, soft

# BAR 2: Everyone enters – Diane on piano with 7th chords, Marcus walks, you enter with motif
def bar2():
    # Diane: 7th chords on 2 and 4, dynamic contrast
    # Dm7: D, F, A, C
    # Play on 2 and 4 – 2nd and 4th beats
    beat = int(160 * 0.375)
    beat2 = 2 * beat
    beat4 = 4 * beat
    for b in [beat2, beat4]:
        # Random amplitude between 0.3 and 0.6
        amp = np.random.uniform(0.3, 0.6)
        chord = sine_wave(d, 0.05, phase_offset=0.0) * amp
        chord += sine_wave(f, 0.05, phase_offset=0.0) * amp
        chord += sine_wave(a, 0.05, phase_offset=0.0) * amp
        chord += sine_wave(c, 0.05, phase_offset=0.0) * amp
        audio[b:b+len(chord)] += chord * volume

    # Marcus: Walking bass, chromatic approach to D
    # Starts on C#, moves up to D
    # 4 notes per bar
    for i in range(4):
        freq = 277.18  # C#4
        if i == 3:
            freq = d
        note = sine_wave(freq, 0.05, phase_offset=0.05 * i)
        pos = int(i * beat) + beat // 2
        audio[pos:pos+len(note)] += note * volume * 0.3

    # You: Melody on tenor – start the motif
    # One short phrase: D, F, A, rest
    # Dynamic variation: softer on D, stronger on F
    # Start on first beat
    note1 = sine_wave(d, 0.1, phase_offset=0.0) * 0.5
    note2 = sine_wave(f, 0.1, phase_offset=0.0) * 0.6
    note3 = sine_wave(a, 0.1, phase_offset=0.0) * 0.5
    note4 = sine_wave(0, 0.1)  # rest

    audio[0:0+len(note1)] += note1 * volume
    audio[beat:beat+len(note2)] += note2 * volume
    audio[2*beat:2*beat+len(note3)] += note3 * volume
    audio[3*beat:3*beat+len(note4)] += note4 * volume

# BAR 3: Continue the motif, build tension
def bar3():
    # Diane: 7th chords again, slightly louder
    for b in [beat2, beat4]:
        amp = np.random.uniform(0.4, 0.7)
        chord = sine_wave(d, 0.05, phase_offset=0.0) * amp
        chord += sine_wave(f, 0.05, phase_offset=0.0) * amp
        chord += sine_wave(a, 0.05, phase_offset=0.0) * amp
        chord += sine_wave(c, 0.05, phase_offset=0.0) * amp
        audio[b:b+len(chord)] += chord * volume

    # Marcus: Chromatic walk again, starts on A
    for i in range(4):
        if i == 0:
            freq = a
        elif i == 1:
            freq = a + (d - a) * 0.25  # chromatic approach
        elif i == 2:
            freq = a + (d - a) * 0.5
        elif i == 3:
            freq = a + (d - a) * 0.75
        note = sine_wave(freq, 0.05, phase_offset=0.05 * i)
        pos = int(i * beat) + beat // 2
        audio[pos:pos+len(note)] += note * volume * 0.3

    # You: Continue the motif, rest on D
    # D, rest, F, rest
    note1 = sine_wave(d, 0.1, phase_offset=0.0) * 0.5
    note2 = sine_wave(0, 0.1)  # rest
    note3 = sine_wave(f, 0.1, phase_offset=0.0) * 0.6
    note4 = sine_wave(0, 0.1)  # rest

    audio[0:0+len(note1)] += note1 * volume
    audio[beat:beat+len(note2)] += note2 * volume
    audio[2*beat:2*beat+len(note3)] += note3 * volume
    audio[3*beat:3*beat+len(note4)] += note4 * volume

# BAR 4: Finish the motif – answer the question
def bar4():
    # Diane: 7th chords again, dynamic contrast
    for b in [beat2, beat4]:
        amp = np.random.uniform(0.5, 0.8)
        chord = sine_wave(d, 0.05, phase_offset=0.0) * amp
        chord += sine_wave(f, 0.05, phase_offset=0.0) * amp
        chord += sine_wave(a, 0.05, phase_offset=0.0) * amp
        chord += sine_wave(c, 0.05, phase_offset=0.0) * amp
        audio[b:b+len(chord)] += chord * volume

    # Marcus: Chromatic walk back down
    for i in range(4):
        if i == 0:
            freq = a + (d - a) * 0.75
        elif i == 1:
            freq = a + (d - a) * 0.5
        elif i == 2:
            freq = a + (d - a) * 0.25
        elif i == 3:
            freq = a
        note = sine_wave(freq, 0.05, phase_offset=0.05 * i)
        pos = int(i * beat) + beat // 2
        audio[pos:pos+len(note)] += note * volume * 0.3

    # You: Finish the motif
    # A, rest, D, D
    note1 = sine_wave(a, 0.1, phase_offset=0.0) * 0.5
    note2 = sine_wave(0, 0.1)  # rest
    note3 = sine_wave(d, 0.1, phase_offset=0.0) * 0.6
    note4 = sine_wave(d, 0.1, phase_offset=0.0) * 0.5

    audio[0:0+len(note1)] += note1 * volume
    audio[beat:beat+len(note2)] += note2 * volume
    audio[2*beat:2*beat+len(note3)] += note3 * volume
    audio[3*beat:3*beat+len(note4)] += note4 * volume

# BAR 1
bar1()

# BAR 2
bar2()

# BAR 3
bar3()

# BAR 4
bar4()

# Normalize to prevent clipping
audio = audio / np.max(np.abs(audio))

# Export as WAV
write("jazz_intro.wav", sample_rate, audio.astype(np.float32))

# Play the audio
sd.play(audio, sample_rate)
time.sleep(total_duration)
sd.stop()

print("Jazz intro generated and played. Wayne is listening.")
