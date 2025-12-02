
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F major
key = 'F'

# Time signature is 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)

pm.time_signature_changes.append(time_signature)

# Set the instrument for each musician
# 0: Drums (percussion)
# 1: Bass (acoustic bass)
# 2: Piano (electric piano)
# 3: Tenor Sax (acoustic sax)

# Create instruments
drum_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drum_inst = pretty_midi.Instrument(program=drum_program)
bass_inst = pretty_midi.Instrument(program=bass_program)
piano_inst = pretty_midi.Instrument(program=piano_program)
sax_inst = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(drum_inst)
pm.instruments.append(bass_inst)
pm.instruments.append(piano_inst)
pm.instruments.append(sax_inst)

# Define note durations in seconds (at 160 BPM, 1 beat = 0.375s)
beat = 0.375
bar = 4 * beat  # 1.5 seconds per bar
quarter = beat
eighth = beat / 2
sixteenth = beat / 4

# Bar 1: Little Ray (drums) alone
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time starts at 0
bar_1_start = 0.0
kick_notes = [60, 60]  # C3 (kick)
snare_notes = [62, 62]  # D3 (snare)
hihat_notes = [42] * 8  # 8 hihats on every eighth

# Kick on 1 and 3
kick_times = [bar_1_start + 0.0, bar_1_start + 2.0 * beat]
for note, time in zip(kick_notes, kick_times):
    drum_inst.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))

# Snare on 2 and 4
snare_times = [bar_1_start + 1.0 * beat, bar_1_start + 3.0 * beat]
for note, time in zip(snare_notes, snare_times):
    drum_inst.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.1))

# Hihat on every eighth
hihat_times = [bar_1_start + i * eighth for i in range(8)]
for time in hihat_times:
    drum_inst.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.05))

# Bar 2: Everyone comes in
bar_2_start = bar_1_start + bar

# Marcus (bass) - walking line in F major with chromatic approaches
# F major scale: F G A Bb C D E
# Chromatic approaches on the 3rd and 7th
bass_notes = [71, 72, 73, 71, 69, 71, 72, 74]  # F G A G E F G A
bass_times = [bar_2_start + i * beat for i in range(8)]
for note, time in zip(bass_notes, bass_times):
    bass_inst.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Diane (piano) - 7th chords on 2 and 4
# Fmaj7, Am7, D7, Bbm7
piano_notes = [
    65, 69, 72, 76,  # Fmaj7
    69, 71, 76, 79,  # Am7
    72, 76, 79, 82,  # D7
    65, 69, 72, 76   # Bbm7
]
piano_times = [bar_2_start + 1.0 * beat, bar_2_start + 3.0 * beat]
for i, time in enumerate(piano_times):
    for note in piano_notes[i * 4 : (i + 1) * 4]:
        piano_inst.notes.append(pretty_midi.Note(velocity=95, pitch=note, start=time, end=time + 0.5))

# Little Ray (drums) - same pattern as Bar 1
kick_times = [bar_2_start + 0.0, bar_2_start + 2.0 * beat]
for note, time in zip(kick_notes, kick_times):
    drum_inst.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1))

snare_times = [bar_2_start + 1.0 * beat, bar_2_start + 3.0 * beat]
for note, time in zip(snare_notes, snare_times):
    drum_inst.notes.append(pretty_midi.Note(velocity=85, pitch=note, start=time, end=time + 0.1))

hihat_times = [bar_2_start + i * eighth for i in range(8)]
for time in hihat_times:
    drum_inst.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.05))

# Bar 3: You (sax) - your motif
bar_3_start = bar_2_start + bar

# Tenor sax motif: short phrase, space between notes, emotional
# Notes: F (65), Ab (67), C (69), Bb (67), F (65) — descending with a chromatic twist
sax_notes = [65, 67, 69, 67, 65]
sax_times = [bar_3_start + 0.0, bar_3_start + 0.5, bar_3_start + 1.0, bar_3_start + 1.375, bar_3_start + 1.75]
sax_velocities = [100, 90, 100, 95, 100]

for note, time, vel in zip(sax_notes, sax_times, sax_velocities):
    sax_inst.notes.append(pretty_midi.Note(velocity=vel, pitch=note, start=time, end=time + 0.25))

# Bar 4: You continue the motif, completing it
bar_4_start = bar_3_start + bar

# Complete the motif, resolving on F
sax_notes = [65]
sax_times = [bar_4_start + 0.0]
sax_velocities = [100]

for note, time, vel in zip(sax_notes, sax_times, sax_velocities):
    sax_inst.notes.append(pretty_midi.Note(velocity=vel, pitch=note, start=time, end=time + 0.5))

# Add dynamics with velocity changes
# (Already included in note velocities)

# Save the MIDI file
pm.write('dante_intro.mid')

print("MIDI file created: 'dante_intro.mid'")
