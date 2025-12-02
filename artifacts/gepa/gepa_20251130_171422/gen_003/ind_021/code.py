
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

midi.instruments = [bass, piano, drums, sax]

# BPM = 160, 4/4 time
# 6 seconds for 4 bars
# 1 bar = 1.5 seconds
# 1 beat = 0.375 seconds
# 160 BPM = 160 beats per minute = 2.666 beats per second → 0.375 seconds per beat

# Define a function to add a note
def add_note(instrument, pitch, start, end, velocity=100):
    note = pretty_midi.Note(velocity, pitch, start, end)
    instrument.notes.append(note)

# --- Bars 1-4: 6 seconds total (0 to 6) ---

# Bar 1: Little Ray on drums (0 to 1.5 seconds)
# Kick on 1 and 3, Snare on 2 and 4, Hi-hat on every eighth
bar1_start = 0
bar1_end = 1.5

# Kick on 1 and 3 (0 and 0.75)
add_note(drums, 36, bar1_start, bar1_start + 0.1)
add_note(drums, 36, bar1_start + 0.75, bar1_start + 0.85)

# Snare on 2 and 4 (0.375 and 1.125)
add_note(drums, 38, bar1_start + 0.375, bar1_start + 0.475)
add_note(drums, 38, bar1_start + 1.125, bar1_start + 1.225)

# Hi-hat on every eighth (0, 0.375, 0.75, 1.125)
for i in range(4):
    add_note(drums, 42, bar1_start + i * 0.375, bar1_start + i * 0.375 + 0.1)

# Bar 2: Bass (Marcus) - Walking line, chromatic, no repetition
# Fm Walking bass line: F, Gb, Ab, A, Bb, B, C, Db, etc.
bar2_start = 1.5
bar2_end = 3.0

# Walking bass (16th note steps)
notes = [71, 70, 68, 69, 67, 68, 69, 71]  # F, Gb, Ab, A, Bb, B, C, Db in Fm
for i, pitch in enumerate(notes):
    start = bar2_start + i * 0.1875
    end = start + 0.1875
    add_note(bass, pitch, start, end, velocity=70)

# Piano (Diane) - 7th chords on 2 and 4
bar2_2nd_beat = bar2_start + 0.75
bar2_4th_beat = bar2_start + 1.5

# Fm7 chord: F, Ab, Bb, Db (pitches 71, 68, 67, 65)
for pitch in [71, 68, 67, 65]:
    add_note(piano, pitch, bar2_2nd_beat, bar2_2nd_beat + 0.25, velocity=85)

add_note(piano, 68, bar2_4th_beat, bar2_4th_beat + 0.25, velocity=85)  # Ab again for texture

# Bar 3: Sax (Dante) - Motif: F, Ab, Bb, C (melody)
bar3_start = 3.0
bar3_end = 4.5

# Motif: F (71), Ab (68), Bb (67), C (69)
for i, pitch in enumerate([71, 68, 67, 69]):
    start = bar3_start + i * 0.375
    end = start + 0.25
    add_note(sax, pitch, start, end, velocity=100)

# Bar 4: Full band, sax continues, piano fills, bass walks
bar4_start = 4.5
bar4_end = 6.0

# Sax continues the motif
add_note(sax, 69, bar4_start, bar4_start + 0.25, velocity=100)  # C

# Piano fills with run across the 7th chord (Fm7)
for pitch in [71, 68, 67, 65, 70, 68, 67, 65]:  # F, Ab, Bb, Db, Gb, Ab, Bb, Db
    add_note(piano, pitch, bar4_start + 0.125, bar4_start + 0.125 + 0.0625, velocity=80)

# Bass continues walking
notes = [71, 70, 68, 69, 67, 68, 69, 71]
for i, pitch in enumerate(notes):
    start = bar4_start + i * 0.1875
    end = start + 0.1875
    add_note(bass, pitch, start, end, velocity=70)

# Drums continue (kick on 1 and 3, snare on 2 and 4)
# Kick on 1 (4.5) and 3 (5.25)
add_note(drums, 36, bar4_start, bar4_start + 0.1)
add_note(drums, 36, bar4_start + 0.75, bar4_start + 0.85)

# Snare on 2 (4.875) and 4 (5.625)
add_note(drums, 38, bar4_start + 0.375, bar4_start + 0.475)
add_note(drums, 38, bar4_start + 1.125, bar4_start + 1.225)

# Hi-hat on every eighth
for i in range(4):
    add_note(drums, 42, bar4_start + i * 0.375, bar4_start + i * 0.375 + 0.1)

# Write the MIDI file
midi.write("dante_intro.mid")
print("MIDI file written as 'dante_intro.mid'")
