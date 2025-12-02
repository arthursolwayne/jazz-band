
import pretty_midi
import numpy as np

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Set tempo
midi.instruments = [bass, piano, drums, sax]

# BPM = 160 => 1 beat = 0.375 seconds
# 4 bars = 6 seconds
# Each bar = 1.5 seconds

def add_note(instrument, note, start_time, end_time, velocity):
    note_obj = pretty_midi.Note(velocity=velocity, pitch=note, start=start_time, end=end_time)
    instrument.notes.append(note_obj)

# Bar 1: Drums only — tension, anticipation, waiting
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 0.0 to 1.5 seconds
time = 0.0

# Kick on 1 and 3 (beats 1 and 3)
add_note(drums, pretty_midi.note_number_to_name(36), time + 0.0, time + 0.1, 90)
add_note(drums, pretty_midi.note_number_to_name(36), time + 0.75, time + 0.85, 90)

# Snare on 2 and 4 (beats 2 and 4)
add_note(drums, pretty_midi.note_number_to_name(38), time + 0.375, time + 0.475, 95)
add_note(drums, pretty_midi.note_number_to_name(38), time + 0.75, time + 0.85, 95)  # Wait, this is same as kick? No — this is beat 4

# Hihat on every eighth
add_note(drums, pretty_midi.note_number_to_name(42), time + 0.0, time + 0.05, 65)
add_note(drums, pretty_midi.note_number_to_name(42), time + 0.1875, time + 0.2375, 65)
add_note(drums, pretty_midi.note_number_to_name(42), time + 0.375, time + 0.425, 65)
add_note(drums, pretty_midi.note_number_to_name(42), time + 0.5625, time + 0.6125, 65)
add_note(drums, pretty_midi.note_number_to_name(42), time + 0.75, time + 0.8, 65)
add_note(drums, pretty_midi.note_number_to_name(42), time + 0.9375, time + 0.9875, 65)
add_note(drums, pretty_midi.note_name_to_number("D#4"), time + 1.125, time + 1.175, 65)
add_note(drums, pretty_midi.note_name_to_number("D#4"), time + 1.3125, time + 1.3625, 65)

# Bar 2: All instruments enter, sax takes the melody

# Bass line: Walking line with chromatic approaches (F, G, A#, Bb, B, C#, D#, E, F)
# Time is 1.5 to 3.0 seconds
bass_notes = [78, 81, 83, 82, 83, 85, 87, 88, 78]
bass_durations = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0]  # last note is rest
bass_time = 1.5

for i, note in enumerate(bass_notes):
    start = bass_time + i * 0.25
    if i < len(bass_notes) - 1:
        duration = bass_durations[i]
    else:
        duration = 0.0
    add_note(bass, note, start, start + duration, 85)

# Piano: 7th chords on 2 and 4 (in bar 2 and 3)
# F7 on 2, Bb7 on 4
piano_notes = [78, 80, 82, 85, 83, 85, 87, 90]
piano_times = [1.5 + 0.375, 1.5 + 0.375, 1.5 + 0.375, 1.5 + 0.375, 1.5 + 0.75, 1.5 + 0.75, 1.5 + 0.75, 1.5 + 0.75]
piano_durations = [0.15] * 8

for i, note in enumerate(piano_notes):
    add_note(piano, note, piano_times[i], piano_times[i] + piano_durations[i], 80)

# Saxophone: Your motif — short, singable, leaves a question
# Motif: F (78), Bb (82), C# (85), E (87) — but with unique durations and rests

# Bar 2: 1.5 to 3.0
# Start with F (78) on beat 1 — 1.5s
# Follow with Bb (82) on beat 2, hold into beat 3
# Then a rest, then C# on beat 4

add_note(sax, 78, 1.5, 1.6, 100)
add_note(sax, 82, 1.875, 2.125, 105)  # Beat 2 to 3 (1.875 to 2.125)
add_note(sax, 85, 2.625, 2.75, 100)  # Beat 4 (2.625 to 2.75)

# Add a rest in the middle to create space and tension
# Bar 3: 3.0 to 4.5

# No sax in bar 3 (let the question hang)
# Bar 4: 4.5 to 6.0

# Repeat Bb and C# with variation

add_note(sax, 82, 4.5, 4.875, 105)  # Beat 1 to 2 (4.5 to 4.875)
add_note(sax, 85, 5.25, 5.375, 100)  # Beat 3 to 4 (5.25 to 5.375)

# Final rest, creating an open-ended question
add_note(sax, 78, 5.75, 5.75, 0)  # 0 velocity = rest, but this is a dummy note to create silence

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
