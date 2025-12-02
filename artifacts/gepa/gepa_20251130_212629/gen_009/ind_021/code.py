
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
drums = pretty_midi.Instrument(program=10)
piano = pretty_midi.Instrument(program=0)
bass = pretty_midi.Instrument(program=33)
sax = pretty_midi.Instrument(program=64)

# Tempo: 160 BPM = 0.375 seconds per beat, 1.5 seconds per bar

# -------------------
# Bar 1: Little Ray (Drums)
# -------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Let the rhythm breathe with subtle dynamics

bar_length = 1.5  # 1.5 seconds per bar
beat = bar_length / 4  # 0.375 seconds per beat

# Hihat every eighth
for i in range(0, 8):
    time = i * (beat / 2)
    note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# Kick on 1 and 3
kick_times = [0.0, beat * 2]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [beat, beat * 3]
for t in snare_times:
    note = pretty_midi.Note(velocity=90, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

pm.instruments.append(drums)

# -------------------
# Bars 2-4: Full Quartet
# -------------------
# Time: Start at 1.5 seconds

# -------------------
# Marcus (Bass) - Walking line, chromatic approaches, no repetition
# -------------------
# Bass line in D minor (D Dorian)
# D - C - B - A - G - F# - E - D (chromatic descent)
# Walking bass line for 3 bars (12 beats)

bass_notes = [
    (1.5, 62),  # D4
    (1.875, 60), # C4
    (2.25, 59),  # B4
    (2.625, 67), # A4
    (3.0, 65),   # G4
    (3.375, 64), # F#4
    (3.75, 62),  # E4
    (4.125, 62), # D4
    (4.5, 60),   # C4
    (4.875, 59), # B4
    (5.25, 67),  # A4
    (5.625, 65)  # G4
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

pm.instruments.append(bass)

# -------------------
# Diane (Piano) - 7th chords, comp on 2 and 4
# -------------------
# D7 chord: D F# A C (D7)
# We'll play a rootless voicing: F# A C D (6th, 9th, 7th, root)
# Comp on 2 and 4 in each bar

def play_chord(chord, time):
    chords = {
        'D7': [66, 69, 71, 73],  # F#, A, C, D
        'C7': [60, 64, 67, 69],  # C, E, G, Bb (C7)
        'B7': [62, 66, 69, 71],  # B, D#, F#, A (B7)
        'A7': [65, 68, 70, 72],  # A, C#, E, G (A7)
        'G7': [67, 70, 72, 74],  # G, B, D, F (G7)
        'F#7': [64, 68, 71, 73], # F#, A, C#, E (F#7)
        'E7': [64, 67, 70, 72]   # E, G, B, D (E7)
    }
    if chord not in chords:
        return
    for pitch in chords[chord]:
        note = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + 0.25)
        piano.notes.append(note)

# Bar 2 (D7 on 2 and 4)
play_chord('D7', 1.875)
play_chord('D7', 2.625)

# Bar 3 (C7 on 2 and 4)
play_chord('C7', 3.375)
play_chord('C7', 4.125)

# Bar 4 (B7 on 2 and 4)
play_chord('B7', 4.875)
play_chord('B7', 5.625)

pm.instruments.append(piano)

# -------------------
# Little Ray (Drums) - Continue the energy
# -------------------
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
for i in range(0, 8):
    time = 1.5 + i * (beat / 2)
    note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

for t in [1.5, 1.5 + beat * 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in [1.5 + beat, 1.5 + beat * 3]:
    note = pretty_midi.Note(velocity=90, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 3
for i in range(0, 8):
    time = 3.0 + i * (beat / 2)
    note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

for t in [3.0, 3.0 + beat * 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in [3.0 + beat, 3.0 + beat * 3]:
    note = pretty_midi.Note(velocity=90, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

# Bar 4
for i in range(0, 8):
    time = 4.5 + i * (beat / 2)
    note = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

for t in [4.5, 4.5 + beat * 2]:
    note = pretty_midi.Note(velocity=100, pitch=36, start=t, end=t + 0.1)
    drums.notes.append(note)

for t in [4.5 + beat, 4.5 + beat * 3]:
    note = pretty_midi.Note(velocity=90, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

# -------------------
# Dante (Sax) - The Motif
# -------------------
# Start with a lyrical motif: D - E - B - rest, pause, then resolve with C
# Use dynamics and rests to make it sing

# D (D4, 62), E (E4, 64), B (B4, 71), rest, then C (C4, 60)
note1 = pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6)
note2 = pretty_midi.Note(velocity=95, pitch=64, start=1.6, end=1.7)
note3 = pretty_midi.Note(velocity=110, pitch=71, start=1.7, end=1.8)
note4 = pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.1)

sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

pm.instruments.append(sax)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
