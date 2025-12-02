
import numpy as np
from scipy.io.wavfile import write
import sounddevice as sd
import time

# Settings
sample_rate = 44100
duration_seconds = 6.0
bpm = 160
beats_per_bar = 4
notes_per_beat = 4  # 16th notes
total_notes = beats_per_bar * notes_per_bar
tempo = 60.0 / bpm  # seconds per beat
note_duration = tempo / notes_per_bar  # seconds per 16th note

# Frequencies (F major scale for reference)
frequencies = {
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'Bb': 466.16,
    'B': 493.88,
    'C': 523.25,
    'D': 587.33,
    'Eb': 622.25,
    'E': 659.25,
    'F#': 698.46
}

# Function to generate a sine wave
def generate_sine_wave(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(2 * np.pi * freq * t)
    return wave

# Generate the 4-bar jazz piece
# Bar 1: Drums only
# Bar 2-4: Full ensemble

# Define the saxophone motif (bar 2-4)
sax_notes = [
    ('F', 0),   # Start on F
    ('Bb', 1),  # Chromatic up
    ('B', 2),   # Then up
    ('C', 3),   # Then up
    ('D', 4),   # Then up
    ('Eb', 5),  # Then up
    ('F', 6),   # Then back
    ('G', 7),   # Then up to G
    ('F', 8),   # Then back down
    ('Eb', 9),  # Then back
    ('D', 10),  # Then down
    ('C', 11),  # Then down
    ('Bb', 12), # Then back to Bb
    ('F', 13)   # End on F
]

# Define the bass line (chromatic walking line, 4 bars = 16 notes)
bass_notes = [
    ('F', 0), ('F#', 1), ('G', 2), ('Ab', 3), ('A', 4),
    ('Bb', 5), ('B', 6), ('C', 7), ('Db', 8), ('D', 9),
    ('Eb', 10), ('E', 11), ('F', 12), ('F#', 13), ('G', 14),
    ('Ab', 15)
]

# Define the piano chords (7th chords on 2 and 4)
piano_notes = {
    1: [],        # No chord on 1
    2: ['F7'],    # 2nd beat of bar 2: F7
    3: [],        # No chord on 3
    4: ['Bb7']    # 4th beat of bar 2: Bb7
}

# Define the drum pattern
drum_pattern = {
    0: 'kick',   # 1st beat
    1: 'snare',  # 2nd beat
    2: 'kick',   # 3rd beat
    3: 'snare',  # 4th beat
    4: 'hihat',  # 1st 16th note
    5: 'hihat',  # 2nd 16th note
    6: 'hihat',  # 3rd 16th note
    7: 'hihat',  # 4th 16th note
    8: 'hihat',  # 5th 16th note
    9: 'hihat',  # 6th 16th note
    10: 'hihat', # 7th 16th note
    11: 'hihat', # 8th 16th note
    12: 'hihat', # 9th 16th note
    13: 'hihat', # 10th 16th note
    14: 'hihat', # 11th 16th note
    15: 'hihat'  # 12th 16th note
}

# Generate the music
output = np.zeros(int(sample_rate * duration_seconds))

# Bar 1: Drums only
for note_index in range(16):
    if note_index in drum_pattern:
        if drum_pattern[note_index] == 'kick':
            kick_freq = 80.0  # Low bass kick
            kick_wave = generate_sine_wave(kick_freq, note_duration, sample_rate)
            output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += kick_wave
        elif drum_pattern[note_index] == 'snare':
            snare_freq = 160.0  # High-pitched snare
            snare_wave = generate_sine_wave(snare_freq, note_duration, sample_rate)
            output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += snare_wave
        elif drum_pattern[note_index] == 'hihat':
            hihat_freq = 1000.0  # High hat
            hihat_wave = generate_sine_wave(hihat_freq, note_duration, sample_rate)
            output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += hihat_wave

# Bar 2-4: Full ensemble
for bar in range(2, 5):  # bars 2, 3, 4
    for note_index in range(16):
        # Saxophone
        if note_index < len(sax_notes):
            note, start_beat = sax_notes[note_index]
            if start_beat == bar - 2:
                freq = frequencies[note]
                sax_wave = generate_sine_wave(freq, note_duration, sample_rate)
                output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += sax_wave

        # Bass
        note, start_beat = bass_notes[note_index]
        if start_beat == bar - 2:
            freq = frequencies[note]
            bass_wave = generate_sine_wave(freq, note_duration, sample_rate)
            output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += bass_wave

        # Piano
        if note_index < len(piano_notes):
            if piano_notes[note_index] and start_beat == bar - 2:
                chord = piano_notes[note_index][0]
                if chord == 'F7':
                    # F7 = F, A, C, Eb
                    for note in ['F', 'A', 'C', 'Eb']:
                        freq = frequencies[note]
                        piano_wave = generate_sine_wave(freq, note_duration, sample_rate)
                        output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += piano_wave
                elif chord == 'Bb7':
                    # Bb7 = Bb, D, F, Ab
                    for note in ['Bb', 'D', 'F', 'Ab']:
                        freq = frequencies[note]
                        piano_wave = generate_sine_wave(freq, note_duration, sample_rate)
                        output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += piano_wave

        # Drums (continue pattern)
        if note_index in drum_pattern:
            if drum_pattern[note_index] == 'kick':
                kick_freq = 80.0
                kick_wave = generate_sine_wave(kick_freq, note_duration, sample_rate)
                output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += kick_wave
            elif drum_pattern[note_index] == 'snare':
                snare_freq = 160.0
                snare_wave = generate_sine_wave(snare_freq, note_duration, sample_rate)
                output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += snare_wave
            elif drum_pattern[note_index] == 'hihat':
                hihat_freq = 1000.0
                hihat_wave = generate_sine_wave(hihat_freq, note_duration, sample_rate)
                output[int(note_index * sample_rate * note_duration):int((note_index + 1) * sample_rate * note_duration)] += hihat_wave

# Normalize the output
output /= np.max(np.abs(output)) * 0.9

# Play the audio
sd.play(output, sample_rate)
time.sleep(duration_seconds)
sd.stop()

# Save as WAV file
write("dante_russo_intro.wav", sample_rate, output)
print("4-bar intro saved as 'dante_russo_intro.wav'")
