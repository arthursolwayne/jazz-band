
import pretty_midi
from pretty_midi import Note, Instrument
import numpy as np

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)
bar_length = 6.0  # 4 bars in 6 seconds
beat_length = bar_length / 4  # 1.5 seconds per bar
note_length = beat_length / 4  # 0.375 seconds per beat

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Define instruments
drums = Instrument(program=10, is_drum=True, name="Drums")
bass = Instrument(program=33, name="Bass")
piano = Instrument(program=0, name="Piano")
saxophone = Instrument(program=64, name="Saxophone")

# Add instruments to the PrettyMIDI object
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(saxophone)

# Function to create a note with start and end time
def create_note(note_number, start_time, duration):
    note = Note(velocity=100, pitch=note_number, start=start_time, end=start_time + duration)
    return note

# Function to play a rhythmic pattern on drums
def play_drums():
    # Kick on 1 and 3
    kick_notes = [create_note(36, 0, note_length), create_note(36, 2 * note_length, note_length)]

    # Snare on 2 and 4
    snare_notes = [create_note(38, note_length, note_length), create_note(38, 3 * note_length, note_length)]

    # Hihat on every eighth note
    hihat_notes = [create_note(42, i * note_length, note_length) for i in range(8)]

    # Add all notes to the drums instrument
    for note in kick_notes + snare_notes + hihat_notes:
        drums.notes.append(note)

# Function to play walking bass line (chromatic with approaches)
def play_bass():
    # Fm scale: F, Gb, Ab, Bb, C, Db, Eb
    # Walking bass with chromatic approaches
    bass_line = [53, 54, 52, 50, 51, 50, 49, 51, 53, 54, 52, 50, 51, 50, 49, 51]
    for i, note in enumerate(bass_line):
        start = i * note_length
        duration = note_length
        bass.notes.append(create_note(note, start, duration))

# Function to play piano comping on 2 and 4
def play_piano():
    # Fm7: F, Ab, Bb, C
    # Comping on 2 and 4 with 7th chords
    # Fm7 on beat 2 and Cm7 on beat 4
    chord1 = [53, 56, 58, 60]  # Fm7
    chord2 = [60, 63, 65, 67]  # Cm7

    # Play chords on beat 2 and 4
    for chord, beat in zip([chord1, chord2], [1, 3]):
        for note in chord:
            start = beat * note_length
            duration = note_length
            piano.notes.append(create_note(note, start, duration))

# Function to play saxophone intro
def play_sax():
    # One short motif: F, Ab, Bb, F (melodic fragment)
    # Start on beat 1, leave it hanging, come back to finish it
    # Use rests and space

    # First note on beat 1
    sax.notes.append(create_note(53, 0, note_length))  # F

    # Rest on beat 2
    # Rest on beat 3
    # Then Ab on beat 4
    sax.notes.append(create_note(56, 3 * note_length, note_length))  # Ab

    # Then Bb on beat 5
    sax.notes.append(create_note(58, 4 * note_length, note_length))  # Bb

    # Then F on beat 6
    sax.notes.append(create_note(53, 5 * note_length, note_length))  # F

# Play the parts
play_drums()
play_bass()
play_piano()
play_sax()

# Save the MIDI file
pm.write("dante_intro.mid")

print("MIDI file 'dante_intro.mid' created successfully.")
