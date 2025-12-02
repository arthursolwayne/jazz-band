
import pretty_midi
from pretty_midi import Note, Instrument

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to D major
pm.key_signature.key = 'D'

# Define the time signature (4/4)
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Define instrument tracks
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')

# Create instruments
bass_instr = Instrument(program=bass_program, is_drum=False)
piano_instr = Instrument(program=piano_program, is_drum=False)
drums_instr = Instrument(program=drums_program, is_drum=True)
sax_instr = Instrument(program=sax_program, is_drum=False)

# Add instruments to the MIDI file
pm.instruments.append(bass_instr)
pm.instruments.append(piano_instr)
pm.instruments.append(drums_instr)
pm.instruments.append(sax_instr)

# Set the time per bar (160 BPM, 4/4 time)
notes_per_beat = 4
beat_duration = 60 / 160  # seconds per beat
bar_duration = beat_duration * 4  # 4 beats per bar
total_duration = bar_duration * 4  # 4 bars

# ===================
# Bar 1: Drums Only — Set the tension
# ===================

# Kick on 1 and 3
drums_instr.notes.append(Note(36, 60, 0, 0.5))  # Kick on beat 1 (start)
drums_instr.notes.append(Note(36, 60, 1.5, 0.5))  # Kick on beat 3

# Snare on 2 and 4
drums_instr.notes.append(Note(38, 60, 1.0, 0.5))  # Snare on beat 2
drums_instr.notes.append(Note(38, 60, 2.5, 0.5))  # Snare on beat 4

# Hi-hat on every eighth note
hi_hat_notes = [42, 42, 42, 42, 42, 42, 42, 42]
hi_hat_times = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
for note, time in zip(hi_hat_notes, hi_hat_times):
    drums_instr.notes.append(Note(note, 60, time, 0.25))

# ===================
# Bar 2: All in — Sax starts the motif
# ===================

# Sax: Melody — one short phrase, starts on beat 1, ends on beat 3 with a rest
sax_notes = [62, 60, 62, 60]  # D, C, D, C — simple motif
sax_times = [0.0, 0.5, 0.75, 1.25]
sax_durations = [0.5, 0.25, 0.5, 0.25]
sax_velocities = [90, 85, 90, 75]  # Vary dynamics

for note, time, duration, velocity in zip(sax_notes, sax_times, sax_durations, sax_velocities):
    sax_instr.notes.append(Note(note, velocity, time, duration))

# Bass: Walking line with chromatic approach
bass_notes = [55, 57, 59, 56, 58, 60, 59, 57]  # D, E, F#, E, F#, G, F#, E
bass_times = [0.0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75]
bass_durations = [0.25] * 8
bass_velocities = [70] * 8

for note, time, duration, velocity in zip(bass_notes, bass_times, bass_durations, bass_velocities):
    bass_instr.notes.append(Note(note, velocity, time, duration))

# Piano: 7th chords on 2 and 4, comp on beat 2 and 4
piano_notes = [
    # Beat 2 (C7 = C, E, G, B)
    (60, 64, 67, 71),  # C7
    # Beat 4 (F7 = F, A, C, E)
    (65, 69, 72, 76)   # F7
]
piano_times = [1.0, 2.5]
piano_durations = [0.5, 0.5]
piano_velocity = 80

for chord_notes, time, duration in zip(piano_notes, piano_times, piano_durations):
    for note in chord_notes:
        piano_instr.notes.append(Note(note, piano_velocity, time, duration))

# ===================
# Bar 3: Sax repeats motif, slightly altered
# ===================

# Sax: Same motif, same rhythm, but with a slight inflection
sax_notes = [62, 60, 62, 60]  # D, C, D, C
sax_times = [2.0, 2.5, 2.75, 3.25]
sax_durations = [0.5, 0.25, 0.5, 0.25]
sax_velocities = [90, 85, 90, 75]

for note, time, duration, velocity in zip(sax_notes, sax_times, sax_durations, sax_velocities):
    sax_instr.notes.append(Note(note, velocity, time, duration))

# Bass: Walking line again
bass_notes = [55, 57, 59, 56, 58, 60, 59, 57]
bass_times = [2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75]
bass_durations = [0.25] * 8
bass_velocities = [70] * 8

for note, time, duration, velocity in zip(bass_notes, bass_times, bass_durations, bass_velocities):
    bass_instr.notes.append(Note(note, velocity, time, duration))

# Piano: Comp on 2 and 4 again
piano_notes = [
    (60, 64, 67, 71),  # C7
    (65, 69, 72, 76)   # F7
]
piano_times = [3.0, 4.5]
piano_durations = [0.5, 0.5]

for chord_notes, time, duration in zip(piano_notes, piano_times, piano_durations):
    for note in chord_notes:
        piano_instr.notes.append(Note(note, piano_velocity, time, duration))

# ===================
# Bar 4: End with a question — sax leaves it hanging
# ===================

# Sax: Motif again, but ends on an incomplete phrase
sax_notes = [62, 60, 62, 60, 62]  # D, C, D, C, D — ends on a held D
sax_times = [4.0, 4.5, 4.75, 5.25, 5.5]
sax_durations = [0.5, 0.25, 0.5, 0.25, 0.5]
sax_velocities = [90, 85, 90, 75, 85]

for note, time, duration, velocity in zip(sax_notes, sax_times, sax_durations, sax_velocities):
    sax_instr.notes.append(Note(note, velocity, time, duration))

# Bass: Walking line once more
bass_notes = [55, 57, 59, 56, 58, 60, 59, 57]
bass_times = [4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75]
bass_durations = [0.25] * 8
bass_velocities = [70] * 8

for note, time, duration, velocity in zip(bass_notes, bass_times, bass_durations, bass_velocities):
    bass_instr.notes.append(Note(note, velocity, time, duration))

# Piano: Comp on 2 and 4 again
piano_notes = [
    (60, 64, 67, 71),  # C7
    (65, 69, 72, 76)   # F7
]
piano_times = [5.0, 6.5]
piano_durations = [0.5, 0.5]

for chord_notes, time, duration in zip(piano_notes, piano_times, piano_durations):
    for note in chord_notes:
        piano_instr.notes.append(Note(note, piano_velocity, time, duration))

# Drums: Same pattern again, but perhaps a little more urgency
# Kick on 1 and 3
drums_instr.notes.append(Note(36, 60, 4.0, 0.5))
drums_instr.notes.append(Note(36, 60, 5.5, 0.5))

# Snare on 2 and 4
drums_instr.notes.append(Note(38, 60, 4.5, 0.5))
drums_instr.notes.append(Note(38, 60, 6.0, 0.5))

# Hi-hat on every eighth
hi_hat_notes = [42, 42, 42, 42, 42, 42, 42, 42]
hi_hat_times = [4.0, 4.25, 4.5, 4.75, 5.0, 5.25, 5.5, 5.75]
for note, time in zip(hi_hat_notes, hi_hat_times):
    drums_instr.notes.append(Note(note, 60, time, 0.25))

# Save the MIDI file
pm.write("dante_intro.mid")
