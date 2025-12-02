
import pretty_midi
import numpy as np

# Set up the MIDI file
pm = pretty_midi.PrettyMidi(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor Sax
pm.instruments.append(instrument)

# Define the key: D Major
# Tonic: D (62)
# Scale: D, E, F#, G, A, B, C#, D

# Bar length in seconds
bar_length = 1.5  # 4/4 at 160 BPM
beat_length = bar_length / 4

# Time for each note in seconds
beat = beat_length  # 0.375 seconds per beat

# Function to add a note
def add_note(note_number, start_time, duration, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start_time, end=start_time + duration)
    instrument.notes.append(note)

# Bar 1: Little Ray (Drums) - 6/8 feel, with space
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Drums will be on a separate instrument
drum_program = pretty_midi.Instrument(program=0)  # Drum Kit
pm.instruments.append(drum_program)

# Kick on 1 and 3
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=0, end=0.1)
drum_program.notes.append(kick_note)
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=beat*2, end=beat*2 + 0.1)
drum_program.notes.append(kick_note)

# Snare on 2 and 4
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=beat, end=beat + 0.1)
drum_program.notes.append(snare_note)
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=beat*3, end=beat*3 + 0.1)
drum_program.notes.append(snare_note)

# Hi-hat on every eighth note
for t in np.arange(0, bar_length, beat / 2):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drum_program.notes.append(hihat)

# Bar 2: Diane (Piano) - 7th chords on 2 and 4, comp on 2 and 4
# D7 chord: D (62), F# (67), A (69), C# (67), but we'll use 7th intervals
# D7 = D, F#, A, C#

# Time at start of bar 2 = bar_length
bar2_start = bar_length

# Diane plays on beat 2 and 4 of bar 2 (time = bar2_start + beat*1 and beat*3)
# D7 chord - root note D (62), 7th C# (67), but we'll use just the 7th chord notes
# We can use a simple comping pattern

# Use note durations to create space and tension
# Comp on 2 and 4 with slight variations in timing and dynamics

# Bar 2, beat 2
note = pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + beat*1 - 0.05, end=bar2_start + beat*1 + 0.1)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + beat*1 - 0.05, end=bar2_start + beat*1 + 0.1)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=69, start=bar2_start + beat*1 - 0.05, end=bar2_start + beat*1 + 0.1)
instrument.notes.append(note)

# Bar 2, beat 4
note = pretty_midi.Note(velocity=100, pitch=62, start=bar2_start + beat*3 - 0.05, end=bar2_start + beat*3 + 0.1)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=bar2_start + beat*3 - 0.05, end=bar2_start + beat*3 + 0.1)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=69, start=bar2_start + beat*3 - 0.05, end=bar2_start + beat*3 + 0.1)
instrument.notes.append(note)

# Marcus (Bass) - Walking line, chromatic approaches, no repeated notes
# Start at the D note (62) on beat 1 of bar 2
# Walking line: D, C#, B, A, G#, F#, E, D, C#, B, A, G#, F#, E, D
# Let's do a short chromatic descent with variation

bass_notes = [62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48]

for i, note in enumerate(bass_notes):
    start = bar2_start + (beat * i)
    end = start + 0.1
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    instrument.notes.append(note_obj)

# Little Ray (Drums) continues in bar 2
# Same pattern as bar 1 but slightly emphasized on beat 2 and 4

# Kick on 1 and 3
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start, end=bar2_start + 0.1)
drum_program.notes.append(kick_note)
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar2_start + beat*2, end=bar2_start + beat*2 + 0.1)
drum_program.notes.append(kick_note)

# Snare on 2 and 4
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + beat, end=bar2_start + beat + 0.1)
drum_program.notes.append(snare_note)
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=bar2_start + beat*3, end=bar2_start + beat*3 + 0.1)
drum_program.notes.append(snare_note)

# Hi-hat on every eighth
for t in np.arange(bar2_start, bar2_start + bar_length, beat / 2):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drum_program.notes.append(hihat)

# Bar 3: Diane continues comping on beat 2 and 4
bar3_start = bar2_start + bar_length

# Bar 3, beat 2
note = pretty_midi.Note(velocity=100, pitch=62, start=bar3_start + beat*1 - 0.05, end=bar3_start + beat*1 + 0.1)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=bar3_start + beat*1 - 0.05, end=bar3_start + beat*1 + 0.1)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=69, start=bar3_start + beat*1 - 0.05, end=bar3_start + beat*1 + 0.1)
instrument.notes.append(note)

# Bar 3, beat 4
note = pretty_midi.Note(velocity=100, pitch=62, start=bar3_start + beat*3 - 0.05, end=bar3_start + beat*3 + 0.1)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=67, start=bar3_start + beat*3 - 0.05, end=bar3_start + beat*3 + 0.1)
instrument.notes.append(note)
note = pretty_midi.Note(velocity=75, pitch=69, start=bar3_start + beat*3 - 0.05, end=bar3_start + beat*3 + 0.1)
instrument.notes.append(note)

# Marcus continues walking line
bass_notes = [62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48]

for i, note in enumerate(bass_notes):
    start = bar3_start + (beat * i)
    end = start + 0.1
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    instrument.notes.append(note_obj)

# Little Ray continues on bar 3
# Same pattern as before

# Kick on 1 and 3
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start, end=bar3_start + 0.1)
drum_program.notes.append(kick_note)
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar3_start + beat*2, end=bar3_start + beat*2 + 0.1)
drum_program.notes.append(kick_note)

# Snare on 2 and 4
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + beat, end=bar3_start + beat + 0.1)
drum_program.notes.append(snare_note)
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=bar3_start + beat*3, end=bar3_start + beat*3 + 0.1)
drum_program.notes.append(snare_note)

# Hi-hat on every eighth
for t in np.arange(bar3_start, bar3_start + bar_length, beat / 2):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drum_program.notes.append(hihat)

# Bar 4: Your solo — the question, not the statement
bar4_start = bar3_start + bar_length

# Start with a short motif — D, F#, A, D
# But leave it hanging — end on the A
# D (62), F# (67), A (69), D (62) — but omit the final D

# Play each with slight variation in timing and dynamics
# First note: D (62), start at bar4_start, end bar4_start + 0.2
note = pretty_midi.Note(velocity=100, pitch=62, start=bar4_start, end=bar4_start + 0.2)
instrument.notes.append(note)

# Second note: F# (67), start at bar4_start + 0.15, end bar4_start + 0.3
note = pretty_midi.Note(velocity=100, pitch=67, start=bar4_start + 0.15, end=bar4_start + 0.3)
instrument.notes.append(note)

# Third note: A (69), start at bar4_start + 0.25, end bar4_start + 0.4
note = pretty_midi.Note(velocity=100, pitch=69, start=bar4_start + 0.25, end=bar4_start + 0.4)
instrument.notes.append(note)

# Leave the last note (D) hanging — not played
# End the phrase with the A — the question

# Marcus continues walking line
bass_notes = [62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48]

for i, note in enumerate(bass_notes):
    start = bar4_start + (beat * i)
    end = start + 0.1
    note_obj = pretty_midi.Note(velocity=80, pitch=note, start=start, end=end)
    instrument.notes.append(note_obj)

# Little Ray continues
# Kick on 1 and 3
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start, end=bar4_start + 0.1)
drum_program.notes.append(kick_note)
kick_note = pretty_midi.Note(velocity=100, pitch=36, start=bar4_start + beat*2, end=bar4_start + beat*2 + 0.1)
drum_program.notes.append(kick_note)

# Snare on 2 and 4
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + beat, end=bar4_start + beat + 0.1)
drum_program.notes.append(snare_note)
snare_note = pretty_midi.Note(velocity=100, pitch=38, start=bar4_start + beat*3, end=bar4_start + beat*3 + 0.1)
drum_program.notes.append(snare_note)

# Hi-hat on every eighth
for t in np.arange(bar4_start, bar4_start + bar_length, beat / 2):
    hihat = pretty_midi.Note(velocity=80, pitch=42, start=t, end=t + 0.05)
    drum_program.notes.append(hihat)

# Save the MIDI file
pm.write("dante_intro.mid")
