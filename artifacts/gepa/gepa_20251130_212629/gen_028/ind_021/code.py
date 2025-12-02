
import pretty_midi
import numpy as np

# Constants
BPM = 160
TEMPO = 60 / BPM  # seconds per beat
BAR_DURATION = 1.5  # seconds per bar
NOTE_DURATION = 0.25  # quarter note in seconds
REST_DURATION = 0.25  # quarter note in seconds
TIME_SIGNATURE = (4, 4)
KEY = 'F'

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(*TIME_SIGNATURE, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(BPM, 0.0)]

# Function to convert note name to MIDI note number
def note_to_midi(note, octave=4):
    note_map = {'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
                'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
                'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11}
    return note_map[note] + (octave + 1) * 12

# Instrument assignments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instruments
drums = pretty_midi.Instrument(program=drums_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, piano, bass, sax]

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick_notes = [note_to_midi('C', 3)]  # C3
snare_notes = [note_to_midi('C', 4)]  # C4
hihat_notes = [note_to_midi('C', 5)]  # C5

time = 0
for i in range(4):
    if i == 0 or i == 2:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=100, pitch=kick_notes[0], start=time, end=time + NOTE_DURATION)
        drums.notes.append(note)
    if i == 1 or i == 3:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=90, pitch=snare_notes[0], start=time, end=time + NOTE_DURATION)
        drums.notes.append(note)
    # Hihat on every eighth
    for j in range(2):
        note = pretty_midi.Note(velocity=60, pitch=hihat_notes[0], start=time + j * (NOTE_DURATION / 2),
                                end=time + j * (NOTE_DURATION / 2) + (NOTE_DURATION / 2))
        drums.notes.append(note)
    time += NOTE_DURATION

# Bar 2-4: All instruments in
# Bar 2: Start of melody
sax_notes = [note_to_midi('G', 4), note_to_midi('A', 4), note_to_midi('Bb', 4), note_to_midi('C', 5)]
time = 0.75  # Bar 1 is 1.5 seconds, we start on the 3rd beat of Bar 2

# Sax melody: G4 - A4 - Bb4 - C5 (half note, then rest)
note = pretty_midi.Note(velocity=100, pitch=sax_notes[0], start=time, end=time + NOTE_DURATION)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=sax_notes[1], start=time + NOTE_DURATION, end=time + 2 * NOTE_DURATION)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=sax_notes[2], start=time + 2 * NOTE_DURATION, end=time + 3 * NOTE_DURATION)
sax.notes.append(note)
note = pretty_midi.Note(velocity=100, pitch=sax_notes[3], start=time + 3 * NOTE_DURATION, end=time + 4 * NOTE_DURATION)
sax.notes.append(note)

# Piano: 7th chords on 2 and 4
# F7 (F, A, C, Eb)
piano_notes = [note_to_midi('F', 4), note_to_midi('A', 4), note_to_midi('C', 5), note_to_midi('Eb', 5)]
time = 1.5  # Bar 2, beat 2
note = pretty_midi.Note(velocity=80, pitch=piano_notes[0], start=time, end=time + NOTE_DURATION)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=piano_notes[1], start=time, end=time + NOTE_DURATION)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=piano_notes[2], start=time, end=time + NOTE_DURATION)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=piano_notes[3], start=time, end=time + NOTE_DURATION)
piano.notes.append(note)

time = 3.0  # Bar 2, beat 4
note = pretty_midi.Note(velocity=80, pitch=piano_notes[0], start=time, end=time + NOTE_DURATION)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=piano_notes[1], start=time, end=time + NOTE_DURATION)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=piano_notes[2], start=time, end=time + NOTE_DURATION)
piano.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=piano_notes[3], start=time, end=time + NOTE_DURATION)
piano.notes.append(note)

# Bass: Walking line with chromatic approach
bass_notes = [note_to_midi('F', 3), note_to_midi('G', 3), note_to_midi('Ab', 3), note_to_midi('A', 3),
              note_to_midi('Bb', 3), note_to_midi('B', 3), note_to_midi('C', 4), note_to_midi('Db', 4)]
time = 0.0  # Start of Bar 2

for i in range(4):
    note = pretty_midi.Note(velocity=70, pitch=bass_notes[i * 2], start=time + i * NOTE_DURATION,
                            end=time + i * NOTE_DURATION + NOTE_DURATION)
    bass.notes.append(note)
    note = pretty_midi.Note(velocity=60, pitch=bass_notes[i * 2 + 1], start=time + i * NOTE_DURATION,
                            end=time + i * NOTE_DURATION + NOTE_DURATION)
    bass.notes.append(note)

# Drums continue with same pattern
time = 1.5  # Bar 2
for i in range(2):
    if i == 0 or i == 2:
        note = pretty_midi.Note(velocity=100, pitch=kick_notes[0], start=time + i * NOTE_DURATION,
                                end=time + i * NOTE_DURATION + NOTE_DURATION)
        drums.notes.append(note)
    if i == 1 or i == 3:
        note = pretty_midi.Note(velocity=90, pitch=snare_notes[0], start=time + i * NOTE_DURATION,
                                end=time + i * NOTE_DURATION + NOTE_DURATION)
        drums.notes.append(note)
    for j in range(2):
        note = pretty_midi.Note(velocity=60, pitch=hihat_notes[0], start=time + i * NOTE_DURATION + j * (NOTE_DURATION / 2),
                                end=time + i * NOTE_DURATION + j * (NOTE_DURATION / 2) + (NOTE_DURATION / 2))
        drums.notes.append(note)

# Save MIDI file
pm.write('jazz_intro.mid')
print("MIDI file 'jazz_intro.mid' created successfully.")
