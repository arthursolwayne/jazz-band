
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Create instruments
drums_program = pretty_midi.programs.Program(0)  # Drums
bass_program = pretty_midi.programs.Program(33)  # Electric Bass
piano_program = pretty_midi.programs.Program(0)  # Acoustic Piano
sax_program = pretty_midi.programs.Program(64)   # Tenor Sax

drums = pretty_midi.Instrument(program=0)
bass = pretty_midi.Instrument(program=33)
piano = pretty_midi.Instrument(program=0)
sax = pretty_midi.Instrument(program=64)

pm.instruments = [drums, bass, piano, sax]

# Function to create a note
def note(note_number, start, end, velocity=100):
    n = pretty_midi.Note(velocity=velocity, pitch=note_number, start=start, end=end)
    return n

# Time in seconds (6 seconds total)
time_per_bar = 1.5  # 160 BPM, 4/4 time => 1.5s per bar
time_per_beat = 0.375  # 1.5s / 4 beats

# BAR 1: Drums — sparse, deliberate
# Kick on 1 and 3, snare on 2 and 4
# Hihat on every 8th note, but soft and distant

# Kick on beat 1
drums.notes.append(note(36, 0.0, 0.1, velocity=90))  # C2, kick
drums.notes.append(note(36, time_per_beat * 2, 0.1 + time_per_beat * 2, velocity=90))

# Snare on beat 2 and 4
drums.notes.append(note(38, time_per_beat, 0.1 + time_per_beat, velocity=70))  # Snare
drums.notes.append(note(38, time_per_beat * 3, 0.1 + time_per_beat * 3, velocity=70))

# Hihat on every 8th (very soft, almost not there)
for i in range(8):
    time = i * time_per_beat / 2
    drums.notes.append(note(42, time, time + 0.05, velocity=60))

# BAR 2: Full ensemble — sax begins

# Tenor Sax (You) — short motif, no scale runs, just a phrase that sings
# D, E, F#, B (scale degrees 1, 2, 3, 7) — but with a twist

# First note: D4 (62) at beat 1 (0.375s)
sax.notes.append(note(62, 0.375, 0.375 + 0.15, velocity=100))  # D4
sax.notes.append(note(64, 0.375 + 0.15, 0.375 + 0.3, velocity=90))  # E4
sax.notes.append(note(66, 0.375 + 0.3, 0.375 + 0.45, velocity=80))  # F#4
sax.notes.append(note(69, 0.375 + 0.45, 0.375 + 0.6, velocity=100))  # B4

# Let it hang — no resolution on the first bar

# Bass (Marcus) — chromatic walking line
# From D2 (50) to F#2 (60) – chromatic approach
notes = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60]
for i, note_num in enumerate(notes):
    start = 0.375 + i * 0.15
    end = start + 0.15
    bass.notes.append(note(note_num, start, end, velocity=80))

# Piano (Diane) — 7th chords, comp on 2 and 4
# D7: D, F#, A, C
# Cmaj7: C, E, G, B
# Start on beat 2 and beat 4

# Beat 2 (time = 0.75s)
piano.notes.append(note(62, 0.75, 0.9, velocity=85))  # D
piano.notes.append(note(67, 0.75, 0.9, velocity=85))  # A
piano.notes.append(note(64, 0.75, 0.9, velocity=85))  # F#
piano.notes.append(note(60, 0.75, 0.9, velocity=85))  # C

# Beat 4 (time = 1.5s)
piano.notes.append(note(60, 1.5, 1.7, velocity=85))  # C
piano.notes.append(note(65, 1.5, 1.7, velocity=85))  # G
piano.notes.append(note(67, 1.5, 1.7, velocity=85))  # B
piano.notes.append(note(64, 1.5, 1.7, velocity=85))  # E

# BAR 3: Full ensemble — sax continues with motif variation

# Second motif, starting at beat 1 of bar 2 (0.375s) — shifted up slightly
# D4 -> E4 -> F#4 -> C4 (melodic variation, no resolution)
sax.notes.append(note(64, 0.375 + 1.5, 0.375 + 1.5 + 0.15, velocity=100))
sax.notes.append(note(66, 0.375 + 1.5 + 0.15, 0.375 + 1.5 + 0.3, velocity=90))
sax.notes.append(note(69, 0.375 + 1.5 + 0.3, 0.375 + 1.5 + 0.45, velocity=80))
sax.notes.append(note(60, 0.375 + 1.5 + 0.45, 0.375 + 1.5 + 0.6, velocity=100))

# Bass continues chromatic walking line
# From F#2 (60) to A2 (65)
notes = [60, 61, 62, 63, 64, 65]
for i, note_num in enumerate(notes):
    start = 0.375 + 1.5 + i * 0.15
    end = start + 0.15
    bass.notes.append(note(note_num, start, end, velocity=80))

# Piano (Diane) — 7th chords again, but this time with a twist
# A7: A, C#, E, G
# D7: D, F#, A, C

# Beat 2 (time = 0.75s + 1.5s = 2.25s)
piano.notes.append(note(69, 2.25, 2.4, velocity=85))  # A
piano.notes.append(note(71, 2.25, 2.4, velocity=85))  # C#
piano.notes.append(note(74, 2.25, 2.4, velocity=85))  # E
piano.notes.append(note(71, 2.25, 2.4, velocity=85))  # G

# Beat 4 (time = 1.5s + 1.5s = 3.0s)
piano.notes.append(note(62, 3.0, 3.2, velocity=85))  # D
piano.notes.append(note(67, 3.0, 3.2, velocity=85))  # A
piano.notes.append(note(64, 3.0, 3.2, velocity=85))  # F#
piano.notes.append(note(60, 3.0, 3.2, velocity=85))  # C

# BAR 4: Full ensemble — sax ends the phrase with new tension

# Third motif — D4 -> F#4 -> B4 -> G4 — unresolved, leaving tension
sax.notes.append(note(62, 0.375 + 3.0, 0.375 + 3.0 + 0.15, velocity=100))
sax.notes.append(note(66, 0.375 + 3.0 + 0.15, 0.375 + 3.0 + 0.3, velocity=90))
sax.notes.append(note(69, 0.375 + 3.0 + 0.3, 0.375 + 3.0 + 0.45, velocity=80))
sax.notes.append(note(71, 0.375 + 3.0 + 0.45, 0.375 + 3.0 + 0.6, velocity=100))

# Bass continues with chromatic walking
# From A2 (65) to C3 (67)
notes = [65, 66, 67]
for i, note_num in enumerate(notes):
    start = 0.375 + 3.0 + i * 0.15
    end = start + 0.15
    bass.notes.append(note(note_num, start, end, velocity=80))

# Piano — last 7th chord: G7 (G, B, D, F) on beat 4 (time = 3.0s + 1.5s = 4.5s)
piano.notes.append(note(71, 4.5, 4.7, velocity=85))  # G
piano.notes.append(note(76, 4.5, 4.7, velocity=85))  # B
piano.notes.append(note(74, 4.5, 4.7, velocity=85))  # D
piano.notes.append(note(71, 4.5, 4.7, velocity=85))  # F

# Add the instruments back to the MIDI file
pm.instruments = [drums, bass, piano, sax]

# Save the MIDI file
pm.write("dante_russo_intro.mid")
