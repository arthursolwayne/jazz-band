
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create a time signature of 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: D minor (key_number 29)
pm.key_signature_changes = [pretty_midi.KeySignature(29, 0)]

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')  # MIDI drum kit uses 0
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time in seconds: 1 bar = 1.5 seconds (160 BPM)
bar_length = 1.5
start_time = 0.0

# ---------------------------
# Bar 1: Little Ray on drums (6 beats: 0.375s per beat)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time signature: 4/4 — each bar has 4 beats
# 8 notes per bar (eighth notes)

for beat in range(4):
    time = start_time + beat * 0.375
    # Kick on 1 and 3
    if beat == 0 or beat == 2:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Snare on 2 and 4
    if beat == 1 or beat == 3:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.1)
    drums.notes.append(note)

# ---------------------------
# Bar 2-4: Everyone in. Sax takes the melody.
# D minor scale: D, Eb, F, G, Ab, Bb, C, D
# Motif: D, F, G, Ab — a minor 3rd, then a minor 2nd, tension

# Time for bars 2-4: 3 bars = 4.5 seconds
# Start at bar 1 end: 1.5s
start_time = 1.5

# Define the sax motif (D, F, G, Ab)
# Notes in MIDI: D4 = 62, F4 = 65, G4 = 67, Ab4 = 68
note_lengths = [0.25, 0.25, 0.25, 0.25]  # quarter notes
note_pitches = [62, 65, 67, 68]
note_velocities = [100, 100, 100, 100]

# Insert the phrase into the sax instrument
for i in range(4):
    start = start_time + i * 0.375
    note = pretty_midi.Note(velocity=note_velocities[i], pitch=note_pitches[i], start=start, end=start + note_lengths[i])
    sax.notes.append(note)

# ---------------------------
# Bar 2-4: Marcus on bass (walking line, chromatic approaches)
# Start at bar 2: 1.5s + 0.375 = 1.875s
# Bass line: D, Eb, F, G, Ab, Bb, C, D (chromatic up, 8 notes)

bass_notes = [62, 63, 65, 67, 68, 69, 71, 72]
bass_velocities = [85 for _ in range(8)]
bass_durations = [0.375 for _ in range(8)]  # 8 eighth notes over 3 bars

for i in range(8):
    start = 1.5 + i * 0.375
    note = pretty_midi.Note(velocity=bass_velocities[i], pitch=bass_notes[i], start=start, end=start + bass_durations[i])
    bass.notes.append(note)

# ---------------------------
# Bar 2-4: Diane on piano (7th chords, comp on 2 and 4)
# Dm7: D, F, Ab, C (pitches: 62, 65, 68, 71)
# Play on beats 2 and 4 of each bar (bars 2 and 3)
# Duration: 0.375s

for bar in range(2, 4):  # Bars 2 and 3
    # Beat 2: bar starts at 1.5s, beat 2 is 1.5 + 0.75 = 2.25s
    # Beat 4: bar starts at 1.5s, beat 4 is 1.5 + 1.5 = 3.0s
    for beat in [2, 4]:
        time = 1.5 + (bar - 2) * 1.5 + (beat - 1) * 0.375
        for pitch in [62, 65, 68, 71]:
            note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.375)
            piano.notes.append(note)

# ---------------------------
# Output the MIDI file
pm.write("dante_cellar_intro.mid")
print("MIDI file written as 'dante_cellar_intro.mid'")
