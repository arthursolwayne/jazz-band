
import pretty_midi
import numpy as np

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to F minor (F, Gb, Ab, Bb, B, Db, Eb)
key = 'F minor'

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)
pm.instruments.append(bass)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)
pm.instruments.append(piano)

drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
drums = pretty_midi.Instrument(program=drums_program)
pm.instruments.append(drums)

tenor_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
tenor = pretty_midi.Instrument(program=tenor_program)
pm.instruments.append(tenor)

# Tempo and timing
bpm = 160
quarter_note = 60.0 / bpm
beat = quarter_note / 4  # 0.375 seconds per beat (since 160 BPM = 60/160 = 0.375 per beat)
bar_length = 4 * beat  # 1.5 seconds per bar (4/4 time)
total_time = 4 * bar_length  # 6 seconds total

# Function to create a note on a given instrument
def add_note(instrument, note_number, start, duration, velocity=100):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=start + duration)
    instrument.notes.append(note)

# Bar 1: Little Ray on drums — kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll use the piano to simulate the drum sounds with MIDI note numbers
# Kick (C2), Snare (C3), Hihat (C6), Crash (F6)

# Time in seconds (bar 1)
bar1_start = 0.0

# Kick on 1 and 3 (beat 0 and 2)
add_note(drums, 60, bar1_start, 0.1)  # Kick on beat 1
add_note(drums, 60, bar1_start + 2 * beat, 0.1)  # Kick on beat 3

# Snare on 2 and 4 (beat 1 and 3)
add_note(drums, 72, bar1_start + beat, 0.1)  # Snare on beat 2
add_note(drums, 72, bar1_start + 3 * beat, 0.1)  # Snare on beat 4

# Hihat on every eighth note (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5)
for i in range(0, 4):
    add_note(drums, 72, bar1_start + i * beat * 0.5, 0.05)
    add_note(drums, 72, bar1_start + i * beat * 0.5 + 0.05, 0.05)

# Bar 2: Everyone in — tenor takes the melody
bar2_start = bar_length
tenor_notes = [
    # Bar 2: Tenor sax starts a short, expressive motif
    (64, bar2_start, 0.3),  # Ab (Fm7)
    (67, bar2_start + 0.3, 0.3),  # C (Fm7)
    (69, bar2_start + 0.6, 0.3),  # Db (Fm7)
    (64, bar2_start + 0.9, 0.3),  # Ab (Fm7)
    (67, bar2_start + 1.2, 0.3),  # C (Fm7)
    (69, bar2_start + 1.5, 0.3),  # Db (Fm7)
    (71, bar2_start + 1.8, 0.3),  # Eb (Fm7)
    (74, bar2_start + 2.1, 0.3),  # Gb (Fm7)
    (76, bar2_start + 2.4, 0.3),  # Ab (Fm7)
    (71, bar2_start + 2.7, 0.3),  # Eb (Fm7)
    (69, bar2_start + 3.0, 0.3),  # Db (Fm7)
    (64, bar2_start + 3.3, 0.3),  # Ab (Fm7)
]
for note, start, dur in tenor_notes:
    add_note(tenor, note, start, dur)

# Bass: Walking line in Fm, chromatic approaches
# Fm7: F, Ab, Bb, Db
bass_notes = [
    (64, bar2_start, 0.5),  # F (root)
    (66, bar2_start + 0.5, 0.5),  # Gb (chromatic up)
    (65, bar2_start + 1.0, 0.5),  # G (chromatic down)
    (64, bar2_start + 1.5, 0.5),  # F (root)
    (67, bar2_start + 2.0, 0.5),  # Ab (3rd)
    (69, bar2_start + 2.5, 0.5),  # Bb (4th)
    (67, bar2_start + 3.0, 0.5),  # Ab (3rd)
    (65, bar2_start + 3.5, 0.5),  # G (chromatic)
]
for note, start, dur in bass_notes:
    add_note(bass, note, start, dur)

# Piano: Comp on 2 and 4 with 7th chords
# Fm7 = F, Ab, Bb, Db (7th chord)
piano_notes = [
    # Bar 2: 7th chords on 2 and 4 (beat 1 and 3)
    # Fm7 on beat 2 (start + beat)
    (64, bar2_start + beat, 0.25),  # F
    (69, bar2_start + beat, 0.25),  # Bb
    (67, bar2_start + beat, 0.25),  # Ab
    (65, bar2_start + beat, 0.25),  # Db (7th)

    # Fm7 on beat 4 (start + 3 * beat)
    (64, bar2_start + 3 * beat, 0.25),  # F
    (69, bar2_start + 3 * beat, 0.25),  # Bb
    (67, bar2_start + 3 * beat, 0.25),  # Ab
    (65, bar2_start + 3 * beat, 0.25),  # Db (7th)
]
for note, start, dur in piano_notes:
    add_note(piano, note, start, dur)

# Bar 3: Drums continue, same pattern
bar3_start = 2 * bar_length
for i in range(0, 4):
    add_note(drums, 60, bar3_start + i * beat * 0.5, 0.05)
    add_note(drums, 60, bar3_start + i * beat * 0.5 + 0.05, 0.05)
    add_note(drums, 72, bar3_start + i * beat * 0.5, 0.05)
    add_note(drums, 72, bar3_start + i * beat * 0.5 + 0.05, 0.05)

# Bar 4: Tenor sax resolves the motif, ends on a strong chord
bar4_start = 3 * bar_length
tenor_notes = [
    (64, bar4_start, 0.3),      # Ab
    (67, bar4_start + 0.3, 0.3), # C
    (71, bar4_start + 0.6, 0.3), # Eb
    (64, bar4_start + 0.9, 0.3), # Ab
    (67, bar4_start + 1.2, 0.3), # C
    (71, bar4_start + 1.5, 0.3), # Eb
    (69, bar4_start + 1.8, 0.3), # Db
    (64, bar4_start + 2.1, 0.3), # Ab
    (67, bar4_start + 2.4, 0.3), # C
    (71, bar4_start + 2.7, 0.3), # Eb
    (69, bar4_start + 3.0, 0.3), # Db
]
for note, start, dur in tenor_notes:
    add_note(tenor, note, start, dur)

# Bass walks again, resolves to F
bass_notes = [
    (64, bar4_start, 0.5),  # F
    (66, bar4_start + 0.5, 0.5),  # Gb
    (65, bar4_start + 1.0, 0.5),  # G
    (64, bar4_start + 1.5, 0.5),  # F
    (67, bar4_start + 2.0, 0.5),  # Ab
    (69, bar4_start + 2.5, 0.5),  # Bb
    (67, bar4_start + 3.0, 0.5),  # Ab
    (65, bar4_start + 3.5, 0.5),  # G
]
for note, start, dur in bass_notes:
    add_note(bass, note, start, dur)

# Piano: Resolves to Fm7 on beat 4
piano_notes = [
    (64, bar4_start + 3 * beat, 0.25),  # F
    (69, bar4_start + 3 * beat, 0.25),  # Bb
    (67, bar4_start + 3 * beat, 0.25),  # Ab
    (65, bar4_start + 3 * beat, 0.25),  # Db (7th)
]
for note, start, dur in piano_notes:
    add_note(piano, note, start, dur)

# Write the MIDI file to disk
pm.write("fminor_intro.mid")
print("MIDI file written as 'fminor_intro.mid' — ready to make Wayne lean forward.")
