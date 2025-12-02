
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new MIDI file at 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax = Instrument(program=66)       # Saxophone
bass = Instrument(program=33)      # Bass
piano = Instrument(program=0)      # Piano
drums = Instrument(program=0, is_drum=True)  # Drums

# Add instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Bar 1: Little Ray (Drums) 0.0 - 1.5s
# Basic groove with kick, snare, hihat
drum_notes = [
    Note(velocity=100, start=0.0, end=0.25, pitch=36),  # Kick
    Note(velocity=100, start=0.5, end=0.75, pitch=38),  # Snare
    Note(velocity=80, start=0.0, end=1.5, pitch=42),    # Hi-Hat
    Note(velocity=100, start=1.0, end=1.25, pitch=36),  # Kick
    Note(velocity=100, start=1.5, end=1.75, pitch=38),  # Snare
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full Quartet (1.5 - 3.0s)

# Sax: Short melodic motif in F major
sax_notes = [
    Note(velocity=100, start=1.5, end=1.75, pitch=69),  # A
    Note(velocity=100, start=2.0, end=2.25, pitch=71),  # B
    Note(velocity=100, start=2.5, end=2.75, pitch=69),  # A
    Note(velocity=100, start=3.0, end=3.25, pitch=67),  # G
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking bass line in F major
bass_notes = [
    Note(velocity=100, start=1.5, end=1.75, pitch=71),  # F
    Note(velocity=100, start=1.75, end=2.0, pitch=70),  # E
    Note(velocity=100, start=2.0, end=2.25, pitch=72),  # F#
    Note(velocity=100, start=2.25, end=2.5, pitch=71),  # F
    Note(velocity=100, start=2.5, end=2.75, pitch=69),  # E
    Note(velocity=100, start=2.75, end=3.0, pitch=71),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Comping with 7th chords
piano_notes = [
    Note(velocity=80, start=1.5, end=1.75, pitch=69),  # A
    Note(velocity=80, start=1.5, end=1.75, pitch=64),  # F
    Note(velocity=80, start=1.5, end=1.75, pitch=67),  # G
    Note(velocity=80, start=1.5, end=1.75, pitch=71),  # B
    Note(velocity=80, start=2.0, end=2.25, pitch=65),  # F#
    Note(velocity=80, start=2.0, end=2.25, pitch=68),  # G#
    Note(velocity=80, start=2.0, end=2.25, pitch=72),  # C
    Note(velocity=80, start=2.0, end=2.25, pitch=74),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Continue groove (3.0 - 4.5s)
# Drums: repeat the same pattern
for note in drum_notes:
    note.start += 3.0
    note.end += 3.0
    drums.notes.append(note)

# Bar 4: End with a resolution (4.5 - 6.0s)
# Sax: Repeat the same motif
for note in sax_notes:
    note.start += 3.0
    note.end += 3.0
    sax.notes.append(note)

# Bass: Repeat the same walking line
for note in bass_notes:
    note.start += 3.0
    note.end += 3.0
    bass.notes.append(note)

# Piano: Resolve with a C7 chord (V7 in F major)
piano_notes_end = [
    Note(velocity=80, start=4.5, end=4.75, pitch=72),  # C
    Note(velocity=80, start=4.5, end=4.75, pitch=74),  # D
    Note(velocity=80, start=4.5, end=4.75, pitch=76),  # E
    Note(velocity=80, start=4.5, end=4.75, pitch=79),  # G
]

for note in piano_notes_end:
    piano.notes.append(note)

# Output the MIDI file
midi.write('jazz_quartet_in_f.mid')
