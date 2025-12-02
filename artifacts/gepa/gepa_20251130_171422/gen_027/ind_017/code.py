
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instrument definitions
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
drums_program = pretty_midi.instrument_name_to_program('Drum Kit')

# Create instruments
sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

# Add instruments to the MIDI file
pm.instruments.append(sax)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)

# Time per beat (in seconds)
time_per_beat = 60.0 / pm.estimate_tempo()  # 60 / 160 = 0.375 seconds per beat
bar_length = 4 * time_per_beat  # 1.5 seconds per bar

# Define the key
key = 'F major'

# --- Bar 1: Little Ray on drums alone ---
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.625))

# Hihat on every eighth
hihat_velocity = 70
hihat_pitch = 42

# Eighth notes in bar 1
for i in range(0, 4):
    start = i * 0.375
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=hihat_velocity, pitch=hihat_pitch, start=start, end=end))

# --- Bars 2-4: Full ensemble enters, sax motif ---
# Saxophone motif: F - Bb - Bb - G (F7 chord shape, but with a twist)
# Notes in F major: F (72), Bb (70), Bb (70), G (71)
# Start at 1.5 seconds (Bar 2), with space before the entrance

# Bar 2: Start motif on beat 1
sax.notes.append(pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.65))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.4))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=2.775))
sax.notes.append(pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.15))

# Bar 3: Bass line - Chromatic walking, not just rhythm
# Notes: F (72), Gb (71), G (71), Ab (70), A (72), Bb (70), Bb (70), B (72)
# Each note on a beat (16 notes in 4 bars, but here only in bar 3)
for i in range(0, 4):
    start = 1.5 + (i * time_per_beat)
    note = 72 - i
    if note < 64:
        note = 64
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=start + 0.375))

# Bar 3: Piano comping with emotion - 7th chords on 2 and 4
# F7 on beat 2, Bb7 on beat 4
# F7: F, A, C, Eb
# Bb7: Bb, D, F, Ab
# Use velocities to reflect emotional tension

# F7 on beat 2 (time = 2.25)
for pitch in [72, 76, 79, 70]:
    piano.notes.append(pretty_midi.Note(velocity=95, pitch=pitch, start=2.25, end=2.375))

# Bb7 on beat 4 (time = 3.0)
for pitch in [70, 74, 72, 69]:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=3.0, end=3.125))

# Bar 4: Drums continue, more intensity
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=4.125, end=4.5))

# Snare on 2 and 4 (slightly louder)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625))

# Hihat continues, with more variation in velocity
hihat_velocity = 75
for i in range(0, 4):
    start = 3.0 + (i * 0.375)
    end = start + 0.125
    drums.notes.append(pretty_midi.Note(velocity=hihat_velocity, pitch=hihat_pitch, start=start, end=end))

# Save the MIDI file
pm.write("jazz_intro_wayne.mid")
print("MIDI file written to 'jazz_intro_wayne.mid'")
