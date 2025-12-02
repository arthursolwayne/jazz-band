
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the key and time signature
pm.time_signature_changes[0].numerator = 4
pm.time_signature_changes[0].denominator = 4

# Define the instruments
# Bass (Marcus)
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = Instrument(program=bass_program, is_drum=False)
pm.instruments.append(bass)

# Piano (Diane)
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = Instrument(program=piano_program, is_drum=False)
pm.instruments.append(piano)

# Drums (Little Ray)
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
drums = Instrument(program=drums_program, is_drum=True)
pm.instruments.append(drums)

# Tenor Sax (You)
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = Instrument(program=sax_program, is_drum=False)
pm.instruments.append(sax)

# Define the tempo and note values
BPM = 160
beat = 60.0 / BPM  # seconds per beat
bar = beat * 4  # seconds per bar

# Bar 1: Drums only — build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time: 0.0s - 1.5s

# Kick on 1
drums.notes.append(Note(36, 60, 0.0, 0.375))  # Kick
# Snare on 2
drums.notes.append(Note(38, 60, 0.75, 0.375))  # Snare
# Hihat on 1
drums.notes.append(Note(42, 64, 0.0, 0.375))  # Hihat
# Hihat on 2
drums.notes.append(Note(42, 64, 0.75, 0.375))  # Hihat
# Kick on 3
drums.notes.append(Note(36, 60, 1.125, 0.375))  # Kick
# Snare on 4
drums.notes.append(Note(38, 60, 1.5, 0.375))  # Snare
# Hihat on 3
drums.notes.append(Note(42, 64, 1.125, 0.375))  # Hihat
# Hihat on 4
drums.notes.append(Note(42, 64, 1.5, 0.375))  # Hihat

# Bar 2: Everyone comes in — sax starts the melody
# Time: 1.5s - 3.0s

# Saxophone (You) — short motif starting with a question or challenge
# Fm7 chord: F, Ab, Bb, D
# Motif: F, Ab, Bb, F (melodic question)
note_duration = 0.375  # quarter note
note_start = 1.5

sax.notes.append(Note(84, 84, note_start, note_start + note_duration))   # F
sax.notes.append(Note(81, 81, note_start + note_duration, note_start + 2 * note_duration))  # Ab
sax.notes.append(Note(82, 82, note_start + 2 * note_duration, note_start + 3 * note_duration))  # Bb
sax.notes.append(Note(84, 84, note_start + 3 * note_duration, note_start + 4 * note_duration))  # F

# Bass (Marcus) — walking line in Fm with chromatic approaches
# Fm: F, Ab, Bb, D
# Walking line: F, Gb, Ab, A, Bb, B, C, Db, D, Eb, F...

bass_notes = [
    (53, 53, 1.5, 1.875),  # F
    (52, 52, 1.875, 2.25),  # Gb (chromatic)
    (51, 51, 2.25, 2.625),  # Ab
    (53, 53, 2.625, 3.0),   # A (chromatic approach)
]

for pitch, velocity, start, end in bass_notes:
    bass.notes.append(Note(pitch, velocity, start, end))

# Piano (Diane) — comping on 2 and 4
# Fm7 = F, Ab, Bb, D
# On 2 and 4

piano_notes = [
    (53, 80, 2.25, 2.625),  # F
    (60, 80, 2.25, 2.625),  # Ab
    (62, 80, 2.25, 2.625),  # Bb
    (56, 80, 2.25, 2.625),  # D
    (53, 80, 3.0, 3.375),   # F
    (60, 80, 3.0, 3.375),   # Ab
    (62, 80, 3.0, 3.375),   # Bb
    (56, 80, 3.0, 3.375),   # D
]

for pitch, velocity, start, end in piano_notes:
    piano.notes.append(Note(pitch, velocity, start, end))

# Drums — continue the pattern
# Kick on 1
drums.notes.append(Note(36, 60, 3.0, 3.375))  # Kick
# Snare on 2
drums.notes.append(Note(38, 60, 3.375, 3.75))  # Snare
# Hihat on 1
drums.notes.append(Note(42, 64, 3.0, 3.375))  # Hihat
# Hihat on 2
drums.notes.append(Note(42, 64, 3.375, 3.75))  # Hihat
# Kick on 3
drums.notes.append(Note(36, 60, 3.75, 4.125))  # Kick
# Snare on 4
drums.notes.append(Note(38, 60, 4.125, 4.5))  # Snare
# Hihat on 3
drums.notes.append(Note(42, 64, 3.75, 4.125))  # Hihat
# Hihat on 4
drums.notes.append(Note(42, 64, 4.125, 4.5))  # Hihat

# Bar 3: Continue the melody and support
# Time: 3.0s - 4.5s

# Saxophone (You) — repeat the opening motif, but with a slight variation
note_start = 3.0

sax.notes.append(Note(84, 84, note_start, note_start + note_duration))   # F
sax.notes.append(Note(81, 81, note_start + note_duration, note_start + 2 * note_duration))  # Ab
sax.notes.append(Note(82, 82, note_start + 2 * note_duration, note_start + 3 * note_duration))  # Bb
sax.notes.append(Note(84, 84, note_start + 3 * note_duration, note_start + 4 * note_duration))  # F

# Bass (Marcus) — continue the walking line
bass_notes = [
    (54, 54, 3.0, 3.375),    # A (chromatic)
    (55, 55, 3.375, 3.75),   # B (chromatic)
    (57, 57, 3.75, 4.125),   # C (chromatic)
    (52, 52, 4.125, 4.5),    # Db (chromatic)
]

for pitch, velocity, start, end in bass_notes:
    bass.notes.append(Note(pitch, velocity, start, end))

# Piano (Diane) — continue comping on 2 and 4
piano_notes = [
    (53, 80, 3.75, 4.125),   # F
    (60, 80, 3.75, 4.125),   # Ab
    (62, 80, 3.75, 4.125),   # Bb
    (56, 80, 3.75, 4.125),   # D
    (53, 80, 4.5, 4.875),    # F
    (60, 80, 4.5, 4.875),    # Ab
    (62, 80, 4.5, 4.875),    # Bb
    (56, 80, 4.5, 4.875),    # D
]

for pitch, velocity, start, end in piano_notes:
    piano.notes.append(Note(pitch, velocity, start, end))

# Drums — continue the pattern
# Kick on 1
drums.notes.append(Note(36, 60, 4.5, 4.875))  # Kick
# Snare on 2
drums.notes.append(Note(38, 60, 4.875, 5.25))  # Snare
# Hihat on 1
drums.notes.append(Note(42, 64, 4.5, 4.875))  # Hihat
# Hihat on 2
drums.notes.append(Note(42, 64, 4.875, 5.25))  # Hihat
# Kick on 3
drums.notes.append(Note(36, 60, 5.25, 5.625))  # Kick
# Snare on 4
drums.notes.append(Note(38, 60, 5.625, 6.0))  # Snare
# Hihat on 3
drums.notes.append(Note(42, 64, 5.25, 5.625))  # Hihat
# Hihat on 4
drums.notes.append(Note(42, 64, 5.625, 6.0))  # Hihat

# Bar 4: End on a strong, unresolved chord, leaving the story hanging
# Time: 4.5s - 6.0s

# Saxophone (You) — end with the first note of the motif again, leaving it open
note_start = 4.5
sax.notes.append(Note(84, 84, note_start, note_start + note_duration))   # F

# Bass (Marcus) — continue the walking line with a resolution
bass_notes = [
    (58, 58, 4.5, 4.875),    # D (chromatic)
    (53, 53, 4.875, 5.25),   # F
    (60, 60, 5.25, 5.625),   # Ab
    (62, 62, 5.625, 6.0),    # Bb
]

for pitch, velocity, start, end in bass_notes:
    bass.notes.append(Note(pitch, velocity, start, end))

# Piano (Diane) — comping on 2 and 4
piano_notes = [
    (53, 80, 5.25, 5.625),   # F
    (60, 80, 5.25, 5.625),   # Ab
    (62, 80, 5.25, 5.625),   # Bb
    (56, 80, 5.25, 5.625),   # D
    (53, 80, 5.625, 6.0),    # F
]

for pitch, velocity, start, end in piano_notes:
    piano.notes.append(Note(pitch, velocity, start, end))

# Save the MIDI file
pm.write("dante_russo_intro.mid")
