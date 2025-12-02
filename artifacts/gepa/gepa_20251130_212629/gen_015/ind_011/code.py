
import pretty_midi
from pretty_midi import Note, Instrument

# Initialize the Pretty MIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.tempo_changes = [pretty_midi.TempoChange(160, 0.0)]

# Set the key (D minor)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0.0)]  # 2 = D minor

# Create instruments
drums = Instrument(program=10, is_drum=True)
bass = Instrument(program=33)
piano = Instrument(program=0)
sax = Instrument(program=64)

# Function to add a note to an instrument
def add_note(instrument, pitch, start, end, velocity=100):
    note = Note(pitch=pitch, start=start, end=end, velocity=velocity)
    instrument.notes.append(note)

# Define the tempo and bar length
BPM = 160
beats_per_bar = 4
seconds_per_beat = 60.0 / BPM
bar_length = seconds_per_beat * beats_per_bar

# Bar 1: Drums only
# Kick on 1 and 3
add_note(drums, 36, 0.0, 0.25)  # Kick on beat 1
add_note(drums, 36, 1.5, 1.75)  # Kick on beat 3
# Snare on 2 and 4
add_note(drums, 38, 0.75, 0.95)  # Snare on beat 2
add_note(drums, 38, 2.25, 2.45)  # Snare on beat 4
# Hi-hat on every eighth
for i in range(8):
    add_note(drums, 42, i * 0.375, i * 0.375 + 0.1)

# Bar 2: All instruments come in
# Bass: Walking line in Dm (D C Bb A G F Eb)
# Notes: D (D), C (C), Bb (Bb), A (A), G (G), F (F), Eb (Eb), D (D)
bass_notes = [62, 60, 57, 59, 61, 58, 57, 62]
for i, pitch in enumerate(bass_notes):
    add_note(bass, pitch, bar_length * 0.25 * i, bar_length * 0.25 * (i + 1))

# Piano: 7th chords on 2 and 4
# Dm7 (D F A C)
# Dm7 chord pitches: D (62), F (65), A (69), C (67)
# On beat 2 and 4 (position 1.5s and 3.0s)
for time in [1.5, 3.0]:
    add_note(piano, 62, time, time + 0.25)  # D
    add_note(piano, 65, time, time + 0.25)  # F
    add_note(piano, 67, time, time + 0.25)  # C
    add_note(piano, 69, time, time + 0.25)  # A

# Drums: full rhythm
for i in range(8):
    add_note(drums, 42, bar_length + i * 0.375, bar_length + i * 0.375 + 0.1)
add_note(drums, 36, bar_length, bar_length + 0.25)  # Kick on beat 1
add_note(drums, 36, bar_length + 1.5, bar_length + 1.75)  # Kick on beat 3
add_note(drums, 38, bar_length + 0.75, bar_length + 0.95)  # Snare on beat 2
add_note(drums, 38, bar_length + 2.25, bar_length + 2.45)  # Snare on beat 4

# Sax: Melodic motif (Dm scale, but with space)
# Phrase: D (62) -> F (65) -> D (62) -> Bb (61) -> rest
# Start at bar 2 (time = 1.5s)
add_note(sax, 62, bar_length + 0.0, bar_length + 0.375)  # D
add_note(sax, 65, bar_length + 0.375, bar_length + 0.75)  # F
add_note(sax, 62, bar_length + 0.75, bar_length + 1.125)  # D
add_note(sax, 61, bar_length + 1.125, bar_length + 1.5)  # Bb

# Add instruments to the PrettyMIDI object
pm.instruments = [drums, bass, piano, sax]

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
