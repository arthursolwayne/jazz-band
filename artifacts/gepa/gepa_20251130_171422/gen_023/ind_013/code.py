
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax (program 64)
midi.instruments.append(instrument)

# Key: F major
# Scale: F, G, A, Bb, C, D, E
# Notes in MIDI:
F = 65
G = 67
A = 69
Bb = 70
C = 72
D = 74
E = 76

# Time signatures: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Bar durations (160 BPM = 6/160 = 0.0375 seconds per beat)
bar_length = 6.0  # 4 bars = 6 seconds
beat_length = bar_length / 4
note_length = beat_length / 2  # Half note length

# Define the four bars
# Bar 1: Drums only
# Bar 2: All instruments enter, sax plays the motif
# Bars 3-4: Development, tension, space, emotional build

# ================ DRUMS ================

# Little Ray's pattern - 4/4, hihat on every 8th, kick on 1 and 3, snare on 2 and 4
drums = pretty_midi.Instrument(program=10)  # Drums (program 10)
midi.instruments.append(drums)

# Drums in Bar 1 (only)
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625))

# Hihat on every 8th
hihat_pitch = 42
hihat_velocity = 80
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=hihat_velocity, pitch=hihat_pitch, start=start, end=end))

# ================ BASS ================

# Marcus's walking line, chromatic approach, dynamic variation
bass = pretty_midi.Instrument(program=33)  # Double Bass (program 33)
midi.instruments.append(bass)

# Bass line in Bar 2 (starts at 1.5 seconds)
# Chromatic approach from F to Bb, with syncopation and space
# Notes: F (65), Gb (66), G (67), Ab (68), A (69), Bb (70)
# Rhythmic pattern: syncopated 8th notes with accents and rests

bass_notes = [
    (65, 1.5, 1.625, 100),     # F, 8th note
    (66, 1.625, 1.75, 80),     # Gb, 8th note
    (67, 1.75, 1.875, 100),    # G, 8th note
    (68, 1.875, 2.0, 75),      # Ab, 8th note
    (69, 2.0, 2.125, 100),     # A, 8th note
    (70, 2.125, 2.25, 90),     # Bb, 8th note
    (72, 2.25, 2.375, 100),    # C, 8th note
    (74, 2.375, 2.5, 90),      # D, 8th note
    (76, 2.5, 2.625, 100),     # E, 8th note
    (70, 2.625, 2.75, 100),    # Bb, 8th note
    (69, 2.75, 2.875, 90),     # A, 8th note
    (67, 2.875, 3.0, 100)      # G, 8th note
]

for pitch, start, end, vel in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=end))

# ================ PIANO ================

# Diane's piano: 7th chords, comp on 2 and 4, emotional shading
piano = pretty_midi.Instrument(program=0)  # Acoustic Piano (program 0)
midi.instruments.append(piano)

# Bar 2: Comp on 2 and 4
# 7th chords, with space and emotion
# F7: F, A, C, Eb (65, 69, 72, 67)
# G7: G, B, D, F (67, 71, 74, 65)
# A7: A, C, E, G (69, 72, 76, 67)

# Bar 2: comp on 2 and 4 (start at 1.5)
# 2nd beat: F7
note_f7 = [(65, 1.75, 2.0, 80), (69, 1.75, 2.0, 80), (72, 1.75, 2.0, 80), (67, 1.75, 2.0, 80)]
for pitch, start, end, vel in note_f7:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=end))

# 4th beat: G7
note_g7 = [(67, 2.25, 2.5, 85), (71, 2.25, 2.5, 85), (74, 2.25, 2.5, 85), (65, 2.25, 2.5, 85)]
for pitch, start, end, vel in note_g7:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=end))

# ================ SAX (DANTE) ================

# Your motif: short, haunting, a question
# F - Ab - Bb - C (65, 70, 70, 72)
# Held for 1/2 beat each, with space in between

# Bar 2: motivic statement, starting at 1.5s
# F (65) - 1.5s
# Ab (70) - 1.875s
# Bb (70) - 2.25s
# C (72) - 2.625s

# Use velocity and dynamics to make it sing
sax_notes = [
    (65, 1.5, 1.625, 95),     # F, soft, lingering
    (70, 1.875, 2.0, 100),    # Ab, a little stronger
    (70, 2.25, 2.375, 95),    # Bb, softer again, echoing
    (72, 2.625, 2.75, 100)    # C, a resolution that doesn't quite resolve
]

for pitch, start, end, vel in sax_notes:
    instrument.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=end))

# Save the MIDI file
midi.write("jazz_intro_wayne.mid")
