
import pretty_midi

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Alto Sax')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define the tempo (160 BPM, 4/4 time)
# Each quarter note is 0.75 seconds at 160 BPM
# 1 bar = 4 quarter notes = 3 seconds
# So each beat (quarter note) is 0.75 seconds

# Time per beat
beat_time = 0.75  # 60 / 160 = 0.375 seconds per 8th note, 0.75 per quarter note

# Create a function to add a note to an instrument
def add_note(instrument, pitch, start, end, velocity=100):
    note = pretty_midi.Note(velocity, pitch, start, end)
    instrument.notes.append(note)

# ------------------------------
# Bar 1: Little Ray on drums (snare and kick on 1 and 3)
# Bar is 3 seconds long (4 beats at 0.75 per beat)

# Kick on 1 and 3
add_note(drums, pretty_midi.note_number_to_name(36), 0.0, 0.25, 100)  # Kick
add_note(drums, pretty_midi.note_number_to_name(36), 1.5, 1.75, 100)  # Kick

# Snare on 2 and 4
add_note(drums, pretty_midi.note_number_to_name(42), 0.75, 0.95, 100)  # Snare
add_note(drums, pretty_midi.note_number_to_name(42), 2.25, 2.45, 100)  # Snare

# Hihat on every eighth note (0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625)
for t in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625]:
    add_note(drums, pretty_midi.note_number_to_name(55), t, t + 0.15, 80)  # Hihat

# ------------------------------
# Bars 2-4: Full ensemble

# Start time for bars 2-4: 3.0 seconds (end of Bar 1)

# Marcus: Walking bass line in D, key of D, chromatic approaches, no repeated notes
# D Dorian scale: D, E, F#, G, A, B, C
# Walking line: D, F#, G, A, B, C, D, F#, etc.

bass_line = [62, 66, 67, 69, 71, 72, 62, 66]  # D, F#, G, A, B, C, D, F#
for i, pitch in enumerate(bass_line):
    time = 3.0 + i * 0.75
    add_note(bass, pitch, time, time + 0.5, 100)

# Diane: Piano comping on 2 and 4, 7th chords in D minor
# D7 (D, F#, A, C)
# Bm7 (B, D, F#, A)
# Comp on 2 and 4 (0.75 and 2.25 in bar 2)

# Bar 2: D7 (chord on 2)
add_note(piano, 62, 3.75, 4.0, 100)  # D
add_note(piano, 66, 3.75, 4.0, 100)  # F#
add_note(piano, 69, 3.75, 4.0, 100)  # A
add_note(piano, 72, 3.75, 4.0, 100)  # C

# Bar 3: Bm7 (chord on 2)
add_note(piano, 71, 6.75, 7.0, 100)  # B
add_note(piano, 62, 6.75, 7.0, 100)  # D
add_note(piano, 66, 6.75, 7.0, 100)  # F#
add_note(piano, 69, 6.75, 7.0, 100)  # A

# Bar 4: D7 (chord on 2)
add_note(piano, 62, 9.75, 10.0, 100)  # D
add_note(piano, 66, 9.75, 10.0, 100)  # F#
add_note(piano, 69, 9.75, 10.0, 100)  # A
add_note(piano, 72, 9.75, 10.0, 100)  # C

# Little Ray fills in bar 2 and 3 with syncopation and dynamic velocity

# Bar 2 fill: snare on 2.5 and 3.0
add_note(drums, 42, 4.5, 4.7, 100)  # Snare
add_note(drums, 42, 5.0, 5.2, 100)  # Snare

# Bar 3 fill: snare on 6.5 and 7.0
add_note(drums, 42, 7.5, 7.7, 100)  # Snare
add_note(drums, 42, 8.0, 8.2, 100)  # Snare

# Bar 4 fill: snare on 9.5 and 10.0
add_note(drums, 42, 10.5, 10.7, 100)  # Snare
add_note(drums, 42, 11.0, 11.2, 100)  # Snare

# ------------------------------
# Dante: Tenor sax — one short motif, start it, leave it hanging, come back

# Motif: D, F#, A, B — ascending, then back down to D
# Start on 3.0 (beginning of bar 2)
# Bar 2: D, F#, A, B (at 3.0, 3.375, 3.75, 4.0)
# Bar 3: pause, then D at 6.0
# Bar 4: F#, A, D (at 9.0, 9.375, 9.75)

# Bar 2
add_note(sax, 62, 3.0, 3.25, 100)  # D
add_note(sax, 66, 3.375, 3.625, 100)  # F#
add_note(sax, 69, 3.75, 4.0, 100)  # A
add_note(sax, 71, 4.0, 4.25, 100)  # B

# Bar 3 — "leave it hanging"
# No notes here, just silence to let the idea breathe

# Bar 4 — come back and finish
add_note(sax, 62, 9.0, 9.25, 100)  # D (return)
add_note(sax, 66, 9.375, 9.625, 100)  # F#
add_note(sax, 69, 9.75, 10.0, 100)  # A
add_note(sax, 62, 10.0, 10.25, 100)  # D (resolve)

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
