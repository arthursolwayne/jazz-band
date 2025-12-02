
# Jazz Intro Generator in Python for 4 bars of F Major at 160 BPM
# Composed by Dante Russo for Wayne Shorter — 4 bars to make him lean in.

import time
import numpy as np
import sounddevice as sd
import midiutil

# Parameters
sample_rate = 44100
duration = 6.0  # in seconds
tempo = 160  # BPM
time_signature = (4, 4)

# Bar Length (in seconds)
bar_length = duration / 4
beat_length = bar_length / 4  # 0.375 seconds per beat

# Define instruments
# 0: Tenor Sax (You)
# 1: Piano (Diane)
# 2: Bass (Marcus)
# 3: Drums (Little Ray)

# MIDI Channels
SAX_CHANNEL = 0
PIANO_CHANNEL = 1
BASS_CHANNEL = 2
DRUMS_CHANNEL = 9  # MIDI channel 9 is reserved for drums

# Define the 4-bar structure
# Bar 1: Drums only (build tension)
# Bars 2-4: Full ensemble (you take the melody)

# Function to generate a simple melody (tenor sax)
def generate_sax_melody(note_durations, pitches, tempo=160):
    melody = []
    for i in range(len(pitches)):
        duration = note_durations[i] * 60 / tempo  # in seconds
        start = i * (note_durations[i] * 60 / tempo)
        melody.append((start, pitches[i], duration))
    return melody

# Function to generate a walking bass line
def generate_walking_bass(pitches, tempo=160):
    bass = []
    for i in range(len(pitches)):
        duration = 60 / tempo  # 1 beat = 60 / tempo
        start = i * duration
        bass.append((start, pitches[i], duration))
    return bass

# Function to generate piano chords (7th chords, comp on 2 and 4)
def generate_piano_chords(chords, tempo=160):
    piano = []
    for i in range(len(chords)):
        duration = 60 / tempo  # 1 beat
        # Comp on beat 2 and 4
        if (i + 1) % 2 == 0:
            start = i * duration
            piano.append((start, chords[i], duration))
    return piano

# Function to generate drum pattern (kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
def generate_drums(tempo=160):
    beat_length = 60 / tempo
    eighth_note = beat_length / 2
    drums = []

    # Kick on 1 and 3
    for i in range(0, 4):
        if i % 2 == 0:  # Beats 1 and 3
            start = i * beat_length
            drums.append((start, 36, 0.1))  # Kick drum

    # Snare on 2 and 4
    for i in range(1, 4):
        if i % 2 == 1:  # Beats 2 and 4
            start = i * beat_length
            drums.append((start, 38, 0.1))  # Snare

    # Hihat on every eighth note
    for i in range(0, 8):
        start = i * eighth_note
        drums.append((start, 42, 0.05))  # Hihat

    return drums

# Define pitches in F Major
F_MAJOR_SCALE = [65, 67, 69, 72, 74, 76, 77]  # F, G, A, Bb, B, C, D
F7 = [65, 67, 69, 72]  # F7 chord

# Bar 1: Drums only
drums_bar1 = generate_drums(tempo)
drums_bar1 = drums_bar1[:int(len(drums_bar1) / 2)]  # Only the first half of the pattern

# Bar 2: Full ensemble
# Tenor sax line — your motif
sax_melody = generate_sax_melody([0.5, 0.5, 0.5, 0.5], [69, 72, 74, 69])  # A, Bb, B, A

# Bass line — walking in F
# F, G, Ab, A, Bb, B, C, D
bass_line = generate_walking_bass([65, 67, 69, 72, 74, 76, 77, 65])

# Piano chords — 7th chords on 2 and 4
piano_chords = generate_piano_chords([F7, F7, F7, F7])

# Combine all into a MIDI file
def generate_midi_file(filename, events):
    track = 0
    time = 0
    midi_file = midiutil.MIDIFile(1, ticks_per_quarternote=96)

    for event in events:
        start_time, pitch, duration = event
        start_tick = int(start_time * midi_file.ticks_per_quarternote * tempo / 60)
        duration_tick = int(duration * midi_file.ticks_per_quarternote * tempo / 60)
        midi_file.addNote(track, 0, pitch, start_tick, duration_tick, 100)

    with open(filename, "wb") as output_file:
        midi_file.writeFile(output_file)
    print(f"MIDI file saved as {filename}")

# Combine all events
all_events = []

# Bar 1: Drums only
for event in drums_bar1:
    all_events.append(event)

# Bar 2: Sax, Bass, Piano
for event in sax_melody:
    all_events.append((event[0] + bar_length, event[1], event[2]))
for event in bass_line:
    all_events.append((event[0] + bar_length, event[1], event[2]))
for event in piano_chords:
    all_events.append((event[0] + bar_length, event[1], event[2]))

# Output MIDI
generate_midi_file("dante_intro.mid", all_events)

print("Composition complete. Replay 'dante_intro.mid' — it's your moment.")
