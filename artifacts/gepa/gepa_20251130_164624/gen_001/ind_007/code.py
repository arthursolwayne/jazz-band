
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drum_program = pretty_midi.instrument_name_to_program('Drums')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drum_program)

# Helper function to add note
def add_note(instrument, pitch, start, end, velocity=100):
    note = pretty_midi.Note(velocity, pitch, start, end)
    instrument.notes.append(note)

# Bar duration in seconds (160 BPM, 4/4 time)
bar_length = 60.0 / 160 * 4

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for beat in range(4):
    time = beat * (bar_length / 4)
    if beat % 2 == 0:
        add_note(drums, pretty_midi.note_number_to_name(36), time, time + 0.125, 100)  # Kick
        add_note(drums, pretty_midi.note_number_to_name(56), time, time + 0.125, 80)  # Hihat
    else:
        add_note(drums, pretty_midi.note_number_to_name(49), time, time + 0.125, 100)  # Snare
        add_note(drums, pretty_midi.note_number_to_name(56), time, time + 0.125, 80)  # Hihat

# Bar 2: Everyone enters
# Bass line: Walking line, chromatic approaches
bass_notes = [
    (62, 0.0),  # D4
    (63, 0.25), # Eb4
    (64, 0.5),  # E4
    (62, 0.75), # D4
    (60, 1.0),  # C4
    (62, 1.25), # D4
    (63, 1.5),  # Eb4
    (64, 1.75), # E4
    (62, 2.0),  # D4
]

for pitch, time in bass_notes:
    add_note(bass, pitch, time, time + 0.25)

# Piano: 7th chords, comp on 2 and 4
# Bar 2: D7 (D F# A C#)
# Bar 3: F#7 (F# A# C# E)
# Bar 4: B7 (B D# F# A)
for beat in range(4):
    time = beat * (bar_length / 4)
    if beat in [1, 3]:
        if beat == 1:
            # D7
            add_note(piano, 62, time, time + 0.25)
            add_note(piano, 67, time, time + 0.25)
            add_note(piano, 69, time, time + 0.25)
            add_note(piano, 72, time, time + 0.25)
        else:
            # F#7
            add_note(piano, 67, time, time + 0.25)
            add_note(piano, 72, time, time + 0.25)
            add_note(piano, 74, time, time + 0.25)
            add_note(piano, 77, time, time + 0.25)

# Saxophone melody: One short motif, make it sing
# Start on D, go to F#, back to C#, end on D
# Bar 2: D (62) -> F# (67) -> C# (67) -> D (62)
add_note(sax, 62, 0.0, 0.375)
add_note(sax, 67, 0.375, 0.75)
add_note(sax, 67, 0.75, 1.125)
add_note(sax, 62, 1.125, 1.5)

# Add the rest of the sax melody in bar 3 and 4
# Bar 3: A (69) -> G (67) -> F# (67) -> D (62)
add_note(sax, 69, 1.5, 1.875)
add_note(sax, 67, 1.875, 2.25)
add_note(sax, 67, 2.25, 2.625)
add_note(sax, 62, 2.625, 3.0)

# Bar 4: Drums continue
for beat in range(4):
    time = (beat + 2) * (bar_length / 4)
    if beat % 2 == 0:
        add_note(drums, pretty_midi.note_number_to_name(36), time, time + 0.125, 100)  # Kick
        add_note(drums, pretty_midi.note_number_to_name(56), time, time + 0.125, 80)  # Hihat
    else:
        add_note(drums, pretty_midi.note_number_to_name(49), time, time + 0.125, 100)  # Snare
        add_note(drums, pretty_midi.note_number_to_name(56), time, time + 0.125, 80)  # Hihat

# Add the instruments to the PrettyMIDI object
pm.instruments.append(sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Save the MIDI file
pm.write("dante_intro.mid")
