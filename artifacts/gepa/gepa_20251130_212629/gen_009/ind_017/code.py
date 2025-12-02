
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set the time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Set the key (Fm) — F minor
pm.key_signature_changes = [pretty_midi.KeySignature(key_number=21, time=0)]

# Create instruments for each player
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
piano_program = pretty_midi.instrument_name_to_program('Electric Piano 1')
drums_program = pretty_midi.instrument_name_to_program('Drums')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = Instrument(program=bass_program)
piano = Instrument(program=piano_program)
drums = Instrument(program=drums_program)
sax = Instrument(program=sax_program)

pm.instruments = [drums, bass, piano, sax]

# Define note durations in seconds
beat = 0.375  # 160 BPM → 60 / 160 = 0.375s per beat
bar = 1.5  # 4 beats per bar

# ---------------------------
# BAR 1: Little Ray (Drums) — Set it up. Make them wait.
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Start at time 0.0

# Kick on beat 0 (1)
drums.notes.append(Note(60, 100, 0.0, 0.375))
# Kick on beat 2 (3)
drums.notes.append(Note(60, 100, 0.75, 1.125))
# Snare on beat 1 (2)
drums.notes.append(Note(62, 100, 0.375, 0.75))
# Snare on beat 3 (4)
drums.notes.append(Note(62, 100, 1.125, 1.5))
# Hihat on every eighth note
drums.notes.extend([
    Note(42, 60, 0.0, 0.1875),
    Note(42, 60, 0.1875, 0.375),
    Note(42, 60, 0.375, 0.5625),
    Note(42, 60, 0.5625, 0.75),
    Note(42, 60, 0.75, 0.9375),
    Note(42, 60, 0.9375, 1.125),
    Note(42, 60, 1.125, 1.3125),
    Note(42, 60, 1.3125, 1.5)
])

# ---------------------------
# BAR 2: Everyone in. Tenor sax starts the melody.

# Tenor Sax — One short motif that sings and leaves it hanging
# Fm scale: F, Gb, Ab, A, Bb, B, Db
# Motif: F (Ab) -> A (Db) -> Bb (F) -> Ab (Gb)

# Bar 2: Start motif on beat 1 (time 1.5)
sax.notes.append(Note(65, 105, 1.5, 1.875))  # F (Ab)
sax.notes.append(Note(68, 105, 1.875, 2.25))  # A (Db)
sax.notes.append(Note(67, 105, 2.25, 2.625))  # Bb (F)
sax.notes.append(Note(68, 105, 2.625, 3.0))   # Ab (Gb)

# ---------------------------
# Bar 2: Bass — Walking line in Fm (chromatic approach)
# Fm key: F, Gb, Ab, A, Bb, B, Db
# Walking line: F (Gb) -> Ab (A) -> Bb (B) -> Db (F)
# Time: 1.5 to 1.875 (beat 1), etc.

bass.notes.append(Note(65, 80, 1.5, 1.875))   # F
bass.notes.append(Note(66, 80, 1.875, 2.25))  # Gb
bass.notes.append(Note(68, 80, 2.25, 2.625))  # Ab
bass.notes.append(Note(69, 80, 2.625, 3.0))   # A

# ---------------------------
# Bar 2: Piano — 7th chords on 2 & 4
# Fm7 = F, Ab, Bb, Db
# Time 1.875 (beat 2) and 3.0 (beat 4)

# Fm7: 1.875
piano.notes.extend([
    Note(65, 90, 1.875, 2.25),
    Note(68, 90, 1.875, 2.25),
    Note(67, 90, 1.875, 2.25),
    Note(69, 90, 1.875, 2.25)
])

# Fm7: 3.0
piano.notes.extend([
    Note(65, 90, 3.0, 3.375),
    Note(68, 90, 3.0, 3.375),
    Note(67, 90, 3.0, 3.375),
    Note(69, 90, 3.0, 3.375)
])

# ---------------------------
# BAR 3: Drums — same pattern (no change)
# BAR 3: Sax — repeat motif, this time finish it

# Bar 3: Start at time 3.0
sax.notes.append(Note(65, 105, 3.0, 3.375))  # F (Ab)
sax.notes.append(Note(68, 105, 3.375, 3.75))  # A (Db)
sax.notes.append(Note(67, 105, 3.75, 4.125))  # Bb (F)
sax.notes.append(Note(66, 105, 4.125, 4.5))   # Gb (Ab)

# ---------------------------
# BAR 3: Bass — Walk again
bass.notes.append(Note(66, 80, 3.0, 3.375))   # Gb
bass.notes.append(Note(68, 80, 3.375, 3.75))  # Ab
bass.notes.append(Note(69, 80, 3.75, 4.125))  # A
bass.notes.append(Note(67, 80, 4.125, 4.5))   # Bb

# ---------------------------
# BAR 3: Piano — 7th chords again
piano.notes.extend([
    Note(65, 90, 3.375, 3.75),
    Note(68, 90, 3.375, 3.75),
    Note(67, 90, 3.375, 3.75),
    Note(69, 90, 3.375, 3.75)
])

piano.notes.extend([
    Note(65, 90, 4.5, 4.875),
    Note(68, 90, 4.5, 4.875),
    Note(67, 90, 4.5, 4.875),
    Note(69, 90, 4.5, 4.875)
])

# ---------------------------
# BAR 4: Drums — same pattern, closing the 4-bar intro
# BAR 4: Bass — End on F
# Bar 4: Piano — End with Fm7

# Drums same as before (just copy-paste for now)

# Bass ends on F at 4.5
bass.notes.append(Note(65, 80, 4.5, 4.875))

# Piano ends with Fm7 at 4.5
piano.notes.extend([
    Note(65, 90, 4.5, 4.875),
    Note(68, 90, 4.5, 4.875),
    Note(67, 90, 4.5, 4.875),
    Note(69, 90, 4.5, 4.875)
])

# Save the MIDI file
pm.write("dante_introduction.mid")
