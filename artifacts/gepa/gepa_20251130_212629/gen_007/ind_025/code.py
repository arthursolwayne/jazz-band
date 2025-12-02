
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F major
key = 'F'

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)

# Set the time signature
midi.time_signature_changes = [time_signature]

# Define the tempo (BPM)
midi.tempo_changes = [pretty_midi.TempoChange(tempo=160, time=0)]

# Define the note durations in terms of beats
beat = 60.0 / 160  # seconds per beat
bar_length = 4 * beat  # seconds per bar

# Create instruments
sax_instrument = pretty_midi.Instrument(program=64)  # Tenor sax
piano_instrument = pretty_midi.Instrument(program=0)  # Piano
bass_instrument = pretty_midi.Instrument(program=33)  # Bass
drums_instrument = pretty_midi.Instrument(program=128)  # Drums

# Add instruments to the MIDI
midi.instruments = [sax_instrument, piano_instrument, bass_instrument, drums_instrument]

# Helper function to convert note name to MIDI number
def note_to_midi(note):
    note_map = {
        'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3, 'E': 4,
        'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8, 'Ab': 8, 'A': 9,
        'A#': 10, 'Bb': 10, 'B': 11
    }
    octave = note[-1]
    if octave == '': octave = 4
    else: octave = int(octave)
    note_name = note[:-1]
    return note_map[note_name] + (octave + 1) * 12

# Function to add a note to an instrument
def add_note(instrument, note_name, start, end, velocity=100):
    note_number = note_to_midi(note_name)
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=end)
    instrument.notes.append(note)

# DRUMS: Bar 1 - Little Ray sets it up
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * bar_length + beat * beat
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            add_note(drums_instrument, 'C1', time, time + 0.1, velocity=100)
        elif beat == 1 or beat == 3:
            # Snare on 2 and 4
            add_note(drums_instrument, 'Snare', time, time + 0.1, velocity=100)
        # Hi-Hat on every eighth note
        for eighth in range(2):
            add_note(drums_instrument, 'HiHat', time + eighth * 0.1875, time + eighth * 0.1875 + 0.05, velocity=80)

# BASS: Walking line, chromatic approaches, no repeated notes
# Bar 1: F - Gb - G - A (chromatic approach)
# Bar 2: Bb - B - C - D (chromatic approach)
# Bar 3: E - F - G - Ab (chromatic approach)
# Bar 4: D - Eb - F - G (chromatic approach)

for bar in range(4):
    start_time = bar * bar_length
    if bar == 0:
        notes = ['F2', 'Gb2', 'G2', 'A2']
    elif bar == 1:
        notes = ['Bb2', 'B2', 'C2', 'D2']
    elif bar == 2:
        notes = ['E2', 'F2', 'G2', 'Ab2']
    else:
        notes = ['D2', 'Eb2', 'F2', 'G2']
    for i, note in enumerate(notes):
        add_note(bass_instrument, note, start_time + i * beat, start_time + (i + 1) * beat, velocity=70)

# PIANO: 7th chords, on 2 and 4, comp on 2 and 4
# Bar 1: F7 on beat 2 and 4
# Bar 2: Bb7 on beat 2 and 4
# Bar 3: E7 on beat 2 and 4
# Bar 4: D7 on beat 2 and 4

chords = {
    0: {'F7': [note_to_midi('F'), note_to_midi('A'), note_to_midi('C'), note_to_midi('E')], 'time': 1},
    1: {'Bb7': [note_to_midi('Bb'), note_to_midi('D'), note_to_midi('F'), note_to_midi('Ab')], 'time': 1},
    2: {'E7': [note_to_midi('E'), note_to_midi('G'), note_to_midi('B'), note_to_midi('D')], 'time': 1},
    3: {'D7': [note_to_midi('D'), note_to_midi('F'), note_to_midi('A'), note_to_midi('C')], 'time': 1}
}

for bar in range(4):
    start_time = bar * bar_length
    chord = chords[bar]
    chord_notes = chord['F7'] if bar == 0 else chord['Bb7'] if bar == 1 else chord['E7'] if bar == 2 else chord['D7']
    for note in chord_notes:
        add_note(piano_instrument, f"{note_to_midi(note)}", start_time + chord['time'] * beat, start_time + chord['time'] * beat + 0.5, velocity=80)
    # Add root note on beat 2 and 4
    add_note(piano_instrument, 'F3', start_time + 1 * beat, start_time + 1 * beat + 0.5, velocity=100)
    add_note(piano_instrument, 'F3', start_time + 3 * beat, start_time + 3 * beat + 0.5, velocity=100)

# SAX: Melody in F major (Bars 2-4)
# Bar 1: Rest (drums only)
# Bar 2: Start of motif
# Bar 3: Continue, leave it hanging
# Bar 4: Resolve

# Bar 2: F - G - A - Bb (motive)
# Bar 3: C - D - Eb - F (continuation)
# Bar 4: G - A - Bb - C (resolution)

for bar in range(2, 4):
    start_time = bar * bar_length
    if bar == 2:
        notes = ['F4', 'G4', 'A4', 'Bb4']
    elif bar == 3:
        notes = ['C4', 'D4', 'Eb4', 'F4']
    else:
        notes = ['G4', 'A4', 'Bb4', 'C5']
    for i, note in enumerate(notes):
        add_note(sax_instrument, note, start_time + i * beat, start_time + (i + 1) * beat, velocity=110)

# Save the MIDI file
midi.write("waynes_shot.mid")
