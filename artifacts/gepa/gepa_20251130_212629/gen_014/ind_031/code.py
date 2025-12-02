
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up the time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key: F major (no sharps, no flats)
# F major scale: F, G, A, Bb, C, D, E

# Create instruments
drums = pretty_midi.Instrument(program=128, is_drum=True)  # Drums
bass = pretty_midi.Instrument(program=33)                  # Bass
piano = pretty_midi.Instrument(program=0)                 # Piano
sax = pretty_midi.Instrument(program=69)                  # Tenor Sax

pm.instruments = [drums, bass, piano, sax]

# Define timing: 160 BPM = 6/160 = 0.0375 seconds per beat
# 4 bars = 16 beats = 6 seconds
# Each beat = 0.375 seconds

# Function to convert beat to time in seconds
def beat_to_time(beat):
    return beat * 0.375

# -------------------
# Bar 1: Drums (Little Ray) - 6 seconds of energy
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Fill the bar with energy but make space

for beat in range(16):  # 16 beats in 4 bars, but let's just do 16 beats for this
    time = beat_to_time(beat)
    if beat % 2 == 0:
        # Kick on 1 and 3
        if beat % 4 == 0 or beat % 4 == 2:
            note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + 0.1)
            drums.notes.append(note)
        # Snare on 2 and 4
        elif beat % 4 == 1 or beat % 4 == 3:
            note = pretty_midi.Note(velocity=100, pitch=64, start=time, end=time + 0.1)
            drums.notes.append(note)
    # Hi-hat on every eighth note
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note)
    elif beat % 2 == 1:
        note = pretty_midi.Note(velocity=90, pitch=42, start=time, end=time + 0.05)
        drums.notes.append(note)

# -------------------
# Bar 2: Bass (Marcus) - Walking line in F major
# Chromatic approaches, no repeating notes

# F major scale: F, G, A, Bb, C, D, E
# Use chromatic approach to each note
# F -> D -> E (chromatic up)
# G -> E -> F (chromatic down)
# A -> G -> Bb (chromatic up)
# Bb -> A -> Bb
# C -> Bb -> C
# D -> C -> D
# E -> D -> E

bass_notes = [65, 67, 69, 70, 72, 74, 76]  # F, G, A, Bb, C, D, E

for i in range(4):  # 4 bars, one note per beat
    beat = i
    time = beat_to_time(beat)
    note = bass_notes[i % 7]
    # Chromatic approach
    if i % 2 == 0:
        approach_note = note - 2  # chromatic down
    else:
        approach_note = note + 1  # chromatic up
    # Approach on beat 1
    note_app = pretty_midi.Note(velocity=80, pitch=approach_note, start=time, end=time + 0.1)
    bass.notes.append(note_app)
    # Main note on beat 2
    note_main = pretty_midi.Note(velocity=100, pitch=note, start=time + 0.1, end=time + 0.2)
    bass.notes.append(note_main)

# -------------------
# Bar 3: Piano (Diane) - 7th chords on 2 and 4
# F7: F, A, C, Eb
# C7: C, E, G, Bb
# G7: G, B, D, F
# D7: D, F#, A, C

# Bar 3: F7 on beat 2 and 4
for beat in [1, 3]:  # beat 2 and 4
    time = beat_to_time(beat)
    # F7: F, A, C, Eb
    for pitch in [65, 68, 72, 69]:
        note = pretty_midi.Note(velocity=90, pitch=pitch, start=time, end=time + 0.1)
        piano.notes.append(note)

# -------------------
# Bar 4: Tenor Sax (You) - Short motif, lyrical, suspended
# Motif: F, Bb, D, rest
# Start on beat 1, but rest on beat 2
# Let the motif hang — it's the question

# First note: F (65)
note1 = pretty_midi.Note(velocity=100, pitch=65, start=beat_to_time(0), end=beat_to_time(0) + 0.3)
sax.notes.append(note1)

# Second note: Bb (69)
note2 = pretty_midi.Note(velocity=100, pitch=69, start=beat_to_time(1), end=beat_to_time(1) + 0.3)
sax.notes.append(note2)

# Third note: D (74)
note3 = pretty_midi.Note(velocity=100, pitch=74, start=beat_to_time(2), end=beat_to_time(2) + 0.3)
sax.notes.append(note3)

# Rest (leave the question hanging)
# No note on beat 3

# Save the MIDI file
pm.write('jazz_intro.mid')
print("MIDI file 'jazz_intro.mid' has been created.")
