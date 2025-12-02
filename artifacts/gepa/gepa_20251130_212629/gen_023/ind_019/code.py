
import pretty_midi
import numpy as np

# Create a PrettyMIDI object with 4/4 time and 160 BPM
pm = pretty_midi.PrettyMIDI(initial_tempo=160)
instrument = pretty_midi.Instrument(program=64)  # Tenor sax (program 64)
pm.instruments.append(instrument)

# Time parameters (160 BPM = 6/160 = 0.0375 seconds per beat)
beat = 0.375
bar = beat * 4  # 1.5 seconds per bar
note_duration = beat / 2  # 16th note = 0.1875 seconds

# Define time markers (in seconds)
bar_1 = 0.0
bar_2 = bar
bar_3 = bar * 2
bar_4 = bar * 3

#--------------------------
# Bar 1: Little Ray (Drums) - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
#--------------------------

# Kick on 1 and 3
kick_1 = pretty_midi.Note(velocity=100, pitch=36, start=bar_1, end=bar_1 + note_duration)
kick_3 = pretty_midi.Note(velocity=100, pitch=36, start=bar_1 + beat * 2, end=bar_1 + beat * 2 + note_duration)
instrument.notes.extend([kick_1, kick_3])

# Snare on 2 and 4
snare_2 = pretty_midi.Note(velocity=100, pitch=38, start=bar_1 + beat, end=bar_1 + beat + note_duration)
snare_4 = pretty_midi.Note(velocity=100, pitch=38, start=bar_1 + beat * 3, end=bar_1 + beat * 3 + note_duration)
instrument.notes.extend([snare_2, snare_4])

# Hi-hats on every eighth note (no rests)
for i in range(0, 8):
    start = bar_1 + note_duration * i
    hihat = pretty_midi.Note(velocity=70, pitch=46, start=start, end=start + note_duration)
    instrument.notes.append(hihat)

#--------------------------
# Bar 2: Diane (Piano) - 7th chords, comp on 2 and 4
#--------------------------

# Key is Fm (F, Ab, C)
# 7th chords: F7 (F, A, C, Eb), Ab7 (Ab, C, Eb, Gb), C7 (C, E, G, Bb)

# Bar 2 - Comp on beat 2 and 4
note_list = [
    # Beat 2: F7
    (65, 100, bar_2 + beat),       # F
    (69, 100, bar_2 + beat),       # A
    (67, 100, bar_2 + beat),       # C
    (64, 100, bar_2 + beat),       # Eb

    # Beat 4: Ab7
    (68, 100, bar_2 + beat * 3),   # Ab
    (71, 100, bar_2 + beat * 3),   # C
    (69, 100, bar_2 + beat * 3),   # Eb
    (67, 100, bar_2 + beat * 3),   # Gb
]

# Add notes with duration
for pitch, velocity, start in note_list:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration)
    instrument.notes.append(note)

#--------------------------
# Bar 3: Marcus (Bass) - Walking line, chromatic approaches
#--------------------------

# Fm7 -> Ab7 -> C7 -> F7
# Walking line in Fm (F, Gb, Ab, A, Bb, B, C, Db, D, Eb, E, F)
# Start on F, walk down chromatically

bass_notes = [
    # Bar 3
    (65, 80, bar_3),               # F
    (64, 80, bar_3 + note_duration),  # Gb
    (67, 80, bar_3 + note_duration * 2),  # Ab
    (69, 80, bar_3 + note_duration * 3),  # A
    (68, 80, bar_3 + note_duration * 4),  # Bb
    (67, 80, bar_3 + note_duration * 5),  # B
    (65, 80, bar_3 + note_duration * 6),  # C
    (63, 80, bar_3 + note_duration * 7),  # Db
    (65, 80, bar_3 + note_duration * 8),  # D
    (64, 80, bar_3 + note_duration * 9),  # Eb
    (65, 80, bar_3 + note_duration * 10), # E
    (65, 80, bar_3 + note_duration * 11), # F
]

# Add notes
for pitch, velocity, start in bass_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration)
    instrument.notes.append(note)

#--------------------------
# Bar 4: Dante (Tenor Sax) - Motif, one phrase that ends with a question
#--------------------------

# Start with a short phrase in Fm: F, Ab, Bb, C
# F (65) - rest - Ab (67) - rest - Bb (68) - rest - C (67) - rest (ending on a question)

note_list = [
    (65, 100, bar_4),               # F
    (67, 100, bar_4 + note_duration * 2),  # Ab
    (68, 100, bar_4 + note_duration * 4),  # Bb
    (67, 100, bar_4 + note_duration * 6),  # C
]

# Add notes with duration
for pitch, velocity, start in note_list:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + note_duration)
    instrument.notes.append(note)

#--------------------------
# Add a rest at the end of the phrase to make it feel like a question
#--------------------------

# End on a rest, not a resolution
# Note: We're not adding a note here, but we make sure the last note ends at the end of the 4th bar
# and the final note (C) ends at 6.0 seconds

# Save the MIDI file
pm.write("jazz_intro_fm.mid")
print("MIDI file 'jazz_intro_fm.mid' created.")
