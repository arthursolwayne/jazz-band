
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Set tempo and time signature
tempo = 160
time_signature = (4, 4)

# Create a new MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=tempo)

# Create a time signature change at the beginning
time_signature_change = pretty_midi.TimeSignatureChange(
    time=0.0,
    numerator=time_signature[0],
    denominator=time_signature[1]
)
midi.time_signature_changes = [time_signature_change]

# -------------------------------
# Create instruments
# -------------------------------

# Drums (Little Ray)
drums = Instrument(program=Program.DRUMS, is_drum=True)
midi.instruments.append(drums)

# Tenor Sax (Dante)
sax = Instrument(program=Program.SOPRANO_SAX, name="Tenor Sax")
midi.instruments.append(sax)

# Piano (Diane)
piano = Instrument(program=Program.PIANO, name="Piano")
midi.instruments.append(piano)

# Bass (Marcus)
bass = Instrument(program=Program.BASS, name="Bass")
midi.instruments.append(bass)

# -------------------------------
# Bar 1: Only Drums
# -------------------------------

# Time per bar = 60 / 160 * 4 = 1.5 seconds
bar_duration = 1.5
time = 0.0

# Drums: Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
# Bar 1: Just kick on 1 and 3

# Kick on 1
drum_kick = Note(36, 100, time, time + 0.1)
drums.notes.append(drum_kick)

# Kick on 3
drum_kick = Note(36, 100, time + 0.75, time + 0.85)
drums.notes.append(drum_kick)

# -------------------------------
# Bar 2 - 4: Full Ensemble
# -------------------------------
time = bar_duration

# Bass: Walking line, chromatic approaches
# F major scale: F, G, A, Bb, B, C, D
# Bass line: F -> G -> Ab -> Bb -> B -> C -> D -> Eb
# For 3 bars, we'll loop a walking pattern that's chromatic and subtle

bass_notes = [
    Note(44, 70, time, time + 0.375),  # F (low)
    Note(45, 70, time + 0.375, time + 0.75),  # G
    Note(43, 70, time + 0.75, time + 1.125),  # Ab
    Note(44, 70, time + 1.125, time + 1.5),  # Bb
    Note(45, 70, time + 1.5, time + 1.875),  # B
    Note(46, 70, time + 1.875, time + 2.25),  # C
    Note(47, 70, time + 2.25, time + 2.625),  # D
    Note(45, 70, time + 2.625, time + 3.0),  # Eb
    # Repeat for next bars
    Note(44, 70, time + 3.0, time + 3.375),
    Note(45, 70, time + 3.375, time + 3.75),
    Note(43, 70, time + 3.75, time + 4.125),
    Note(44, 70, time + 4.125, time + 4.5),
    Note(45, 70, time + 4.5, time + 4.875),
    Note(46, 70, time + 4.875, time + 5.25),
    Note(47, 70, time + 5.25, time + 5.625),
    Note(45, 70, time + 5.625, time + 6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
# F7 = F, A, C, E♭
# Chords on beats 2 and 4, with voicings that move

piano_notes = []

# Bar 2 (time = 1.5) — chord on beat 2 (1.5 + 0.75 = 2.25)
piano_notes.append(Note(60, 90, 2.25, 2.25 + 0.1))  # F
piano_notes.append(Note(64, 90, 2.25, 2.25 + 0.1))  # A
piano_notes.append(Note(65, 90, 2.25, 2.25 + 0.1))  # C
piano_notes.append(Note(62, 90, 2.25, 2.25 + 0.1))  # E♭

# Bar 2 — chord on beat 4 (time = 1.5 + 1.5 = 3.0)
piano_notes.append(Note(60, 90, 3.0, 3.0 + 0.1))
piano_notes.append(Note(64, 90, 3.0, 3.0 + 0.1))
piano_notes.append(Note(65, 90, 3.0, 3.0 + 0.1))
piano_notes.append(Note(62, 90, 3.0, 3.0 + 0.1))

# Bar 3 — chord on beat 2 (time = 3.0 + 0.75 = 3.75)
piano_notes.append(Note(60, 90, 3.75, 3.75 + 0.1))
piano_notes.append(Note(64, 90, 3.75, 3.75 + 0.1))
piano_notes.append(Note(65, 90, 3.75, 3.75 + 0.1))
piano_notes.append(Note(62, 90, 3.75, 3.75 + 0.1))

# Bar 3 — chord on beat 4 (time = 3.0 + 1.5 = 4.5)
piano_notes.append(Note(60, 90, 4.5, 4.5 + 0.1))
piano_notes.append(Note(64, 90, 4.5, 4.5 + 0.1))
piano_notes.append(Note(65, 90, 4.5, 4.5 + 0.1))
piano_notes.append(Note(62, 90, 4.5, 4.5 + 0.1))

# Bar 4 — chord on beat 2 (time = 4.5 + 0.75 = 5.25)
piano_notes.append(Note(60, 90, 5.25, 5.25 + 0.1))
piano_notes.append(Note(64, 90, 5.25, 5.25 + 0.1))
piano_notes.append(Note(65, 90, 5.25, 5.25 + 0.1))
piano_notes.append(Note(62, 90, 5.25, 5.25 + 0.1))

# Bar 4 — chord on beat 4 (time = 6.0)
piano_notes.append(Note(60, 90, 6.0, 6.0 + 0.1))
piano_notes.append(Note(64, 90, 6.0, 6.0 + 0.1))
piano_notes.append(Note(65, 90, 6.0, 6.0 + 0.1))
piano_notes.append(Note(62, 90, 6.0, 6.0 + 0.1))

for note in piano_notes:
    piano.notes.append(note)

# Drums: Full rhythm in Bars 2–4
# Kick on 1 & 3, snare on 2 & 4, hihat on every eighth

# Bar 2
drum_kick = Note(36, 100, time, time + 0.1)
drums.notes.append(drum_kick)
drum_snare = Note(38, 90, time + 0.75, time + 0.85)
drums.notes.append(drum_snare)
drum_hihat = Note(42, 60, time, time + 0.375)
drums.notes.append(drum_hihat)
drum_hihat = Note(42, 60, time + 0.375, time + 0.75)
drums.notes.append(drum_hihat)
drum_hihat = Note(42, 60, time + 0.75, time + 1.125)
drums.notes.append(drum_hihat)
drum_hihat = Note(42, 60, time + 1.125, time + 1.5)
drums.notes.append(drum_hihat)

# Bar 3
drum_kick = Note(36, 100, time + 1.5, time + 1.6)
drums.notes.append(drum_kick)
drum_snare = Note(38, 90, time + 2.25, time + 2.35)
drums.notes.append(drum_snare)
drum_hihat = Note(42, 60, time + 1.5, time + 1.875)
drums.notes.append(drum_hihat)
drum_hihat = Note(42, 60, time + 1.875, time + 2.25)
drums.notes.append(drum_hihat)
drum_hihat = Note(42, 60, time + 2.25, time + 2.625)
drums.notes.append(drum_hihat)
drum_hihat = Note(42, 60, time + 2.625, time + 3.0)
drums.notes.append(drum_hihat)

# Bar 4
drum_kick = Note(36, 100, time + 3.0, time + 3.1)
drums.notes.append(drum_kick)
drum_snare = Note(38, 90, time + 3.75, time + 3.85)
drums.notes.append(drum_snare)
drum_hihat = Note(42, 60, time + 3.0, time + 3.375)
drums.notes.append(drum_hihat)
drum_hihat = Note(42, 60, time + 3.375, time + 3.75)
drums.notes.append(drum_hihat)
drum_hihat = Note(42, 60, time + 3.75, time + 4.125)
drums.notes.append(drum_hihat)
drum_hihat = Note(42, 60, time + 4.125, time + 4.5)
drums.notes.append(drum_hihat)

# Tenor Sax Motif: Bar 2–4
# Start on F (65), play a simple melodic line that ends on a suspension or unresolved note

# Bar 2: F -> G -> E -> F (suspension of E)
note1 = Note(65, 100, time, time + 0.375)
note2 = Note(67, 100, time + 0.375, time + 0.75)
note3 = Note(62, 100, time + 0.75, time + 1.125)
note4 = Note(65, 100, time + 1.125, time + 1.5)
sax.notes.append(note1)
sax.notes.append(note2)
sax.notes.append(note3)
sax.notes.append(note4)

# Bar 3: Move the motif up a half step (G -> A -> F# -> G)
note5 = Note(67, 100, time + 1.5, time + 1.875)
note6 = Note(69, 100, time + 1.875, time + 2.25)
note7 = Note(64, 100, time + 2.25, time + 2.625)
note8 = Note(67, 100, time + 2.625, time + 3.0)
sax.notes.append(note5)
sax.notes.append(note6)
sax.notes.append(note7)
sax.notes.append(note8)

# Bar 4: Move it up again (A -> B -> G -> A), but end on B (a question)
note9 = Note(69, 100, time + 3.0, time + 3.375)
note10 = Note(71, 100, time + 3.375, time + 3.75)
note11 = Note(67, 100, time + 3.75, time + 4.125)
note12 = Note(71, 100, time + 4.125, time + 4.5)
sax.notes.append(note9)
sax.notes.append(note10)
sax.notes.append(note11)
sax.notes.append(note12)

# Add a final note that hangs — the question
note13 = Note(71, 100, time + 4.5, time + 6.0)
sax.notes.append(note13)

# Save the MIDI file
midi.write("dante_intro.mid")

print("MIDI file generated: dante_intro.mid")
