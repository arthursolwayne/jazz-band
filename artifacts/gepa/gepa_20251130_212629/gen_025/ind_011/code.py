
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Initialize MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set up time signatures (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define note values
quarter = 1.0
eighth = 0.5
sixteenth = 0.25

# Function to create a note
def create_note(note_number, start, end, velocity):
    return Note(note_number, start, end, velocity)

# Define the key: F major
F = pretty_midi.note_number_to_name(65)  # F4 is the tonic, but we'll use F3 as base
note_numbers = [65, 67, 69, 71, 72, 74, 76]  # F, G, A, Bb, B, C, D

# ================================
# 1. Drums (Little Ray) - Bar 1 (0 to 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_program = Program(0, 0)
drum_inst = Instrument(program=drum_program, is_drum=True)

# Kick (60 for kick)
drum_inst.notes.append(create_note(60, 0, 0.375, 100))
drum_inst.notes.append(create_note(60, 1.125, 1.5, 100))

# Snare (62 for snare)
drum_inst.notes.append(create_note(62, 0.75, 1.0, 100))
drum_inst.notes.append(create_note(62, 1.5, 1.75, 100))

# Hihat (42 for hihat)
for t in [0.0, 0.375, 0.75, 1.125, 1.5, 1.875]:
    drum_inst.notes.append(create_note(42, t, t + 0.25, 90))

pm.instruments.append(drum_inst)

# ================================
# 2. Bass (Marcus) - Bars 2-4 (1.5s to 4.5s)
bass_program = Program(33, 0)  # Acoustic Bass
bass_inst = Instrument(program=bass_program)

# Walking line in F major, chromatic motion, no repeated notes
# Start on F (65), walk up chromatically: F G Ab Bb B C D
# Then take a moment, then repeat with a slight variation

# Bar 2
bass_inst.notes.append(create_note(65, 1.5, 1.75, 80))  # F
bass_inst.notes.append(create_note(67, 1.75, 2.0, 80))  # G
bass_inst.notes.append(create_note(69, 2.0, 2.25, 80))  # A
bass_inst.notes.append(create_note(71, 2.25, 2.5, 80))  # Bb
bass_inst.notes.append(create_note(72, 2.5, 2.75, 80))  # B
bass_inst.notes.append(create_note(74, 2.75, 3.0, 80))  # C
bass_inst.notes.append(create_note(76, 3.0, 3.25, 80))  # D

# Bar 3
bass_inst.notes.append(create_note(76, 3.25, 3.5, 80))  # D
bass_inst.notes.append(create_note(74, 3.5, 3.75, 80))  # C
bass_inst.notes.append(create_note(72, 3.75, 4.0, 80))  # B
bass_inst.notes.append(create_note(71, 4.0, 4.25, 80))  # Bb
bass_inst.notes.append(create_note(69, 4.25, 4.5, 80))  # A

# Bar 4
bass_inst.notes.append(create_note(67, 4.5, 4.75, 80))  # G
bass_inst.notes.append(create_note(65, 4.75, 5.0, 80))  # F

pm.instruments.append(bass_inst)

# ================================
# 3. Piano (Diane) - Bars 2-4 (1.5s to 4.5s)
piano_program = Program(0, 0)  # Acoustic Piano
piano_inst = Instrument(program=piano_program)

# Diane plays 7th chords on 2 and 4
# F7 on 2 (bar 2), Bb7 on 2 (bar 3), D7 on 2 (bar 4)

# Bar 2
piano_inst.notes.append(create_note(65, 2.0, 2.25, 80))  # F
piano_inst.notes.append(create_note(67, 2.0, 2.25, 80))  # G
piano_inst.notes.append(create_note(72, 2.0, 2.25, 80))  # B
piano_inst.notes.append(create_note(71, 2.0, 2.25, 80))  # Bb

# Bar 3
piano_inst.notes.append(create_note(71, 3.0, 3.25, 80))  # Bb
piano_inst.notes.append(create_note(73, 3.0, 3.25, 80))  # C
piano_inst.notes.append(create_note(77, 3.0, 3.25, 80))  # D
piano_inst.notes.append(create_note(76, 3.0, 3.25, 80))  # C#

# Bar 4
piano_inst.notes.append(create_note(65, 4.0, 4.25, 80))  # F
piano_inst.notes.append(create_note(67, 4.0, 4.25, 80))  # G
piano_inst.notes.append(create_note(72, 4.0, 4.25, 80))  # B
piano_inst.notes.append(create_note(76, 4.0, 4.25, 80))  # D

pm.instruments.append(piano_inst)

# ================================
# 4. Tenor Sax (Dante) - Bars 2-4 (1.5s to 4.5s)
sax_program = Program(64, 0)  # Tenor Sax
sax_inst = Instrument(program=sax_program)

# Dante's motif: F (65) on beat 1, F# (66) on beat 2, wait, then return to F
# Ends on a question — F# (66) on beat 4

# Bar 2: Motif starts
sax_inst.notes.append(create_note(65, 1.5, 1.75, 100))  # F
sax_inst.notes.append(create_note(66, 1.75, 2.25, 100))  # F# (hangs)
sax_inst.notes.append(create_note(66, 2.75, 3.0, 100))  # F# (return)

# Bar 3: continuation (repeats motif with variation)
sax_inst.notes.append(create_note(65, 3.0, 3.25, 100))  # F
sax_inst.notes.append(create_note(66, 3.25, 3.75, 100))  # F# (hangs)
sax_inst.notes.append(create_note(66, 4.25, 4.5, 100))  # F# (return with a question)

pm.instruments.append(sax_inst)

# Save the MIDI file
pm.write('jazz_intro_f_major.mid')
print("MIDI file 'jazz_intro_f_major.mid' has been generated.")
