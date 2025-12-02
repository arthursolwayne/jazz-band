
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define key: F Major
key = 'F'

# Define instruments
# Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = pretty_midi.Instrument(program=bass_program)

# Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 2')
piano = pretty_midi.Instrument(program=piano_program)

# Drums (Little Ray)
drum_program = pretty_midi.instrument_name_to_program('Drums')
drums = pretty_midi.Instrument(program=drum_program)

# Tenor Sax (You)
sax_program = pretty_midi.instrument_name_to_program('Soprano Sax')
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the PrettyMIDI object
pm.instruments = [bass, piano, drums, sax]

# Timing constants
BPM = 160
BAR_DURATION = 6.0  # 4 bars = 6 seconds
BEAT_DURATION = BAR_DURATION / 4
NOTE_DURATION = BEAT_DURATION / 2  # Half note per beat

# Utility function to convert time to seconds
def time_to_sec(time):
    return time

# --- Bar 1: Drums only (Little Ray) ---
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Time in seconds for each beat
beat_times = [0.0, BEAT_DURATION, 2 * BEAT_DURATION, 3 * BEAT_DURATION]

# Kick
for time in beat_times[::2]:  # 1 and 3
    note = pretty_midi.Note(velocity=80, pitch=36, start=time, end=time + NOTE_DURATION / 4)
    drums.notes.append(note)

# Snare
for time in beat_times[1::2]:  # 2 and 4
    note = pretty_midi.Note(velocity=80, pitch=38, start=time, end=time + NOTE_DURATION / 4)
    drums.notes.append(note)

# Hi-hat on every eighth (8 notes per bar)
for i in range(8):
    time = i * (BEAT_DURATION / 2)
    note = pretty_midi.Note(velocity=80, pitch=42, start=time, end=time + 0.05)
    drums.notes.append(note)

# --- Bar 2: Everyone enters, sax takes melody (Dante) ---

# Define sax motif: F, G#, A#, C
# In F major, F G# A# C = F, G# (Bb), A# (B), C
# Transpose to sax range: F (65), G# (67), A# (69), C (72)

# Time for bar 2: 0.0 to 1.5s
note_start = 1.5  # start of bar 2
note_duration = 0.25  # quarter note

# Motif: F, G#, A#, C (quarter notes)
notes = [65, 67, 69, 72]
for i, pitch in enumerate(notes):
    start = note_start + i * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# --- Bar 3: Bass (Marcus) walking line, chromatic approach to F ---

# In F major, walking line: E, F, G#, A#, Bb, B, C, D
# Chromatic approach to F: E, F (or E#, F)
# Walking line in F (root movement, chromatic)
# Start at note_start = 1.5 (bar 2), bar 3: 1.5 - 3.0
# 8 notes: walking quarter notes

# Bass line: E, F, G#, A#, Bb, B, C, D
bass_notes = [64, 65, 67, 69, 70, 71, 72, 74]
for i, pitch in enumerate(bass_notes):
    start = note_start + i * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=end)
    bass.notes.append(note)

# --- Bar 3: Piano (Diane) comping on 2 and 4 with 7th chords ---

# Comping on 2 and 4
# Use dominant 7th chords: F7, B7, etc.
# F7: F, A, C, Eb (but we'll use F, A, C, E)
# Time for comp: bar 2.5 (beat 2) and bar 3.0 (beat 4)
comp_notes = [
    # F7 (root position): F, A, C, E
    # Duration: eighth note (0.125s)
    pretty_midi.Note(velocity=80, pitch=65, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=67, start=2.5, end=2.625),
    
    # B7 (root position): B, D#, F#, A
    # Duration: eighth note (0.125s)
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=75, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=77, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=79, start=3.0, end=3.125)
]

for note in comp_notes:
    piano.notes.append(note)

# --- Bar 4: Sax returns with a resolution and twist ---

# Repeat motif but end on A#
# Motif: F, G#, A#, C, then F, G#, A#
# End on A# to create a twist (no resolution)
note_start = 3.0  # start of bar 3
note_duration = 0.25  # quarter note

notes = [65, 67, 69, 72, 65, 67, 69]
for i, pitch in enumerate(notes):
    start = note_start + i * note_duration
    end = start + note_duration
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=start, end=end)
    sax.notes.append(note)

# Save the MIDI file
pm.write('jazz_intro.mid')
print("MIDI file 'jazz_intro.mid' has been created.")
