
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: D major
key = 'D'

# Define instruments for each player
# 0: Tenor Sax (Program 64)
# 23: Electric Bass (Program 33)
# 0: Acoustic Piano (Program 0)
# 5: Acoustic Drum Set (Program 5)

# Create instrument tracks
tenor_sax = pretty_midi.Instrument(program=64)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
drums = pretty_midi.Instrument(program=5)

# Add tracks to the PrettyMIDI object
pm.instruments = [tenor_sax, bass, piano, drums]

# Define tempo and bar settings
BPM = 160
bar_length = 6.0  # 6 seconds for 4 bars
beat = bar_length / 4  # 1.5 seconds per beat
note_length = 0.375  # 0.375 seconds per 8th note

# Time markers in seconds
bar_1_start = 0.0
bar_2_start = bar_length / 4 * 1
bar_3_start = bar_length / 4 * 2
bar_4_start = bar_length / 4 * 3

# Create a function to convert note names to MIDI notes
def note_to_midi(note_name):
    notes = {
        'C': 12, 'C#': 13, 'Db': 13, 'D': 14, 'D#': 15, 'Eb': 15,
        'E': 16, 'F': 17, 'F#': 18, 'Gb': 18, 'G': 19, 'G#': 20, 'Ab': 20,
        'A': 21, 'A#': 22, 'Bb': 22, 'B': 23
    }
    return notes[note_name] + 12 * (ord(note_name[0]) - ord('C') + 1)

# Tenor Sax part: sparse, expressive melody
tenor_notes = [
    # Bar 1: mysterious, one note with a rest
    # D (MIDI 62) at 0.0s, velocity 90
    pretty_midi.Note(velocity=90, pitch=note_to_midi('D'), start=bar_1_start, end=bar_1_start + note_length),
    
    # Bar 2: Tension, two notes with space
    pretty_midi.Note(velocity=80, pitch=note_to_midi('F'), start=bar_2_start, end=bar_2_start + note_length),
    pretty_midi.Note(velocity=75, pitch=note_to_midi('B'), start=bar_2_start + note_length * 3, end=bar_2_start + note_length * 4),
    
    # Bar 3: Glimmer of resolution
    pretty_midi.Note(velocity=95, pitch=note_to_midi('G'), start=bar_3_start, end=bar_3_start + note_length),
    pretty_midi.Note(velocity=90, pitch=note_to_midi('A'), start=bar_3_start + note_length * 2, end=bar_3_start + note_length * 3),
    
    # Bar 4: Lingering question, half note on D
    pretty_midi.Note(velocity=85, pitch=note_to_midi('D'), start=bar_4_start, end=bar_4_start + note_length * 2),
]

tenor_sax.notes = tenor_notes

# Bass part: walking line with chromatic approaches
bass_notes = []
start_time = bar_1_start

for i in range(4):
    # D (62)
    bass_notes.append(pretty_midi.Note(velocity=70, pitch=note_to_midi('D'), start=start_time, end=start_time + note_length))
    # Eb (63) - chromatic approach
    bass_notes.append(pretty_midi.Note(velocity=65, pitch=note_to_midi('Eb'), start=start_time + note_length, end=start_time + note_length * 2))
    # F (64)
    bass_notes.append(pretty_midi.Note(velocity=70, pitch=note_to_midi('F'), start=start_time + note_length * 2, end=start_time + note_length * 3))
    # G (65)
    bass_notes.append(pretty_midi.Note(velocity=70, pitch=note_to_midi('G'), start=start_time + note_length * 3, end=start_time + note_length * 4))
    start_time += beat

bass.notes = bass_notes

# Piano part: 7th chords on 2 and 4
piano_notes = []

def add_seventh_chord(root, start_time):
    root_midi = note_to_midi(root)
    seventh = (root_midi + 10) % 12  # 7th interval
    notes = [root_midi, root_midi + 2, root_midi + 7, seventh]
    for note in notes:
        piano_notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=start_time + note_length * 2))
    return

# Bar 2 and Bar 4
add_seventh_chord('D', bar_2_start)
add_seventh_chord('G', bar_4_start)

piano.notes = piano_notes

# Drum part: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = []

def add_kick(start_time):
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.1))

def add_snare(start_time):
    drum_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time, end=start_time + 0.1))

def add_hihat(start_time):
    drum_notes.append(pretty_midi.Note(velocity=80, pitch=42, start=start_time, end=start_time + 0.1))

start_time = bar_1_start
for i in range(4):
    add_hihat(start_time)
    add_kick(start_time)
    add_hihat(start_time + note_length)
    add_hihat(start_time + note_length * 2)
    add_snare(start_time + note_length * 2)
    add_hihat(start_time + note_length * 3)
    add_kick(start_time + note_length * 3)
    add_hihat(start_time + note_length * 4)
    start_time += beat

drums.notes = drum_notes

# Save the MIDI file
pm.write("dante_russo_intro.mid")
print("MIDI file saved as 'dante_russo_intro.mid'")
