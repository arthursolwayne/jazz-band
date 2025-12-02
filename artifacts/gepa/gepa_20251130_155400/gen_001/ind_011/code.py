
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new pretty_midi object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: Dm (D minor)
key = 'D minor'

# Time signature: 4/4
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)

pm.time_signature_changes.append(time_signature)

# Define the instruments
# 1. Bass (Program 33 - Acoustic Bass)
bass_program = Program(program=33)
bass_instrument = Instrument(program=bass_program, is_drum=False)
pm.instruments.append(bass_instrument)

# 2. Piano (Program 0 - Acoustic Grand Piano)
piano_program = Program(program=0)
piano_instrument = Instrument(program=piano_program, is_drum=False)
pm.instruments.append(piano_instrument)

# 3. Drums (Program 0 - Acoustic Drum Kit)
drum_program = Program(program=0)
drum_instrument = Instrument(program=drum_program, is_drum=True)
pm.instruments.append(drum_instrument)

# 4. Tenor Sax (Program 62 - Tenor Saxophone)
sax_program = Program(program=62)
sax_instrument = Instrument(program=sax_program, is_drum=False)
pm.instruments.append(sax_instrument)

# Define the timing (160 BPM, 4/4 time)
# 1 bar = 1.5 seconds
# 1 beat = 0.375 seconds
# 1 sixteenth note = 0.09375 seconds

# Bar 1: Drums only
# Use a simple kick and snare pattern
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0.0 to 1.5 seconds)
# Kick on 0.0, 0.75
kick_notes = [Note(36, 0.0, 0.1), Note(36, 0.75, 0.1)]
for note in kick_notes:
    drum_instrument.notes.append(note)

# Snare on 0.375, 1.125
snare_notes = [Note(38, 0.375, 0.1), Note(38, 1.125, 0.1)]
for note in snare_notes:
    drum_instrument.notes.append(note)

# Hihat on every eighth
hihat_notes = []
for i in range(0, 8):
    start = i * 0.09375
    hihat_notes.append(Note(42, start, 0.05))
for note in hihat_notes:
    drum_instrument.notes.append(note)

# Bar 2 (1.5 to 3.0 seconds)
# Bass line: Walking line, chromatic approaches, no repeated notes
# Dm7 = D F A C
# Start with D, walk up chromatically

bass_notes = [
    Note(62, 1.5, 0.375),  # D
    Note(63, 1.875, 0.375),  # Eb
    Note(65, 2.25, 0.375),  # F
    Note(67, 2.625, 0.375),  # G
    Note(69, 3.0, 0.375),  # A
]

for note in bass_notes:
    bass_instrument.notes.append(note)

# Piano comping: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Dm7 in root position = D, F, A, C
# Use a rootless voicing: F, A, C, D

# Bar 2: Comp on 2 and 4
# 2 = 1.875
# 4 = 2.625

chord_notes = [(65, 1.875, 0.1), (68, 1.875, 0.1), (71, 1.875, 0.1), (72, 1.875, 0.1),
               (65, 2.625, 0.1), (68, 2.625, 0.1), (71, 2.625, 0.1), (72, 2.625, 0.1)]

for pitch, start, duration in chord_notes:
    piano_instrument.notes.append(Note(pitch, start, duration))

# Tenor sax: One short motif, unique durations, rests, space
# Start at 1.5 (Bar 2), leave it hanging, return in Bar 4

# Melody: D (62) on beat 2, rest on beat 3, Bb (62 - 2 semitones = 60) on beat 4
# Then return in Bar 4 with a descending line

# Bar 2: D (beat 2), rest on beat 3, Bb on beat 4
note1 = Note(62, 1.875, 0.25)
note2 = Note(60, 2.625, 0.25)
sax_instrument.notes.append(note1)
sax_instrument.notes.append(note2)

# Bar 3 (3.0 to 4.5 seconds): Bass line, chromatic walk-down
# D -> C -> B -> A -> G

bass_notes = [
    Note(62, 3.0, 0.375),  # D
    Note(60, 3.375, 0.375),  # C
    Note(59, 3.75, 0.375),  # B
    Note(69, 4.125, 0.375),  # A
    Note(67, 4.5, 0.375),  # G
]

for note in bass_notes:
    bass_instrument.notes.append(note)

# Piano comping: Tension and release
# Use a tritone substitution: G7 (G B D F)
# Rootless voicing: B, D, F, G

chord_notes = [(62, 3.375, 0.1), (64, 3.375, 0.1), (67, 3.375, 0.1), (69, 3.375, 0.1),
               (62, 4.125, 0.1), (64, 4.125, 0.1), (67, 4.125, 0.1), (69, 4.125, 0.1)]

for pitch, start, duration in chord_notes:
    piano_instrument.notes.append(Note(pitch, start, duration))

# Drums: Same pattern again
# Kick on 3.0, 3.75
kick_notes = [Note(36, 3.0, 0.1), Note(36, 3.75, 0.1)]
for note in kick_notes:
    drum_instrument.notes.append(note)

# Snare on 3.375, 4.125
snare_notes = [Note(38, 3.375, 0.1), Note(38, 4.125, 0.1)]
for note in snare_notes:
    drum_instrument.notes.append(note)

# Hihat on every eighth
hihat_notes = []
for i in range(0, 8):
    start = 3.0 + i * 0.09375
    hihat_notes.append(Note(42, start, 0.05))
for note in hihat_notes:
    drum_instrument.notes.append(note)

# Bar 4 (4.5 to 6.0 seconds)
# Bass: Chromatic walk-up from G to D

bass_notes = [
    Note(67, 4.5, 0.375),  # G
    Note(69, 4.875, 0.375),  # A
    Note(71, 5.25, 0.375),  # B
    Note(72, 5.625, 0.375),  # C
    Note(62, 6.0, 0.375),  # D
]

for note in bass_notes:
    bass_instrument.notes.append(note)

# Piano comping: Return to Dm7
# Rootless voicing: F, A, C, D

chord_notes = [(65, 4.875, 0.1), (68, 4.875, 0.1), (71, 4.875, 0.1), (72, 4.875, 0.1),
               (65, 5.625, 0.1), (68, 5.625, 0.1), (71, 5.625, 0.1), (72, 5.625, 0.1)]

for pitch, start, duration in chord_notes:
    piano_instrument.notes.append(Note(pitch, start, duration))

# Tenor sax: Complete the motif — return to the beginning with a descending line
# C (60) on beat 1, B (59) on beat 2, A (69) on beat 3, rest on beat 4

note1 = Note(60, 4.5, 0.25)
note2 = Note(59, 4.875, 0.25)
note3 = Note(69, 5.25, 0.25)
sax_instrument.notes.append(note1)
sax_instrument.notes.append(note2)
sax_instrument.notes.append(note3)

# Drums: Same pattern again
# Kick on 4.5, 5.25
kick_notes = [Note(36, 4.5, 0.1), Note(36, 5.25, 0.1)]
for note in kick_notes:
    drum_instrument.notes.append(note)

# Snare on 4.875, 5.625
snare_notes = [Note(38, 4.875, 0.1), Note(38, 5.625, 0.1)]
for note in snare_notes:
    drum_instrument.notes.append(note)

# Hihat on every eighth
hihat_notes = []
for i in range(0, 8):
    start = 4.5 + i * 0.09375
    hihat_notes.append(Note(42, start, 0.05))
for note in hihat_notes:
    drum_instrument.notes.append(note)

# Write the MIDI file
pm.write("dante_russo_intro.mid")
