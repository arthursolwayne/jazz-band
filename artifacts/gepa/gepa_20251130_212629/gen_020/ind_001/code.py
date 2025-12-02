
import pretty_midi
import numpy as np

# Initialize MIDI file
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]
pm.tempos = [pretty_midi.TempoChange(160, 0)]

# Define the key: D minor (D, Eb, F, G, Ab, Bb, C)
# MIDI note numbers:
# D3 = 62, Eb3 = 63, F3 = 64, G3 = 65, Ab3 = 66, Bb3 = 67, C4 = 60

# Define the 4 bars (each bar is 6 beats at 160 BPM, 1.5s per bar)
# Bar indices: 0, 1, 2, 3
# Each bar has 4 beats (quarter notes)

# --- S A X O P H O N E (Tenor) ---
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

# Define the sax melody: a simple, haunting motif
# Dm7 -> G7 -> Cm7 -> F7
# D3, F3, Ab3, Bb3, D4
# Start on beat 2 of bar 2, play a short motif, then leave it hanging.

note_lengths = [0.5, 0.25, 0.25, 0.25]  # 16th notes
note_times = [0.75, 1.0, 1.25, 1.5]  # Start on beat 2 of bar 2

notes = [62, 64, 66, 67]  # D3, F3, Ab3, Bb3
for time, pitch in zip(note_times, notes):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.25)
    sax.notes.append(note)

pm.instruments.append(sax)

# --- P I A N O (Diane) ---
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

# Diane plays 7th chords, comping on 2 and 4
# We'll create a pattern for bars 2–4

# Define 7th chords in Dm
# Dm7 (D, F, Ab, C) for bar 2
# G7 (G, Bb, D, F) for bar 3
# Cm7 (C, Eb, G, Bb) for bar 4

# Bar 2, 2nd beat
piano_notes = [62, 64, 66, 60]
piano_times = [1.0, 1.0, 1.0, 1.0]
for time, pitch in zip(piano_times, piano_notes):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Bar 3, 2nd beat
piano_notes = [65, 67, 62, 64]
piano_times = [2.0, 2.0, 2.0, 2.0]
for time, pitch in zip(piano_times, piano_notes):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

# Bar 4, 2nd beat
piano_notes = [60, 63, 65, 67]
piano_times = [3.0, 3.0, 3.0, 3.0]
for time, pitch in zip(piano_times, piano_notes):
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.5)
    piano.notes.append(note)

pm.instruments.append(piano)

# --- B A S S (Marcus) ---
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)

# Walking bass line in Dm
# Bar 2-4
# D, Eb, F, G, Ab, Bb, C, D

notes = [62, 63, 64, 65, 66, 67, 60, 62]
times = [1.0, 1.25, 1.5, 1.75, 2.0, 2.25, 2.5, 2.75]

for time, pitch in zip(times, notes):
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + 0.25)
    bass.notes.append(note)

pm.instruments.append(bass)

# --- D R U M S (Little Ray) ---
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
drums = pretty_midi.Instrument(program=drum_program)

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1 is 0 to 1.5 seconds

# Kick on 0.0, 0.75
for time in [0.0, 0.75]:
    kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
    drums.notes.append(kick)

# Snare on 0.5, 1.25
for time in [0.5, 1.25]:
    snare = pretty_midi.Note(velocity=90, pitch=38, start=time, end=time + 0.1)
    drums.notes.append(snare)

# Hihat on every eighth
for time in np.arange(0.0, 1.5, 0.125):
    hihat = pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(hihat)

# Bar 2–4: Keep same pattern but with syncopation and dynamic variation
# Add some syncopation and variation in velocity

for bar in range(2, 4):
    bar_start = bar * 1.5
    for time in [bar_start + 0.0, bar_start + 0.75]:
        kick = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(kick)
    for time in [bar_start + 0.5, bar_start + 1.25]:
        snare = pretty_midi.Note(velocity=85, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(snare)
    for time in np.arange(bar_start, bar_start + 1.5, 0.125):
        hihat_velocity = 60 + (np.random.rand() * 25)
        hihat = pretty_midi.Note(velocity=int(hihat_velocity), pitch=42, start=time, end=time + 0.05)
        drums.notes.append(hihat)

pm.instruments.append(drums)

# Save the MIDI file
pm.write("dante_cellar_intro.mid")
print("MIDI file saved as 'dante_cellar_intro.mid'")
