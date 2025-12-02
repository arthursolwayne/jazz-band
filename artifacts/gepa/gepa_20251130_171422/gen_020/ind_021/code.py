
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import time

# Parameters
sample_rate = 44100
duration = 6.0  # seconds
bpm = 160
beats_per_bar = 4
total_beats = 4
total_samples = int(sample_rate * duration)

# Create a buffer
buffer = np.zeros(total_samples)

# Utility functions
def note_to_freq(note):
    A4 = 440.0
    # Map note to MIDI pitch (Fm scale: F, Gb, Ab, Bb, B, Db, Eb)
    note_map = {
        'F': 64,  # F3
        'Gb': 65, # Gb3
        'Ab': 66, # Ab3
        'Bb': 67, # Bb3
        'B': 68,  # B3
        'Db': 69, # Db4
        'Eb': 70  # Eb4
    }
    return A4 * (2 ** ((note_map[note] - 69) / 12))

# Function to generate a sine wave tone
def generate_tone(freq, duration, sample_rate, amplitude=0.5):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = amplitude * np.sin(2 * np.pi * freq * t)
    return wave

# Function to apply a filter (simple low-pass for realism)
def low_pass_filter(signal, cutoff_freq, sample_rate, order=4):
    from scipy.signal import butter, lfilter
    nyquist = 0.5 * sample_rate
    normal_cutoff = cutoff_freq / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    y = lfilter(b, a, signal)
    return y

# Function to play a note with duration and offset
def play_note(note, start_time, duration, amp=0.3):
    freq = note_to_freq(note)
    tone = generate_tone(freq, duration, sample_rate, amp)
    tone = low_pass_filter(tone, 5000, sample_rate)
    start_index = int(start_time * sample_rate)
    end_index = start_index + len(tone)
    buffer[start_index:end_index] += tone

# Function to play a chord (stacked third intervals)
def play_chord(chord_notes, start_time, duration, amp=0.3, detune=0.05):
    tones = []
    for note in chord_notes:
        freq = note_to_freq(note)
        detuned_freq = freq * (1 + (np.random.rand() - 0.5) * detune)
        tone = generate_tone(detuned_freq, duration, sample_rate, amp)
        tone = low_pass_filter(tone, 5000, sample_rate)
        tones.append(tone)
    mixed = np.sum(tones, axis=0)
    start_index = int(start_time * sample_rate)
    end_index = start_index + len(mixed)
    buffer[start_index:end_index] += mixed

# Function to play a drum hit (kick, snare, hihat)
def play_drums(drums, start_time, duration, amp=0.5):
    if 'kick' in drums:
        kick = generate_tone(60, duration, sample_rate, amp)
        kick = low_pass_filter(kick, 200, sample_rate)
        start_index = int(start_time * sample_rate)
        buffer[start_index:start_index + len(kick)] += kick
    if 'snare' in drums:
        # Snare is a burst of noise
        noise = np.random.normal(0, 0.1, int(duration * sample_rate))
        noise = low_pass_filter(noise, 2000, sample_rate)
        start_index = int(start_time * sample_rate)
        buffer[start_index:start_index + len(noise)] += noise * amp
    if 'hihat' in drums:
        # Hihat is high-pitched white noise
        noise = np.random.normal(0, 0.05, int(duration * sample_rate))
        noise = low_pass_filter(noise, 6000, sample_rate)
        start_index = int(start_time * sample_rate)
        buffer[start_index:start_index + len(noise)] += noise * amp

# Tempo based timing
beat_length = 60.0 / bpm  # seconds per beat
bar_length = beat_length * beats_per_bar

# Bar 1: Drums only
play_drums({'kick': True, 'snare': False, 'hihat': True}, 0, beat_length)

# Bar 2: Full ensemble enters
bar_start = beat_length

# Marcus - walking bass line (Fm scale: F, Gb, Ab, Bb, B, Db, Eb)
# Walking in Fm: F, Gb, Ab, Bb, B, Db, Eb, F
# Chromatic approach: F (Db), Gb (B), Ab (Eb), Bb (F), B (Gb), Db (Ab), Eb (Bb), F (Db)
bass_notes = ['Db', 'B', 'Eb', 'F', 'Gb', 'Ab', 'Bb', 'Db']
bass_times = [bar_start + 0.0, bar_start + 0.25, bar_start + 0.5, bar_start + 0.75,
              bar_start + 1.0, bar_start + 1.25, bar_start + 1.5, bar_start + 1.75]
for note, time in zip(bass_notes, bass_times):
    play_note(note, time, 0.05)

# Diane - piano comp on 2 and 4 (F7, Bb7, F7, Bb7)
piano_notes = [
    ['F', 'A', 'Bb', 'Db'],  # F7
    ['Bb', 'Db', 'Eb', 'F'],  # Bb7
    ['F', 'A', 'Bb', 'Db'],  # F7
    ['Bb', 'Db', 'Eb', 'F']   # Bb7
]
piano_times = [bar_start + 0.5, bar_start + 1.0, bar_start + 1.5, bar_start + 2.0]
for notes, time in zip(piano_notes, piano_times):
    play_chord(notes, time, 0.1)

# Little Ray - kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_beats = [
    {'kick': True, 'snare': False, 'hihat': True},  # beat 1
    {'kick': False, 'snare': True, 'hihat': True},  # beat 2
    {'kick': True, 'snare': False, 'hihat': True},  # beat 3
    {'kick': False, 'snare': True, 'hihat': True}   # beat 4
]
for i, beat in enumerate(drum_beats):
    time = bar_start + (i * beat_length)
    play_drums(beat, time, beat_length * 0.2)

# Bar 3: Your saxophone motif
# Motif in Fm: F, Bb, Db, F (ascending minor third + tritone)
# Start at bar_start + 0.0
# Play it once, leave it hanging, then come back and finish it
# Make it sing — subtle vibrato, space between notes
sax_notes = ['F', 'Bb', 'Db', 'F']
sax_times = [bar_start + 0.0, bar_start + 0.3, bar_start + 0.6, bar_start + 0.9]
for note, time in zip(sax_notes, sax_times):
    play_note(note, time, 0.08, amp=0.6)

# Bar 4: Repeat the motif, but with a slight variation — the same notes, but with a chromatic approach
sax_notes_2 = ['Eb', 'F', 'Bb', 'Db', 'F']
sax_times_2 = [bar_start + 1.0, bar_start + 1.3, bar_start + 1.6, bar_start + 1.9, bar_start + 2.2]
for note, time in zip(sax_notes_2, sax_times_2):
    play_note(note, time, 0.08, amp=0.6)

# Normalize the buffer and play it
buffer = buffer / np.max(np.abs(buffer))
sd.play(buffer, sample_rate)
sd.wait()

# Save the audio as a WAV file (optional)
write('intro.wav', sample_rate, buffer.astype(np.float32))
print("Intro saved as 'intro.wav'")
