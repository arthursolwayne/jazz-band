
import pretty_midi
import numpy as np

# Initialize the MIDI object
pm = pretty_midi.PrettyMIDI()
pm.resolution = 480  # Standard MIDI resolution (1 beat = 480 ticks at 120 BPM)

# Set tempo (160 BPM)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define the key: D major
key = 'D'
scale_degrees = [0, 2, 4, 7, 9, 11, 12]  # D, E, F#, A, B, C#, D
scale = [pretty_midi.note_number_from_name(f"{key}#{i}") for i in [0, 2, 4, 7, 9, 11, 12]]

# Helper to convert bar time to ticks
def bar_to_ticks(bar):
    return bar * pretty_midi.tick_conversion(160, 480, 4)

# ---------------------
# 1. DRUMS: Little Ray
# ---------------------

drums = pretty_midi.Instrument(program=10)  # Drums

# Kick on 1 and 3 of each bar
for bar in range(4):
    kick_time = bar_to_ticks(bar) + pretty_midi.tick_conversion(160, 480, 1)
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.15)
    drums.notes.append(kick_note)

    kick_time = bar_to_ticks(bar) + pretty_midi.tick_conversion(160, 480, 3)
    kick_note = pretty_midi.Note(velocity=100, pitch=36, start=kick_time, end=kick_time + 0.15)
    drums.notes.append(kick_note)

# Snare on 2 and 4
for bar in range(4):
    snare_time = bar_to_ticks(bar) + pretty_midi.tick_conversion(160, 480, 2)
    snare_note = pretty_midi.Note(velocity=90, pitch=38, start=snare_time, end=snare_time + 0.10)
    drums.notes.append(snare_note)

    snare_time = bar_to_ticks(bar) + pretty_midi.tick_conversion(160, 480, 4)
    snare_note = pretty_midi.Note(velocity=90, pitch=38, start=snare_time, end=snare_time + 0.10)
    drums.notes.append(snare_note)

# Hi-hats on every eighth note, with some dynamic variation
for bar in range(4):
    for i in range(0, 8):  # 8 eighth notes per bar
        time = bar_to_ticks(bar) + pretty_midi.tick_conversion(160, 480, i/2)
        velocity = np.random.randint(70, 110)  # Random velocity between 70-110
        hihat_note = pretty_midi.Note(velocity=velocity, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(hihat_note)

pm.instruments.append(drums)

# ---------------------
# 2. BASS: Marcus
# ---------------------

bass = pretty_midi.Instrument(program=33)  # Double Bass

# Walking line with chromatic approaches
bass_notes = [
    # Bar 1
    (bar_to_ticks(0) + 0.2, 65, 80),  # D3
    (bar_to_ticks(0) + 0.6, 64, 85),  # C#3
    (bar_to_ticks(0) + 1.0, 67, 80),  # E3
    (bar_to_ticks(0) + 1.4, 69, 85),  # F#3
    # Bar 2
    (bar_to_ticks(1) + 0.2, 71, 80),  # A3
    (bar_to_ticks(1) + 0.6, 72, 85),  # B3
    (bar_to_ticks(1) + 1.0, 74, 80),  # C#4
    (bar_to_ticks(1) + 1.4, 76, 85),  # D4
    # Bar 3
    (bar_to_ticks(2) + 0.2, 71, 80),  # A3
    (bar_to_ticks(2) + 0.6, 72, 85),  # B3
    (bar_to_ticks(2) + 1.0, 69, 80),  # F#3
    (bar_to_ticks(2) + 1.4, 67, 85),  # E3
    # Bar 4
    (bar_to_ticks(3) + 0.2, 65, 80),  # D3
    (bar_to_ticks(3) + 0.6, 64, 85),  # C#3
    (bar_to_ticks(3) + 1.0, 67, 80),  # E3
    (bar_to_ticks(3) + 1.4, 69, 85),  # F#3
]

for start, pitch, vel in bass_notes:
    note = pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + 0.2)
    bass.notes.append(note)

pm.instruments.append(bass)

# ---------------------
# 3. PIANO: Diane
# ---------------------

piano = pretty_midi.Instrument(program=0)  # Acoustic Piano

# Comping with 7th chords on beats 2 and 4
def chord_to_notes(root, seventh):
    interval = [0, 4, 7, 11]  # Root, 4th, 7th, 11th
    notes = [root + i for i in interval]
    return notes

# D7 chord: D, F#, A, C#
notes = chord_to_notes(65, 79)
for i, note in enumerate(notes):
    start = bar_to_ticks(0) + pretty_midi.tick_conversion(160, 480, 2)
    vel = 80 + (i * 10)
    note = pretty_midi.Note(velocity=vel, pitch=note, start=start, end=start + 0.4)
    piano.notes.append(note)

notes = chord_to_notes(67, 79)  # E7
for i, note in enumerate(notes):
    start = bar_to_ticks(1) + pretty_midi.tick_conversion(160, 480, 4)
    vel = 80 + (i * 10)
    note = pretty_midi.Note(velocity=vel, pitch=note, start=start, end=start + 0.4)
    piano.notes.append(note)

notes = chord_to_notes(69, 79)  # F#7
for i, note in enumerate(notes):
    start = bar_to_ticks(2) + pretty_midi.tick_conversion(160, 480, 2)
    vel = 80 + (i * 10)
    note = pretty_midi.Note(velocity=vel, pitch=note, start=start, end=start + 0.4)
    piano.notes.append(note)

notes = chord_to_notes(65, 79)  # D7
for i, note in enumerate(notes):
    start = bar_to_ticks(3) + pretty_midi.tick_conversion(160, 480, 4)
    vel = 80 + (i * 10)
    note = pretty_midi.Note(velocity=vel, pitch=note, start=start, end=start + 0.4)
    piano.notes.append(note)

pm.instruments.append(piano)

# ---------------------
# 4. SAXOPHONE: Dante
# ---------------------

sax = pretty_midi.Instrument(program=62)  # Tenor Saxophone

# A short, emotional motif — start on D, leave it hanging, come back

# Bar 1: D - F# - A - rest
note1 = pretty_midi.Note(velocity=100, pitch=65, start=bar_to_ticks(0) + 0.1, end=bar_to_ticks(0) + 0.4)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=bar_to_ticks(0) + 0.5, end=bar_to_ticks(0) + 0.8)
note3 = pretty_midi.Note(velocity=100, pitch=69, start=bar_to_ticks(0) + 1.0, end=bar_to_ticks(0) + 1.3)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)

# Bar 3: Repeat with slight deviation — D - F# - C# - A?
note1 = pretty_midi.Note(velocity=100, pitch=65, start=bar_to_ticks(2) + 0.1, end=bar_to_ticks(2) + 0.4)
note2 = pretty_midi.Note(velocity=100, pitch=67, start=bar_to_ticks(2) + 0.5, end=bar_to_ticks(2) + 0.8)
note3 = pretty_midi.Note(velocity=100, pitch=64, start=bar_to_ticks(2) + 1.0, end=bar_to_ticks(2) + 1.3)
note4 = pretty_midi.Note(velocity=100, pitch=69, start=bar_to_ticks(2) + 1.4, end=bar_to_ticks(2) + 1.7)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
