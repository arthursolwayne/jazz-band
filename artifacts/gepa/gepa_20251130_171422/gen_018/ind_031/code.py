
import pretty_midi
from pretty_midi import note_number_to_name, Note

# Create a new PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up instruments
drums = pretty_midi.Instrument(program=10)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Define the tempo (160 BPM)
# 1 bar = 6 seconds, so each beat = 0.375 seconds
# 60 / 160 = 0.375 seconds per beat
# Each bar = 1.5 seconds (4 beats)

# Define time in seconds
beat_time = 0.375  # seconds per beat
bar_time = beat_time * 4  # 1.5 seconds per bar
total_time = bar_time * 4  # 6 seconds total

#---------------------
# Bar 1: Little Ray on Drums (4/4 time, 6/8 feel)
#---------------------
# Kick on 1 and 3
drums.notes.append(Note(36, 100, time=0, duration=0.125))  # Kick on 1
drums.notes.append(Note(36, 100, time=beat_time * 2, duration=0.125))  # Kick on 3

# Snare on 2 and 4
drums.notes.append(Note(38, 100, time=beat_time, duration=0.125))  # Snare on 2
drums.notes.append(Note(38, 100, time=beat_time * 3, duration=0.125))  # Snare on 4

# Hi-hats on every eighth note
for i in range(0, 8):
    time = i * beat_time / 2
    if i % 2 == 0:
        drums.notes.append(Note(42, 100, time=time, duration=0.0625))  # Closed hi-hat
    else:
        drums.notes.append(Note(43, 100, time=time, duration=0.0625))  # Open hi-hat

#---------------------
# Bar 2: All instruments join in
#---------------------

# Bass line: walking line with chromatic approaches
bass_notes = [
    (62, 0),  # D3 (root)
    (64, 0.25),  # E3 (chromatic up)
    (61, 0.5),  # C#3 (chromatic down)
    (63, 0.75),  # D#3
    (65, 1),  # F3
    (62, 1.25),  # D3
    (64, 1.5),  # E3
    (61, 1.75),  # C#3
    (63, 2),  # D#3
    (65, 2.25),  # F3
    (62, 2.5),  # D3
    (64, 2.75),  # E3
    (61, 3),  # C#3
    (63, 3.25),  # D#3
    (65, 3.5),  # F3
    (62, 3.75),  # D3
    (64, 4),  # E3
    (61, 4.25),  # C#3
    (63, 4.5),  # D#3
    (65, 4.75),  # F3
]

for note_num, time in bass_notes:
    bass.notes.append(Note(note_num, 90, time=time, duration=0.25))

# Piano: 7th chords on 2 and 4
# D7 = D, F#, A, C
# G7 = G, B, D, F
# Bm7b5 = B, D, F, A
# E7 = E, G#, B, D
# Vamp on 2 and 4

# Bar 2: Time = 1.5s
piano.notes.append(Note(62, 100, time=1.5, duration=0.25))  # D
piano.notes.append(Note(67, 100, time=1.5, duration=0.25))  # F#
piano.notes.append(Note(69, 100, time=1.5, duration=0.25))  # A
piano.notes.append(Note(64, 100, time=1.5, duration=0.25))  # C

# Bar 3: Time = 3.0s
piano.notes.append(Note(67, 100, time=3.0, duration=0.25))  # G
piano.notes.append(Note(71, 100, time=3.0, duration=0.25))  # B
piano.notes.append(Note(69, 100, time=3.0, duration=0.25))  # D
piano.notes.append(Note(66, 100, time=3.0, duration=0.25))  # F

# Bar 4: Time = 4.5s
piano.notes.append(Note(69, 100, time=4.5, duration=0.25))  # B
piano.notes.append(Note(71, 100, time=4.5, duration=0.25))  # D
piano.notes.append(Note(67, 100, time=4.5, duration=0.25))  # F
piano.notes.append(Note(69, 100, time=4.5, duration=0.25))  # A

#---------------------
# Sax: Your motif
#---------------------
# Start with a short motif: D, F#, B, D
# Then leave it hanging: a rest after D
# Then restate the motif with a slight variation

# Bar 2 (start of motif)
sax.notes.append(Note(62, 110, time=1.5, duration=0.25))  # D
sax.notes.append(Note(67, 110, time=1.75, duration=0.25))  # F#
sax.notes.append(Note(69, 110, time=2.0, duration=0.25))  # B
sax.notes.append(Note(62, 110, time=2.25, duration=0.25))  # D

# Bar 3: Rest for a quarter note (0.375 seconds)
# Then restate the motif with a short legato run
sax.notes.append(Note(62, 110, time=3.0, duration=0.25))  # D
sax.notes.append(Note(67, 110, time=3.25, duration=0.25))  # F#
sax.notes.append(Note(69, 110, time=3.5, duration=0.25))  # B
sax.notes.append(Note(62, 110, time=3.75, duration=0.25))  # D

#---------------------
# Write the MIDI file
#---------------------
midi.write("dante_intro.mid")

print("MIDI file generated: 'dante_intro.mid'")
