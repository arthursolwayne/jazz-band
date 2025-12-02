
from midiutil import MIDIFile
import numpy as np

# Constants
BPM = 160
TEMPO = BPM * 60 / 4  # In MIDI terms, tempo is in microseconds per beat
TIME_SIGNATURE = (4, 4)
KEY = 'D'  # D major

# Initialize MIDIFile
midi = MIDIFile(1)
track = 0
time = 0
midi.addTrackName(track, time, "Dante's Intro")
midi.addTempo(track, time, TEMPO)
midi.addTimeSignature(track, time, *TIME_SIGNATURE, 24, 8)

# Note durations and velocities
NOTE_DURATION = 0.375  # 1 beat in 160 BPM = 0.375 seconds
VEL = 100  # Moderate velocity

# Time: 0.0s - Bar 1 (Little Ray alone)
# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0.0s to 1.5s)
# Kick at 0.0, 0.75 (beat 1 and 3)
# Snare at 0.375, 1.125 (beat 2 and 4)
# Hi-hat on every eighth (0.0, 0.375, 0.75, 1.125, 1.5)

# Kick (MIDI note 36 = C1)
midi.addNote(track, 9, 36, 0.0, NOTE_DURATION, VEL)
midi.addNote(track, 9, 36, 0.75, NOTE_DURATION, VEL)

# Snare (MIDI note 38 = D1)
midi.addNote(track, 9, 38, 0.375, NOTE_DURATION, VEL)
midi.addNote(track, 9, 38, 1.125, NOTE_DURATION, VEL)

# Hi-hat (MIDI note 42 = F#1)
for t in [0.0, 0.375, 0.75, 1.125, 1.5]:
    midi.addNote(track, 9, 42, t, NOTE_DURATION, 50)  # 50% volume for hi-hat

# Bar 2 (1.5s to 3.0s) - Everyone in

# Diane: 7th chords, comp on 2 and 4
# D7 = D, F#, A, C
# In MIDI: D = 62, F# = 64, A = 69, C = 60
# Comp on beat 2 and 4 (1.875 and 3.375 seconds)

# Diane
diane_notes = [62, 64, 69, 60]  # D7
for note in diane_notes:
    midi.addNote(track, 0, note, 1.875, NOTE_DURATION, VEL)
for note in diane_notes:
    midi.addNote(track, 0, note, 3.375, NOTE_DURATION, VEL)

# Marcus: Walking bass line in D major
# D minor pentatonic over D major (D, F, G, A, C) with chromatic approaches
# Bar 2: D (beat 1), F (beat 2), G (beat 3), A (beat 4), C (beat 1 next bar)
# MIDI: D (62), F (65), G (67), A (69), C (60)

# Marcus
bass_notes = [62, 65, 67, 69]
for i, note in enumerate(bass_notes):
    midi.addNote(track, 1, note, 1.5 + i * NOTE_DURATION, NOTE_DURATION, VEL)

# You: Tenor saxophone - short motif, make it sing
# D (62), F# (64), A (69), D (62) -> D, F#, A, D
# Start it, leave it hanging — then finish it

# Bar 2: Start the motif
sax_notes = [62, 64, 69]  # D, F#, A
for i, note in enumerate(sax_notes):
    midi.addNote(track, 2, note, 1.5 + i * NOTE_DURATION, NOTE_DURATION, VEL)

# Bar 3: Repeat the motif
for i, note in enumerate(sax_notes):
    midi.addNote(track, 2, note, 3.0 + i * NOTE_DURATION, NOTE_DURATION, VEL)

# Bar 4: Finish the motif
# End on D (62)
midi.addNote(track, 2, 62, 4.5, NOTE_DURATION, VEL)

# Save the MIDI file
with open("dantes_intro.mid", "wb") as output_file:
    midi.writeFile(output_file)

print("MIDI file 'dantes_intro.mid' has been created.")
