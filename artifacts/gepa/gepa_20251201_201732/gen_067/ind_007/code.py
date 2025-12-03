
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: F major (no sharps/flats)
key = 'F'

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time and tempo
BPM = 160
note_duration = 60 / BPM  # Seconds per beat
bar_duration = note_duration * 4  # 4 beats per bar

# Utility to add a note
def add_note(instrument, pitch, start, end, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    instrument.notes.append(note)

# 4 bars = 6 seconds
time = 0.0

# Bar 1: Little Ray on drums (kick on 1 and 3, snare on 2 and 4, hihat on every 8th)
# 4 beats per bar, with 8th notes

# Kick on 1 and 3
add_note(drums, 36, time, time + note_duration / 2, velocity=100)
add_note(drums, 36, time + note_duration * 2, time + note_duration * 2 + note_duration / 2, velocity=100)

# Snare on 2 and 4
add_note(drums, 38, time + note_duration, time + note_duration + note_duration / 2, velocity=100)
add_note(drums, 38, time + note_duration * 3, time + note_duration * 3 + note_duration / 2, velocity=100)

# Hihat on every 8th
for i in range(8):
    add_note(drums, 42, time + i * note_duration / 2, time + i * note_duration / 2 + note_duration / 4, velocity=80)

time += bar_duration

# Bar 2: All instruments come in
# Bass: Walking line in F major, roots and fifths, chromatic approaches
# F - C - G - D - A - E - Bb - F
# With chromatic approaches: Eb -> F, B -> C, F -> G, etc.

# Bass line: F, G, A, Bb
bass_notes = [71, 72, 74, 69]
for i, pitch in enumerate(bass_notes):
    add_note(bass, pitch, time + i * note_duration, time + i * note_duration + note_duration, velocity=80)

# Piano: Open voicings, resolve on beat 4
# Chord progression: F7 (bar 2), C7 (bar 3), G7 (bar 4)
# Bar 2: F7 as F, A, C, E
add_note(piano, 71, time, time + note_duration, velocity=100)
add_note(piano, 74, time, time + note_duration, velocity=90)
add_note(piano, 72, time, time + note_duration, velocity=85)
add_note(piano, 76, time, time + note_duration, velocity=95)

# Bar 3: C7 as C, E, G, B
add_note(piano, 72, time + note_duration, time + note_duration * 2, velocity=100)
add_note(piano, 76, time + note_duration, time + note_duration * 2, velocity=90)
add_note(piano, 74, time + note_duration, time + note_duration * 2, velocity=85)
add_note(piano, 79, time + note_duration, time + note_duration * 2, velocity=95)

# Bar 4: G7 as G, B, D, F
add_note(piano, 74, time + note_duration * 2, time + note_duration * 3, velocity=100)
add_note(piano, 79, time + note_duration * 2, time + note_duration * 3, velocity=90)
add_note(piano, 72, time + note_duration * 2, time + note_duration * 3, velocity=85)
add_note(piano, 76, time + note_duration * 2, time + note_duration * 3, velocity=95)

# Drums: Full beat
# Kick on 1 and 3
add_note(drums, 36, time, time + note_duration / 2, velocity=100)
add_note(drums, 36, time + note_duration * 2, time + note_duration * 2 + note_duration / 2, velocity=100)

# Snare on 2 and 4
add_note(drums, 38, time + note_duration, time + note_duration + note_duration / 2, velocity=100)
add_note(drums, 38, time + note_duration * 3, time + note_duration * 3 + note_duration / 2, velocity=100)

# Hihat on every 8th
for i in range(8):
    add_note(drums, 42, time + i * note_duration / 2, time + i * note_duration / 2 + note_duration / 4, velocity=80)

# Sax: Motif — a short, expressive phrase
# Start with a quarter-note F (71)
add_note(sax, 71, time, time + note_duration, velocity=100)

# Then a short rest or space
# Then a descending line to resolve on the 4th beat
# F -> Eb -> D -> C

add_note(sax, 69, time + note_duration * 2, time + note_duration * 2 + note_duration / 2, velocity=100)
add_note(sax, 67, time + note_duration * 3, time + note_duration * 3 + note_duration / 2, velocity=100)
add_note(sax, 65, time + note_duration * 3.5, time + note_duration * 3.5 + note_duration / 2, velocity=100)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' has been created.")
