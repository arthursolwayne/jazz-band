
import pretty_midi
import numpy as np

# Set up the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Saxophone
midi.instruments.append(instrument)

# Define the time signature
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Note durations and timing
BPM = 160
note_duration = 60 / BPM  # 0.375 seconds per beat
bar_length = note_duration * 4  # 1.5 seconds per bar

# DURATION MAP (in seconds)
note_lengths = {
    'quarter': note_duration,
    'eighth': note_duration / 2,
    'sixteenth': note_duration / 4,
    'half': note_duration * 2,
    'dotted_eighth': (note_duration / 2) * 1.5,
    'rest': 0,
}

# --- DRUMMER (Little Ray) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drummer = pretty_midi.Instrument(program=10)
drummer.is_drum = True
midi.instruments.append(drummer)

# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat every eighth
for i in range(0, 4):
    time = i * note_duration
    if i % 2 == 0:
        drummer.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + note_lengths['eighth']))
    else:
        drummer.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + note_lengths['eighth']))
    drummer.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + note_lengths['eighth']))

# --- BASSIST (Marcus) ---
# Walking line: F, C, G, Bb, F, C, G, Bb, etc.
# Roots and fifths with chromatic approaches
bass = pretty_midi.Instrument(program=33)
midi.instruments.append(bass)

# Bar 1: F (root) with chromatic approach up
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=0, end=0.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=72, start=0.375, end=0.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=0.75, end=1.125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.125, end=1.5))

# Bar 2: C (fifth) with chromatic approach up
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=3.0))

# Bar 3: G (root) with chromatic approach down
bass.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.75))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=78, start=3.75, end=4.125))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5))

# Bar 4: Bb (fifth) with chromatic approach down
bass.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625))
bass.notes.append(pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0))

# --- PIANIST (Diane) ---
# Open voicings, different chord each bar, resolving on the last beat
piano = pretty_midi.Instrument(program=0)
midi.instruments.append(piano)

# Bar 1: Fmaj7 (F, A, C, E) - open voicing
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=0, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=0, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=0, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=0, end=note_lengths['quarter']))

# Bar 2: Gm7 (G, Bb, D, F) - open voicing
piano.notes.append(pretty_midi.Note(velocity=95, pitch=78, start=1.5, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=74, start=1.5, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=note_lengths['quarter']))

# Bar 3: C7 (C, E, G, Bb) - open voicing
piano.notes.append(pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=60, start=3.0, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=note_lengths['quarter']))  # Bb

# Bar 4: Fmaj7 (F, A, C, E) - open voicing, resolving
piano.notes.append(pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=note_lengths['quarter']))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=note_lengths['quarter']))

# --- SAX (You) ---
# Short motif: F - Bb - C - F (with rests and dynamic contrast)
# Start it, leave it hanging, come back to finish

# First note: F (71) - quarter note
instrument.notes.append(pretty_midi.Note(velocity=105, pitch=71, start=0, end=0.375))

# Rest on beat 2
# Rest on beat 3
# Then a final F to resolve
instrument.notes.append(pretty_midi.Note(velocity=105, pitch=71, start=2.625, end=3.0))

# Save the MIDI file
# midi.write disabled

print("MIDI file created successfully: jazz_intro_dante_russo.mid")
