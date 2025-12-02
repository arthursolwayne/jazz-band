
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to F major
key = 'F'

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Initialize instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments = [drums, bass, piano, sax]

# BPM = 160 => 60 / 160 = 0.375 seconds per beat
# 4 bars = 16 beats = 6.0 seconds

# Define tempo in BPM (160)
pm.set_tempo(160)

# Bar 1: Drums only
# Kick: 1 and 3
# Snare: 2 and 4
# Hi-hat: every 8th

for bar in range(1):
    for beat in range(4):
        time = bar * 4 + beat
        time_sec = time * 0.375

        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time_sec, end=time_sec + 0.1)
            drums.notes.append(note)

        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time_sec, end=time_sec + 0.1)
            drums.notes.append(note)

        # Hi-hat on every 8th
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time_sec + eighth * 0.1875, end=time_sec + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Bar 2-4: All instruments

# Time for bars 2-4 (each bar = 1.5 sec)
start_time = 1.5  # Start of Bar 2

# Define sax melody (Bars 2-4 — 3 bars total)
# Melody: F (F4), Gm7 (G4), Bb (Bb4), Ab (Ab4), F (F4), Bb (Bb4), Eb (Eb4), G (G4)
# Notes in MIDI numbers:
# F4 = 65, G4 = 67, Bb4 = 71, Ab4 = 70, Eb4 = 62, G = 67

sax_notes = [
    (65, 0.25, start_time),
    (67, 0.25, start_time + 0.25),
    (71, 0.25, start_time + 0.5),
    (70, 0.25, start_time + 0.75),
    (65, 0.25, start_time + 1.0),
    (71, 0.25, start_time + 1.25),
    (62, 0.25, start_time + 1.5),
    (67, 0.5, start_time + 1.75)
]

for pitch, duration, time in sax_notes:
    note = pretty_midi.Note(velocity=105, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Bass line – walking, chromatic, no repeated notes
bass_notes = [
    (60, 0.25, start_time),         # E4
    (62, 0.25, start_time + 0.25),  # F#4
    (63, 0.25, start_time + 0.5),   # G4
    (65, 0.25, start_time + 0.75),  # A4
    (67, 0.25, start_time + 1.0),   # B4
    (69, 0.25, start_time + 1.25),  # C#5
    (71, 0.25, start_time + 1.5),   # D5
    (72, 0.25, start_time + 1.75)   # Eb5
]

for pitch, duration, time in bass_notes:
    note = pretty_midi.Note(velocity=75, pitch=pitch, start=time, end=time + duration)
    bass.notes.append(note)

# Piano comping – 7th chords on 2 and 4
# F7 (F, A, C, E)
# Gm7 (G, Bb, D, F)
# Bb7 (Bb, D, F, Ab)

# Bar 2: F7 on 2 and 4
piano_notes = [
    (65, 0.25, start_time + 0.5),  # F
    (69, 0.25, start_time + 0.5),  # A
    (60, 0.25, start_time + 0.5),  # C
    (64, 0.25, start_time + 0.5),  # E
    (65, 0.25, start_time + 1.0),  # F
    (69, 0.25, start_time + 1.0),  # A
    (60, 0.25, start_time + 1.0),  # C
    (64, 0.25, start_time + 1.0),  # E
]

# Bar 3: Gm7 on 2 and 4
piano_notes.extend([
    (67, 0.25, start_time + 2.5),  # G
    (71, 0.25, start_time + 2.5),  # Bb
    (62, 0.25, start_time + 2.5),  # D
    (65, 0.25, start_time + 2.5),  # F
    (67, 0.25, start_time + 3.0),  # G
    (71, 0.25, start_time + 3.0),  # Bb
    (62, 0.25, start_time + 3.0),  # D
    (65, 0.25, start_time + 3.0),  # F
])

# Bar 4: Bb7 on 2 and 4
piano_notes.extend([
    (71, 0.25, start_time + 4.0),  # Bb
    (74, 0.25, start_time + 4.0),  # D
    (65, 0.25, start_time + 4.0),  # F
    (70, 0.25, start_time + 4.0),  # Ab
    (71, 0.25, start_time + 4.5),  # Bb
    (74, 0.25, start_time + 4.5),  # D
    (65, 0.25, start_time + 4.5),  # F
    (70, 0.25, start_time + 4.5)   # Ab
])

for pitch, duration, time in piano_notes:
    note = pretty_midi.Note(velocity=85, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# Drums for bars 2-4
# Kick: 1 and 3
# Snare: 2 and 4
# Hi-hat: every 8th

for bar in range(2, 5):
    for beat in range(4):
        time = (bar - 2) * 4 + beat
        time_sec = start_time + (time * 0.375)

        # Kick on 1 and 3
        if beat == 0 or beat == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time_sec, end=time_sec + 0.1)
            drums.notes.append(note)

        # Snare on 2 and 4
        if beat == 1 or beat == 3:
            note = pretty_midi.Note(velocity=110, pitch=38, start=time_sec, end=time_sec + 0.1)
            drums.notes.append(note)

        # Hi-hat on every 8th
        for eighth in range(2):
            note = pretty_midi.Note(velocity=80, pitch=42, start=time_sec + eighth * 0.1875, end=time_sec + eighth * 0.1875 + 0.05)
            drums.notes.append(note)

# Save MIDI file
pm.write("dante_russo_intro.mid")
