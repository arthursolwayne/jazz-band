
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = pretty_midi.Instrument(program=128)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Key: D major (key number 2)
pm.key_signature_changes = [pretty_midi.KeySignature(2, 0)]

# Set the tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(160, 0)]

# Define the time in seconds for each bar (160 BPM, 4/4 => 6 seconds for 4 bars)
bar_length_seconds = 1.5

# Bar 1: Little Ray on drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time in seconds for each beat: 0.375 seconds per beat (60 / 160 = 0.375)
beat_length = 0.375

# Bar 1:
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=beat_length * 2, end=beat_length * 2 + 0.375))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat_length, end=beat_length + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat_length * 3, end=beat_length * 3 + 0.375))

# Hihat on every eighth note (1, 2, 3, 4, 5, 6, 7, 8)
for i in range(8):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * beat_length, end=i * beat_length + 0.125))

# Bar 2: Bass enters with walking line in D major
# D major scale: D, E, F#, G, A, B, C#, D
# Walking line with chromatic approaches

# Bar 2 - 0.0 to 1.5 seconds
# D (2nd octave) = 62
# Chromatic approach to E (64) from D# (63)
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=1.5, end=1.5 + 0.375))  # D#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5 + 0.375, end=1.5 + 0.75))  # E
bass.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.5 + 0.75, end=1.5 + 1.125))  # F#
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5 + 1.125, end=1.5 + 1.5))  # A

# Bar 3: Piano enters with 7th chords on 2 and 4
# Comping on 2 and 4, D7 = D, F#, A, C
# Time for bar 3 is 3.0 to 4.5 seconds

# On beat 2 (time = 3.0)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.125))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.125))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.0 + 0.125))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.0 + 0.125))  # C

# On beat 4 (time = 4.5)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.5 + 0.125))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.125))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.5 + 0.125))  # F#
piano.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.5 + 0.125))  # C

# Bar 4: Tenor sax takes the melody
# One short motif, singable, leaving it hanging

# D (62) + F# (65) + A (67) + C (69)
# Motif: D -> F# -> A -> C (half note, then resolution)

# Start at 3.0 seconds, hold for 1.5 seconds (bar 4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0 + 0.75, end=3.0 + 1.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0 + 1.5, end=3.0 + 2.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0 + 2.25, end=3.0 + 3.0))

# Add the instruments to the PrettyMIDI object
pm.instruments = [drums, bass, piano, sax]

# Save the MIDI file
pm.write("dante_intro.mid")
