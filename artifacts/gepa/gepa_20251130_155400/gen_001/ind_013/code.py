
import pretty_midi
from pretty_midi import Note, Instrument

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)
duration_per_beat = 60.0 / tempo  # seconds per beat
bar_length = 4 * duration_per_beat  # seconds per bar
total_length = 4 * bar_length  # 4 bars total

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature=(4, 4))

# Define instrument programs
drums_program = 0
bass_program = 33
piano_program = 0
sax_program = 64

# Add instruments
drums = Instrument(program=drums_program)
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
sax = Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Function to add a note to an instrument
def add_note(instrument, note_number, start_time, end_time):
    note = Note(note_number, start_time, end_time)
    instrument.notes.append(note)

# Bar 1: Drums only (Kick on 1 and 3, snare on 2 and 4, hihat on every eighth)
bar_1_start = 0.0
bar_1_end = bar_length

# Kick on 1 and 3
add_note(drums, 36, bar_1_start + 0.0, bar_1_start + duration_per_beat)  # Kick on beat 1
add_note(drums, 36, bar_1_start + 2 * duration_per_beat, bar_1_start + 3 * duration_per_beat)  # Kick on beat 3

# Snare on 2 and 4
add_note(drums, 38, bar_1_start + duration_per_beat, bar_1_start + 2 * duration_per_beat)  # Snare on beat 2
add_note(drums, 38, bar_1_start + 3 * duration_per_beat, bar_1_start + 4 * duration_per_beat)  # Snare on beat 4

# Hihat on every eighth
for i in range(8):
    add_note(drums, 42, bar_1_start + i * duration_per_beat / 2, bar_1_start + i * duration_per_beat / 2 + duration_per_beat / 2)

# Bars 2-4: Full quartet

# Time for bars 2-4
bar_2_start = bar_length
bar_3_start = 2 * bar_length
bar_4_start = 3 * bar_length

# Define the key: D major
key = 'D'

# Define the saxophone motif
# D - E - G - A (starting on D), but with a unique note duration on the G
# D (62), E (64), G (67), A (69)
# D (beat 1), E (beat 2), G (beat 3, 0.5 beat duration), A (beat 4)
sax_notes = [
    Note(62, bar_2_start + 0.0, bar_2_start + duration_per_beat),  # D on beat 1
    Note(64, bar_2_start + duration_per_beat, bar_2_start + 2 * duration_per_beat),  # E on beat 2
    Note(67, bar_2_start + 2 * duration_per_beat, bar_2_start + 2.5 * duration_per_beat),  # G on beat 3 (0.5 beat duration)
    Note(69, bar_2_start + 3 * duration_per_beat, bar_2_start + 4 * duration_per_beat)  # A on beat 4
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line with chromatic approaches
# D - F - E - D - C - B - A - G (chromatic descending from D)
# Notes: D (62), F (65), E (64), D (62), C (60), B (59), A (57), G (67)
bass_notes = [
    Note(62, bar_2_start + 0.0, bar_2_start + duration_per_beat),
    Note(65, bar_2_start + duration_per_beat, bar_2_start + 2 * duration_per_beat),
    Note(64, bar_2_start + 2 * duration_per_beat, bar_2_start + 3 * duration_per_beat),
    Note(62, bar_2_start + 3 * duration_per_beat, bar_2_start + 4 * duration_per_beat)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on beats 2 and 4
# D7 (D, F#, A, C) = D (62), F# (66), A (69), C (60)
# Notes scheduled on beat 2 of bars 2-4 (i.e., bar_2 + 1 beat, bar_3 + 1 beat, bar_4 + 1 beat)
for bar in range(2, 5):
    bar_start = (bar - 1) * bar_length
    # D7 chord on beat 2
    for note in [62, 66, 69, 60]:
        add_note(piano, note, bar_start + duration_per_beat, bar_start + 2 * duration_per_beat)

# Drums: Continue kick, snare, hihat for bars 2-4
for bar in range(2, 5):
    bar_start = (bar - 1) * bar_length
    # Kick on 1 and 3
    add_note(drums, 36, bar_start + 0.0, bar_start + duration_per_beat)
    add_note(drums, 36, bar_start + 2 * duration_per_beat, bar_start + 3 * duration_per_beat)
    
    # Snare on 2 and 4
    add_note(drums, 38, bar_start + duration_per_beat, bar_start + 2 * duration_per_beat)
    add_note(drums, 38, bar_start + 3 * duration_per_beat, bar_start + 4 * duration_per_beat)
    
    # Hihat on every eighth
    for i in range(8):
        add_note(drums, 42, bar_start + i * duration_per_beat / 2, bar_start + i * duration_per_beat / 2 + duration_per_beat / 2)

# Save the MIDI file
pm.write("dante_russo_intro.mid")
