
import numpy as np
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Constants
BPM = 160
BAR_DURATION = 1.5  # seconds per bar
BEAT_DURATION = 0.375  # seconds per beat
NOTE_DURATION = 0.1875  # 0.375 / 2 (half a beat)

# Key: F major
# Scale degrees: F (1), G (2), A (3), Bb (4), C (5), D (6), E (7)
# Mode: Mixolydian (for "haunting" feel) — F G A Bb C D E

# Time signature: 4/4
# Tempo: 160 BPM
# Duration of 4 bars: 6.0 seconds

# Initialize MIDI file
midi = pretty_midi.PrettyMIDI()

# Create instruments
drums = Instrument(program=0, is_drum=True)
bass = Instrument(program=33)
piano = Instrument(program=0)
sax = Instrument(program=64)

# Add instruments to MIDI
midi.instruments.append(drums)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)

# Function to add a note to an instrument
def add_note(instrument, time, pitch, duration, velocity=100):
    note = Note(pitch=pitch, start=time, end=time + duration, velocity=velocity)
    instrument.notes.append(note)

# Time starts at 0
time = 0.0

# -------------------------------
# Bar 1: Little Ray (Drums) - Set the mood
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time 0.0 to 1.5 seconds

# Kick on 1 (0.0) and 3 (1.125)
add_note(drums, 0.0, 36, NOTE_DURATION, velocity=110)  # Kick
add_note(drums, 1.125, 36, NOTE_DURATION, velocity=110)  # Kick

# Snare on 2 (0.375) and 4 (1.5)
add_note(drums, 0.375, 38, NOTE_DURATION, velocity=100)  # Snare
add_note(drums, 1.5, 38, NOTE_DURATION, velocity=100)  # Snare

# Hihat on every eighth (0.0, 0.375, 0.75, 1.125)
add_note(drums, 0.0, 42, NOTE_DURATION, velocity=90)  # Hihat
add_note(drums, 0.375, 42, NOTE_DURATION, velocity=90)
add_note(drums, 0.75, 42, NOTE_DURATION, velocity=90)
add_note(drums, 1.125, 42, NOTE_DURATION, velocity=90)

# -------------------------------
# Bar 2: Everyone in. Diane (Piano) - Open voicings, resolve on the last bar

# Bar 2: Chord F7 (F A C Eb) - open voicing, root on 2
add_note(piano, 1.5, 69, NOTE_DURATION)  # C (root: F is 65, but here we go for open voicing)
add_note(piano, 1.5, 74, NOTE_DURATION)  # A
add_note(piano, 1.5, 77, NOTE_DURATION)  # C (octave)
add_note(piano, 1.5, 71, NOTE_DURATION)  # Eb

# Bar 3: Chord Bb7 (Bb D F Ab) - open voicing
add_note(piano, 1.875, 71, NOTE_DURATION)  # Bb
add_note(piano, 1.875, 76, NOTE_DURATION)  # D
add_note(piano, 1.875, 79, NOTE_DURATION)  # F
add_note(piano, 1.875, 74, NOTE_DURATION)  # Ab

# Bar 4: Chord C7 (C E G Bb) - resolve on the last bar
add_note(piano, 2.25, 67, NOTE_DURATION)  # C
add_note(piano, 2.25, 72, NOTE_DURATION)  # E
add_note(piano, 2.25, 76, NOTE_DURATION)  # G
add_note(piano, 2.25, 79, NOTE_DURATION)  # Bb

# -------------------------------
# Bar 2: Marcus (Bass) - Walking line, roots and fifths with chromatic approaches

# Bar 2: F (65) -> G (67) with chromatic approach
add_note(bass, 1.5, 65, NOTE_DURATION * 2)  # F root
add_note(bass, 1.5, 66, NOTE_DURATION * 0.5)  # Chromatic approach

# Bar 3: Bb (62) -> C (65) with chromatic approach
add_note(bass, 1.875, 62, NOTE_DURATION * 2)  # Bb root
add_note(bass, 1.875, 63, NOTE_DURATION * 0.5)  # Chromatic approach

# Bar 4: C (65) -> D (67) with chromatic approach
add_note(bass, 2.25, 65, NOTE_DURATION * 2)  # C root
add_note(bass, 2.25, 66, NOTE_DURATION * 0.5)  # Chromatic approach

# -------------------------------
# Bar 2: You (Sax) - Tenor sax, one short motif, haunting, leave it hanging

# Start with a phrase: F (65) -> Eb (64) -> D (62), then rest
add_note(sax, 1.5, 65, NOTE_DURATION)  # F
add_note(sax, 1.5 + NOTE_DURATION, 64, NOTE_DURATION)  # Eb
add_note(sax, 1.5 + NOTE_DURATION * 2, 62, NOTE_DURATION)  # D

# Silence for the rest of the 4 bars (1.5 to 3.0 seconds)
# Let it hang — the question is out there

# -------------------------------
# Save the MIDI file
midi.save("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
