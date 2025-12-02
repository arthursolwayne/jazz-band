
import numpy as np
import librosa
import sounddevice as sd
from scipy.io.wavfile import write

# Parameters
BPM = 160
BEAT = 60.0 / BPM  # seconds per beat
BAR = 4 * BEAT  # 6.0 seconds per bar
SAMPLE_RATE = 44100
DURATION = BAR * 4  # 4 bars
OUTPUT_FILE = "jazz_intro_f.wav"

# Notes in F major scale: F, G, A, Bb, B, C, D
# Key: F
# Time signature: 4/4

# Saxophone motif (tenor) - One short, memorable, unique phrase
# Notes in F: F, Ab, Bb, D
# Rhythm: eighth, eighth, eighth, quarter
# Timing: 0.0, 0.375, 0.75, 1.125 (relative to bar start)
# Duration: 0.375, 0.375, 0.375, 0.75

# Bass line (Marcus) - Walking line with chromatic approaches
# Starts on F, walks down: F, Eb, D, C, B, Bb, A, G, F, etc.
# Each note is a quarter note, with chromatic approach on the upbeats

# Piano (Diane) - 7th chords on 2 and 4
# Bar 2: F7 (F, A, C, Eb)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: F7 again

# Drums (Little Ray) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Fill the bar with consistent energy

# Generate waveform
def generate_synth_note(freq, duration, sample_rate):
    t = np.linspace(0, duration, int(duration * sample_rate), False)
    wave = 0.5 * np.sin(2 * np.pi * freq * t)
    return wave

# Map MIDI note to frequency
def midi_to_freq(midi_note):
    return 440.0 * (2.0 ** ((midi_note - 69) / 12.0))

# Convert note names to frequencies (assuming middle C = 60)
note_map = {
    'F': 69,     # F4
    'Ab': 66,    # A flat 4
    'Bb': 67,    # B flat 4
    'D': 62,     # D4
    'Eb': 64,    # E flat 4
    'C': 60,     # C4
    'G': 67,     # G4
    'A': 69,     # A4
    'B': 71,     # B4
    'Bb7': (67, 71, 60, 64),  # F7: F, A, C, Eb
    'F7': (69, 71, 60, 64),  # F7: F, A, C, Eb
    'Bb7': (67, 71, 60, 64),  # Bb7: Bb, D, F, Ab
    'C': 60
}

# Generate audio data
audio = np.zeros(int(DURATION * SAMPLE_RATE))

# Define bar timing
start_bar = 0
end_bar = DURATION

# Saxophone motif
note_times = [0.0, 0.375, 0.75, 1.125]  # in seconds
note_durations = [0.375, 0.375, 0.375, 0.75]
note_frequencies = [midi_to_freq(note_map['F']), midi_to_freq(note_map['Ab']), midi_to_freq(note_map['Bb']), midi_to_freq(note_map['D'])]

for i in range(len(note_times)):
    start = start_bar + note_times[i]
    end = start + note_durations[i]
    wave = generate_synth_note(note_frequencies[i], note_durations[i], SAMPLE_RATE)
    audio[int(start * SAMPLE_RATE):int(end * SAMPLE_RATE)] += wave

# Bass line (Marcus)
bass_notes = [69, 66, 62, 60, 61, 64, 62, 60]
bass_times = [0.0, 0.75, 1.5, 2.25, 3.0, 3.75, 4.5, 5.25]
bass_durations = [0.75] * len(bass_notes)

for i in range(len(bass_notes)):
    start = start_bar + bass_times[i]
    end = start + bass_durations[i]
    wave = generate_synth_note(midi_to_freq(bass_notes[i]), bass_durations[i], SAMPLE_RATE)
    audio[int(start * SAMPLE_RATE):int(end * SAMPLE_RATE)] += wave

# Piano chords (Diane)
# Bar 2: F7
chord_start = 1.5
chord_duration = 0.75
chord_frequencies = [midi_to_freq(note_map['F']), midi_to_freq(note_map['A']), midi_to_freq(note_map['C']), midi_to_freq(note_map['Eb'])]
chord_wave = np.zeros(int(chord_duration * SAMPLE_RATE))
for freq in chord_frequencies:
    chord_wave += generate_synth_note(freq, chord_duration, SAMPLE_RATE)
audio[int(chord_start * SAMPLE_RATE):int((chord_start + chord_duration) * SAMPLE_RATE)] += chord_wave

# Bar 3: Bb7
chord_start = 3.0
chord_frequencies = [midi_to_freq(note_map['Bb']), midi_to_freq(note_map['D']), midi_to_freq(note_map['F']), midi_to_freq(note_map['Ab'])]
chord_wave = np.zeros(int(chord_duration * SAMPLE_RATE))
for freq in chord_frequencies:
    chord_wave += generate_synth_note(freq, chord_duration, SAMPLE_RATE)
audio[int(chord_start * SAMPLE_RATE):int((chord_start + chord_duration) * SAMPLE_RATE)] += chord_wave

# Bar 4: F7 (again)
chord_start = 4.5
chord_frequencies = [midi_to_freq(note_map['F']), midi_to_freq(note_map['A']), midi_to_freq(note_map['C']), midi_to_freq(note_map['Eb'])]
chord_wave = np.zeros(int(chord_duration * SAMPLE_RATE))
for freq in chord_frequencies:
    chord_wave += generate_synth_note(freq, chord_duration, SAMPLE_RATE)
audio[int(chord_start * SAMPLE_RATE):int((chord_start + chord_duration) * SAMPLE_RATE)] += chord_wave

# Drums (Little Ray)
# Kick on 1 and 3
kick_times = [0.0, 1.5, 3.0, 4.5]
kick_freq = 88.0  # C5
kick_duration = 0.1
for t in kick_times:
    start = start_bar + t
    end = start + kick_duration
    wave = generate_synth_note(kick_freq, kick_duration, SAMPLE_RATE)
    audio[int(start * SAMPLE_RATE):int(end * SAMPLE_RATE)] += wave

# Snare on 2 and 4
snare_times = [0.75, 2.25, 3.75, 5.25]
snare_freq = 130.81  # E5
snare_duration = 0.15
for t in snare_times:
    start = start_bar + t
    end = start + snare_duration
    wave = generate_synth_note(snare_freq, snare_duration, SAMPLE_RATE)
    audio[int(start * SAMPLE_RATE):int(end * SAMPLE_RATE)] += wave

# Hi-hat on every eighth note
hihat_freq = 400.0  # high-pitched chime
hihat_duration = 0.05
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]
for t in hihat_times:
    start = start_bar + t
    end = start + hihat_duration
    wave = generate_synth_note(hihat_freq, hihat_duration, SAMPLE_RATE)
    audio[int(start * SAMPLE_RATE):int(end * SAMPLE_RATE)] += wave

# Normalize audio
audio = audio / np.max(np.abs(audio))

# Save as WAV file
write(OUTPUT_FILE, SAMPLE_RATE, audio.astype(np.float32))

# Play through speakers
sd.play(audio, SAMPLE_RATE)
sd.wait()

print(f"File saved as {OUTPUT_FILE}")
print("The intro is ready. Make him lean forward.")
