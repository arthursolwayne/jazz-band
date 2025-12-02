
import pretty_midi
import numpy as np

# Initialize the MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')

drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)

pm.instruments = [drums, sax, bass, piano]

# BPM = 160 => 1 beat = 0.375 seconds
# 1 bar = 4 beats = 1.5 seconds

# Bar 1: Drums only (short, sparse)
# Kick on beat 1, snare on beat 3, hihat on beat 2 and 4 (but softer)
bar1_start = 0.0
bar1_end = 1.5

# Kick on beat 1 (0.0)
drums.notes.append(pretty_midi.Note(
    velocity=75, pitch=36, start=bar1_start, end=bar1_start + 0.1
))

# Snare on beat 3 (0.75)
drums.notes.append(pretty_midi.Note(
    velocity=60, pitch=38, start=bar1_start + 0.75, end=bar1_start + 0.85
))

# Hihat on beat 2 (0.375) and beat 4 (1.125)
drums.notes.append(pretty_midi.Note(
    velocity=50, pitch=42, start=bar1_start + 0.375, end=bar1_start + 0.425
))
drums.notes.append(pretty_midi.Note(
    velocity=50, pitch=42, start=bar1_start + 1.125, end=bar1_start + 1.175
))

# Bar 2–4: Full ensemble

bar2_start = 1.5
bar4_end = 4.5

# Bass line (Marcus) – Walking line with chromatic approaches
# D -> C# -> D -> E -> F -> E -> D -> C -> D
bass_notes = [62, 61, 62, 64, 65, 64, 62, 60, 62]
bass_durations = [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.25]
bass_velocities = [65, 67, 63, 68, 70, 66, 64, 63, 65]

for i in range(len(bass_notes)):
    start = bar2_start + i * 0.25
    end = start + bass_durations[i]
    bass.notes.append(pretty_midi.Note(velocity=bass_velocities[i], pitch=bass_notes[i], start=start, end=end))

# Piano chords (Diane) – 7th chords, comp on 2 & 4
# Bar 2: D7 at beat 2
# Bar 3: G7 at beat 2
# Bar 4: C7 at beat 2 and 4
# Chord definitions (7th chords)
D7 = [62, 64, 67, 69]
G7 = [67, 69, 71, 74]
C7 = [60, 62, 67, 69]

# Bar 2: D7 at beat 2 (0.375)
for pitch in D7:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=bar2_start + 0.375, end=bar2_start + 0.425))

# Bar 3: G7 at beat 2 (0.375)
for pitch in G7:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=bar2_start + 0.375 + 1.5, end=bar2_start + 0.425 + 1.5))

# Bar 4: C7 at beat 2 (0.375) and 4 (1.125)
for pitch in C7:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=bar2_start + 0.375 + 3.0, end=bar2_start + 0.425 + 3.0))
    piano.notes.append(pretty_midi.Note(velocity=65, pitch=pitch, start=bar2_start + 1.125 + 3.0, end=bar2_start + 1.175 + 3.0))

# Drums for Bars 2–4
# Full kit, dynamic variation, space
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0, 1, 2]:
    start_time = bar2_start + bar * 1.5
    kick_velocity = 75 if bar == 2 else 70
    snare_velocity = 65 if bar == 2 else 60
    hihat_velocity = 55

    # Kick on beat 1 and 3 (0.0 and 0.75)
    drums.notes.append(pretty_midi.Note(velocity=kick_velocity, pitch=36, start=start_time, end=start_time + 0.1))
    drums.notes.append(pretty_midi.Note(velocity=kick_velocity, pitch=36, start=start_time + 0.75, end=start_time + 0.85))

    # Snare on beat 2 and 4 (0.375 and 1.125)
    drums.notes.append(pretty_midi.Note(velocity=snare_velocity, pitch=38, start=start_time + 0.375, end=start_time + 0.425))
    drums.notes.append(pretty_midi.Note(velocity=snare_velocity, pitch=38, start=start_time + 1.125, end=start_time + 1.175))

    # Hihat on every eighth note
    for i in range(8):
        time = start_time + i * 0.1875
        end_time = time + 0.05
        drums.notes.append(pretty_midi.Note(velocity=hihat_velocity, pitch=42, start=time, end=end_time))

# Saxophone motif – D F# B (rest)
# Bar 2, beat 1 (0.0 on bar2_start = 1.5)
sax.notes.append(pretty_midi.Note(velocity=95, pitch=62, start=bar2_start, end=bar2_start + 0.35))  # D, held
sax.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=bar2_start + 0.35, end=bar2_start + 0.75))  # F#, half note
sax.notes.append(pretty_midi.Note(velocity=85, pitch=69, start=bar2_start + 0.75, end=bar2_start + 0.95))  # B, quarter note
# Rest on beat 4 (1.125), no note

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file generated: 'dante_intro.mid'")
