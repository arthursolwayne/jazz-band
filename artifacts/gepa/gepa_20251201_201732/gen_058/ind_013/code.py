
import pretty_midi
import numpy as np

# Set tempo and time signature
tempo = 160  # BPM
time_signature = (4, 4)

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=tempo, time_signature_numerator=4, time_signature_denominator=4)

# Define the key: F minor (F, Gb, Ab, Bb, B, Db, Eb)
# We'll stay in Fm for the entire piece — no modulation.

# Time per beat (in seconds)
beat_time = 60.0 / tempo  # 0.375 seconds per beat

# Time per bar (4/4 time)
bar_time = beat_time * 4  # 1.5 seconds per bar

# Define instruments
instrument_names = ["Drums", "Bass", "Piano", "Tenor Saxophone"]
instrument_programs = [0, 33, 0, 64]  # General MIDI programs

instruments = [pretty_midi.Instrument(program=program, is_drum=(i == 0)) for i, program in enumerate(instrument_programs)]

pm.instruments = instruments

#**********************************************************************
# 1. Bar 1: Little Ray on Drums
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
#**********************************************************************

# Drums (Instrument 0)
drum = pm.instruments[0]

# Kick on beats 1 and 3 of Bar 1
for beat in [0, 2]:
    time = beat * beat_time
    note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.05)
    drum.notes.append(note)

# Snare on beats 2 and 4 of Bar 1
for beat in [1, 3]:
    time = beat * beat_time
    note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.05)
    drum.notes.append(note)

# Hihat on every eighth note (0, 0.375, 0.75, 1.125, 1.5, etc.)
for i in range(0, 8):
    time = i * beat_time * 0.5
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drum.notes.append(note)

#**********************************************************************
# 2. Bar 2: Marcus on Bass (Walking line in Fm, D2-G2)
#**********************************************************************

# Bass (Instrument 1)
bass = pm.instruments[1]

# Fm bass line: D2, Eb2, F2, Gb2, Ab2, Bb2, B2, Db3 (Fm scale with chromatic approach)
bass_notes = [50, 51, 53, 54, 55, 57, 58, 60]  # MIDI notes for D2 to Db3

# Roots and fifths with chromatic approach
for i, note in enumerate(bass_notes):
    time = (i * 0.5) * beat_time  # On every eighth note
    note_obj = pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.1)
    bass.notes.append(note_obj)

#**********************************************************************
# 3. Bar 2-4: Diane on Piano (Open voicings, resolve on the last beat)
#**********************************************************************

# Piano (Instrument 2)
piano = pm.instruments[2]

# Chord per bar — open voicings, resolve on last beat
# Bar 2: Fm7 (F, Ab, Bb, D) => Open voicing: F, Ab, Bb, D
# Bar 3: Gbmaj7 (Gb, Bb, Db, F) => Open voicing: Gb, Bb, Db, F
# Bar 4: Am7b5 (A, C, Eb, G) => Open voicing: A, C, Eb, G

chords = [
    [71, 76, 77, 79],  # Fm7 (F, Ab, Bb, D)
    [72, 77, 79, 82],  # Gbmaj7 (Gb, Bb, Db, F)
    [81, 84, 86, 89]   # Am7b5 (A, C, Eb, G)
]

# Play each chord on beat 2 and 4 (comp on 2 and 4)
for bar_idx, chord in enumerate(chords):
    for beat in [1, 3]:
        time = (bar_idx * 4 + beat) * beat_time
        # Play each note at the same time
        for pitch in chord:
            note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1)
            piano.notes.append(note)

#**********************************************************************
# 4. Bar 2-4: You on Tenor Sax (One short motif, make it sing)
#**********************************************************************

# Tenor Sax (Instrument 3)
sax = pm.instruments[3]

# Tenor sax motif in Fm — short, emotional, open-ended
# Motif: F (61), Ab (64), Bb (62), rest (note at 62), F (61) — a questioning melody
# Start at bar 2, beat 1

# Bar 2, beat 1: F (61)
note_f = pretty_midi.Note(velocity=100, pitch=61, start=beat_time * 2, end=beat_time * 2 + 0.2)
sax.notes.append(note_f)

# Bar 2, beat 2: Ab (64)
note_ab = pretty_midi.Note(velocity=100, pitch=64, start=beat_time * 2 + 0.375, end=beat_time * 2 + 0.5)
sax.notes.append(note_ab)

# Bar 2, beat 3: Bb (62)
note_bb = pretty_midi.Note(velocity=100, pitch=62, start=beat_time * 2 + 0.75, end=beat_time * 2 + 0.9)
sax.notes.append(note_bb)

# Bar 2, beat 4: Rest — silence is the answer
# Bar 3, beat 1: F again — come back, unfinished
note_f2 = pretty_midi.Note(velocity=100, pitch=61, start=beat_time * 4, end=beat_time * 4 + 0.1)
sax.notes.append(note_f2)

# Write the MIDI to a file
pm.write('jazz_intro.mid')

print("MIDI file generated as 'jazz_intro.mid'")
