
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key: F minor (Fm)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # F minor is key number 5

# Define the time per beat (in seconds)
time_per_beat = 60.0 / 160.0  # 0.375 seconds per beat

# Define the four bars (each bar is 4 beats)
bar_length = 4 * time_per_beat  # 1.5 seconds per bar

# Define the start time for each bar
bar_start_times = [0, bar_length, 2 * bar_length, 3 * bar_length]

# -----------------------------
# 1. Drums: Little Ray (Bar 1)
# -----------------------------

# Create drum track
drum_program = pretty_midi.instrument_name_to_program('Drums')
drum_track = pretty_midi.Instrument(program=drum_program)

# Kick on 1 and 3 of Bar 1
drum_track.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start_times[0], end=bar_start_times[0] + time_per_beat))
drum_track.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=bar_start_times[0] + 2 * time_per_beat, end=bar_start_times[0] + 2 * time_per_beat + time_per_beat))

# Snare on 2 and 4 of Bar 1
drum_track.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start_times[0] + time_per_beat, end=bar_start_times[0] + time_per_beat + time_per_beat))
drum_track.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=bar_start_times[0] + 3 * time_per_beat, end=bar_start_times[0] + 3 * time_per_beat + time_per_beat))

# Hi-hat on every 8th note
for i in range(8):
    drum_track.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=bar_start_times[0] + i * time_per_beat / 2, end=bar_start_times[0] + i * time_per_beat / 2 + time_per_beat / 2))

pm.instruments.append(drum_track)

# -----------------------------
# 2. Bass: Marcus (Bars 1-4)
# -----------------------------

# Bass track (Fm key: F, Ab, Bb, C, Db, Eb, F)
# Walking line in Fm with chromatic approaches

bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass_track = pretty_midi.Instrument(program=bass_program)

# Bar 1
bass_notes = [
    (38, 0),         # F2 (root)
    (36, 0.25),      # Eb2 (chromatic approach)
    (37, 0.75),      # E2 (chromatic approach)
    (40, 1.0)        # Ab2 (fifth)
]
for note, time in bass_notes:
    bass_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[0] + time, end=bar_start_times[0] + time + time_per_beat / 4))

# Bar 2
bass_notes = [
    (40, 0),         # Ab2 (fifth)
    (37, 0.5),       # E2 (chromatic approach)
    (36, 0.75),      # Eb2 (chromatic approach)
    (38, 1.0)        # F2 (root)
]
for note, time in bass_notes:
    bass_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[1] + time, end=bar_start_times[1] + time + time_per_beat / 4))

# Bar 3
bass_notes = [
    (38, 0),         # F2 (root)
    (41, 0.25),      # Bb2 (sixth)
    (42, 0.75),      # Bb2 (chromatic approach)
    (36, 1.0)        # Eb2 (fourth)
]
for note, time in bass_notes:
    bass_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[2] + time, end=bar_start_times[2] + time + time_per_beat / 4))

# Bar 4
bass_notes = [
    (36, 0),         # Eb2 (fourth)
    (37, 0.25),      # E2 (chromatic approach)
    (41, 0.75),      # Bb2 (sixth)
    (38, 1.0)        # F2 (root)
]
for note, time in bass_notes:
    bass_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[3] + time, end=bar_start_times[3] + time + time_per_beat / 4))

pm.instruments.append(bass_track)

# -----------------------------
# 3. Piano: Diane (Bars 1-4)
# -----------------------------

# Piano track (open voicings, each bar a new chord, resolve on last beat)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano_track = pretty_midi.Instrument(program=piano_program)

# Bar 1: Cm7 (Fm key, ii chord)
# Cm7: C, Eb, Gb, Bb
for note in [60, 64, 66, 67]:
    piano_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[0], end=bar_start_times[0] + time_per_beat))

# Bar 2: G7 (V chord with tritone substitution of D7)
# G7: G, B, D, F
for note in [71, 74, 76, 79]:
    piano_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[1], end=bar_start_times[1] + time_per_beat))

# Bar 3: Dm7 (vi chord)
# Dm7: D, F, A, C
for note in [62, 65, 69, 72]:
    piano_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[2], end=bar_start_times[2] + time_per_beat))

# Bar 4: Fm7 (i chord, resolves back)
# Fm7: F, Ab, C, Eb
for note in [53, 56, 60, 64]:
    piano_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[3], end=bar_start_times[3] + time_per_beat))

pm.instruments.append(piano_track)

# -----------------------------
# 4. Sax: Dante (Bars 2-4)
# -----------------------------

# Tenor sax (Fm key: F, Ab, Bb, C, Db, Eb, F)
# Motif: Start with a melodic line, leave it hanging, return to finish it.

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax_track = pretty_midi.Instrument(program=sax_program)

# Bar 2: Start the motif
# F (53), Ab (56), Bb (58), C (60)
sax_notes = [
    (53, 0),         # F
    (56, 0.25),      # Ab
    (58, 0.5),       # Bb
    (60, 0.75)       # C
]
for note, time in sax_notes:
    sax_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[1] + time, end=bar_start_times[1] + time + 0.15))

# Bar 3: Let it hang, but add some tension
# F (53), Db (55), Bb (58)
sax_notes = [
    (53, 0),         # F
    (55, 0.5),       # Db
    (58, 0.75)       # Bb
]
for note, time in sax_notes:
    sax_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[2] + time, end=bar_start_times[2] + time + 0.15))

# Bar 4: Return with a resolution
# F (53), Eb (64), C (60)
sax_notes = [
    (53, 0),         # F
    (64, 0.25),      # Eb
    (60, 0.75)       # C
]
for note, time in sax_notes:
    sax_track.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=bar_start_times[3] + time, end=bar_start_times[3] + time + 0.15))

pm.instruments.append(sax_track)

# -----------------------------
# Save the MIDI file
# -----------------------------

pm.write('jazz_intro_wayne.mid')
print("MIDI file saved as 'jazz_intro_wayne.mid'")
