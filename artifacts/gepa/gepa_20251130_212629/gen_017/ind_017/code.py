
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMidi(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax - program 64
midi.instruments.append(instrument)

# Time signatures and timing
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Define the tempo in beats per minute (BPM)
bpm = 160
beat_seconds = 60.0 / bpm  # 0.375 seconds per beat
bar_seconds = beat_seconds * 4  # 1.5 seconds per bar

# Define pitches for each instrument
tenor_sax_notes = []
bass_notes = []
piano_notes = []
drums_notes = []

# Bar 1: Little Ray (drums) alone — setup
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll just use MIDI note 35 (Kick), 38 (Snare), 42 (HiHat)
bar1_start = 0.0

# Kick on beat 1 and 3
drums_notes.append(pretty_midi.Note(velocity=100, pitch=35, start=bar1_start + 0.0, end=bar1_start + 0.05))
drums_notes.append(pretty_midi.Note(velocity=100, pitch=35, start=bar1_start + 0.75, end=bar1_start + 0.80))
# Snare on beat 2 and 4
drums_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 0.375, end=bar1_start + 0.425))
drums_notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar1_start + 1.125, end=bar1_start + 1.175))
# HiHat on every eighth note
for i in range(8):
    start = bar1_start + (i * beat_seconds / 8)
    end = start + 0.03
    drums_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=start, end=end))

# Bar 2: Everyone enters — Tenor starts the melody
bar2_start = bar_seconds

# Tenor sax melody — short motif, one phrase, ends with a question
# Notes: D (D4), F# (F#4), B (B4), A (A4), E (E4), G (G4) — D minor pentatonic
# D4 = 62, F#4 = 66, B4 = 71, A4 = 69, E4 = 64, G4 = 67

# First note: D4, quarter note
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar2_start, end=bar2_start + beat_seconds))

# Second note: F#4, eighth note
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=bar2_start + beat_seconds/2, end=bar2_start + beat_seconds/2 + beat_seconds/4))

# Third note: B4, eighth note
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar2_start + beat_seconds/2 + beat_seconds/4, end=bar2_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4))

# Fourth note: A4, sixteenth note
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar2_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4, end=bar2_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4 + beat_seconds/8))

# Fifth note: E4, sixteenth note
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar2_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4 + beat_seconds/8, end=bar2_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4 + beat_seconds/8 + beat_seconds/8))

# Sixth note: G4, rest — leave it hanging
# No note here, just space

# Bass: walking line, chromatic approaches
# D, Eb, E, F, F#, G, G#, A, A#, B, C, C#, D
# Create a walking line in D minor with chromatic passing tones

bass_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=bar2_start, end=bar2_start + beat_seconds/4))
bass_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=bar2_start + beat_seconds/4, end=bar2_start + beat_seconds/2))
bass_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=bar2_start + beat_seconds/2, end=bar2_start + beat_seconds*3/4))
bass_notes.append(pretty_midi.Note(velocity=80, pitch=65, start=bar2_start + beat_seconds*3/4, end=bar2_start + beat_seconds))

# Piano: 7th chords, comp on 2 and 4
# D7 = D (62), F# (66), A (69), C (60)
# D minor 7 = D (62), F (65), A (69), C (60)

# Comp on 2 and 4
# 2nd beat: D minor 7
piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + beat_seconds/2, end=bar2_start + beat_seconds/2 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=bar2_start + beat_seconds/2, end=bar2_start + beat_seconds/2 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + beat_seconds/2, end=bar2_start + beat_seconds/2 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar2_start + beat_seconds/2, end=bar2_start + beat_seconds/2 + 0.05))

# 4th beat: D7
piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar2_start + beat_seconds*1.5, end=bar2_start + beat_seconds*1.5 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=66, start=bar2_start + beat_seconds*1.5, end=bar2_start + beat_seconds*1.5 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar2_start + beat_seconds*1.5, end=bar2_start + beat_seconds*1.5 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar2_start + beat_seconds*1.5, end=bar2_start + beat_seconds*1.5 + 0.05))

# Bar 3: Continue the motif, build tension
bar3_start = bar2_start + bar_seconds

# Tenor sax: repeat the motif with slight variation in timing
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=62, start=bar3_start, end=bar3_start + beat_seconds))
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=66, start=bar3_start + beat_seconds/2, end=bar3_start + beat_seconds/2 + beat_seconds/4))
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar3_start + beat_seconds/2 + beat_seconds/4, end=bar3_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4))
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=69, start=bar3_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4, end=bar3_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4 + beat_seconds/8))
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar3_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4 + beat_seconds/8, end=bar3_start + beat_seconds/2 + beat_seconds/4 + beat_seconds/4 + beat_seconds/8 + beat_seconds/8))

# Bass: continue walking line
bass_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=bar3_start, end=bar3_start + beat_seconds/4))
bass_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=bar3_start + beat_seconds/4, end=bar3_start + beat_seconds/2))
bass_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=bar3_start + beat_seconds/2, end=bar3_start + beat_seconds*3/4))
bass_notes.append(pretty_midi.Note(velocity=80, pitch=65, start=bar3_start + beat_seconds*3/4, end=bar3_start + beat_seconds))

# Piano: comp on 2 and 4 again
piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar3_start + beat_seconds/2, end=bar3_start + beat_seconds/2 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=bar3_start + beat_seconds/2, end=bar3_start + beat_seconds/2 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + beat_seconds/2, end=bar3_start + beat_seconds/2 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar3_start + beat_seconds/2, end=bar3_start + beat_seconds/2 + 0.05))

piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar3_start + beat_seconds*1.5, end=bar3_start + beat_seconds*1.5 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=66, start=bar3_start + beat_seconds*1.5, end=bar3_start + beat_seconds*1.5 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar3_start + beat_seconds*1.5, end=bar3_start + beat_seconds*1.5 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar3_start + beat_seconds*1.5, end=bar3_start + beat_seconds*1.5 + 0.05))

# Bar 4: Tenor sax ends with a question, no resolution
bar4_start = bar3_start + bar_seconds

# Tenor sax: ends with the last note of the motif, but no resolution
tenor_sax_notes.append(pretty_midi.Note(velocity=100, pitch=64, start=bar4_start, end=bar4_start + beat_seconds/2))

# Bass: continue walking line
bass_notes.append(pretty_midi.Note(velocity=80, pitch=62, start=bar4_start, end=bar4_start + beat_seconds/4))
bass_notes.append(pretty_midi.Note(velocity=80, pitch=63, start=bar4_start + beat_seconds/4, end=bar4_start + beat_seconds/2))
bass_notes.append(pretty_midi.Note(velocity=80, pitch=64, start=bar4_start + beat_seconds/2, end=bar4_start + beat_seconds*3/4))
bass_notes.append(pretty_midi.Note(velocity=80, pitch=65, start=bar4_start + beat_seconds*3/4, end=bar4_start + beat_seconds))

# Piano: comp on 2 and 4 again
piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + beat_seconds/2, end=bar4_start + beat_seconds/2 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=65, start=bar4_start + beat_seconds/2, end=bar4_start + beat_seconds/2 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar4_start + beat_seconds/2, end=bar4_start + beat_seconds/2 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar4_start + beat_seconds/2, end=bar4_start + beat_seconds/2 + 0.05))

piano_notes.append(pretty_midi.Note(velocity=90, pitch=62, start=bar4_start + beat_seconds*1.5, end=bar4_start + beat_seconds*1.5 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=66, start=bar4_start + beat_seconds*1.5, end=bar4_start + beat_seconds*1.5 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=69, start=bar4_start + beat_seconds*1.5, end=bar4_start + beat_seconds*1.5 + 0.05))
piano_notes.append(pretty_midi.Note(velocity=90, pitch=60, start=bar4_start + beat_seconds*1.5, end=bar4_start + beat_seconds*1.5 + 0.05))

# Add notes to instruments
for note in tenor_sax_notes:
    instrument.notes.append(note)

# Drums are on a separate instrument (drum kit)
drum_instrument = pretty_midi.Instrument(program=0)
midi.instruments.append(drum_instrument)
for note in drums_notes:
    drum_instrument.notes.append(note)

# Add piano notes to their instrument
piano_instrument = pretty_midi.Instrument(program=0)
midi.instruments.append(piano_instrument)
for note in piano_notes:
    piano_instrument.notes.append(note)

# Add bass (string bass) to another instrument
bass_instrument = pretty_midi.Instrument(program=33)  # String bass
midi.instruments.append(bass_instrument)
for note in bass_notes:
    bass_instrument.notes.append(note)

# Write the MIDI file to disk
midi.write('dante_intro.mid')
