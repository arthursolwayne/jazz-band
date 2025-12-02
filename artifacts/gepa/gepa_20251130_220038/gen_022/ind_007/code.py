
from music21 import *
import numpy as np

# Set tempo and time signature
tempo = 160
time_signature = '4/4'

# Define key
key = 'F major'

# Create a new stream
s = stream.Stream()
s.append(tempo.MetronomeMark(number=tempo))
s.append(meter.TimeSignature(time_signature))

# Define the 4-bar structure

# BAR 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth
drum_pattern = [
    note.Note('kick', type='quarter'), note.Note('snare', type='quarter'),
    note.Note('kick', type='quarter'), note.Note('snare', type='quarter'),
    note.Note('hihat', type='eighth'), note.Note('hihat', type='eighth'),
    note.Note('hihat', type='eighth'), note.Note('hihat', type='eighth'),
    note.Note('hihat', type='eighth'), note.Note('hihat', type='eighth'),
    note.Note('hihat', type='eighth'), note.Note('hihat', type='eighth'),
    note.Note('hihat', type='eighth'), note.Note('hihat', type='eighth'),
    note.Note('hihat', type='eighth'), note.Note('hihat', type='eighth')
]
drums = stream.Part(id='Drums')
drums.timeSignature = meter.TimeSignature(time_signature)
for n in drum_pattern:
    drums.append(n)
s.insert(0, drums)

# BAR 1: Marcus on bass — chromatic walking line
bass_part = stream.Part(id='Bass', instrument=instrument.Bass())
bass_line = [
    note.Note('F', type='quarter'),
    note.Note('F#', type='eighth'),
    note.Note('G', type='eighth'),
    note.Note('G#', type='quarter'),
    note.Note('A', type='eighth'),
    note.Note('A#', type='eighth'),
    note.Note('Bb', type='quarter'),
    note.Note('B', type='eighth'),
    note.Note('C', type='eighth'),
    note.Note('C#', type='quarter'),
    note.Note('D', type='eighth'),
    note.Note('D#', type='eighth'),
    note.Note('Eb', type='quarter'),
    note.Note('E', type='eighth'),
    note.Note('F', type='eighth'),
    note.Note('F', type='quarter')
]
for n in bass_line:
    bass_part.append(n)
s.insert(0, bass_part)

# BAR 1: Diane on piano — 7th chords on 2 and 4
piano_part = stream.Part(id='Piano', instrument=instrument.Piano())
chords = [
    chord.Chord(['F', 'A', 'C', 'D#'], quarterLength=1),
    chord.Chord(['G', 'Bb', 'D', 'F'], quarterLength=1),
    chord.Chord(['A', 'C', 'E', 'G'], quarterLength=1),
    chord.Chord(['Bb', 'D', 'F', 'A'], quarterLength=1)
]
for c in chords:
    piano_part.append(c)
s.insert(0, piano_part)

# BAR 2–4: You on sax — haunting, simple, with rests and unique durations
sax_part = stream.Part(id='Sax', instrument=instrument.Saxophone())
# Motif: F - Eb - D - rest - C - Bb - rest - F
sax_notes = [
    note.Note('F', type='eighth'),
    note.Note('Eb', type='eighth'),
    note.Note('D', type='quarter'),  
    note.Rest(type='quarter'),
    note.Note('C', type='eighth'),
    note.Note('Bb', type='eighth'),
    note.Rest(type='quarter'),
    note.Note('F', type='quarter')
]
for n in sax_notes:
    sax_part.append(n)
s.insert(0, sax_part)

# Output to MIDI
s.show('midi')
s.show('text')
