
import pretty_midi
import numpy as np

# Initialize a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
bass = pretty_midi.Instrument(program=bass_program)

piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
piano = pretty_midi.Instrument(program=piano_program)

drums_program = pretty_midi.instrument_name_to_program('Drums')
drums = pretty_midi.Instrument(program=drums_program)

sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Time parameters
bpm = 160
note_length = 60 / bpm  # seconds per beat
bar_length = 4 * note_length  # 4/4 time, 4 beats per bar
total_length = 4 * bar_length  # 4 bars

# Time for each bar in seconds
bar_times = [i * bar_length for i in range(4)]

# --- BAR 1: DRUMS ALONE ---
# Little Ray sets the mood, subtle, with space and energy
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# We'll use velocity to add emotion and tension

# Drum note numbers from General MIDI
kick = 36
snare = 38
hihat_closed = 42
hihat_open = 46

# Bar 1: 0.0 to 1.5 seconds
# Kick on 1 and 3
kick_times = [0.0, 0.75]
for kick_time in kick_times:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=kick_time, end=kick_time + 0.1)
    drums.notes.append(note)

# Snare on 2 and 4
snare_times = [0.5, 1.25]
for snare_time in snare_times:
    note = pretty_midi.Note(velocity=90, pitch=snare, start=snare_time, end=snare_time + 0.1)
    drums.notes.append(note)

# Hihat on every eighth note (0.0, 0.375, 0.75, 1.125)
hihat_times = [0.0, 0.375, 0.75, 1.125]
for hihat_time in hihat_times:
    note = pretty_midi.Note(velocity=70, pitch=hihat_closed, start=hihat_time, end=hihat_time + 0.1)
    drums.notes.append(note)

# --- BAR 2: ALL IN ---

# Time for bar 2: 1.5 to 3.0 seconds

# Bass line: Chromatic walking line, no repeated notes
# D (D3), Eb (E3b?), E (E3), F (F3), G (G3), A (A3), B (B3), C# (C#4), D (D4) — chromatic up, then back

bass_notes = [
    (1.5, 62),  # D3
    (1.75, 63), # Eb3
    (2.0, 64),  # E3
    (2.25, 65), # F3
    (2.5, 67),  # G3
    (2.75, 69), # A3
    (3.0, 71),  # B3
    (3.25, 73), # C#4
    (3.5, 74),  # D4
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comping with space
# D7: D, F#, A, C
# G7: G, B, D, F
# Bm7: B, D, F#, A
# Em7: E, G, B, D

# Bar 2: 1.5 to 3.0
# 2 and 4 are at 1.75s and 2.75s

# D7 on 2 (1.75s)
d7_notes = [62, 67, 69, 64]  # D, F#, A, C
for note in d7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=1.75, end=1.75 + 0.25)
    piano.notes.append(piano_note)

# G7 on 4 (2.75s)
g7_notes = [67, 71, 69, 65]  # G, B, D, F
for note in g7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=2.75, end=2.75 + 0.25)
    piano.notes.append(piano_note)

# --- BAR 3: CONTINUE WITH SPACE AND DYNAMICS ---

# Bar 3: 3.0 to 4.5 seconds

# Bass continues with chromatic line
bass_notes = [
    (3.5, 74),  # D4
    (3.75, 76), # Eb4
    (4.0, 77),  # E4
    (4.25, 79), # F#4
    (4.5, 81),  # G#4
    (4.75, 83), # A#4
    (5.0, 85),  # C5
    (5.25, 86), # C#5
    (5.5, 87),  # D5
]

for start, pitch in bass_notes:
    note = pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=start + 0.25)
    bass.notes.append(note)

# Piano: Bm7 on 2 (4.0s), Em7 on 4 (5.0s)
# Bm7: B, D, F#, A
# Em7: E, G, B, D

# Bm7 on 2 (4.0s)
bm7_notes = [71, 74, 77, 69]  # B, D, F#, A
for note in bm7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=4.0, end=4.0 + 0.25)
    piano.notes.append(piano_note)

# Em7 on 4 (5.0s)
em7_notes = [65, 67, 71, 74]  # E, G, B, D
for note in em7_notes:
    piano_note = pretty_midi.Note(velocity=90, pitch=note, start=5.0, end=5.0 + 0.25)
    piano.notes.append(piano_note)

# --- BAR 4: SAX TAKES THE MELODY, HANGS ON A QUESTION --

# Bar 4: 4.5 to 6.0 seconds

# Sax motif — short, melodic, ends on a question
# D (D4) -> F# (F#4) -> B (B4) -> D (D5) — descending with a slight lift

# Notes:
# D4 (62), F#4 (67), B4 (71), D5 (74)

# Time points: 4.75, 5.125, 5.5, 5.875
# Each note is 0.25s long, with a slight delay between them

sax_notes = [
    (4.75, 62, 100),  # D4
    (5.125, 67, 100), # F#4
    (5.5, 71, 100),   # B4
    (5.875, 74, 90),  # D5 (softly, questioning)
]

for start, pitch, velocity in sax_notes:
    note = pretty_midi.Note(velocity=velocity, pitch=pitch, start=start, end=start + 0.25)
    sax.notes.append(note)

# --- EXPORT TO MIDI FILE ---

# Save the MIDI file
pm.write('jazz_intro_d_mood.mid')
print("MIDI file created: jazz_intro_d_mood.mid")
