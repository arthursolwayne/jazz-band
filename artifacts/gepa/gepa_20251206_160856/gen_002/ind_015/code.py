
import pretty_midi
import numpy as np

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set key to F minor (F, Gb, Ab, Bb, B, Db, Eb)
key = 'F minor'

# Set time signature to 4/4
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Create instruments
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
sax_program = pretty_midi.instrument_name_to_program('Tenor Sax')

drum_instr = pretty_midi.Instrument(program=drum_program)
bass_instr = pretty_midi.Instrument(program=bass_program)
piano_instr = pretty_midi.Instrument(program=piano_program)
sax_instr = pretty_midi.Instrument(program=sax_program)

pm.instruments.append(drum_instr)
pm.instruments.append(bass_instr)
pm.instruments.append(piano_instr)
pm.instruments.append(sax_instr)

# Time per bar in seconds (160 BPM = 0.75 seconds per beat, 3 beats per bar)
time_per_bar = 0.75 * 4  # 3 beats per bar at 160 BPM

# Time for each bar
bar_lengths = [time_per_bar] * 4

# Helper function to convert beat to time in seconds
def beat_to_time(beat):
    return beat / 160 * 60

# ---------------------------
# DRUMS: Little Ray
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Each bar is 4 beats
# Total time per bar: 3.0 seconds (at 160 BPM)
# 1 beat = 0.375 seconds
# 8th note = 0.1875 seconds

for bar in range(4):
    start_time = bar * time_per_bar
    for beat in [0, 2]:  # Kick on 1 and 3
        drum_instr.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=start_time + beat * 0.375, end=start_time + beat * 0.375 + 0.1))
    for beat in [1, 3]:  # Snare on 2 and 4
        drum_instr.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=start_time + beat * 0.375, end=start_time + beat * 0.375 + 0.1))
    for beat in range(4):  # Hihat on every eighth
        drum_instr.notes.append(pretty_midi.Note(velocity=70, pitch=42, start=start_time + beat * 0.1875, end=start_time + beat * 0.1875 + 0.05))

# ---------------------------
# BASS: Marcus
# Walking line in Fm (F, Ab, Bb, Db)
# Roots and fifths with chromatic approaches
# F (F), Gb (F#), Ab (Ab), Bb (Bb), B (B), Db (Db), Eb (Eb), F (F)
# Each bar: 4 beats
# Start time for each bar

# Fm key: F (7), Ab (8), Bb (2), Db (3)
# Walking pattern: F, Gb, Ab, Bb, B, Db, Eb, F

bass_notes = [
    7,  # F
    7,  # F
    8,  # Gb
    2,  # Bb
    11, # B
    3,  # Db
    5,  # Eb
    7   # F
]

bass_durations = [0.25] * 8  # 8 eighth notes in 4 bars

for i, note in enumerate(bass_notes):
    bar = i // 4
    beat = i % 4
    start_time = bar * time_per_bar + beat * 0.375
    bass_instr.notes.append(pretty_midi.Note(velocity=100, pitch=note + 12, start=start_time, end=start_time + bass_durations[i]))

# ---------------------------
# PIANO: Diane
# Open voicings, different chord each bar, resolve on the last.

# Bar 1: Fm7 (F, Ab, Bb, Db)
# Bar 2: Bb7 (Bb, Db, F, Ab)
# Bar 3: Eb7 (Eb, Gb, Bb, Db)
# Bar 4: Ab7 (Ab, B, Db, F)

# Each bar: chord on beat 2 and 4 (comp on 2 and 4)

chords = {
    0: [7, 10, 11, 14],   # Fm7 (F, Ab, Bb, Db)
    1: [11, 14, 7, 10],   # Bb7 (Bb, Db, F, Ab)
    2: [5, 8, 11, 14],    # Eb7 (Eb, Gb, Bb, Db)
    3: [10, 12, 14, 7]    # Ab7 (Ab, B, Db, F)
}

chord_lengths = [0.5] * 4  # 0.5 seconds per chord on 2 and 4

for bar in range(4):
    start_time = bar * time_per_bar + 0.75  # Beat 2
    for pitch in chords[bar]:
        piano_instr.notes.append(pretty_midi.Note(velocity=100, pitch=pitch + 12, start=start_time, end=start_time + chord_lengths[bar]))
    start_time = bar * time_per_bar + 1.5  # Beat 4
    for pitch in chords[bar]:
        piano_instr.notes.append(pretty_midi.Note(velocity=100, pitch=pitch + 12, start=start_time, end=start_time + chord_lengths[bar]))

# ---------------------------
# SAX: You (Dante)
# One short motif, start it, leave it hanging. Come back and finish it.
# No scale runs. Let the space between the notes be as important as the notes themselves.

# Motif: F, Ab, Bb, F (Fm scale)
# Bars 1: F (beat 1), Ab (beat 2), Bb (beat 3), leave it hanging
# Bars 2-4: Play the motif again but end on Bb

sax_notes = [
    # Bar 1
    (7 + 12, 0.375),  # F on beat 1
    (10 + 12, 0.375),  # Ab on beat 2
    (11 + 12, 0.375),  # Bb on beat 3
    # Bar 2
    (7 + 12, 0.375),  # F
    (10 + 12, 0.375),  # Ab
    (11 + 12, 0.375),  # Bb
    # Bar 3
    (7 + 12, 0.375),  # F
    (10 + 12, 0.375),  # Ab
    (11 + 12, 0.375),  # Bb
    # Bar 4
    (7 + 12, 0.375),  # F
    (10 + 12, 0.375),  # Ab
    (11 + 12, 0.375)   # Bb
]

# Start times for each note
for i, (pitch, duration) in enumerate(sax_notes):
    bar = i // 4
    beat = i % 4
    start_time = bar * time_per_bar + beat * 0.375
    sax_instr.notes.append(pretty_midi.Note(velocity=110, pitch=pitch, start=start_time, end=start_time + duration))

# Save the MIDI file
pm.write('dante_intro.mid')
