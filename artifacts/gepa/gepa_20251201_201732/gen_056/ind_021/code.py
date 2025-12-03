
import pretty_midi
import numpy as np

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drum_program = pretty_midi.instrument_name_to_program('Drums')
drum_inst = pretty_midi.Instrument(program=drum_program)
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass_inst = pretty_midi.Instrument(program=bass_program)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano_inst = pretty_midi.Instrument(program=piano_program)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_inst = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(drum_inst)
pm.instruments.append(bass_inst)
pm.instruments.append(piano_inst)
pm.instruments.append(sax_inst)

# Define MIDI note values
D2 = 38
G2 = 43
Bb2 = 41
F3 = 53
C3 = 48
A2 = 45
Db3 = 46
F3 = 53
G3 = 55
C4 = 60
D4 = 62
F4 = 65
A4 = 69

# Function to add notes with velocity and timing
def add_notes(instrument, notes, time, velocity=100, duration=0.375):
    for note in notes:
        instrument.notes.append(pretty_midi.Note(
            velocity=velocity,
            pitch=note,
            start=time,
            end=time + duration
        ))

# Duration in seconds per beat
beat_length = 0.375  # 160 BPM = 60/160 = 0.375 per beat

# Bar 1: Drums only — hihat on every eighth, kick on 1 and 3
for i in range(8):
    if i % 2 == 0:  # every eighth note
        add_notes(drum_inst, [42], i * beat_length / 2, velocity=60)  # hihat
    if i == 0 or i == 3:  # kick on 1 and 3
        add_notes(drum_inst, [36], i * beat_length / 2, velocity=100)

# Bar 2: Bass (walking line starting from D2)
notes = [D2, Bb2, G2, F3, C3, A2, G2, D2]
for i, note in enumerate(notes):
    add_notes(bass_inst, [note], i * beat_length, velocity=70)

# Bar 2: Piano — Dm7 (D F A C)
add_notes(piano_inst, [D4, F4, A4, C5], 1.5, velocity=90)

# Bar 3: Bass (walking line starting from G2)
notes = [G2, F3, C3, Bb2, A2, G2, F3, D2]
for i, note in enumerate(notes):
    add_notes(bass_inst, [note], (1 + i) * beat_length, velocity=70)

# Bar 3: Piano — Bb7 (Bb D F A)
add_notes(piano_inst, [Bb4, D5, F5, A5], 3.0, velocity=90)

# Bar 4: Bass (walking line starting from F2)
notes = [F2, G2, A2, Bb2, C3, D3, F3, G3]
for i, note in enumerate(notes):
    add_notes(bass_inst, [note], (2 + i) * beat_length, velocity=70)

# Bar 4: Piano — G7 (G B D F)
add_notes(piano_inst, [G4, B4, D5, F5], 4.5, velocity=90)

# Bar 4: Sax — motif that starts, leaves it hanging, returns
# Motif: D4 (start), F4 (hold), C4 (resolve)
# Play D4 at beat 1, F4 at beat 2 (hold), C4 at beat 4
add_notes(sax_inst, [D4], 0.0, velocity=100)  # bar 1, beat 1
add_notes(sax_inst, [F4], 1.5, velocity=100)  # bar 2, beat 1
add_notes(sax_inst, [C4], 3.0, velocity=100)  # bar 3, beat 1
add_notes(sax_inst, [D4], 4.5, velocity=100)  # bar 4, beat 1

# Write MIDI file
pm.write('dante_intro.mid')
