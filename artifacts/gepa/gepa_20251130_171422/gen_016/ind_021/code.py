
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define time per beat and bar
beats_per_bar = 4
notes_per_beat = 4  # quarter notes
time_per_beat = 60.0 / 160  # seconds per beat
time_per_bar = time_per_beat * beats_per_bar
time_per_note = time_per_beat / 4  # quarter note = 0.375s

# --- DRUMS ---
drums = Instrument(program=Program.DRUMS)
drum_notes = []

# Kick on 1 and 3 of each bar
for bar in range(4):
    kick_time = bar * time_per_bar + 0.0
    kick = Note(36, 127, kick_time, kick_time + 0.1)
    drum_notes.append(kick)

    kick_time = bar * time_per_bar + time_per_beat * 2.0
    kick = Note(36, 127, kick_time, kick_time + 0.1)
    drum_notes.append(kick)

# Snare on 2 and 4 of each bar
for bar in range(4):
    snare_time = bar * time_per_bar + time_per_beat * 1.0
    snare = Note(38, 127, snare_time, snare_time + 0.1)
    drum_notes.append(snare)

    snare_time = bar * time_per_bar + time_per_beat * 3.0
    snare = Note(38, 127, snare_time, snare_time + 0.1)
    drum_notes.append(snare)

# Hi-hat on every eighth note
for bar in range(4):
    for i in range(8):
        hihat_time = bar * time_per_bar + (i * time_per_beat / 2.0)
        hihat = Note(42, 127, hihat_time, hihat_time + 0.05)
        drum_notes.append(hihat)

drums.notes = drum_notes
pm.instruments.append(drums)

# --- BASS ---
bass = Instrument(program=Program.BASS)
bass_notes = []

# Chromatic walking line
# D major scale: D, E, F#, G, A, B, C#, D
# Chromatic line from D to G
note_values = [62, 63, 64, 65, 66, 67, 68, 69]  # D to G (chromatic)

for bar in range(4):
    for i, note in enumerate(note_values):
        start_time = bar * time_per_bar + i * time_per_note
        end_time = start_time + time_per_note
        bass_notes.append(Note(note, 100, start_time, end_time))

bass.notes = bass_notes
pm.instruments.append(bass)

# --- PIANO ---
piano = Instrument(program=Program.PIANO)
piano_notes = []

# 7th chords on 2 and 4
# D7: D, F#, A, C
# G7: G, B, D, F
# A7: A, C#, E, G
# B7: B, D#, F#, A

# Bar 1: D7 on 2 and 4
piano_notes.append(Note(62, 100, time_per_beat * 1.0, time_per_beat * 1.5))  # D
piano_notes.append(Note(67, 100, time_per_beat * 1.0, time_per_beat * 1.5))  # F#
piano_notes.append(Note(69, 100, time_per_beat * 1.0, time_per_beat * 1.5))  # A
piano_notes.append(Note(64, 100, time_per_beat * 1.0, time_per_beat * 1.5))  # C

piano_notes.append(Note(62, 100, time_per_beat * 3.0, time_per_beat * 3.5))  # D
piano_notes.append(Note(67, 100, time_per_beat * 3.0, time_per_beat * 3.5))  # F#
piano_notes.append(Note(69, 100, time_per_beat * 3.0, time_per_beat * 3.5))  # A
piano_notes.append(Note(64, 100, time_per_beat * 3.0, time_per_beat * 3.5))  # C

# Bar 2: G7 on 2 and 4
piano_notes.append(Note(67, 100, time_per_beat * 1.0 + time_per_bar, time_per_beat * 1.5 + time_per_bar))  # G
piano_notes.append(Note(71, 100, time_per_beat * 1.0 + time_per_bar, time_per_beat * 1.5 + time_per_bar))  # B
piano_notes.append(Note(69, 100, time_per_beat * 1.0 + time_per_bar, time_per_beat * 1.5 + time_per_bar))  # D
piano_notes.append(Note(65, 100, time_per_beat * 1.0 + time_per_bar, time_per_beat * 1.5 + time_per_bar))  # F

piano_notes.append(Note(67, 100, time_per_beat * 3.0 + time_per_bar, time_per_beat * 3.5 + time_per_bar))  # G
piano_notes.append(Note(71, 100, time_per_beat * 3.0 + time_per_bar, time_per_beat * 3.5 + time_per_bar))  # B
piano_notes.append(Note(69, 100, time_per_beat * 3.0 + time_per_bar, time_per_beat * 3.5 + time_per_bar))  # D
piano_notes.append(Note(65, 100, time_per_beat * 3.0 + time_per_bar, time_per_beat * 3.5 + time_per_bar))  # F

# Bar 3: A7 on 2 and 4
piano_notes.append(Note(69, 100, time_per_beat * 1.0 + 2 * time_per_bar, time_per_beat * 1.5 + 2 * time_per_bar))  # A
piano_notes.append(Note(74, 100, time_per_beat * 1.0 + 2 * time_per_bar, time_per_beat * 1.5 + 2 * time_per_bar))  # C#
piano_notes.append(Note(72, 100, time_per_beat * 1.0 + 2 * time_per_bar, time_per_beat * 1.5 + 2 * time_per_bar))  # E
piano_notes.append(Note(67, 100, time_per_beat * 1.0 + 2 * time_per_bar, time_per_beat * 1.5 + 2 * time_per_bar))  # G

piano_notes.append(Note(69, 100, time_per_beat * 3.0 + 2 * time_per_bar, time_per_beat * 3.5 + 2 * time_per_bar))  # A
piano_notes.append(Note(74, 100, time_per_beat * 3.0 + 2 * time_per_bar, time_per_beat * 3.5 + 2 * time_per_bar))  # C#
piano_notes.append(Note(72, 100, time_per_beat * 3.0 + 2 * time_per_bar, time_per_beat * 3.5 + 2 * time_per_bar))  # E
piano_notes.append(Note(67, 100, time_per_beat * 3.0 + 2 * time_per_bar, time_per_beat * 3.5 + 2 * time_per_bar))  # G

# Bar 4: B7 on 2 and 4
piano_notes.append(Note(71, 100, time_per_beat * 1.0 + 3 * time_per_bar, time_per_beat * 1.5 + 3 * time_per_bar))  # B
piano_notes.append(Note(76, 100, time_per_beat * 1.0 + 3 * time_per_bar, time_per_beat * 1.5 + 3 * time_per_bar))  # D#
piano_notes.append(Note(74, 100, time_per_beat * 1.0 + 3 * time_per_bar, time_per_beat * 1.5 + 3 * time_per_bar))  # F#
piano_notes.append(Note(69, 100, time_per_beat * 1.0 + 3 * time_per_bar, time_per_beat * 1.5 + 3 * time_per_bar))  # A

piano_notes.append(Note(71, 100, time_per_beat * 3.0 + 3 * time_per_bar, time_per_beat * 3.5 + 3 * time_per_bar))  # B
piano_notes.append(Note(76, 100, time_per_beat * 3.0 + 3 * time_per_bar, time_per_beat * 3.5 + 3 * time_per_bar))  # D#
piano_notes.append(Note(74, 100, time_per_beat * 3.0 + 3 * time_per_bar, time_per_beat * 3.5 + 3 * time_per_bar))  # F#
piano_notes.append(Note(69, 100, time_per_beat * 3.0 + 3 * time_per_bar, time_per_beat * 3.5 + 3 * time_per_bar))  # A

piano.notes = piano_notes
pm.instruments.append(piano)

# --- SAX (Tenor) ---
sax = Instrument(program=Program.SAXOPHONE)
sax_notes = []

# Motif: D, F#, G, D (minor 3rd + chromatic)
# Start at bar 2, on 1
start_time = time_per_beat * 0.0 + time_per_bar * 1.0
sax_notes.append(Note(62, 100, start_time, start_time + time_per_note))
sax_notes.append(Note(67, 100, start_time + time_per_note, start_time + 2 * time_per_note))
sax_notes.append(Note(69, 100, start_time + 2 * time_per_note, start_time + 3 * time_per_note))
sax_notes.append(Note(62, 100, start_time + 3 * time_per_note, start_time + 4 * time_per_note))

# Let it hang on D (resolve at the end of bar 2)
sax_notes.append(Note(62, 70, start_time + 4 * time_per_note, start_time + 5 * time_per_note))

# Repeat the motif in bar 3
start_time = time_per_beat * 0.0 + time_per_bar * 2.0
sax_notes.append(Note(62, 100, start_time, start_time + time_per_note))
sax_notes.append(Note(67, 100, start_time + time_per_note, start_time + 2 * time_per_note))
sax_notes.append(Note(69, 100, start_time + 2 * time_per_note, start_time + 3 * time_per_note))
sax_notes.append(Note(62, 100, start_time + 3 * time_per_note, start_time + 4 * time_per_note))

# Let it hang again
sax_notes.append(Note(62, 70, start_time + 4 * time_per_note, start_time + 5 * time_per_note))

sax.notes = sax_notes
pm.instruments.append(sax)

# Save the MIDI file
pm.write("montclair_whisper.mid")
