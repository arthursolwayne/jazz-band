
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.tempo = 160  # 160 BPM

# Define time in seconds per bar
BPM = 160
beats_per_bar = 4
seconds_per_beat = 60 / BPM
seconds_per_bar = seconds_per_beat * beats_per_bar

# Function to convert beat to time in seconds
def beat_to_time(beat):
    return beat * seconds_per_beat

# ====== DRUMS (Little Ray) ======
drum_program = Program(program=12, is_drum=True)
drum_inst = Instrument(program=drum_program)
pm.instruments.append(drum_inst)

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time: [0.0, 0.375, 0.75, 1.125, 1.5, 1.875, 2.25, 2.625, 3.0]
# Bar 1: 0.0 to 3.0 seconds

# Kick on 1 (0.0), 3 (1.5)
drum_inst.notes.append(Note(36, 100, beat_to_time(0.0), beat_to_time(0.0) + 0.25))
drum_inst.notes.append(Note(36, 100, beat_to_time(1.5), beat_to_time(1.5) + 0.25))

# Snare on 2 (0.75), 4 (2.25)
drum_inst.notes.append(Note(38, 100, beat_to_time(0.75), beat_to_time(0.75) + 0.25))
drum_inst.notes.append(Note(38, 100, beat_to_time(2.25), beat_to_time(2.25) + 0.25))

# Hi-hat on every eighth
for i in range(0, 8):
    time = beat_to_time(i * 0.125)
    drum_inst.notes.append(Note(42, 100, time, time + 0.125))

# ====== BASS (Marcus) ======
bass_program = Program(program=33)
bass_inst = Instrument(program=bass_program)
pm.instruments.append(bass_inst)

# Bar 2: Bass enters with a walking line in F minor
# Fm key: F, Ab, Bb, D, Eb, G, A, C
# Walking line: F → G → Ab → Bb (bar 2)
# Time: 3.0 to 6.0 seconds

# F (3.0)
bass_inst.notes.append(Note(65, 80, 3.0, 3.25))
# G (3.375)
bass_inst.notes.append(Note(67, 80, 3.375, 3.625))
# Ab (3.75)
bass_inst.notes.append(Note(68, 80, 3.75, 4.0))
# Bb (4.125)
bass_inst.notes.append(Note(71, 80, 4.125, 4.375))

# ====== PIANO (Diane) ======
piano_program = Program(program=0)
piano_inst = Instrument(program=piano_program)
pm.instruments.append(piano_inst)

# Bar 3: Diane enters with comping chords on 2 and 4
# Fm7 = F, Ab, C, Eb
# Comp on 2 and 4 (time: 4.5 and 6.0)
# Use 7th chords, chromatic tension

# Fm7 on beat 2 (4.5)
# F, Ab, C, Eb — all on beat 2
piano_inst.notes.append(Note(65, 80, 4.5, 4.625))
piano_inst.notes.append(Note(68, 80, 4.5, 4.625))
piano_inst.notes.append(Note(72, 80, 4.5, 4.625))
piano_inst.notes.append(Note(69, 80, 4.5, 4.625))

# Add some tension: Bb (71) on 4.625
piano_inst.notes.append(Note(71, 90, 4.625, 4.75))

# Fm7 on beat 4 (6.0)
piano_inst.notes.append(Note(65, 80, 6.0, 6.125))
piano_inst.notes.append(Note(68, 80, 6.0, 6.125))
piano_inst.notes.append(Note(72, 80, 6.0, 6.125))
piano_inst.notes.append(Note(69, 80, 6.0, 6.125))

# ====== SAXOPHONE (You) ======
sax_program = Program(program=64)
sax_inst = Instrument(program=sax_program)
pm.instruments.append(sax_inst)

# Bar 4: You enter with a short, expressive motif
# F (65) -> Ab (68) -> Bb (71) -> F (65)
# Start at 6.0 seconds, high note, then resolve

# F (65) — high note, short sustain
sax_inst.notes.append(Note(65, 100, 6.0, 6.15))
# Ab (68) — slightly lower, unresolved tension
sax_inst.notes.append(Note(68, 90, 6.15, 6.3))
# Bb (71) — unresolved
sax_inst.notes.append(Note(71, 95, 6.3, 6.45))
# F (65) — resolves back
sax_inst.notes.append(Note(65, 100, 6.45, 6.6))

# Save the MIDI file
pm.write("jazz_intro_f_minor.mid")
