
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

# Create instrument tracks
drums = pretty_midi.Instrument(program=drums_program)
piano = pretty_midi.Instrument(program=piano_program)
bass = pretty_midi.Instrument(program=bass_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, piano, bass, sax]

# Time per bar at 160 BPM
# 60 / 160 = 0.375 seconds per beat, 1.5 seconds per bar
# Total duration: 6 seconds (4 bars)
duration = 6.0

# Define the Dm7 chord (D F A C)
Dm7_notes = [pretty_midi.note_number_to_name(62),  # D
             pretty_midi.note_number_to_name(64),  # F
             pretty_midi.note_number_to_name(67),  # A
             pretty_midi.note_number_to_name(71)]  # C

# Convert to MIDI note numbers
Dm7_midi_notes = [62, 64, 67, 71]

# Bar 1: Little Ray (drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# 1 bar = 1.5 seconds
# 4 beats per bar at 160 BPM
# 0.375s per beat
# 8 eighth notes per bar

# Kick on beats 1 and 3
kick_times = [0.0, 0.75]
kick_notes = [36] * len(kick_times)
for time, note in zip(kick_times, kick_notes):
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

# Snare on beats 2 and 4
snare_times = [0.375, 1.125]
snare_notes = [38] * len(snare_times)
for time, note in zip(snare_times, snare_notes):
    drums.notes.append(pretty_midi.Note(velocity=110, pitch=note, start=time, end=time + 0.25))

# Hi-hat on every eighth
hihat_times = np.arange(0.0, 1.5, 0.375)
hihat_notes = [42] * len(hihat_times)
for time, note in zip(hihat_times, hihat_notes):
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.125))

# Bar 2: Bass (Marcus) walks with chromatic approach to D
# Walk Dm7 with chromatic passing tones

# Dm7: D F A C
# Chromatic approach to D: C# -> D
# Bass line: C# (on beat 1), D (beat 2), F (beat 3), A (beat 4)

bass_notes = [61, 62, 64, 67]
bass_times = [1.5, 1.875, 2.25, 2.625]
for time, note in zip(bass_times, bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Bar 2: Piano (Diane) comps with Dm7 on beats 2 and 4
piano_notes = [62, 64, 67, 71]
piano_times = [1.875, 2.625]
for time in piano_times:
    for note in piano_notes:
        piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Bar 2: Sax (Dante) plays first part of the motif
# D - F - A (with a half note on D, then a pickup to F)
sax_notes = [62, 64, 67]
sax_times = [1.5, 1.875, 2.25]
sax_durations = [0.375, 0.375, 0.375]
for time, note, duration in zip(sax_times, sax_notes, sax_durations):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

# Bar 3: Bass continues walking
# F -> G -> A -> Bb (chromatic approach to A)
bass_notes = [64, 65, 67, 69]
bass_times = [2.625, 2.875, 3.25, 3.625]
for time, note in zip(bass_times, bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Bar 3: Piano comps again on beats 2 and 4
piano_times = [3.125, 3.875]
for time in piano_times:
    for note in piano_notes:
        piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Bar 3: Sax plays the second part of the motif
# C (on beat 3), then a rest, then a pickup to D again
sax_notes = [71]
sax_times = [3.25, 3.875]
sax_durations = [0.375, 0.375]
for time, note, duration in zip(sax_times, sax_notes, sax_durations):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

# Bar 4: Bass repeats F -> G -> A -> Bb again
bass_notes = [64, 65, 67, 69]
bass_times = [3.625, 3.875, 4.25, 4.625]
for time, note in zip(bass_times, bass_notes):
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.375))

# Bar 4: Piano comps on beats 2 and 4
piano_times = [4.125, 4.875]
for time in piano_times:
    for note in piano_notes:
        piano.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.25))

# Bar 4: Sax finishes the motif
# D (on beat 1), then a rest
sax_notes = [62]
sax_times = [4.5, 4.875]
sax_durations = [0.375, 0.375]
for time, note, duration in zip(sax_times, sax_notes, sax_durations):
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + duration))

# Write the MIDI file
pm.write('dante_intro.mid')
