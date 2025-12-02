
import pretty_midi
import numpy as np
from pretty_midi import Note, Instrument, Program

# Set up the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)  # 160 BPM

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: Fm (F minor)
# Notes in Fm: F, Ab, Bb, C, Eb, F, G, Ab
# Our piece will be in F minor.

# Define the time per bar in seconds (160 BPM => 0.75 seconds per beat, 3 seconds per bar)
time_per_beat = 0.75
time_per_bar = 3.0

# Create instruments
drums = Instrument(program=Program(0), is_drum=True, name='Drums')
bass = Instrument(program=Program(33), name='Bass')
piano = Instrument(program=Program(0), name='Piano')
sax = Instrument(program=Program(64), name='Saxophone')

pm.instruments = [drums, bass, piano, sax]

# ----------------------------- DRUMS -----------------------------
# Bar 1: Fill the bar with hihat, snare, kick
# Little Ray: kick on 1 and 3, snare on 2 and 4, hihat on every eighth.
# Add some syncopation and velocity variation

def add_drum_notes(instrument, time, type, velocity, duration=0.1):
    note = Note(type, velocity, time, time + duration)
    instrument.notes.append(note)

# Bar 1
for i in range(0, 4):
    beat_time = i * time_per_beat
    # Kick on 1 and 3
    if i in [0, 2]:
        add_drum_notes(drums, beat_time, pretty_midi.note_number_to_name(36), np.random.randint(90, 110))
    # Snare on 2 and 4
    if i in [1, 3]:
        add_drum_notes(drums, beat_time + 0.25, pretty_midi.note_number_to_name(38), np.random.randint(100, 120))
    # Hihat on every eighth
    for j in range(2):
        eighth_time = beat_time + j * 0.375
        add_drum_notes(drums, eighth_time, pretty_midi.note_number_to_name(42), np.random.randint(80, 100))

# Add a half-time fill on beat 4 for tension
add_drum_notes(drums, 2.75, pretty_midi.note_number_to_name(38), 110, duration=0.5)
add_drum_notes(drums, 2.75, pretty_midi.note_number_to_name(42), 100, duration=0.5)

# ----------------------------- BASS -----------------------------
# Marcus: Walking line in Fm, chromatic approaches, never repeating the same note
# Fm scale: F, G, Ab, Bb, B, C, Db, D
# Walking line in 4/4, starting on F

def get_bass_note(time, note, velocity=80, duration=0.75):
    n = Note(note, velocity, time, time + duration)
    bass.notes.append(n)

# Chromatic walking line
bass_notes = [64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79]  # F to E
bass_notes = [n for n in bass_notes if n in [64, 65, 66, 67, 68, 69, 70, 72, 73, 74, 75, 76]]  # Fm scale

for i in range(4):
    time = i * time_per_beat
    # chromatic approach: go up a half step, land on the target
    if i == 0:
        get_bass_note(time, 64)  # F
        get_bass_note(time, 65, duration=0.1)  # F#
    elif i == 1:
        get_bass_note(time, 67)  # Ab
        get_bass_note(time, 66, duration=0.1)  # Gb
    elif i == 2:
        get_bass_note(time, 70)  # Bb
        get_bass_note(time, 69, duration=0.1)  # A
    elif i == 3:
        get_bass_note(time, 72)  # C
        get_bass_note(time, 71, duration=0.1)  # Bb

# ----------------------------- PIANO -----------------------------
# Diane: 7th chords, comp on 2 and 4, emotional and sharp
# Fm7: F, Ab, C, Eb
# Comp on 2 and 4, with a little release and tension

def add_piano_notes(instrument, time, notes, velocity=100, duration=0.75):
    for n in notes:
        Note(n, velocity, time, time + duration)
        instrument.notes.append(Note(n, velocity, time, time + duration))

# Bar 2-4: comp on 2 and 4
# Fm7 on beat 2, C7 on beat 4
for i in range(1, 4):
    time = i * time_per_beat
    if i == 1:  # Bar 2
        add_piano_notes(piano, time, [64, 67, 72, 69], velocity=100)  # Fm7
    elif i == 2:  # Bar 3
        add_piano_notes(piano, time, [72, 74, 76, 77], velocity=100)  # C7
    elif i == 3:  # Bar 4
        add_piano_notes(piano, time, [64, 67, 72, 69], velocity=100)  # Fm7

# Add some tension chord on beat 3 in bar 3 (E7)
add_piano_notes(piano, 2.0, [69, 71, 76, 78], velocity=110, duration=0.5)

# ----------------------------- SAXOPHONE -----------------------------
# You: the melody — simple, haunting, space and silence

# Melody: a short motif — start it, leave it hanging
def add_sax_notes(instrument, time, notes, velocity=90, duration=0.75):
    for n in notes:
        Note(n, velocity, time, time + duration)
        instrument.notes.append(Note(n, velocity, time, time + duration))

# Bar 1: no sax
# Bar 2: start the motif (F, G, Ab, Bb)
# Bar 3: repeat but with a space (rest on Ab)
# Bar 4: resolve with a long note on C

# Bar 2
add_sax_notes(sax, 1.0, [64, 65, 67, 67], duration=0.75)

# Bar 3
add_sax_notes(sax, 2.0, [64, 65, 67], duration=0.5)  # skip Ab
add_sax_notes(sax, 2.5, [67], duration=0.5)  # rest on Ab

# Bar 4
add_sax_notes(sax, 3.0, [72], duration=1.0)  # long note on C

# Save the MIDI
pm.write("wayne_introduction.mid")
