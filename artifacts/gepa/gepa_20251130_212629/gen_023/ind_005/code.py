
import pretty_midi
import numpy as np

# Create a PrettyMIDI object at 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Key: F major
midi.key_signature_changes = [pretty_midi.KeySignature(0, 0.0)]  # F major (no sharps/flats)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the MIDI file
midi.instruments = [bass, piano, drums, sax]

# Time per bar at 160 BPM (seconds per beat = 60/160 = 0.375)
# 4 bars = 6.0 seconds
# Each bar is 1.5 seconds
bar_length = 1.5
time_per_beat = 0.375

# Function to create a note with start time, duration, pitch, and velocity
def create_note(instrument, start, duration, pitch, velocity=100):
    note = pretty_midi.Note(
        velocity=velocity,
        pitch=pitch,
        start=start,
        end=start + duration
    )
    instrument.notes.append(note)

# Bar 1: Little Ray on drums (snare on 2 and 4, kick on 1 and 3)
# Hihat on every eighth
drum_notes = {
    'kick': 36,
    'snare': 38,
    'hihat': 42
}

# 1st bar
bar_1_start = 0.0

# Kick on 1 and 3
create_note(drums, bar_1_start + 0.0, 0.1, drum_notes['kick'])
create_note(drums, bar_1_start + 0.75, 0.1, drum_notes['kick'])

# Snare on 2 and 4
create_note(drums, bar_1_start + 0.375, 0.1, drum_notes['snare'])
create_note(drums, bar_1_start + 0.75 * 3, 0.1, drum_notes['snare'])

# Hihat on every eighth
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5]
for t in hihat_times:
    create_note(drums, t, 0.05, drum_notes['hihat'])

# Bar 2: Everyone comes in. You (sax) play the 4-note motif
bar_2_start = bar_length

# Sax: F - A - C - F (F major triad, but with a twist)
note_durations = [0.15, 0.15, 0.15, 0.15]
note_pitches = [72, 76, 79, 72]  # F, A, C, F (in the key of F major, middle C = 60)
note_start = bar_2_start
for i, (pitch, duration) in enumerate(zip(note_pitches, note_durations)):
    create_note(sax, note_start + i * (duration + 0.05), duration, pitch, velocity=100)

# Diane's piano: 7th chords on beats 2 and 4 (comping)
piano_notes = {
    2: [72, 76, 79, 84],  # F7 (F, A, C, E)
    4: [72, 76, 79, 84]   # F7 again, but with a subtle shift
}

for beat in [2, 4]:
    beat_time = bar_2_start + (beat - 1) * time_per_beat
    for pitch in piano_notes[beat]:
        create_note(piano, beat_time, 0.3, pitch, velocity=90)

# Marcus's bass: walking line with chromatic approaches
# F, Gb, G, A -> F, G, Ab, A -> F, G, Ab, Bb -> F, G, A, Bb
bass_notes = [
    (bar_2_start, 72),  # F
    (bar_2_start + 0.375, 70),  # Gb
    (bar_2_start + 0.75, 71),  # G
    (bar_2_start + 1.125, 77),  # A

    (bar_2_start + 1.5, 72),  # F
    (bar_2_start + 1.875, 71),  # G
    (bar_2_start + 2.25, 70),  # Ab
    (bar_2_start + 2.625, 71),  # A

    (bar_2_start + 3.0, 72),  # F
    (bar_2_start + 3.375, 71),  # G
    (bar_2_start + 3.75, 70),  # Ab
    (bar_2_start + 4.125, 70),  # Bb
]

for time, pitch in bass_notes:
    create_note(bass, time, 0.25, pitch, velocity=80)

# Bar 3: sax repeats the motif but ends on a rest (no resolution)
bar_3_start = bar_2_start + bar_length

note_pitches = [72, 76, 79, 72]  # F, A, C, F
note_start = bar_3_start
for i, pitch in enumerate(note_pitches):
    if i == 3:
        break  # End on the third note, leave it hanging
    create_note(sax, note_start + i * (0.15 + 0.05), 0.15, pitch, velocity=100)

# Bar 4: sax plays a half note on F (a question, not a statement)
bar_4_start = bar_3_start + bar_length

create_note(sax, bar_4_start, 0.75, 72, velocity=100)  # F, held for 3/4 of the bar

# Final silence to let it breathe
# No notes, just space

# Write the MIDI file
midi.write("jazz_intro_f_major.mid")
