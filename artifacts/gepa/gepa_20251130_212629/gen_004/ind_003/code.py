
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define time signatures (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0)]

# Define the key signature (F major)
pm.key_signature_changes = [pretty_midi.KeySignature(0, 0)]  # F major, no accidental

# Define the duration of one beat in seconds (160 BPM = 0.375 seconds per beat)
beat = 0.375
bar_length = 4 * beat  # 1.5 seconds per bar

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
bass = Instrument(program=Program.BASS, name="Bass")
piano = Instrument(program=Program.ACOUSTIC_GRAND_PIANO, name="Piano")
sax = Instrument(program=Program.TENOR_SAX, name="Tenor Sax")

pm.instruments = [drums, bass, piano, sax]

# -------------------------------
# DRUMS: Bar 1 - Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 1 starts at time 0

# Bar 1 (0.0 - 1.5s)
# Kick on 1 and 3 (0.0 and 0.75)
drums.notes.append(Note(36, 100, 0.0, 0.0 + beat/2))
drums.notes.append(Note(36, 100, 0.75, 0.75 + beat/2))

# Snare on 2 and 4 (0.375 and 1.125)
drums.notes.append(Note(38, 100, 0.375, 0.375 + beat/2))
drums.notes.append(Note(38, 100, 1.125, 1.125 + beat/2))

# Hihat on every eighth (0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125)
for i in range(8):
    drums.notes.append(Note(42, 80, i * beat/4, i * beat/4 + beat/8))

# -------------------------------
# BASS: Bar 1 - Walking line, chromatic approaches, no repeating notes
# Bar 1 (0.0 - 1.5s) - start with F (70), then F# (71), G (72), G# (73), A (74), Bb (71), B (72), C (73)

bass_notes = [70, 71, 72, 73, 74, 71, 72, 73]
for i, note in enumerate(bass_notes):
    time = i * beat/4
    bass.notes.append(Note(note, 90, time, time + beat/4))

# -------------------------------
# PIANO: Bar 1 - Rest
# Bar 2 - 7th chords on 2 and 4, comp on 2 and 4
# Bar 2 - Time 1.5 to 3.0

# Bar 2 - 7th chords: C7 (C, E, G, Bb) on beat 2 and 4
# For simplicity, we'll play the 7th chord (C7) on beat 2 and 4
# C7 = 60 (C), 64 (E), 67 (G), 70 (Bb)

# Beat 2 (1.875s)
for note in [60, 64, 67, 70]:
    piano.notes.append(Note(note, 85, 1.875, 1.875 + beat/4))

# Beat 4 (3.0s)
for note in [60, 64, 67, 70]:
    piano.notes.append(Note(note, 85, 3.0, 3.0 + beat/4))

# -------------------------------
# SAX: Bar 1 - Rest
# Bar 2 - Start the melody (your moment)
# Bar 2 - Time 1.5 to 3.0

# Melody in F major, simple and emotional, a whisper-like motif

# Bar 2 (1.5 - 3.0s)
# Motif: F (70) - G (72) - A (74) - G (72) - F (70) - E (69) - D (67) - F (70)
# Rhythmic spacing: quarter, eighth, eighth, eighth, eighth, eighth, eighth, quarter

sax_notes = [
    Note(70, 105, 1.5, 1.5 + beat),
    Note(72, 105, 1.5 + beat, 1.5 + beat + beat/2),
    Note(74, 105, 1.5 + beat + beat/2, 1.5 + beat + beat/2 + beat/2),
    Note(72, 105, 1.5 + beat + beat/2 + beat/2, 1.5 + beat + beat/2 + beat/2 + beat/2),
    Note(70, 105, 1.5 + beat + beat/2 + beat/2 + beat/2, 1.5 + beat + beat/2 + beat/2 + beat/2 + beat/2),
    Note(69, 105, 1.5 + beat + beat/2 + beat/2 + beat/2 + beat/2, 1.5 + beat + beat/2 + beat/2 + beat/2 + beat/2 + beat/2),
    Note(67, 105, 1.5 + beat + beat/2 + beat/2 + beat/2 + beat/2 + beat/2, 1.5 + beat + beat/2 + beat/2 + beat/2 + beat/2 + beat/2 + beat/2),
    Note(70, 105, 1.5 + beat + beat/2 + beat/2 + beat/2 + beat/2 + beat/2 + beat/2, 1.5 + beat + beat/2 + beat/2 + beat/2 + beat/2 + beat/2 + beat/2 + beat)
]

sax.notes.extend(sax_notes)

# Bar 3 and 4 (3.0 - 6.0) - Let the rest of the band continue, you play the motif again at the end of bar 4
# Repeat the same motif at the end of bar 4 (5.25s - 6.0s)

sax_notes = [
    Note(70, 105, 5.25, 5.25 + beat),
    Note(72, 105, 5.25 + beat, 5.25 + beat + beat/2),
    Note(74, 105, 5.25 + beat + beat/2, 5.25 + beat + beat/2 + beat/2),
    Note(72, 105, 5.25 + beat + beat/2 + beat/2, 5.25 + beat + beat/2 + beat/2 + beat/2),
    Note(70, 105, 5.25 + beat + beat/2 + beat/2 + beat/2, 5.25 + beat + beat/2 + beat/2 + beat/2 + beat/2),
    Note(69, 105, 5.25 + beat + beat/2 + beat/2 + beat/2 + beat/2, 5.25 + beat + beat/2 + beat/2 + beat/2 + beat/2 + beat/2),
    Note(67, 105, 5.25 + beat + beat/2 + beat/2 + beat/2 + beat/2 + beat/2, 5.25 + beat + beat/2 + beat/2 + beat/2 + beat/2 + beat/2 + beat/2),
    Note(70, 105, 5.25 + beat + beat/2 + beat/2 + beat/2 + beat/2 + beat/2 + beat/2, 6.0)
]

sax.notes.extend(sax_notes)

# Save the MIDI file
pm.write("jazz_intro_f_major.mid")
