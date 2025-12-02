
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drums: kick=36, snare=38, hihat=42
# Define the notes for each instrument

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Subtle, textural, with space and variation
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=60, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=50, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4, with dynamic variation
    pretty_midi.Note(velocity=80, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=70, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth note, dynamic shading
    pretty_midi.Note(velocity=40, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=35, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=40, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=35, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=40, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=35, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=40, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=35, pitch=42, start=1.3125, end=1.5),
]

# Add the drum notes
for note in drums_notes:
    drums.notes.append(note)

# Bar 2: Saxophone motif (1.5 - 3.0s)
# A concise, emotional motif in Fm (F, Ab, Bb, Db, Eb)
# Start with a question, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F (65)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # Bb (60)
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Db (62)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Eb (64)
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F (65)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Ab (67)
]

# Add the sax notes
for note in sax_notes:
    sax.notes.append(note)

# Bar 2: Bass line (1.5 - 3.0s)
# Walking line with chromatic approaches, melodic phrasing
# Fm bass line: F, Eb, Db, C, Bb, Ab, G, F
# Note numbers: 65, 64, 62, 60, 60, 58, 57, 65
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=70, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=70, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=70, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=70, pitch=60, start=2.5, end=2.75),
    pretty_midi.Note(velocity=70, pitch=58, start=2.75, end=3.0),
    pretty_midi.Note(velocity=70, pitch=57, start=3.0, end=3.25),
    pretty_midi.Note(velocity=70, pitch=65, start=3.25, end=3.5),
]

# Add the bass notes
for note in bass_notes:
    bass.notes.append(note)

# Bar 2: Piano comping (1.5 - 3.0s)
# 7th chords, comp on 2 and 4, emotional tension in every chord
# F7 on 2 and 4
# F, A, C, Eb
# Note numbers: 65, 68, 72, 64
piano_notes = [
    # 2nd beat (1.75 - 2.0)
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=68, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # Eb
    # 4th beat (2.75 - 3.0)
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=68, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=72, start=2.75, end=3.0),
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),
]

# Add piano notes
for note in piano_notes:
    piano.notes.append(note)

# Bar 3 and 4: Continue the quartet
# Sax repeats the motif with a slight variation
# Bar 3 (3.0 - 4.5s)
sax_notes_2 = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),
]

# Add to sax
for note in sax_notes_2:
    sax.notes.append(note)

# Bar 3: Bass continues the walking line
bass_notes_2 = [
    pretty_midi.Note(velocity=70, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=70, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=70, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=70, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=70, pitch=60, start=4.0, end=4.25),
    pretty_midi.Note(velocity=70, pitch=58, start=4.25, end=4.5),
    pretty_midi.Note(velocity=70, pitch=57, start=4.5, end=4.75),
    pretty_midi.Note(velocity=70, pitch=65, start=4.75, end=5.0),
]

# Add to bass
for note in bass_notes_2:
    bass.notes.append(note)

# Bar 3 and 4: Piano continues the comping, adding tension
piano_notes_2 = [
    # 2nd beat (3.25 - 3.5)
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=68, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),
    # 4th beat (4.25 - 4.5)
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=68, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=72, start=4.25, end=4.5),
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),
    # Move to a Bbm7 on the last beat (4.5 - 5.0)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=5.0),  # Db
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=5.0),  # Ab
]

# Add to piano
for note in piano_notes_2:
    piano.notes.append(note)

# Add all instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("4_bar_intro.mid")
