
import pretty_midi

# Create a PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define instruments
drum_program = pretty_midi.programs.DRUMS
bass_program = pretty_midi.instrument_name_to_program("Acoustic Bass")
piano_program = pretty_midi.instrument_name_to_program("Electric Piano 1")
sax_program = pretty_midi.instrument_name_to_program("Tenor Sax")

# Create instruments
drums = pretty_midi.Instrument(program=drum_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the piece
pm.instruments = [drums, bass, piano, sax]

# Tempo: 160 BPM, 4/4 time
# 1 bar = 1.5 seconds
# 1 beat = 0.375 seconds

# Helper function to convert beat to time
def beat_to_time(beat):
    return beat * 0.375

# ---- BAR 1: DRUMS ONLY (Little Ray) - Mysterious, sparse ----
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3 (beats 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=beat_to_time(0), end=beat_to_time(0.375)))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=beat_to_time(2), end=beat_to_time(2.375)))

# Snare on 2 and 4 (beats 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat_to_time(1), end=beat_to_time(1.375)))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=beat_to_time(3), end=beat_to_time(3.375)))

# Hi-hat on every eighth (total 8 notes per bar)
for i in range(8):
    time = beat_to_time(i * 0.25)
    drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=time, end=time + 0.125))

# ---- BAR 2: BASS + PIANO (Marcus + Diane) - Build Tension ----

# Bass line: Walking line with chromatic approaches (F, Gb, G, A, Bb, B, C, Db)
# Time for each note = 0.375 sec
notes = [77, 74, 79, 82, 80, 83, 87, 84]  # F, Gb, G, A, Bb, B, C, Db
velocities = [80, 85, 80, 85, 80, 85, 80, 85]

for i, (pitch, vel) in enumerate(zip(notes, velocities)):
    start = beat_to_time(i)
    duration = 0.375
    bass.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + duration))

# Piano: 7th chords on 2 and 4 (Bdim7 on 2, G7 on 4)
# Bdim7: B, D, F, Ab
# G7: G, B, D, F
# Comp on 2 and 4 (beat 1 and 3)

# Bdim7 on beat 1 (start at 0.375)
for pitch in [76, 71, 69, 67]:  # B, D, F, Ab
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=beat_to_time(1), end=beat_to_time(1.375)))

# G7 on beat 3 (start at 2.375)
for pitch in [79, 82, 76, 69]:  # G, B, D, F
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=beat_to_time(3), end=beat_to_time(3.375)))

# ---- BAR 3: TENOR SAX (You) - Sparse, expressive motif ----

# Melody: F, Eb, D, C (with a rest on beat 3)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=beat_to_time(0), end=beat_to_time(0.375)))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=beat_to_time(1), end=beat_to_time(1.375)))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=beat_to_time(2), end=beat_to_time(2.375)))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=beat_to_time(3), end=beat_to_time(3.375)))  # C

# ---- BAR 4: Repeat with variation (last note suspended) ----

# Repeat the motif but delay the last note by a half beat (linger on C)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=beat_to_time(4), end=beat_to_time(4.375)))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=beat_to_time(5), end=beat_to_time(5.375)))  # Eb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=beat_to_time(6), end=beat_to_time(6.375)))  # D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=beat_to_time(7), end=beat_to_time(8)))     # C (lingers)

# Save the MIDI file
pm.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
