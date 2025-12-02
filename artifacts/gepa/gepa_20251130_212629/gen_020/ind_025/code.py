
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key (D major)
key = 'D'

# Define the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the length of a bar (1.5 seconds at 160 BPM)
bar_length = 1.5

# Define the note values and MIDI notes for D major
note_values = {
    'D4': 62,
    'E4': 64,
    'F#4': 66,
    'G4': 67,
    'A4': 69,
    'B4': 71,
    'C#5': 73
}

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Add instruments
drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
def add_drums(pm, instrument, time, start_time, note, duration):
    note_event = pretty_midi.Note(
        velocity=100,
        pitch=note,
        start=start_time,
        end=start_time + duration
    )
    instrument.notes.append(note_event)

# Bar 1 - Drums
time = 0
bar_start = 0
bar_end = bar_length

# Kick on 1 and 3
add_drums(drums, drums, time, bar_start, 36, 0.375)
add_drums(drums, drums, time, bar_start + 0.75, 36, 0.375)

# Snare on 2 and 4
add_drums(drums, drums, time, bar_start + 0.375, 38, 0.375)
add_drums(drums, drums, time, bar_start + 1.125, 38, 0.375)

# Hi-hat on every eighth
for i in range(0, 8):
    add_drums(drums, drums, time, bar_start + i * 0.375, 42, 0.375)

# Bar 2: Ensemble enters
# Bass: Walking line, chromatic approach to D (C# -> D)
bass_notes = [note_values['C#5'], note_values['D4'], note_values['E4'],
              note_values['F#4'], note_values['G4'], note_values['A4'],
              note_values['B4'], note_values['C#5']]

bass_times = [bar_start + 0.0, bar_start + 0.5, bar_start + 1.0, bar_start + 1.5,
              bar_start + 2.0, bar_start + 2.5, bar_start + 3.0, bar_start + 3.5]

for i in range(len(bass_notes)):
    note_event = pretty_midi.Note(
        velocity=80,
        pitch=bass_notes[i],
        start=bass_times[i],
        end=bass_times[i] + 0.25
    )
    bass.notes.append(note_event)

# Piano: 7th chords on 2 and 4 (D7, G7)
# D7 (D, F#, A, C)
# G7 (G, B, D, F)
piano_notes = [note_values['D4'], note_values['F#4'], note_values['A4'], note_values['C5'],
               note_values['G4'], note_values['B4'], note_values['D5'], note_values['F5']]

piano_times = [bar_start + 0.5, bar_start + 0.5, bar_start + 0.5, bar_start + 0.5,
               bar_start + 1.5, bar_start + 1.5, bar_start + 1.5, bar_start + 1.5]

for i in range(len(piano_notes)):
    note_event = pretty_midi.Note(
        velocity=90,
        pitch=piano_notes[i],
        start=piano_times[i],
        end=piano_times[i] + 0.25
    )
    piano.notes.append(note_event)

# Sax: Short motif, starts on D4, ends on G4 with a rest
sax_notes = [note_values['D4'], note_values['F#4'], note_values['G4']]
sax_times = [bar_start, bar_start + 0.75, bar_start + 1.0]

for i in range(len(sax_notes)):
    note_event = pretty_midi.Note(
        velocity=100,
        pitch=sax_notes[i],
        start=sax_times[i],
        end=sax_times[i] + 0.25
    )
    sax.notes.append(note_event)

# Bar 3: Sax continues with rhythm offset
sax_notes = [note_values['A4'], note_values['C#5'], note_values['B4']]
sax_times = [bar_start + 1.125, bar_start + 1.875, bar_start + 2.125]

for i in range(len(sax_notes)):
    note_event = pretty_midi.Note(
        velocity=100,
        pitch=sax_notes[i],
        start=sax_times[i],
        end=sax_times[i] + 0.25
    )
    sax.notes.append(note_event)

# Bar 4: Sax returns with variation, ends on a suspended note
sax_notes = [note_values['D4'], note_values['E4'], note_values['F#4'], note_values['G4']]
sax_times = [bar_start + 2.25, bar_start + 2.75, bar_start + 3.25, bar_start + 3.5]

for i in range(len(sax_notes)):
    note_event = pretty_midi.Note(
        velocity=100,
        pitch=sax_notes[i],
        start=sax_times[i],
        end=sax_times[i] + 0.25
    )
    sax.notes.append(note_event)

# Save the MIDI file
pm.write('dante_intro.mid')
