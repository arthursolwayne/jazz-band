
import pretty_midi
from pretty_midi import Note, Instrument, Program

# Create a new Pretty MIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Time signature: 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the tempo (160 BPM)
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Define the time (in seconds) per bar
bar_length = 6.0 / 4  # 6 seconds for 4 bars => 1.5 seconds per bar
quarter_length = bar_length / 4  # 0.375 seconds per quarter note

# Define the F minor scale for reference
# Fm: F, Gb, Ab, Bb, B, C, Db
# We'll use F minor 7th chords and chromatic walking bass

# Create instruments
drums = Instrument(program=Program.DRUMS, is_drum=True)
piano = Instrument(program=Program.ELECTRIC_PIANO_1)
bass = Instrument(program=Program.BASS_GUITAR_FINGERSTYLE)
sax = Instrument(program=Program.SAXOPHONE_ALTO)

# Add instruments to the MIDI file
pm.instruments = [drums, piano, bass, sax]

# ========== DRUMS (Little Ray) ==========
# Bar 1: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: All time is 1.5s (bar_length)
# Kick on 1 and 3 (beat 0 and 2)
drums.notes.append(Note(36, 80, 0.0, 0.375))  # Kick 1
drums.notes.append(Note(36, 80, 0.75, 0.375))  # Kick 3

# Snare on 2 and 4 (beat 1 and 3)
drums.notes.append(Note(38, 80, 0.375, 0.375))  # Snare 2
drums.notes.append(Note(38, 80, 1.125, 0.375))  # Snare 4

# Hi-hat on every 8th note
for t in [0.0, 0.375, 0.75, 1.125]:
    drums.notes.append(Note(42, 80, t, 0.1875))  # Hi-hat

# ========== PIANO (Diane) ==========
# Comp on 2 and 4, using Fm7 (F, Ab, Bb, Db) and chromatic variations

# Bar 2: Fm7 chord (F, Ab, Bb, Db) on beat 2
piano.notes.append(Note(71, 100, 1.5, 0.375))   # F (71)
piano.notes.append(Note(76, 100, 1.5, 0.375))   # Ab (76)
piano.notes.append(Note(74, 100, 1.5, 0.375))   # Bb (74)
piano.notes.append(Note(72, 100, 1.5, 0.375))   # Db (72)

# Bar 3: Gbm7 (G, Bb, Db, E) – chromatic approach
piano.notes.append(Note(72, 100, 3.0, 0.375))   # G (72)
piano.notes.append(Note(74, 100, 3.0, 0.375))   # Bb (74)
piano.notes.append(Note(72, 100, 3.0, 0.375))   # Db (72)
piano.notes.append(Note(76, 100, 3.0, 0.375))   # E (76)

# Bar 4: Ab7 (Ab, C, Db, F) – just to keep the tension
piano.notes.append(Note(76, 100, 4.5, 0.375))   # Ab (76)
piano.notes.append(Note(79, 100, 4.5, 0.375))   # C (79)
piano.notes.append(Note(72, 100, 4.5, 0.375))   # Db (72)
piano.notes.append(Note(71, 100, 4.5, 0.375))   # F (71)

# ========== BASS (Marcus) ==========
# Chromatic walking bass line, starting from F and moving down

# Bar 2: F -> Eb -> D -> C
bass.notes.append(Note(64, 80, 1.5, 0.375))   # F (64)
bass.notes.append(Note(63, 80, 1.875, 0.375)) # Eb (63)
bass.notes.append(Note(62, 80, 2.25, 0.375))  # D (62)
bass.notes.append(Note(60, 80, 2.625, 0.375)) # C (60)

# Bar 3: Bb -> A -> G -> F
bass.notes.append(Note(74, 80, 3.0, 0.375))   # Bb (74)
bass.notes.append(Note(72, 80, 3.375, 0.375)) # A (72)
bass.notes.append(Note(71, 80, 3.75, 0.375))  # G (71)
bass.notes.append(Note(64, 80, 4.125, 0.375)) # F (64)

# Bar 4: Ab -> G -> F -> Eb
bass.notes.append(Note(76, 80, 4.5, 0.375))   # Ab (76)
bass.notes.append(Note(74, 80, 4.875, 0.375)) # G (74)
bass.notes.append(Note(64, 80, 5.25, 0.375))  # F (64)
bass.notes.append(Note(63, 80, 5.625, 0.375)) # Eb (63)

# ========== SAX (You) ==========
# A sparse, haunting melody — start with a motif that seems to be hanging, then resolve.

# Bar 2: Melody begins
# F (64) -> Ab (67) -> Bb (69) -> D (62) (fingering-wise, this is a chromatic drop)
# Each note is played with a slight space to make it linger.
sax.notes.append(Note(64, 100, 1.5, 0.25))
sax.notes.append(Note(67, 100, 1.75, 0.25))
sax.notes.append(Note(69, 100, 2.0, 0.25))
sax.notes.append(Note(62, 100, 2.35, 0.25))  # D (chromatic drop)

# Bar 3: Continue the motif, with a space
sax.notes.append(Note(64, 100, 3.0, 0.25))   # F again
sax.notes.append(Note(67, 100, 3.25, 0.25))  # Ab
sax.notes.append(Note(69, 100, 3.5, 0.25))   # Bb
sax.notes.append(Note(62, 100, 3.75, 0.25))  # D

# Bar 4: End on a note that lingers — Bb (69)
sax.notes.append(Note(69, 100, 4.5, 0.5))  # Hold the Bb for a half beat

# Save the MIDI file
pm.write('jazz_intro_f_minor.mid')
