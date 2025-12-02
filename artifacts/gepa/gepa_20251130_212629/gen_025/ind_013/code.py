
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with 4/4 time at 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax (program 64)
pm.instruments.append(instrument)

# Time settings
BPM = 160
BAR_DURATION = 6.0 / 4  # 6 seconds total, 1.5 seconds per bar
BEAT_DURATION = BAR_DURATION / 4  # 0.375 seconds per beat
NOTE_DURATION = BEAT_DURATION / 2  # 0.1875 seconds per note

# Create an empty list to hold notes
notes = []

# --- Bar 1: Little Ray on drums (no other instruments)
# We'll simulate this by leaving the tenor sax part empty

# --- Bars 2-4: Everyone in. Tenor sax takes the melody
# Key: D major (D, E, F#, G, A, B, C#)

# Tenor sax motif: a short, singable phrase that ends with a question
# D (D4) -> F# (F#4) -> A (A4) -> D (D5) -> G (G4)
# But we're going to build it in subtle, uneven phrasing to create tension and anticipation

# Bar 2: Start the motif, leave it hanging
# D4 at beat 1, F#4 at beat 2, A4 at beat 3
note1 = pretty_midi.Note(velocity=100, pitch=62, start=BAR_DURATION * 1, end=BAR_DURATION * 1 + NOTE_DURATION)
note2 = pretty_midi.Note(velocity=90, pitch=66, start=BAR_DURATION * 1 + BEAT_DURATION, end=BAR_DURATION * 1 + BEAT_DURATION + NOTE_DURATION)
note3 = pretty_midi.Note(velocity=85, pitch=69, start=BAR_DURATION * 1 + 2 * BEAT_DURATION, end=BAR_DURATION * 1 + 2 * BEAT_DURATION + NOTE_DURATION)
notes.append(note1)
notes.append(note2)
notes.append(note3)

# Bar 3: Let the motif breathe, add a slight delay to the resolution
# A grace note, then a small rest and a lingering note
note4 = pretty_midi.Note(velocity=95, pitch=69, start=BAR_DURATION * 2, end=BAR_DURATION * 2 + NOTE_DURATION * 0.5)
note5 = pretty_midi.Note(velocity=70, pitch=62, start=BAR_DURATION * 2 + NOTE_DURATION * 1.2, end=BAR_DURATION * 2 + NOTE_DURATION * 1.7)
notes.append(note4)
notes.append(note5)

# Bar 4: End with an incomplete phrase — a question, not a resolution
# G4 at beat 3, then leave it open
note6 = pretty_midi.Note(velocity=110, pitch=67, start=BAR_DURATION * 3 + 2 * BEAT_DURATION, end=BAR_DURATION * 3 + 2 * BEAT_DURATION + 0.1)
notes.append(note6)

# Add the notes to the instrument
for note in notes:
    instrument.notes.append(note)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file 'dante_intro.mid' created successfully.")
