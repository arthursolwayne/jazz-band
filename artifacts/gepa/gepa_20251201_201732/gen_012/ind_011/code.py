
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
pm.time_signature_changes.append(time_signature)

# Define key: F minor
key = 'Fm'

# Define the number of bars and the duration per bar (1.5 seconds at 160 BPM)
num_bars = 4
bar_duration = 1.5
total_duration = num_bars * bar_duration

# Create instruments for each player
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Drums')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(sax)
pm.instruments.append(piano)
pm.instruments.append(bass)
pm.instruments.append(drums)

# Set the start time for each instrument
bar_start_times = [0, 1.5, 3.0, 4.5]  # in seconds
note_durations = [0.25, 0.25, 0.25, 0.25]  # quarter notes

# Define the root note of Fm: F (MIDI note 65)
root = 65

# Define scale using F minor: F, Gb, Ab, A, Bb, B, C
# We'll use chromatic approach for bass and piano, but not scale-based
# Instead, use root, fifth, and chromatic passing tones

# Bar 1: Drums only (Little Ray)
# Open, fluid rhythms with hihat motion
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1: 0 to 1.5s
# Time of each beat: 0.375s (60 / 160 = 0.375s per beat)

# Kick on 1 and 3
kick_times = [0, 0.75]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=35, start=t, end=t + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [0.375, 1.125]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

# Hihat on every eighth
hihat_times = [0, 0.375, 0.75, 1.125]
for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Bar 2: Bass, Piano, Sax (Marcus, Diane, Dante)
# Bass: Walking line (root, fifth, chromatic approaches)
# Fm: root F (65), fifth C (72), Ab (69), Bb (62), etc.

# Bass line: F, Ab, Bb, C
# Bar 2: 1.5 to 3.0s
bass_notes = [
    (65, 1.5, 1.5 + 0.25),  # F
    (69, 1.5 + 0.25, 1.5 + 0.5),  # Ab
    (62, 1.5 + 0.5, 1.5 + 0.75),  # Bb
    (72, 1.5 + 0.75, 1.5 + 1.0),  # C
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Fm7
# In open voicings: F, Ab, C, Eb
piano_notes = [
    (65, 1.5, 1.5 + 0.25),  # F
    (69, 1.5, 1.5 + 0.25),  # Ab
    (72, 1.5, 1.5 + 0.25),  # C
    (67, 1.5, 1.5 + 0.25),  # Eb
]

for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# Saxophone: Motif, searching, with rests
# Start with a motif that feels like it's searching
# Notes: F (65), Ab (69), Bb (62), C (72)
# Rest in between to emphasize the space

sax_notes = [
    (65, 1.5, 1.5 + 0.25),  # F
    (69, 1.5 + 0.5, 1.5 + 0.75),  # Ab
    (62, 1.5 + 1.0, 1.5 + 1.25),  # Bb
    (72, 1.5 + 1.5, 1.5 + 1.75),  # C
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bar 3: Piano, Bass, Sax continue
# Bass: Gb (67), Ab (69), Bb (62), F (65)
bass_notes = [
    (67, 3.0, 3.0 + 0.25),  # Gb
    (69, 3.0 + 0.25, 3.0 + 0.5),  # Ab
    (62, 3.0 + 0.5, 3.0 + 0.75),  # Bb
    (65, 3.0 + 0.75, 3.0 + 1.0),  # F
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: Gm7 (G, Bb, D, F) or Bb7 (Bb, D, F, Ab)
# Let's go with Gm7: G, Bb, D, F
piano_notes = [
    (67, 3.0, 3.0 + 0.25),  # G
    (62, 3.0, 3.0 + 0.25),  # Bb
    (65, 3.0, 3.0 + 0.25),  # D
    (67, 3.0, 3.0 + 0.25),  # F
]

for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# Saxophone: Continue the motif, but with more space
# Rest between notes to emphasize tension
sax_notes = [
    (69, 3.0, 3.0 + 0.25),  # Ab
    (62, 3.0 + 0.5, 3.0 + 0.75),  # Bb
    (72, 3.0 + 1.0, 3.0 + 1.25),  # C
    (67, 3.0 + 1.5, 3.0 + 1.75),  # Gb
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Bar 4: Resolve with a sense of arrival
# Bass: F, Ab, Bb, C again
bass_notes = [
    (65, 4.5, 4.5 + 0.25),  # F
    (69, 4.5 + 0.25, 4.5 + 0.5),  # Ab
    (62, 4.5 + 0.5, 4.5 + 0.75),  # Bb
    (72, 4.5 + 0.75, 4.5 + 1.0),  # C
]

for pitch, start, end in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# Piano: Fm7 again, with a bit of motion
piano_notes = [
    (65, 4.5, 4.5 + 0.25),  # F
    (69, 4.5, 4.5 + 0.25),  # Ab
    (72, 4.5, 4.5 + 0.25),  # C
    (67, 4.5, 4.5 + 0.25),  # Eb
]

for pitch, start, end in piano_notes:
    note = pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=end)
    piano.notes.append(note)

# Saxophone: Resolve with a short rest and a final note
sax_notes = [
    (65, 4.5, 4.5 + 0.25),  # F
    (69, 4.5 + 0.5, 4.5 + 0.75),  # Ab
    (62, 4.5 + 1.0, 4.5 + 1.25),  # Bb
    (72, 4.5 + 1.5, 4.5 + 1.75),  # C
]

for pitch, start, end in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Drums in Bar 4: Same rhythm as Bar 1
# Kick on 1 and 3
kick_times = [4.5, 5.25]
for t in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=35, start=t, end=t + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [4.875, 5.625]
for t in snare_times:
    note = pretty_midi.Note(velocity=100, pitch=38, start=t, end=t + 0.1)
    drums.notes.append(note)

# Hihat on every eighth
hihat_times = [4.5, 4.875, 5.25, 5.625]
for t in hihat_times:
    note = pretty_midi.Note(velocity=100, pitch=42, start=t, end=t + 0.05)
    drums.notes.append(note)

# Save the MIDI file
pm.write("4_bar_intro_Fm.mid")
