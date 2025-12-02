
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key and scale
KEY = 'D'
SCALE = ['D', 'E', 'F#', 'G', 'A', 'B', 'C#']  # D major scale
SCALE_DEGREES = {note: idx for idx, note in enumerate(SCALE)}

# Define instruments
bass_program = Program(instrument=33, name="Acoustic Bass")
piano_program = Program(instrument=0, name="Acoustic Grand Piano")
drums_program = Program(instrument=10, name="Acoustic Drums")
sax_program = Program(instrument=66, name="Tenor Saxophone")

# Create instruments
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

pm.instruments = [bass, piano, drums, sax]

# Define the note duration in seconds (beat = 0.375s)
NOTE_DURATION = 0.375  # 1 beat

# Define the start time (in seconds) for each bar
bar_start = 0.0

# BAR 1: Drums alone
# Kick on 1 and 3
# Snare on 2 and 4
# Hihat on every eighth
# 1 bar = 4 beats = 4 * 0.375 = 1.5 seconds
# 8 eighths = 0.1875s each

for i in range(8):
    time = bar_start + i * 0.1875
    note = Note(velocity=100, start=time, end=time + 0.1875)
    if i % 2 == 0:  # hihat
        note.pitch = 60
        drums.notes.append(note)
    if i == 0 or i == 4:  # kick on 1 and 3
        note.pitch = 36
        note.velocity = 120
        drums.notes.append(note)
    if i == 2 or i == 6:  # snare on 2 and 4
        note.pitch = 38
        note.velocity = 110
        drums.notes.append(note)

bar_start += 1.5  # Move to bar 2

# BAR 2: All instruments in
# SAX: Start the motif on D (62) and leave it hanging
# D, F#, A — a triplet, leaving the A hanging

note = Note(velocity=100, start=bar_start, end=bar_start + NOTE_DURATION)
note.pitch = 62  # D5
sax.notes.append(note)

note = Note(velocity=100, start=bar_start + NOTE_DURATION * (1/3), end=bar_start + NOTE_DURATION * (2/3))
note.pitch = 67  # F#5
sax.notes.append(note)

note = Note(velocity=100, start=bar_start + NOTE_DURATION * (2/3), end=bar_start + NOTE_DURATION)
note.pitch = 69  # A5
sax.notes.append(note)

# BASS: Walking line in D major: D -> E -> F# -> G -> A -> B -> C# -> D
# Each note gets a quarter note

bass_notes = [62, 64, 66, 67, 69, 71, 73, 62]
for i, pitch in enumerate(bass_notes):
    start_time = bar_start + i * NOTE_DURATION
    note = Note(velocity=80, start=start_time, end=start_time + NOTE_DURATION)
    note.pitch = pitch
    bass.notes.append(note)

# PIANO: Comp on 2 and 4 with 7th chords
# D7 on beat 2, G7 on beat 4

# D7 = D, F#, A, C#
note = Note(velocity=90, start=bar_start + NOTE_DURATION * 1.5, end=bar_start + NOTE_DURATION * 2)
note.pitch = 62  # D
piano.notes.append(note)
note = Note(velocity=90, start=bar_start + NOTE_DURATION * 1.5, end=bar_start + NOTE_DURATION * 2)
note.pitch = 67  # F#
piano.notes.append(note)
note = Note(velocity=90, start=bar_start + NOTE_DURATION * 1.5, end=bar_start + NOTE_DURATION * 2)
note.pitch = 69  # A
piano.notes.append(note)
note = Note(velocity=90, start=bar_start + NOTE_DURATION * 1.5, end=bar_start + NOTE_DURATION * 2)
note.pitch = 71  # C#
piano.notes.append(note)

# G7 = G, B, D, F#
note = Note(velocity=90, start=bar_start + NOTE_DURATION * 3.5, end=bar_start + NOTE_DURATION * 4)
note.pitch = 67  # G
piano.notes.append(note)
note = Note(velocity=90, start=bar_start + NOTE_DURATION * 3.5, end=bar_start + NOTE_DURATION * 4)
note.pitch = 71  # B
piano.notes.append(note)
note = Note(velocity=90, start=bar_start + NOTE_DURATION * 3.5, end=bar_start + NOTE_DURATION * 4)
note.pitch = 69  # D
piano.notes.append(note)
note = Note(velocity=90, start=bar_start + NOTE_DURATION * 3.5, end=bar_start + NOTE_DURATION * 4)
note.pitch = 66  # F#
piano.notes.append(note)

# BAR 3: Drums continue
for i in range(8):
    time = bar_start + i * 0.1875
    note = Note(velocity=100, start=time, end=time + 0.1875)
    if i % 2 == 0:  # hihat
        note.pitch = 60
        drums.notes.append(note)
    if i == 0 or i == 4:  # kick on 1 and 3
        note.pitch = 36
        note.velocity = 120
        drums.notes.append(note)
    if i == 2 or i == 6:  # snare on 2 and 4
        note.pitch = 38
        note.velocity = 110
        drums.notes.append(note)

bar_start += 1.5  # Move to bar 4

# BAR 4: Sax returns to finish the motif, bass continues, piano rests

# D, F#, A — finish the motif
note = Note(velocity=100, start=bar_start, end=bar_start + NOTE_DURATION)
note.pitch = 62
sax.notes.append(note)

note = Note(velocity=100, start=bar_start + NOTE_DURATION * (1/3), end=bar_start + NOTE_DURATION * (2/3))
note.pitch = 67
sax.notes.append(note)

note = Note(velocity=100, start=bar_start + NOTE_DURATION * (2/3), end=bar_start + NOTE_DURATION)
note.pitch = 69
sax.notes.append(note)

# BASS: continue walking line
bass_notes = [72, 74, 76, 77, 79, 81, 83, 72]
for i, pitch in enumerate(bass_notes):
    start_time = bar_start + i * NOTE_DURATION
    note = Note(velocity=80, start=start_time, end=start_time + NOTE_DURATION)
    note.pitch = pitch
    bass.notes.append(note)

# PIANO: rests
pass  # No piano in bar 4

# Save the MIDI file
pm.write("dante_introduction.mid")
