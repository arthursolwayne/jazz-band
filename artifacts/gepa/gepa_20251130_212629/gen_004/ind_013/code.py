
import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import pretty_midi
from IPython.display import Audio

# Parameters
sample_rate = 44100
duration = 6.0  # 6 seconds
bpm = 160
beat_seconds = 60.0 / bpm
bar_seconds = beat_seconds * 4
num_samples = int(sample_rate * duration)

# Initialize MIDI
midi = pretty_midi.PrettyMIDI()
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax
midi.instruments.append(instrument)

# Key: D Major
# Scale: D E F# G A B C#
scale_degrees = [0, 2, 3, 5, 7, 9, 11]

# Time in seconds for each note
bar1_time = 0.0
bar2_time = bar_seconds
bar3_time = bar_seconds * 2
bar4_time = bar_seconds * 3

# Bar 1: Little Ray on drums – kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# MIDI representation of a snare (35), kick (36), and hihat (42)
# We'll create a drum track separately

drum_program = pretty_midi.Instrument(program=0)  # Drums
midi.instruments.append(drum_program)

# Bar 1 (0.0 to 1.5 seconds)
# Kick on beat 1 (0.0), beat 3 (0.75)
kick_notes = [36, 36]
kick_times = [0.0, 0.75]
for note, time in zip(kick_notes, kick_times):
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drum_program.notes.append(note)

# Snare on beat 2 (0.375), beat 4 (1.125)
snare_notes = [35, 35]
snare_times = [0.375, 1.125]
for note, time in zip(snare_notes, snare_times):
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.1)
    drum_program.notes.append(note)

# Hihat on every eighth note (0.0, 0.375, 0.75, 1.125)
hihat_notes = [42, 42, 42, 42]
hihat_times = [0.0, 0.375, 0.75, 1.125]
for note, time in zip(hihat_notes, hihat_times):
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.05)
    drum_program.notes.append(note)

# Bar 2: Diane on piano – comping on 2 and 4 with 7th chords
# D7 chord: D F# A C
# E7 chord: E G# B D
# Root position on 2 and 4

# Bar 2 (1.5 to 3.0 seconds)
chord_times = [1.5 + 0.375, 1.5 + 1.125]
chords = [[2, 6, 9, 11], [4, 8, 11, 13]]  # D7 and E7 in MIDI note numbers
for time, chord in zip(chord_times, chords):
    for pitch in chord:
        note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
        instrument.notes.append(note)

# Bar 3: Marcus on bass – walking line starting on D
# D -> E -> F# -> G -> A -> B -> C# -> D
# 1.5 to 3.0 seconds
bass_notes = [2, 4, 6, 7, 9, 11, 13, 2]
bass_times = [1.5 + i * (beat_seconds / 4) for i in range(len(bass_notes))]
for pitch, time in zip(bass_notes, bass_times):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    instrument.notes.append(note)

# Bar 4: You on tenor sax – haunting motif, one phrase, not resolved
# Start with D (2), resolve to F# (6) but leave it hanging
# D -> E -> F# (no resolution), open-ended

# First phrase: D (2), E (4), F# (6)
# Duration: 0.75 seconds
# Then silence for 0.75 seconds
sax_notes = [2, 4, 6]
sax_times = [3.0, 3.125, 3.25]
for pitch, time in zip(sax_notes, sax_times):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
    instrument.notes.append(note)

# Convert to audio
audio = midi.fluidsynth(fs=sample_rate)
# Normalize
audio = audio / np.max(np.abs(audio))

# Save as WAV
write("jazz_intro.wav", sample_rate, audio.astype(np.float32))

# Play in IPython (if available)
Audio(audio, rate=sample_rate)
