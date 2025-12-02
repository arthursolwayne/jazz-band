
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Set the key to F minor (Fm)
pm.key_signature_changes = [pretty_midi.KeySignature(5, 0)]  # 5 = F minor

# Define the time per bar (1.5 seconds at 160 BPM)
time_per_bar = 1.5

# Define the tempo in beats per minute
tempo = 160

# Create instruments
drums_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

drums = pretty_midi.Instrument(program=drums_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
sax = pretty_midi.Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Define note durations (in seconds)
beat = 0.375  # 60 / 160
eighth = beat / 2
quarter = beat * 2
half = beat * 4

# --- BAR 1: Little Ray (Drums) ---
# Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
# But with subtle variation in space and timing

# Bar 1: Kick on 1 & 3, snare on 2 & 4, hihat on every eighth
# Slight delay on hihat to create tension

# Kick
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5))

# Snare
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875))

# Hihat (slightly off-time to create tension)
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0 + 0.03, end=0 + 0.06))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.375 + 0.03, end=0.375 + 0.06))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=0.75 + 0.03, end=0.75 + 0.06))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.125 + 0.03, end=1.125 + 0.06))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.5 + 0.03, end=1.5 + 0.06))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=42, start=1.875 + 0.03, end=1.875 + 0.06))

# --- BAR 2: Bass (Marcus) - Walking line with chromatic motion ---
# Fm scale: F, Gb, Ab, Bb, B, Db, Eb

# Walking bass line in Fm
# Bass line: F -> Gb -> Ab -> Bb -> B -> Db -> Eb -> F
# Start at 1.5s

bass_notes = [
    (1.5, 71),  # F
    (1.875, 69),  # Gb
    (2.25, 67),  # Ab
    (2.625, 65),  # Bb
    (3.0, 66),  # B
    (3.375, 64),  # Db
    (3.75, 62),  # Eb
    (4.125, 71)  # F
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# --- BAR 2: Piano (Diane) - 7th chords on 2 and 4 with tension ---
# Fm7: F, Ab, Bb, Db
# F7: F, Ab, Bb, C
# Cm7: C, Eb, F, Gb
# Gbm7: Gb, Bb, Db, Eb

# Comp on 2 and 4
piano_notes = []

# Bar 2, beat 2 (1.875s)
# Fm7 (F, Ab, Bb, Db)
piano_notes.append((1.875, 71))
piano_notes.append((1.875, 67))
piano_notes.append((1.875, 65))
piano_notes.append((1.875, 64))

# Bar 2, beat 4 (2.625s)
# F7 (F, Ab, Bb, C)
piano_notes.append((2.625, 71))
piano_notes.append((2.625, 67))
piano_notes.append((2.625, 65))
piano_notes.append((2.625, 60))

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# --- BAR 2: Sax (You) - Start the motif. First phrase ---
# Motif: F (71), Ab (67), rest, Bb (65)
# Start at 1.5s, end at 1.5 + 0.75 (beat 1.5 to 2.25)

sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + eighth))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5 + quarter, end=1.5 + quarter + eighth))

# --- BAR 3: Bass (Marcus) - Continue walking line, chromatic approach ---
# B -> C -> Db -> Eb -> F -> Gb -> Ab -> Bb

bass_notes = [
    (4.5, 66),  # B
    (4.875, 60),  # C
    (5.25, 64),  # Db
    (5.625, 62),  # Eb
    (6.0, 71),  # F
    (6.375, 69),  # Gb
    (6.75, 67),  # Ab
    (7.125, 65)  # Bb
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# --- BAR 3: Piano (Diane) - 7th chords on 2 and 4 with tension ---
# Cm7 (C, Eb, F, Gb)
# Gbm7 (Gb, Bb, Db, Eb)

# Comp on 2 and 4
piano_notes = []

# Bar 3, beat 2 (4.875s)
# Cm7 (C, Eb, F, Gb)
piano_notes.append((4.875, 60))
piano_notes.append((4.875, 64))
piano_notes.append((4.875, 71))
piano_notes.append((4.875, 69))

# Bar 3, beat 4 (5.625s)
# Gbm7 (Gb, Bb, Db, Eb)
piano_notes.append((5.625, 69))
piano_notes.append((5.625, 65))
piano_notes.append((5.625, 64))
piano_notes.append((5.625, 62))

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# --- BAR 3: Sax (You) - Second phrase of motif, leave it hanging ---
# Bb (65), rest, Ab (67), rest, F (71)
# Start at 4.5s, end at 4.5 + 0.75 (beat 4.5 to 5.25)

sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.5 + eighth))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.5 + quarter, end=4.5 + quarter + eighth))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5 + 2 * quarter, end=4.5 + 2 * quarter + eighth))

# --- BAR 4: Bass (Marcus) - Walking line, chromatic approach ---
# Bb -> B -> C -> Db -> Eb -> F -> Gb -> Ab

bass_notes = [
    (7.5, 65),  # Bb
    (7.875, 66),  # B
    (8.25, 60),  # C
    (8.625, 64),  # Db
    (9.0, 62),  # Eb
    (9.375, 71),  # F
    (9.75, 69),  # Gb
    (10.125, 67)  # Ab
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# --- BAR 4: Piano (Diane) - 7th chords on 2 and 4 with tension ---
# Abm7 (Ab, Bb, Db, Eb)
# F7 (F, Ab, Bb, C)

# Comp on 2 and 4
piano_notes = []

# Bar 4, beat 2 (7.875s)
# Abm7 (Ab, Bb, Db, Eb)
piano_notes.append((7.875, 67))
piano_notes.append((7.875, 65))
piano_notes.append((7.875, 64))
piano_notes.append((7.875, 62))

# Bar 4, beat 4 (8.625s)
# F7 (F, Ab, Bb, C)
piano_notes.append((8.625, 71))
piano_notes.append((8.625, 67))
piano_notes.append((8.625, 65))
piano_notes.append((8.625, 60))

for start, pitch in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + 0.375))

# --- BAR 4: Sax (You) - Final phrase, end on a question ---
# F (71), rest, Ab (67), rest, Bb (65), rest, end with silence

sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=7.5, end=7.5 + eighth))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=7.5 + quarter, end=7.5 + quarter + eighth))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=7.5 + 2 * quarter, end=7.5 + 2 * quarter + eighth))

# Write the MIDI file
pm.write("dante_russo_intro.mid")
