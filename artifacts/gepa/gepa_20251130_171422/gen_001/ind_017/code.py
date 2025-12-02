
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument

# Set tempo and time signature
BPM = 160
BEATS_PER_BAR = 4
BAR_DURATION = 6.0  # seconds for 4 bars
BEAT_DURATION = BAR_DURATION / BEATS_PER_BAR  # 1.5 seconds per beat
NOTE_DURATION = 0.375  # 1/4 note duration in seconds (240 BPM = 0.25s, 160 BPM = 0.375s)

# Key: D minor (Dm)
KEY = 'Dm'

# MIDI note numbers for Dm7 (D, F, A, C)
D = 62
F = 64
A = 69
C = 60

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=BPM)

# Initialize instruments
bass_instrument = Instrument(program=33)  # Electric Bass
piano_instrument = Instrument(program=0)   # Acoustic Piano
drum_instrument = Instrument(program=0)   # Drums
sax_instrument = Instrument(program=64)   # Tenor Sax

# Add instruments to the MIDI file
midi.instruments = [bass_instrument, piano_instrument, drum_instrument, sax_instrument]

# ====================
# Bar 1: Little Ray (Drums) - Set it up
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar is 6 seconds, so 1 beat = 1.5 seconds
# MIDI note numbers:
# Kick: 36
# Snare: 38
# Hihat: 42

for beat in range(4):
    time = beat * BEAT_DURATION
    
    # Kick on 1 and 3
    if beat % 2 == 0:
        kick = Note(velocity=100, start=time, end=time + NOTE_DURATION)
        drum_instrument.notes.append(kick)
    
    # Snare on 2 and 4
    if beat % 2 == 1:
        snare = Note(velocity=100, start=time, end=time + NOTE_DURATION)
        drum_instrument.notes.append(snare)
    
    # Hihat on every eighth note
    for eighth in range(2):
        hihat_time = time + (eighth * NOTE_DURATION)
        hihat = Note(velocity=80, start=hihat_time, end=hihat_time + NOTE_DURATION / 2)
        drum_instrument.notes.append(hihat)

# ====================
# Bar 2: Everyone in, sax takes melody
# Dm7 chord: D, F, A, C

# Bass line: Walking line in Dm, chromatic approaches
bass_notes = [
    (62, 0),     # D (beat 1)
    (61, 1.5),   # C# (beat 2)
    (64, 3.0),   # F (beat 3)
    (66, 4.5)    # G (beat 4)
]

for note, time in bass_notes:
    bass_note = Note(velocity=100, start=time, end=time + NOTE_DURATION)
    bass_note.pitch = note
    bass_instrument.notes.append(bass_note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    (62, 0),     # D7 (D, F#, A, C) - but in Dm7: D, F, A, C
    (64, 1.5),   # F7 (F, A, C, Eb) - but in Dm7, this is a passing chord
    (62, 3.0),   # D7 again
    (64, 4.5)    # F7
]

for note, time in piano_notes:
    piano_note = Note(velocity=100, start=time, end=time + NOTE_DURATION)
    piano_note.pitch = note
    piano_instrument.notes.append(piano_note)

# Saxophone: Simple motif - D, F, A, leave it hanging
sax_notes = [
    (62, 0),     # D
    (64, 1.5),   # F
    (69, 3.0),   # A
    (62, 4.5)    # D (return to start)
]

for note, time in sax_notes:
    sax_note = Note(velocity=100, start=time, end=time + NOTE_DURATION)
    sax_note.pitch = note
    sax_instrument.notes.append(sax_note)

# ====================
# Save the MIDI to a file
midi.write('dante_russo_intro.mid')

print("MIDI file generated successfully: 'dante_russo_intro.mid'")
