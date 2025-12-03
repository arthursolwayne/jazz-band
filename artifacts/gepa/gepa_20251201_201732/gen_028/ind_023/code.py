
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import mido
from mido import MidiFile, MidiTrack, Message

# Set parameters
sample_rate = 44100
duration = 6.0  # 6 seconds
bpm = 160
tempo = 60.0 / bpm  # seconds per beat
bar_length = 4 * tempo  # 4 beats per bar
total_samples = int(sample_rate * duration)

# Initialize audio buffer
audio = np.zeros(total_samples, dtype=np.float32)

# Define MIDI note to frequency
def note_to_freq(note):
    return 440.0 * (2 ** ((note - 69) / 12))

# Define time positions for each bar
bar_start = [0, bar_length, 2 * bar_length, 3 * bar_length]

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def play_drums():
    for bar in range(4):
        start = bar_start[bar]
        # Kick on 1 and 3
        kick1 = start + 0 * tempo
        kick2 = start + 2 * tempo
        # Snare on 2 and 4
        snare1 = start + 1 * tempo
        snare2 = start + 3 * tempo
        # Hihat on every eighth
        for i in range(8):
            hihat = start + i * tempo / 2
            # Generate kick
            if i == 0 or i == 2:
                kick = np.sin(2 * np.pi * 60 * np.linspace(0, 1, int(tempo * sample_rate / 2)))
                audio[int(kick1):int(kick1 + len(kick))] += kick
            # Generate snare
            if i == 1 or i == 3:
                snare = np.sin(2 * np.pi * 150 * np.linspace(0, 1, int(tempo * sample_rate / 2)))
                audio[int(snare1):int(snare1 + len(snare))] += snare
            # Generate hihat
            hihat = np.sin(2 * np.pi * 1000 * np.linspace(0, 1, int(tempo * sample_rate / 4)))
            audio[int(hihat):int(hihat + len(hihat))] += hihat

# Bass: Walking line (D2-G2), roots and fifths with chromatic approaches
def play_bass():
    notes = [2, 3, 4, 5, 3, 2, 1, 0]  # D2, Eb2, E2, F2, Eb2, D2, C2, Bb2
    for bar in range(4):
        start = bar_start[bar]
        for i, note in enumerate(notes):
            time = start + i * tempo
            freq = note_to_freq(note + 24)  # D2 is MIDI 38
            # Generate bass note (short, punchy)
            bass = np.sin(2 * np.pi * freq * np.linspace(0, 1, int(tempo * sample_rate / 2)))
            audio[int(time):int(time + len(bass))] += bass

# Piano: Open voicings, different chord each bar, resolve on the last
def play_piano():
    chords = [
        ['Dm7', 'G7', 'Cm7', 'F7'],
        ['Dm7', 'G7', 'Cm7', 'F7'],
        ['Dm7', 'G7', 'Cm7', 'F7'],
        ['Dm7', 'G7', 'Cm7', 'F7']
    ]
    for bar in range(4):
        start = bar_start[bar]
        for i in range(4):
            chord = chords[bar][i]
            # Convert chord to MIDI notes (simplified)
            note_map = {
                'Dm7': [2, 4, 7, 10],
                'G7': [7, 9, 11, 10],
                'Cm7': [0, 2, 5, 8],
                'F7': [5, 7, 10, 11]
            }
            notes = note_map[chord]
            # Play chord with open voicings
            for note in notes:
                freq = note_to_freq(note + 36)  # C3 is MIDI 60
                # Generate piano note (short, dynamic)
                piano = np.sin(2 * np.pi * freq * np.linspace(0, 1, int(tempo * sample_rate / 4)))
                audio[int(start + i * tempo):int(start + i * tempo + len(piano))] += piano

# Tenor: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
def play_tenor():
    # Define motif (Dm scale, but with tension)
    notes = [2, 3, 4, 5]  # D, Eb, E, F
    # Play first note
    note = notes[0]
    freq = note_to_freq(note + 36)
    tenor = np.sin(2 * np.pi * freq * np.linspace(0, 1, int(tempo * sample_rate / 2)))
    audio[int(bar_start[0]):int(bar_start[0] + len(tenor))] += tenor
    # Leave it hanging
    # Play the rest in the third bar
    for i, note in enumerate(notes[1:]):
        time = bar_start[2] + i * tempo
        freq = note_to_freq(note + 36)
        tenor = np.sin(2 * np.pi * freq * np.linspace(0, 1, int(tempo * sample_rate / 2)))
        audio[int(time):int(time + len(tenor))] += tenor

# Generate the audio
play_drums()
play_bass()
play_piano()
play_tenor()

# Normalize audio to avoid clipping
audio /= np.max(np.abs(audio))

# Play the audio
sd.play(audio, sample_rate)
sd.wait()

# Save the audio to a file
write("jazz_intro.wav", sample_rate, audio)
