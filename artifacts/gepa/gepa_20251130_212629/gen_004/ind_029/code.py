
import pretty_midi
from pretty_midi import Note, Instrument

# Create a MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
drums = Instrument(program=0, is_drum=True)
bass = Instrument(program=33)
piano = Instrument(program=0)
sax = Instrument(program=64)

# Add instruments to the MIDI file
midi.instruments.append(drums)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(sax)

# Define time in seconds (quarter note = 0.375s at 160 BPM)
quarter = 0.375
sixteenth = quarter / 4
eighth = quarter / 2

# Define F major scale (F, G, A, Bb, C, D, E)
F = 70  # MIDI note for F4
G = 71
A = 72
Bb = 70 + 10  # Bb4 = C4 + 10 (C is 60)
C = 72 + 2  # C5
D = 74
E = 76

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on all eighths
kick = Note(35, 100, 0, quarter)
snare = Note(38, 100, eighth, quarter)
hihat = Note(42, 80, 0, eighth)

drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Bar 2: Everyone joins in

# Bass line: walking line with chromatic approaches
# F -> Gb -> G -> A (chromatic approach to A)
# A -> Bb -> B -> C (chromatic approach to C)
# C -> D -> Eb -> D (chromatic approach to D)
# D -> Eb -> E -> F (chromatic approach to F)

bass_notes = [
    Note(70, 80, 0, quarter),
    Note(69, 80, quarter, quarter),
    Note(71, 80, quarter * 2, quarter),
    Note(72, 80, quarter * 3, quarter),
    Note(71, 80, quarter * 4, quarter),
    Note(70, 80, quarter * 5, quarter),
    Note(71, 80, quarter * 6, quarter),
    Note(72, 80, quarter * 7, quarter)
]

bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: F7 (F, A, C, Eb)
# Bar 3: A7 (A, C, E, G)
# Bar 4: D7 (D, F, A, C)

# Bar 2: F7 on beat 2
f7_notes = [
    Note(70, 100, quarter * 1, eighth),  # F
    Note(72, 100, quarter * 1, eighth),  # A
    Note(74, 100, quarter * 1, eighth),  # C
    Note(69, 100, quarter * 1, eighth)   # Eb
]

# Bar 3: A7 on beat 2
a7_notes = [
    Note(72, 100, quarter * 3, eighth),  # A
    Note(74, 100, quarter * 3, eighth),  # C
    Note(76, 100, quarter * 3, eighth),  # E
    Note(71, 100, quarter * 3, eighth)   # G
]

# Bar 4: D7 on beat 2
d7_notes = [
    Note(74, 100, quarter * 5, eighth),  # D
    Note(72, 100, quarter * 5, eighth),  # F
    Note(76, 100, quarter * 5, eighth),  # A
    Note(74, 100, quarter * 5, eighth)   # C
]

piano.notes.extend(f7_notes)
piano.notes.extend(a7_notes)
piano.notes.extend(d7_notes)

# Saxophone: Motif – starts with a question, leaves space
# F, Eb, D, Bb – ascending chromatic line with a pause

sax_notes = [
    Note(70, 100, 0, eighth),    # F
    Note(69, 100, eighth, eighth), # Eb
    Note(71, 100, quarter, eighth), # D
    Note(70, 100, quarter + eighth, eighth), # Bb
]

sax.notes.extend(sax_notes)

# Bar 3: Drums continue
# Kick on 1 and 3, snare on 2 and 4, hihat on all eighths
kick = Note(35, 100, quarter * 2, quarter)
snare = Note(38, 100, quarter * 2 + eighth, quarter)
hihat = Note(42, 80, quarter * 2, eighth)

drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Bar 4: Drums continue
kick = Note(35, 100, quarter * 4, quarter)
snare = Note(38, 100, quarter * 4 + eighth, quarter)
hihat = Note(42, 80, quarter * 4, eighth)

drums.notes.append(kick)
drums.notes.append(snare)
drums.notes.append(hihat)

# Save the MIDI file
midi.write("dante_intro.mid")
print("MIDI file saved as 'dante_intro.mid'")
