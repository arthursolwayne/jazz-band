
import pretty_midi
from pretty_midi import pretty_midi, Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the time in seconds for each bar (160 BPM, 4/4 time)
bar_length = 6.0 / 4  # 6 seconds for 4 bars, so 1.5 seconds per bar
note_duration = bar_length / 4  # 0.375 seconds per beat

# Define instruments
instruments = {
    'drums': Instrument(program=0, is_drum=True, name='Drums'),
    'bass': Instrument(program=33, name='Bass'),
    'piano': Instrument(program=0, name='Piano'),
    'sax': Instrument(program=64, name='Saxophone')
}

# Add instruments to the PrettyMIDI object
for inst in instruments.values():
    pm.instruments.append(inst)

# Define MIDI note values for D major scale
D_MAJOR = [55, 57, 59, 62, 64, 67, 69]  # D, E, F#, G, A, B, C#

# DRUMS: Bar 1 - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0, 36, 100),  # Kick on 1
    (note_duration * 0.5, 42, 100),  # Snare on 2
    (note_duration * 1, 36, 100),  # Kick on 3
    (note_duration * 1.5, 42, 100),  # Snare on 4
    # Hihat on every eighth note
    (0, 49, 100),
    (note_duration * 0.25, 49, 100),
    (note_duration * 0.5, 49, 100),
    (note_duration * 0.75, 49, 100),
    (note_duration * 1, 49, 100),
    (note_duration * 1.25, 49, 100),
    (note_duration * 1.5, 49, 100)
]

for time, note_number, velocity in drum_notes:
    instruments['drums'].notes.append(Note(note_number, velocity, time, note_duration * 0.25))

# BASS: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 1: D (55), E flat (56), E (57), F# (59)
    (0, 55, 100),
    (note_duration, 56, 100),
    (note_duration * 2, 57, 100),
    (note_duration * 3, 59, 100),
    # Bar 2: G (62), A flat (63), A (64), B flat (66)
    (note_duration * 4, 62, 100),
    (note_duration * 5, 63, 100),
    (note_duration * 6, 64, 100),
    (note_duration * 7, 66, 100),
    # Bar 3: B (67), C (68), C# (69), D (55)
    (note_duration * 8, 67, 100),
    (note_duration * 9, 68, 100),
    (note_duration * 10, 69, 100),
    (note_duration * 11, 55, 100),
    # Bar 4: E (57), F (58), F# (59), G (62)
    (note_duration * 12, 57, 100),
    (note_duration * 13, 58, 100),
    (note_duration * 14, 59, 100),
    (note_duration * 15, 62, 100)
]

for time, note_number, velocity in bass_notes:
    instruments['bass'].notes.append(Note(note_number, velocity, time, note_duration * 0.25))

# PIANO: 7th chords, comp on 2 and 4
# D7 (55, 57, 59, 62)
# G7 (62, 64, 67, 70)
# C7 (60, 62, 64, 67)
# F7 (58, 60, 62, 65)

piano_notes = []

# Bar 2: D7 on beat 2
note_on = note_duration * 1
piano_notes.extend([
    (note_on, 55, 90),
    (note_on, 57, 90),
    (note_on, 59, 90),
    (note_on, 62, 90)
])

# Bar 3: G7 on beat 2
note_on = note_duration * 5
piano_notes.extend([
    (note_on, 62, 90),
    (note_on, 64, 90),
    (note_on, 67, 90),
    (note_on, 70, 90)
])

# Bar 4: C7 on beat 2
note_on = note_duration * 9
piano_notes.extend([
    (note_on, 60, 90),
    (note_on, 62, 90),
    (note_on, 64, 90),
    (note_on, 67, 90)
])

# Bar 4: F7 on beat 4
note_on = note_duration * 13
piano_notes.extend([
    (note_on, 58, 90),
    (note_on, 60, 90),
    (note_on, 62, 90),
    (note_on, 65, 90)
])

for time, note_number, velocity in piano_notes:
    instruments['piano'].notes.append(Note(note_number, velocity, time, note_duration * 0.5))

# SAX: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: D (55), F# (59), A (64)
    (note_duration * 1, 55, 100),
    (note_duration * 1.25, 59, 100),
    (note_duration * 1.5, 64, 100),

    # Silence for tension

    # Bar 3: D (55), B (67)
    (note_duration * 5, 55, 100),
    (note_duration * 5.75, 67, 100),

    # Bar 4: F# (59), A (64), D (55)
    (note_duration * 9, 59, 100),
    (note_duration * 9.5, 64, 100),
    (note_duration * 10, 55, 100)
]

for time, note_number, velocity in sax_notes:
    instruments['sax'].notes.append(Note(note_number, velocity, time, note_duration * 0.25))

# Write the MIDI file to disk
pm.write("dante_russo_intro.mid")
