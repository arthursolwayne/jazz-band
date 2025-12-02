
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the key to D minor (key_number=21)
pm.key_signature = pretty_midi.KeySignature(key_number=21)

# Create instruments
drums_program = pretty_midi.instrument_program('Acoustic Drum Kit')
bass_program = pretty_midi.instrument_program('Fretless Bass')
piano_program = pretty_midi.instrument_program('Electric Piano 1')
sax_program = pretty_midi.instrument_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Define the time in seconds for each bar
bar_length = 1.5  # 160 BPM = 60/160 = 0.375 per beat, 4 beats = 1.5 seconds
total_time = 6.0  # 4 bars

# Define the note durations (in seconds)
quarter = 0.375
eighth = 0.1875
sixteenth = 0.09375

# ---- DRUMS: Little Ray (Bar 1 only) ----
# Kick on 1 and 3, snare on 2 and 4, hihat on every 8th
drum_notes = [
    (0, 36, 0),     # Kick on beat 1
    (eighth, 38, 0), # Snare on beat 2
    (quarter * 2, 36, 0),  # Kick on beat 3
    (quarter * 3, 38, 0),  # Snare on beat 4
    # Hi-hat on every eighth
    (0, 42, 0),     # Hi-hat on 1
    (eighth, 42, 0), # Hi-hat on 2
    (quarter, 42, 0), # Hi-hat on 3
    (quarter * 1.5, 42, 0), # Hi-hat on 4
    (quarter * 2, 42, 0), # Hi-hat on 5
    (quarter * 2.5, 42, 0), # Hi-hat on 6
    (quarter * 3, 42, 0), # Hi-hat on 7
    (quarter * 3.5, 42, 0)  # Hi-hat on 8
]

for time, note, velocity in drum_notes:
    note = pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + sixteenth)
    drums.notes.append(note)

# ---- BASS: Marcus (Bars 1-4) ----
# Chromatic walking line, never repeating a note
# Notes in D minor: D, Eb, F, G, Ab, Bb, B, C
# Use a chromatic pattern: D, Eb, F, G, Ab, Bb, B, C
# Repeating this pattern, starting with D
chromatic_bass_line = [50, 51, 52, 53, 54, 55, 56, 57]  # D to C in D minor

bass_notes = []
for bar in range(4):
    for i in range(8):
        note = chromatic_bass_line[i % 8]
        start_time = bar * bar_length + i * eighth
        end_time = start_time + eighth
        bass_note = pretty_midi.Note(velocity=100, pitch=note, start=start_time, end=end_time)
        bass_notes.append(bass_note)

bass.notes.extend(bass_notes)

# ---- PIANO: Diane (Bars 1-4) ----
# 7th chords on 2 and 4, comping with emotion
# D7 (D, F#, A, C), G7 (G, Bb, D, F), A7 (A, C#, E, G), B7 (B, D#, F#, A)
# Comp on beat 2 and 4 for each bar

chords = [
    # Bar 1: D7 on beat 2 (quarter * 1)
    (quarter * 1, 50, 100, 0.1),  # D
    (quarter * 1, 63, 100, 0.1),  # F#
    (quarter * 1, 67, 100, 0.1),  # A
    (quarter * 1, 60, 100, 0.1),  # C

    # Bar 1: D7 on beat 4 (quarter * 3)
    (quarter * 3, 50, 100, 0.1),
    (quarter * 3, 63, 100, 0.1),
    (quarter * 3, 67, 100, 0.1),
    (quarter * 3, 60, 100, 0.1),

    # Bar 2: G7 on beat 2
    (quarter * 1 + bar_length, 67, 100, 0.1),  # G
    (quarter * 1 + bar_length, 71, 100, 0.1),  # Bb
    (quarter * 1 + bar_length, 60, 100, 0.1),  # D
    (quarter * 1 + bar_length, 65, 100, 0.1),  # F

    # Bar 2: G7 on beat 4
    (quarter * 3 + bar_length, 67, 100, 0.1),
    (quarter * 3 + bar_length, 71, 100, 0.1),
    (quarter * 3 + bar_length, 60, 100, 0.1),
    (quarter * 3 + bar_length, 65, 100, 0.1),

    # Bar 3: A7 on beat 2
    (quarter * 1 + bar_length * 2, 69, 100, 0.1),  # A
    (quarter * 1 + bar_length * 2, 74, 100, 0.1),  # C#
    (quarter * 1 + bar_length * 2, 67, 100, 0.1),  # E
    (quarter * 1 + bar_length * 2, 67, 100, 0.1),  # G (double)

    # Bar 3: A7 on beat 4
    (quarter * 3 + bar_length * 2, 69, 100, 0.1),
    (quarter * 3 + bar_length * 2, 74, 100, 0.1),
    (quarter * 3 + bar_length * 2, 67, 100, 0.1),
    (quarter * 3 + bar_length * 2, 67, 100, 0.1),

    # Bar 4: B7 on beat 2
    (quarter * 1 + bar_length * 3, 71, 100, 0.1),  # B
    (quarter * 1 + bar_length * 3, 76, 100, 0.1),  # D#
    (quarter * 1 + bar_length * 3, 69, 100, 0.1),  # F#
    (quarter * 1 + bar_length * 3, 72, 100, 0.1),  # A

    # Bar 4: B7 on beat 4
    (quarter * 3 + bar_length * 3, 71, 100, 0.1),
    (quarter * 3 + bar_length * 3, 76, 100, 0.1),
    (quarter * 3 + bar_length * 3, 69, 100, 0.1),
    (quarter * 3 + bar_length * 3, 72, 100, 0.1),
]

for time, pitch, velocity, duration in chords:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    piano.notes.append(note)

# ---- SAX: Dante (Bars 2-4) ----
# Melody: Short motif, singable, leaves a question
# Example: D (50), F (55), G (57), D (50)
# Play on beat 1 of bar 2, with rest on beat 2, then repeat with variation

sax_notes = [
    # Bar 2: D (50)
    (bar_length, 50, 100, 0.25),  # D on beat 1
    (bar_length + eighth * 2, 55, 100, 0.25),  # F on beat 3
    (bar_length + eighth * 4, 57, 100, 0.25),  # G on beat 5
    (bar_length + eighth * 6, 50, 100, 0.25),  # D on beat 7

    # Bar 3: D (50)
    (bar_length * 2, 50, 100, 0.25),  # D on beat 1
    (bar_length * 2 + eighth * 2, 55, 100, 0.25),  # F on beat 3
    (bar_length * 2 + eighth * 4, 57, 100, 0.25),  # G on beat 5
    (bar_length * 2 + eighth * 6, 50, 100, 0.25),  # D on beat 7

    # Bar 4: D (50)
    (bar_length * 3, 50, 100, 0.25),  # D on beat 1
    (bar_length * 3 + eighth * 2, 55, 100, 0.25),  # F on beat 3
    (bar_length * 3 + eighth * 4, 57, 100, 0.25),  # G on beat 5
    (bar_length * 3 + eighth * 6, 50, 100, 0.25),  # D on beat 7
]

for time, pitch, velocity, duration in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=time, end=time + duration)
    sax.notes.append(note)

# Write MIDI file
pm.write('dante_intro.mid')
