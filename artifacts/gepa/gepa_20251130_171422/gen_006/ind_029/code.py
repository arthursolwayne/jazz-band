
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Define the key: F Major (F, G, A, Bb, C, D, E)
key = 'F'

# Define instrument programs
tenor_sax_program = Program(66)  # Tenor Saxophone
bass_program = Program(33)      # Acoustic Bass
piano_program = Program(0)     # Acoustic Grand Piano
drums_program = Program(0)     # Acoustic Drums

# Create instruments
tenor_sax = Instrument(program=tenor_sax_program)
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)

pm.instruments.append(tenor_sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Define note durations and timing
beat = 60.0 / tempo  # seconds per beat
bar = beat * 4       # seconds per bar
resolution = 100     # MIDI resolution

# Function to add a note
def add_note(instrument, pitch, start, duration, velocity=100):
    note = Note(pitch=pitch, start=start, end=start + duration, velocity=velocity)
    instrument.notes.append(note)

# Define the tempo and time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% DRUMS %%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Bar 1: Snare on 2 and 4, hihat on every eighth
drum_notes = [
    (38, 0.0, 0.125),  # Hihat on 1
    (38, 0.125, 0.125), # Hihat on 2
    (38, 0.25, 0.125),  # Hihat on 3
    (38, 0.375, 0.125), # Hihat on 4
    (38, 0.5, 0.125),   # Hihat on 5
    (38, 0.625, 0.125), # Hihat on 6
    (38, 0.75, 0.125),  # Hihat on 7
    (38, 0.875, 0.125), # Hihat on 8
    (39, 0.5, 0.125),   # Snare on 2
    (39, 0.875, 0.125)  # Snare on 4
]

for pitch, start, duration in drum_notes:
    add_note(drums, pitch, start, duration)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% BASS %%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Bar 1: Walking line in F major
# F -> Bb -> C -> Eb (chromatic approach to A)
bass_notes = [
    (65, 0.0, 0.25),  # F
    (67, 0.25, 0.25), # Bb
    (69, 0.5, 0.25),  # C
    (67, 0.75, 0.25)  # Eb
]

for pitch, start, duration in bass_notes:
    add_note(bass, pitch, start, duration)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% PIANO %%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Bar 1: Comp on 2 and 4
# F7 on beat 2 (F, A, C, E)
# F7 on beat 4 (F, A, C, E)
piano_notes = [
    (65, 0.25, 0.25), # F
    (69, 0.25, 0.25), # A
    (69, 0.25, 0.25), # C
    (72, 0.25, 0.25), # E

    (65, 0.75, 0.25), # F
    (69, 0.75, 0.25), # A
    (69, 0.75, 0.25), # C
    (72, 0.75, 0.25)  # E
]

for pitch, start, duration in piano_notes:
    add_note(piano, pitch, start, duration)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% TENOR SAX %%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Bar 1: Silence

# Bar 2: Tenor sax motif
# F -> Bb -> C -> Eb (same as bass, but with space)
# Start on beat 1, end on beat 3 (hold)
# Then release on beat 4

tenor_notes = [
    (65, 1.0, 0.5),  # F
    (67, 1.5, 0.5),  # Bb
    (69, 2.0, 0.5),  # C
    (67, 2.5, 0.5)   # Eb
]

for pitch, start, duration in tenor_notes:
    add_note(tenor_sax, pitch, start, duration)

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%% FINALIZE %%%%%%%%%%%%%%%%%%%%%%

# Save the MIDI file
pm.save('intro_in_f.mid')

print("MIDI file saved as 'intro_in_f.mid'")
