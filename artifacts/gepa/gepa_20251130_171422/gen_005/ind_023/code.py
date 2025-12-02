
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time in seconds per beat
beats_per_bar = 4
bpm = 160
seconds_per_beat = 60.0 / bpm
seconds_per_bar = seconds_per_beat * beats_per_bar

# Create instruments
bass_program = Program(instrument=Program.BASS, is_drum=False)
piano_program = Program(instrument=Program.ACOUSTIC_PIANO, is_drum=False)
sax_program = Program(instrument=Program.TENOR_SAX, is_drum=False)
drums_program = Program(instrument=Program.DRUMS, is_drum=True)

bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
sax = Instrument(program=sax_program)
drums = Instrument(program=drums_program)

pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(sax)
pm.instruments.append(drums)

# Helper function to add note
def add_note(instrument, pitch, start, end, velocity=100):
    note = Note(pitch=pitch, start=start, end=end, velocity=velocity)
    instrument.notes.append(note)

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = [0, 0, 0, 0]
snare = [0, 0, 0, 0]
hihat = [0, 0, 0, 0]

# Kick on 1 and 3
kick[0] = 36  # Kick drum
kick[2] = 36

# Snare on 2 and 4
snare[1] = 38  # Snare drum
snare[3] = 38

# Hihat on every eighth
hihat[0] = 42  # Hihat
hihat[1] = 42
hihat[2] = 42
hihat[3] = 42

# Add drum notes
for i in range(4):
    time = i * seconds_per_beat
    if kick[i] != 0:
        add_note(drums, kick[i], time, time + 0.1)
    if snare[i] != 0:
        add_note(drums, snare[i], time, time + 0.1)
    if hihat[i] != 0:
        add_note(drums, hihat[i], time, time + 0.05)

# Bar 2: All instruments join
# Bass - walking line with chromatic approach
bass_notes = [
    (48, 0.0),   # F
    (49, 0.5),   # G
    (47, 1.0),   # E
    (48, 1.5),   # F
]

for note, time in bass_notes:
    add_note(bass, note, time, time + 0.5)

# Piano - 7th chords on beats 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb) on beat 2
    (53, 1.0),   # A
    (60, 1.0),   # C
    (58, 1.0),   # Bb
    (55, 1.0),   # G
    # Bar 3: Bb7 (Bb, D, F, Ab) on beat 4
    (57, 2.5),   # D
    (60, 2.5),   # F
    (55, 2.5),   # G
    (61, 2.5),   # Ab
]

for note, time in piano_notes:
    add_note(piano, note, time, time + 1.0)

# Sax - short motif, start it, leave it hanging
# Motif: F, Bb, F (on beats 1, 2, 3), leave on beat 4
sax_notes = [
    (53, 0.0),   # Bb
    (58, 0.5),   # F
    (53, 1.0),   # Bb
]

for note, time in sax_notes:
    add_note(sax, note, time, time + 0.5)

# Bar 3: Continue the motif, leave it hanging
# Add a resolution on beat 4, but don't resolve completely
sax_notes = [
    (56, 1.5),   # D
    (53, 2.0),   # Bb
]

for note, time in sax_notes:
    add_note(sax, note, time, time + 0.5)

# Bar 4: Continue the tension, don't resolve
# Keep the motif open, let it echo
sax_notes = [
    (53, 2.5),   # Bb
    (58, 3.0),   # F
    (53, 3.5),   # Bb
]

for note, time in sax_notes:
    add_note(sax, note, time, time + 0.5)

# Save the MIDI file
pm.write("jazz_intro.mid")
