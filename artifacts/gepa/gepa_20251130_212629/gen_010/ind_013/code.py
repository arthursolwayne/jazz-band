
import pretty_midi
from pretty_midi import Note, Instrument

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to D minor (you can adjust this if you want D major)
key_signature = pretty_midi.KeySignature(key_number=2)  # D minor
pm.key_signature = key_signature

# Define the tempo and time signature
pm.time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # We'll use this for drum kit
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time per bar (160 BPM = 6/160 = 0.375 seconds per beat, 1.5 seconds per bar)
time_per_bar = 1.5

# Bar 1 - Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: 0.0 seconds to 1.5 seconds

# Kick on 1 (0.0) and 3 (1.125)
drums.notes.append(Note(36, 60, 0.0, 0.125))
drums.notes.append(Note(36, 60, 1.125, 1.25))

# Snare on 2 (0.75) and 4 (1.5)
drums.notes.append(Note(38, 65, 0.75, 0.875))
drums.notes.append(Note(38, 65, 1.5, 1.625))

# Hihat on every eighth
for i in range(0, 8):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(Note(42, 60, start, end))

# Bar 2 - All instruments come in
# Bar 2 starts at 1.5 seconds

# Bass line: walking line, chromatic approach, no repeating notes
# D minor scale: D, E♭, F, G, A, B♭, C
# Walking bass line in D minor
bass_notes = [
    (1.5, 62),  # D (C4 = 60, D is 62)
    (1.875, 61),  # C (chromatic down)
    (2.25, 65),  # G
    (2.625, 64),  # F (chromatic down)
    (3.0, 62),  # D
    (3.375, 61),  # C
    (3.75, 65),  # G
    (4.125, 64),  # F
]

for start, pitch in bass_notes:
    bass.notes.append(Note(36, pitch, start, start + 0.25))

# Piano: Comp on 2 and 4, 7th chords
# Start at 1.5 seconds

# Bar 2: D7 chord (D, F#, A, C) - 7th chord
# On beat 2 and 4
piano.notes.append(Note(48, 62, 1.5 + 0.75, 1.5 + 0.875))  # D4
piano.notes.append(Note(48, 67, 1.5 + 0.75, 1.5 + 0.875))  # F#4
piano.notes.append(Note(48, 69, 1.5 + 0.75, 1.5 + 0.875))  # A4
piano.notes.append(Note(48, 64, 1.5 + 0.75, 1.5 + 0.875))  # C4

# Bar 2: On beat 4 (1.5 + 1.5 = 3.0)
piano.notes.append(Note(48, 62, 3.0, 3.125))
piano.notes.append(Note(48, 67, 3.0, 3.125))
piano.notes.append(Note(48, 69, 3.0, 3.125))
piano.notes.append(Note(48, 64, 3.0, 3.125))

# Sax: Motif — short, singable, leaves it hanging
# The motif: D, F#, G, D (D7 interval, but with a pull)
# Start at 1.5 seconds
sax.notes.append(Note(62, 62, 1.5, 1.625))
sax.notes.append(Note(62, 67, 1.625, 1.75))
sax.notes.append(Note(62, 69, 1.75, 1.875))
sax.notes.append(Note(62, 62, 1.875, 2.0))  # Hold D on beat 4

# Add the motif again at the end of the intro (bar 4)
sax.notes.append(Note(62, 62, 3.0, 3.125))
sax.notes.append(Note(62, 67, 3.125, 3.25))
sax.notes.append(Note(62, 69, 3.25, 3.375))
sax.notes.append(Note(62, 62, 3.375, 3.5))  # End on D

# Add drums again for bar 3 and 4
# Bar 3 (same as bar 1)
for i in range(0, 8):
    start = 1.5 + i * 0.375
    end = start + 0.125
    drums.notes.append(Note(42, 60, start, end))

drums.notes.append(Note(36, 60, 1.5, 1.625))
drums.notes.append(Note(36, 60, 2.625, 2.75))
drums.notes.append(Note(38, 65, 2.25, 2.375))
drums.notes.append(Note(38, 65, 3.5, 3.625))

# Bar 4: Same drum pattern
for i in range(0, 8):
    start = 3.0 + i * 0.375
    end = start + 0.125
    drums.notes.append(Note(42, 60, start, end))

drums.notes.append(Note(36, 60, 3.0, 3.125))
drums.notes.append(Note(36, 60, 4.125, 4.25))
drums.notes.append(Note(38, 65, 3.75, 3.875))
drums.notes.append(Note(38, 65, 4.5, 4.625))

# Save the MIDI
pm.write("dante_intro.mid")
