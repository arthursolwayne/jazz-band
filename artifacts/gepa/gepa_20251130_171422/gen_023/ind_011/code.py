
import pretty_midi
import numpy as np

# Constants
BPM = 160
TEMPO = BPM * 60 / 6  # beats per second (for 6 seconds total)
BAR_DURATION = 1.5  # seconds per bar
NOTE_DURATION = TEMPO  # seconds per beat
TIME_SIGNATURE = (4, 4)

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=BPM)
instrument = pretty_midi.Instrument(program=64)  # Tenor sax
pm.instruments.append(instrument)

# Time line (in seconds)
time = 0.0

# Helper functions
def note_on(note_number, velocity, time):
    note = pretty_midi.Note(velocity=velocity, pitch=note_number, start=time)
    instrument.notes.append(note)

def note_off(note_number, time):
    # We'll let PrettyMIDI handle the end time automatically
    pass

def rest(duration):
    global time
    time += duration

# Bar 1: Little Ray on drums (snare on 2 and 4, kick on 1 and 3)
# Bar 1 is in 4/4 time, 160 BPM, 6.0 seconds total => 1.5 seconds per bar

# Bar 1
time = 0.0

# Kick on 1 and 3
note_on(36, 100, time)  # Kick on beat 1
note_on(36, 100, time + NOTE_DURATION)  # Kick on beat 3

# Snare on 2 and 4
note_on(42, 110, time + NOTE_DURATION * 1)  # Snare on beat 2
note_on(42, 110, time + NOTE_DURATION * 3)  # Snare on beat 4

# Hihat on every eighth note
hihat_velocity = 60
for i in range(8):
    note_on(46, hihat_velocity, time + i * NOTE_DURATION / 2)
    note_on(46, hihat_velocity, time + i * NOTE_DURATION / 2 + 0.02)  # slight dynamic variation
    note_off(46, time + i * NOTE_DURATION / 2 + 0.02)

time += BAR_DURATION

# Bar 2: Everyone comes in, saxophone motif (Fm: F, Ab, Bb, C, Db, Eb, Gb, G)

# Diane: piano comp on 2 and 4
piano_instrument = pretty_midi.Instrument(program=0)
pm.instruments.append(piano_instrument)

# Marcus: walking bass line (Fm7)
bass_instrument = pretty_midi.Instrument(program=33)
pm.instruments.append(bass_instrument)

# Bar 2
time = 0.0

# Bass line: walking, chromatic approach to Fm
bass_notes = [53, 51, 50, 49, 51, 53, 51, 50]
for note in bass_notes:
    note_on(note, np.random.randint(90, 100), time)
    time += NOTE_DURATION

# Piano comp
# Bar 2: 7th chords on 2 and 4
# Fm7 = F, Ab, Bb, Db
# Bb7 = Bb, D, F, Ab
piano_notes = [
    (55, 72, 67, 64),  # Fm7 on beat 2
    (59, 71, 64, 67),  # Bb7 on beat 4
]
for i, chord in enumerate(piano_notes):
    for note in chord:
        note_on(note, 95, time + (i + 1) * NOTE_DURATION)
    note_on(60, 80, time + (i + 1) * NOTE_DURATION)
    note_on(64, 75, time + (i + 1) * NOTE_DURATION)
    note_on(67, 70, time + (i + 1) * NOTE_DURATION)

# Drums
note_on(36, 90, time)  # Kick on beat 1
note_on(42, 100, time + NOTE_DURATION)  # Snare on beat 2
note_on(36, 85, time + NOTE_DURATION * 2)  # Kick on beat 3
note_on(42, 100, time + NOTE_DURATION * 3)  # Snare on beat 4

# Hihat on every eighth note
hihat_velocity = 60
for i in range(8):
    note_on(46, hihat_velocity, time + i * NOTE_DURATION / 2)
    note_on(46, hihat_velocity, time + i * NOTE_DURATION / 2 + 0.02)
    note_off(46, time + i * NOTE_DURATION / 2 + 0.02)

# Saxophone motif (start of melody)
# Fm: F, Ab, Bb, C, Db, Eb, Gb, G
# Let's do a short, emotional motif: F -> Ab -> Bb -> Eb
# Let's play it with dynamics, expression, and space
sax_instrument = pretty_midi.Instrument(program=64)
pm.instruments.append(sax_instrument)

# Set velocity to 95 for normal
note_on(53, 95, time)  # F
note_off(53, time + NOTE_DURATION * 0.5)

note_on(51, 90, time + NOTE_DURATION * 0.5)  # Ab
note_off(51, time + NOTE_DURATION * 1)

note_on(50, 95, time + NOTE_DURATION * 1)  # Bb
note_off(50, time + NOTE_DURATION * 1.25)

note_on(57, 80, time + NOTE_DURATION * 1.25)  # Eb
note_off(57, time + NOTE_DURATION * 1.5)

time += BAR_DURATION

# Bar 3: Continue with the same pattern

# Bass line: walking, chromatic approach to Fm
bass_notes = [53, 51, 50, 49, 51, 53, 51, 50]
for note in bass_notes:
    note_on(note, np.random.randint(90, 100), time)
    time += NOTE_DURATION

# Piano comp
# Fm7 on beat 2
note_on(55, 95, time + NOTE_DURATION)
note_on(67, 75, time + NOTE_DURATION)
note_on(64, 70, time + NOTE_DURATION)
note_on(60, 80, time + NOTE_DURATION)

# Bb7 on beat 4
note_on(59, 95, time + NOTE_DURATION * 3)
note_on(64, 75, time + NOTE_DURATION * 3)
note_on(67, 70, time + NOTE_DURATION * 3)
note_on(60, 80, time + NOTE_DURATION * 3)

# Drums
note_on(36, 90, time)  # Kick on beat 1
note_on(42, 100, time + NOTE_DURATION)  # Snare on beat 2
note_on(36, 85, time + NOTE_DURATION * 2)  # Kick on beat 3
note_on(42, 100, time + NOTE_DURATION * 3)  # Snare on beat 4

# Hihat on every eighth note
hihat_velocity = 60
for i in range(8):
    note_on(46, hihat_velocity, time + i * NOTE_DURATION / 2)
    note_on(46, hihat_velocity, time + i * NOTE_DURATION / 2 + 0.02)
    note_off(46, time + i * NOTE_DURATION / 2 + 0.02)

# Bar 4: End with the motif, but leave it hanging — F -> Ab -> Bb -> rest

note_on(53, 95, time)  # F
note_off(53, time + NOTE_DURATION * 0.5)

note_on(51, 90, time + NOTE_DURATION * 0.5)  # Ab
note_off(51, time + NOTE_DURATION * 1)

note_on(50, 95, time + NOTE_DURATION * 1)  # Bb
note_off(50, time + NOTE_DURATION * 1.3)

# Let it hang — end on a rest, no resolution

# Save the MIDI
pm.write("dante_intro.mid")
