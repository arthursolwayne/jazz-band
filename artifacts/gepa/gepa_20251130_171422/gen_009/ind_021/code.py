
import pretty_midi
import numpy as np

# Set up the piece
midi = pretty_midi.PrettyMIDI()
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
midi.instruments = []

# Create instruments
drums = pretty_midi.Instrument(program=10)
piano = pretty_midi.Instrument(program=0)
bass = pretty_midi.Instrument(program=33)
sax = pretty_midi.Instrument(program=64)

# Add instruments to the MIDI file
midi.instruments.append(drums)
midi.instruments.append(piano)
midi.instruments.append(bass)
midi.instruments.append(sax)

# Constants
BPM = 160
tempo = 60.0 / BPM  # seconds per beat

# Bar 1: Little Ray on drums - kick on 1 & 3, snare on 2 & 4, hi-hat on every eighth
# Bar 1 is 4 beats, with 8 subdivisions

# Create a function to add a note
def add_note(instrument, pitch, start, end, velocity):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=end)
    instrument.notes.append(note)

# Bar 1 (0.0 to 1.5 seconds)
# Kick on beat 1 and 3 (beats 0 and 2 in 0-4)
# Snare on beat 2 and 4 (beats 1 and 3)
# Hi-hat on every eighth note (0, 0.5, 1.0, 1.5)
for i in range(0, 4):
    if i % 2 == 0:
        add_note(drums, 36, i * 0.375, i * 0.375 + 0.2, 110)  # Kick
    else:
        add_note(drums, 38, i * 0.375, i * 0.375 + 0.2, 110)  # Snare
    add_note(drums, 42, i * 0.375, i * 0.375 + 0.1, 100)  # Hi-hat

# Bar 2: Everyone comes in. Start of the sax melody
# Time: 1.5 - 3.0 seconds

# Bass line: walking, chromatic approaches
# D D# E F# G A B C# D

bass_notes = [62, 63, 64, 66, 67, 69, 71, 72]
for i in range(8):
    start = 1.5 + i * 0.375
    end = start + 0.375
    add_note(bass, bass_notes[i % len(bass_notes)], start, end, 90)

# Piano: 7th chords in D: Dmaj7 (D, F#, A, C#), comp on 2 and 4
# Bar 2: Dmaj7 on beat 1 and 3
# Bar 3: D7 on beat 2 and 4 (if needed)
# We'll keep it simple: Dmaj7 on beat 1 and 3 (2 and 4 are empty)

# Bar 2: beat 1 (1.5s) and beat 3 (2.25s)
for beat_offset in [0, 2]:
    start = 1.5 + beat_offset * 0.375
    for note in [62, 66, 69, 72]:  # D, F#, A, C#
        add_note(piano, note, start, start + 0.1, 90)

# Sax: 4-note motif, starts on beat 1 of bar 2 (1.5s), ends on beat 3 (2.25s)
# Motif: D (62), F# (66), B (71), D (62) — ascending 3rd, then wide interval, return

# Beat 1 (1.5s): D (62)
add_note(sax, 62, 1.5, 1.5 + 0.1, 100)

# Beat 2 (1.875s): F# (66)
add_note(sax, 66, 1.875, 1.875 + 0.1, 100)

# Beat 3 (2.25s): B (71)
add_note(sax, 71, 2.25, 2.25 + 0.1, 100)

# Beat 4 (2.625s): End of bar 4, D (62) — leave it hanging
add_note(sax, 62, 2.625, 2.625 + 0.1, 100)

# Bar 3 and 4: Let the rhythm continue, sax leaves it hanging

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file created: dante_intro.mid")
