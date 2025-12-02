
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new MIDI file
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define key: F major (key number 1)
key = 1  # F major

# Define instrument channels
drums_program = Program(0)  # Drums
bass_program = Program(33)  # Double Bass
piano_program = Program(0)  # Acoustic Piano
tenor_program = Program(69)  # Tenor Sax

# Create instruments
drums = Instrument(program=drums_program)
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
tenor = Instrument(program=tenor_program)

# Time signatures
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]

# Time per bar in seconds (160 BPM = 60/160 = 0.375 sec per beat, 1.5 sec per bar)
bar_duration = 1.5

# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Kick on 1 and 3
drums.notes.append(Note(36, 100, 0.0, 0.375))  # Kick on 1
drums.notes.append(Note(36, 100, 1.125, 1.5))  # Kick on 3

# Snare on 2 and 4
drums.notes.append(Note(38, 100, 0.75, 0.375))  # Snare on 2
drums.notes.append(Note(38, 100, 1.875, 0.375))  # Snare on 4

# Hihat on every eighth note
for i in range(0, 8):
    hihat_time = i * 0.375
    drums.notes.append(Note(42, 80, hihat_time, hihat_time + 0.125))

# Bar 2: All instruments in
# Time starts at 1.5

# Bass line: F, G, A, Bb (chromatic approach to Bb, then back to F)
# Walking line, no repeated notes, forward motion

bass_notes = [
    Note(71, 80, 1.5, 1.5 + 0.375),  # F (C4)
    Note(72, 80, 1.875, 1.875 + 0.375),  # G (D4)
    Note(73, 80, 2.25, 2.25 + 0.375),  # A (E4)
    Note(74, 80, 2.625, 2.625 + 0.375),  # Bb (F4)
]

bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords on 2 and 4
# Bar 2: F7 on 2 and 4
# F7: F, A, C, Eb (chord tones), 7th is Eb

# 2nd beat (1.875)
piano_notes = [
    Note(71, 90, 1.875, 1.875 + 0.375),  # F
    Note(74, 90, 1.875, 1.875 + 0.375),  # Eb
    Note(72, 90, 1.875, 1.875 + 0.375),  # G
    Note(76, 90, 1.875, 1.875 + 0.375),  # A
]

# 4th beat (2.625)
piano_notes += [
    Note(71, 90, 2.625, 2.625 + 0.375),  # F
    Note(74, 90, 2.625, 2.625 + 0.375),  # Eb
    Note(72, 90, 2.625, 2.625 + 0.375),  # G
    Note(76, 90, 2.625, 2.625 + 0.375),  # A
]

# Bar 3: No piano (let the motif breathe)
# Bar 4: Piano again with F7

# Bar 3: Tenor sax motif (Dante's moment)
# Motif: F -> Ab -> Bb -> F (octave up)
# Start on beat 2 of bar 2, end on beat 3 of bar 3

# Bar 2, beat 2: F (71)
tenor.notes.append(Note(71, 100, 1.875, 1.875 + 0.1875))

# Bar 2, beat 3: Ab (73)
tenor.notes.append(Note(73, 100, 2.25, 2.25 + 0.1875))

# Bar 2, beat 4: Bb (74)
tenor.notes.append(Note(74, 100, 2.625, 2.625 + 0.1875))

# Bar 3, beat 1: F again (octave up: 81)
tenor.notes.append(Note(81, 100, 3.0, 3.0 + 0.1875))

# Bar 3, beat 2: Rest (space)
# Bar 3, beat 3: End the motif (pass the question)
# No note, just space

# Bar 4: Piano again, F7 on 2 and 4
piano_notes += [
    Note(71, 90, 3.375, 3.375 + 0.375),  # F
    Note(74, 90, 3.375, 3.375 + 0.375),  # Eb
    Note(72, 90, 3.375, 3.375 + 0.375),  # G
    Note(76, 90, 3.375, 3.375 + 0.375),  # A
]

piano.notes.extend(piano_notes)

# Add instruments to the MIDI file
pm.instruments.append(drums)
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(tenor)

# Save the MIDI file
pm.write("dante_sax_intro.mid")
