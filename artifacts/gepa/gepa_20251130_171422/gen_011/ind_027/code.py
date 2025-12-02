
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define key: F minor (F, Gb, Ab, Bb, Cb, Db, Eb)
# We'll use F minor, which is F, Gb, Ab, Bb, Cb, Db, Eb

# Create instruments
bass_program = Program(33)  # Acoustic Bass
piano_program = Program(0)   # Acoustic Grand Piano
drums_program = Program(0)   # Acoustic Grand Piano (we'll use percussion)
sax_program = Program(62)    # Tenor Saxophone

# Create instruments
bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

# Add instruments to MIDI
midi.instruments = [bass, piano, drums, sax]

# Time calculations
# 160 BPM, 4/4 time
# 1 bar = 6 seconds
# 1 beat = 0.375 seconds
# 1 eighth note = 0.1875 seconds

# TIME CONSTANTS
BAR_DURATION = 6.0
BEAT_DURATION = 0.375
EIGHTH_DURATION = 0.1875

# BAR 1: Little Ray (drums) alone
# Snare on 2 and 4, hihat on every eighth, kick on 1 and 3

# Kick on 1 and 3
drums.notes.append(Note(35, 60, 0.0, 0.1875))  # Kick on 1
drums.notes.append(Note(35, 60, 1.125, 0.1875))  # Kick on 3

# Snare on 2 and 4
drums.notes.append(Note(38, 64, 0.5625, 0.1875))  # Snare on 2
drums.notes.append(Note(38, 64, 1.875, 0.1875))  # Snare on 4

# HiHats on every eighth
for i in range(8):
    time = i * EIGHTH_DURATION
    drums.notes.append(Note(42, 60, time, 0.025))  # Open Hi-Hat

# BAR 2: Everyone enters

# BASS LINE: Walking line in F minor
# Fm key: F, Gb, Ab, Bb, Cb, Db, Eb
# Bass walks: F -> Gb -> Ab -> Bb -> Cb -> Db -> Eb -> F

bass_notes = [
    Note(34, 65, 2.0, 0.1875),  # F (65)
    Note(33, 66, 2.1875, 0.1875),  # Gb (66)
    Note(31, 68, 2.375, 0.1875),  # Ab (68)
    Note(30, 69, 2.5625, 0.1875),  # Bb (69)
    Note(29, 67, 2.75, 0.1875),   # Cb (67)
    Note(28, 68, 2.9375, 0.1875),  # Db (68)
    Note(27, 67, 3.125, 0.1875),   # Eb (67)
    Note(34, 65, 3.3125, 0.1875)   # F (65)
]
for note in bass_notes:
    bass.notes.append(note)

# PIANO: 7th chords on 2 and 4, comp on 2 and 4
# Chord progression: Fm7 -> Bb7 -> Eb7 -> Ab7 (but simplified for intro)

# 2nd beat: Fm7
piano_notes = [
    Note(60, 65, 2.5625, 0.1875),  # F (65)
    Note(62, 67, 2.5625, 0.1875),  # Ab (67)
    Note(64, 69, 2.5625, 0.1875),  # Cb (69)
    Note(65, 72, 2.5625, 0.1875)   # Db (72)
]
for note in piano_notes:
    piano.notes.append(note)

# 4th beat: Bb7
piano_notes = [
    Note(59, 69, 3.3125, 0.1875),  # Bb (69)
    Note(61, 71, 3.3125, 0.1875),  # Db (71)
    Note(64, 72, 3.3125, 0.1875),  # F (72)
    Note(66, 76, 3.3125, 0.1875)   # G (76)
]
for note in piano_notes:
    piano.notes.append(note)

# SAX: Tenor sax motif — sparse, emotional, searching
# Motif: F (65) -> Ab (68) -> Gb (66) -> rest

sax_notes = [
    Note(65, 65, 2.0, 0.1875),  # F
    Note(68, 68, 2.375, 0.1875),  # Ab
    Note(66, 66, 2.75, 0.1875),   # Gb
    Note(65, 65, 2.9375, 0.1875)  # F (repeated, but with space)
]

# Add rests and space between notes
# First note: F at 2.0
# Rest from 2.1875 to 2.375
# Then Ab at 2.375
# Rest from 2.5625 to 2.75
# Then Gb at 2.75
# Rest from 2.9375 to 3.125
# Then F again at 3.125

for note in sax_notes:
    sax.notes.append(note)

# Add a final note at the end of bar 4
sax.notes.append(Note(65, 65, 3.5, 0.1875))  # F (to resolve)

# Save the MIDI file
midi.write("jazz_intro_fm.mid")
