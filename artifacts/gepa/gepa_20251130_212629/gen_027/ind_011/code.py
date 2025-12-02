
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key: F minor (F, Gb, Ab, Bb, C, Db, Eb)
# We'll use F minor as the key center

# Create instruments
bass_program = Program(program=33)  # Electric Bass
piano_program = Program(program=0)  # Acoustic Grand Piano
drums_program = Program(program=10)  # Acoustic Drums
sax_program = Program(program=64)   # Tenor Saxophone

# Create instruments
bass_instrument = Instrument(program=bass_program)
piano_instrument = Instrument(program=piano_program)
drums_instrument = Instrument(program=drums_program)
sax_instrument = Instrument(program=sax_program)

pm.instruments.append(bass_instrument)
pm.instruments.append(piano_instrument)
pm.instruments.append(drums_instrument)
pm.instruments.append(sax_instrument)

# Set the tempo
pm.tempo_changes = []

# --- DRUMS: Little Ray (Bar 1: 4/4, kick on 1, 3; snare on 2, 4; hihat on every 8th) ---
# Bar 1: 4/4, kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Calculate beat duration in seconds: 60 / 160 = 0.375s per beat
beat = 0.375

# Bar 1 (0.0 - 1.5s)
drum_notes = [
    Note(36, 0.0, 0.375),  # Kick on beat 1
    Note(38, 0.375, 0.375),  # Snare on beat 2
    Note(36, 0.75, 0.375),  # Kick on beat 3
    Note(38, 1.125, 0.375),  # Snare on beat 4
    Note(42, 0.0, 0.1875),  # Hihat on 1
    Note(42, 0.1875, 0.1875),
    Note(42, 0.375, 0.1875),
    Note(42, 0.5625, 0.1875),
    Note(42, 0.75, 0.1875),
    Note(42, 0.9375, 0.1875),
    Note(42, 1.125, 0.1875),
    Note(42, 1.3125, 0.1875),
]

for note in drum_notes:
    dr = Note(note.pitch, note.start, note.end)
    drums_instrument.notes.append(dr)

# --- BASS: Marcus (Walking line with chromatic approaches, no repeated notes) ---
# Fm7 = F, Ab, Bb, Db
# Walking line in F minor: F, Gb, Ab, A, Bb, C, Db, D

# Bar 1: F - Gb - Ab - A
# Bar 2: Bb - C - Db - D
# Bar 3: Eb - F - Gb - Ab
# Bar 4: Bb - C - Db - D

bass_notes = [
    Note(71, 0.0, 0.375),  # F
    Note(69, 0.375, 0.375),  # Gb
    Note(70, 0.75, 0.375),  # Ab
    Note(71, 1.125, 0.375),  # A

    Note(72, 1.5, 0.375),  # Bb
    Note(74, 1.875, 0.375),  # C
    Note(73, 2.25, 0.375),  # Db
    Note(75, 2.625, 0.375),  # D

    Note(67, 3.0, 0.375),  # Eb
    Note(71, 3.375, 0.375),  # F
    Note(69, 3.75, 0.375),  # Gb
    Note(70, 4.125, 0.375),  # Ab

    Note(72, 4.5, 0.375),  # Bb
    Note(74, 4.875, 0.375),  # C
    Note(73, 5.25, 0.375),  # Db
    Note(75, 5.625, 0.375),  # D
]

for note in bass_notes:
    bass_instrument.notes.append(note)

# --- PIANO: Diane (Comp on 2 and 4 with 7th chords) ---
# Fm7: F, Ab, Bb, Db
# F7: F, Ab, Bb, C

# Bars 2 and 4
# Bar 2: F7 at beat 2
# Bar 4: F7 at beat 4

piano_notes = [
    # Bar 1: No comp
    # Bar 2: F7 on beat 2
    Note(71, 1.875, 0.1875),  # F
    Note(69, 1.875, 0.1875),  # Ab
    Note(72, 1.875, 0.1875),  # Bb
    Note(74, 1.875, 0.1875),  # C

    # Bar 3: No comp
    # Bar 4: F7 on beat 4
    Note(71, 4.875, 0.1875),  # F
    Note(69, 4.875, 0.1875),  # Ab
    Note(72, 4.875, 0.1875),  # Bb
    Note(74, 4.875, 0.1875),  # C
]

for note in piano_notes:
    piano_instrument.notes.append(note)

# --- SAX: YOU (Tenor Sax — your motif) ---
# Motif: F - Gb - Ab - Bb (Fm7), but with dynamics and space
# You start it, leave it hanging — let the question linger

sax_notes = [
    Note(71, 1.5, 0.1875),  # F (start on beat 1 of bar 2)
    Note(69, 1.6875, 0.1875),  # Gb
    Note(70, 1.875, 0.1875),  # Ab
    Note(72, 2.0625, 0.1875),  # Bb
    Note(71, 2.4375, 0.1875),  # F (return on beat 3 of bar 2)
    Note(69, 2.625, 0.1875),  # Gb
    Note(70, 2.8125, 0.1875),  # Ab
    Note(72, 3.0, 0.1875),  # Bb
    Note(71, 3.375, 0.1875),  # F (start of bar 3)
    Note(69, 3.5625, 0.1875),  # Gb
    Note(70, 3.75, 0.1875),  # Ab
    Note(72, 3.9375, 0.1875),  # Bb
    Note(71, 4.3125, 0.1875),  # F (last note — ends on a question)
]

for note in sax_notes:
    sax_instrument.notes.append(note)

# Add dynamic variations
# We'll manually set velocities to create tension and release
# (Note: PrettyMIDI doesn't support velocity changes via Note object directly,
# but we can use a workaround or export to MIDI and edit in DAW, but we'll simulate it here.)

# Example: Set dynamics for the sax
for i, note in enumerate(sax_instrument.notes):
    if i < 4:
        note.velocity = 60  # soft start (F, Gb, Ab, Bb)
    elif i < 8:
        note.velocity = 80  # mid-range
    elif i < 12:
        note.velocity = 65  # slightly softer
    else:
        note.velocity = 60  # end with a question — soft and unresolved

# Save the MIDI file
pm.write('dante_intro.mid')
print("MIDI file saved as 'dante_intro.mid'")
