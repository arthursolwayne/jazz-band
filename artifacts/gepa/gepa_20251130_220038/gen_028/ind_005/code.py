
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Constants
BPM = 160
BEAT_DURATION = 60 / BPM  # seconds per beat
BAR_DURATION = 4 * BEAT_DURATION  # seconds per bar
TIME_PER_BAR = BAR_DURATION
TIME_PER_BEAT = BEAT_DURATION
TIME_PER_EIGHTH = TIME_PER_BEAT / 2
TIME_PER_SIXTEENTH = TIME_PER_BEAT / 4

# Helper function to create a Note
def note_on(time, pitch, velocity, duration, instrument):
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    instrument.notes.append(note)

# ----------------------------- DRUMS (Little Ray) -----------------------------
# Kick on 1 and 3
note_on(0.0, 36, 100, TIME_PER_BEAT, drums)
note_on(2.0, 36, 100, TIME_PER_BEAT, drums)

# Snare on 2 and 4
note_on(1.0, 38, 100, TIME_PER_BEAT, drums)
note_on(3.0, 38, 100, TIME_PER_BEAT, drums)

# Hi-hat on every eighth
for i in range(8):
    note_on(i * TIME_PER_EIGHTH, 42, 90, TIME_PER_SIXTEENTH, drums)

# ----------------------------- BASS (Marcus) -----------------------------
# Walking line in D major (D, E, F#, G, A, B, C#, D)
# Start at bar 1, beat 1
time = 0.0
bass_notes = [62, 64, 66, 67, 69, 71, 73, 62]  # D, E, F#, G, A, B, C#, D
for pitch in bass_notes:
    note_on(time, pitch, 90, TIME_PER_BEAT, bass)
    time += TIME_PER_BEAT

# ----------------------------- PIANO (Diane) -----------------------------
# 7th chords on 2 and 4
# D7 (D F# A C) on beat 2
note_on(1.0, 62, 90, TIME_PER_BEAT, piano)  # D
note_on(1.0, 67, 90, TIME_PER_BEAT, piano)  # A
note_on(1.0, 64, 90, TIME_PER_BEAT, piano)  # F#
note_on(1.0, 69, 90, TIME_PER_BEAT, piano)  # C

# G7 (G B D F) on beat 4
note_on(3.0, 67, 90, TIME_PER_BEAT, piano)  # G
note_on(3.0, 71, 90, TIME_PER_BEAT, piano)  # B
note_on(3.0, 62, 90, TIME_PER_BEAT, piano)  # D
note_on(3.0, 64, 90, TIME_PER_BEAT, piano)  # F

# ----------------------------- SAX (You) -----------------------------
# Your melody: a simple, open, questioning motif
# D (62), F# (67), B (71), E (64) — short and open, like a question

# Bar 2, beat 1: D
note_on(1.0, 62, 100, TIME_PER_SIXTEENTH, sax)

# Bar 2, beat 2: F#
note_on(1.5, 67, 100, TIME_PER_SIXTEENTH, sax)

# Bar 2, beat 3: B
note_on(2.0, 71, 100, TIME_PER_SIXTEENTH, sax)

# Bar 2, beat 4: E
note_on(2.5, 64, 100, TIME_PER_SIXTEENTH, sax)

# Leave it hanging — don’t resolve the question yet

# Add your instrument to the PrettyMIDI object
pm.instruments = [bass, piano, drums, sax]

# Save the MIDI file
pm.write("jazz_intro_question.mid")
