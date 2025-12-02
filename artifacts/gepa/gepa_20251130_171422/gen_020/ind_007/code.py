
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object with 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Time signature: 4/4, 160 BPM
# 1 bar = 0.75 seconds, since 60 / 160 = 0.375 seconds per beat, 4 beats per bar = 1.5 seconds
# But we're compressing to fit 4 bars in 6 seconds (1.5 sec per bar)
# So we're using 60 / 160 * 4 = 1.5 sec per bar

# 1 bar = 1.5 seconds
# 1 beat = 0.375 seconds

# Add instruments to the MIDI
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)
midi.instruments.append(sax)

# Time in seconds
time = 0.0

# Bar 1: Drums alone - subtle, sparse, building tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 - 0.0 to 1.5 seconds
# Kick on 1 (0.0), 3 (0.75)
kick_notes = [36, 36]  # C2
kick_times = [0.0, 0.75]
for note, t in zip(kick_notes, kick_times):
    kick = pretty_midi.Note(velocity=80, pitch=note, start=t, end=t + 0.1)
    drums.notes.append(kick)

# Snare on 2 (0.375), 4 (1.125)
snare_notes = [38, 38]  # D2
snare_times = [0.375, 1.125]
for note, t in zip(snare_notes, snare_times):
    snare = pretty_midi.Note(velocity=80, pitch=note, start=t, end=t + 0.1)
    drums.notes.append(snare)

# Hihat on every eighth (0.0, 0.375, 0.75, 1.125)
hihat_notes = [42, 42, 42, 42]  # G#6
hihat_times = [0.0, 0.375, 0.75, 1.125]
for note, t in zip(hihat_notes, hihat_times):
    hihat = pretty_midi.Note(velocity=80, pitch=note, start=t, end=t + 0.05)
    drums.notes.append(hihat)

time = 1.5  # Move to Bar 2

# Bar 2: All instruments in, sax starts the melody

# Bass: Walking line in Fm (Fm7, Ab, Bb, C, F)
# Fm7 = F, Ab, Bb, Dbb (or Db) => use F, Ab, Bb, C
# Walking bass line (F, Ab, Bb, C, F, Ab, Bb, C, F)
# Time: 1.5 to 3.0 seconds

bass_notes = [53, 57, 59, 60, 53, 57, 59, 60, 53]  # F, Ab, Bb, C
bass_times = [1.5, 1.875, 2.25, 2.625, 2.75, 3.125, 3.5, 3.875, 4.0]
for note, t in zip(bass_notes, bass_times):
    # Duration is 0.375 seconds per beat
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=t, end=t + 0.375)
    bass.notes.append(bass_note)

# Piano: Comp on 2 and 4 (Bar 2 and 4) with 7th chords in Fm
# Bar 2: Fm7 = F, Ab, Bb, C
# Bar 4: Fm7 (same chord)
# Comp on beat 2 and 4 (0.375 and 1.125 in Bar 2, 0.375 and 1.125 in Bar 4)
# Set duration to 0.25 for clarity

# Bar 2, beat 2: Fm7
fm7_notes = [53, 57, 59, 60]  # F, Ab, Bb, C
fm7_time = 1.875
for note in fm7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=fm7_time, end=fm7_time + 0.25)
    piano.notes.append(piano_note)

# Bar 2, beat 4: Fm7
fm7_time2 = 2.625
for note in fm7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=fm7_time2, end=fm7_time2 + 0.25)
    piano.notes.append(piano_note)

# Sax: Start the melody with a short motif — F, Ab, Bb, C
# Start on F (beat 1 of Bar 2), then Ab, Bb, C (beat 2, 3, 4)
# Leave it hanging at C on beat 4 for tension

sax_notes = [53, 57, 59, 60]  # F, Ab, Bb, C
sax_times = [1.5, 1.875, 2.25, 2.625]
for note, t in zip(sax_notes, sax_times):
    sax_note = pretty_midi.Note(velocity=100, pitch=note, start=t, end=t + 0.375)
    sax.notes.append(sax_note)

# Bar 3 & 4: Continue the bass line and piano comp
# Bass continues the walking line
# Piano comp on beat 2 and 4 of Bar 3 and 4

# Bar 3
bass_notes = [60, 53, 57, 59, 60]  # C, F, Ab, Bb
bass_times = [3.0, 3.375, 3.75, 4.125, 4.5]
for note, t in zip(bass_notes, bass_times):
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=t, end=t + 0.375)
    bass.notes.append(bass_note)

# Bar 3, beat 2: Fm7
fm7_time = 3.375
for note in fm7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=fm7_time, end=fm7_time + 0.25)
    piano.notes.append(piano_note)

# Bar 3, beat 4: Fm7
fm7_time2 = 4.125
for note in fm7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=fm7_time2, end=fm7_time2 + 0.25)
    piano.notes.append(piano_note)

# Bar 4
bass_notes = [59, 60, 53, 57, 59, 60]  # Bb, C, F, Ab
bass_times = [4.5, 4.875, 5.25, 5.625, 5.875, 6.0]
for note, t in zip(bass_notes, bass_times):
    bass_note = pretty_midi.Note(velocity=80, pitch=note, start=t, end=t + 0.375)
    bass.notes.append(bass_note)

# Bar 4, beat 2: Fm7
fm7_time = 5.25
for note in fm7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=fm7_time, end=fm7_time + 0.25)
    piano.notes.append(piano_note)

# Bar 4, beat 4: Fm7
fm7_time2 = 5.625
for note in fm7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=fm7_time2, end=fm7_time2 + 0.25)
    piano.notes.append(piano_note)

# Save the MIDI file
midi.write("dante_intro.mid")
