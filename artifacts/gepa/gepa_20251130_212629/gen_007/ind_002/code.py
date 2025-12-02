
import pretty_midi
from pretty_midi import Instrument, Note

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature to 4/4
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]

# Define the key: Dm (D Dorian)
# Scale degrees: D, E, F, G, A, Bb, C
# Root: D (62)
# Notes in Dm7: D, F, A, C (chord tones)

# Define the time in seconds per bar
bar_duration = 1.5  # 160 BPM, 4/4 time
beat_duration = 0.375  # 1 beat = 0.375 seconds

# Create instruments
drums = Instrument(program=0, is_drum=True)
bass = Instrument(program=33)
piano = Instrument(program=0)
sax = Instrument(program=64)

# Add instruments to the PrettyMIDI object
pm.instruments = [drums, bass, piano, sax]

# ===================
# DRUMS: Little Ray
# Kick on 1 and 3
# Snare on 2 and 4
# Hi-hat on every eighth
# ===================

# Bar 1
drums.notes.append(Note(36, 0.0, 0.15))  # Kick on 1
drums.notes.append(Note(38, 0.375, 0.15)) # Snare on 2
drums.notes.append(Note(42, 0.0, 0.15))  # Hi-hat on 1
drums.notes.append(Note(42, 0.1875, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 0.375, 0.15)) # Hi-hat on 2
drums.notes.append(Note(42, 0.5625, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 0.75, 0.15))  # Hi-hat on 3
drums.notes.append(Note(42, 0.9375, 0.15)) # Hi-hat on &
drums.notes.append(Note(36, 0.75, 0.15))  # Kick on 3
drums.notes.append(Note(42, 1.125, 0.15)) # Hi-hat on 4
drums.notes.append(Note(42, 1.3125, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 1.5, 0.15))   # Hi-hat on 4

# Bar 2
drums.notes.append(Note(36, 1.5, 0.15))  # Kick on 1
drums.notes.append(Note(38, 1.875, 0.15)) # Snare on 2
drums.notes.append(Note(42, 1.5, 0.15))  # Hi-hat on 1
drums.notes.append(Note(42, 1.6875, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 1.875, 0.15)) # Hi-hat on 2
drums.notes.append(Note(42, 2.0625, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 2.25, 0.15))  # Hi-hat on 3
drums.notes.append(Note(42, 2.4375, 0.15)) # Hi-hat on &
drums.notes.append(Note(36, 2.25, 0.15))  # Kick on 3
drums.notes.append(Note(42, 2.625, 0.15)) # Hi-hat on 4
drums.notes.append(Note(42, 2.8125, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 3.0, 0.15))   # Hi-hat on 4

# Bar 3
drums.notes.append(Note(36, 3.0, 0.15))  # Kick on 1
drums.notes.append(Note(38, 3.375, 0.15)) # Snare on 2
drums.notes.append(Note(42, 3.0, 0.15))  # Hi-hat on 1
drums.notes.append(Note(42, 3.1875, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 3.375, 0.15)) # Hi-hat on 2
drums.notes.append(Note(42, 3.5625, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 3.75, 0.15))  # Hi-hat on 3
drums.notes.append(Note(42, 3.9375, 0.15)) # Hi-hat on &
drums.notes.append(Note(36, 3.75, 0.15))  # Kick on 3
drums.notes.append(Note(42, 4.125, 0.15)) # Hi-hat on 4
drums.notes.append(Note(42, 4.3125, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 4.5, 0.15))   # Hi-hat on 4

# Bar 4
drums.notes.append(Note(36, 4.5, 0.15))  # Kick on 1
drums.notes.append(Note(38, 4.875, 0.15)) # Snare on 2
drums.notes.append(Note(42, 4.5, 0.15))  # Hi-hat on 1
drums.notes.append(Note(42, 4.6875, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 4.875, 0.15)) # Hi-hat on 2
drums.notes.append(Note(42, 5.0625, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 5.25, 0.15))  # Hi-hat on 3
drums.notes.append(Note(42, 5.4375, 0.15)) # Hi-hat on &
drums.notes.append(Note(36, 5.25, 0.15))  # Kick on 3
drums.notes.append(Note(42, 5.625, 0.15)) # Hi-hat on 4
drums.notes.append(Note(42, 5.8125, 0.15)) # Hi-hat on &
drums.notes.append(Note(42, 6.0, 0.15))   # Hi-hat on 4

# ===================
# BASS: Marcus
# Walking line, chromatic approaches, no repeated notes
# Dm -> D, F, A, C
# Start with a chromatic descent to D (Bb, A, G, F, E, D)
# ===================

# Bar 1: Chromatic descent to D
bass.notes.append(Note(62, 0.0, 0.25))  # D (beat 1)
bass.notes.append(Note(60, 0.375, 0.25)) # Eb
bass.notes.append(Note(59, 0.75, 0.25))  # E
bass.notes.append(Note(57, 1.125, 0.25)) # G

# Bar 2: Chromatic approach down to F
bass.notes.append(Note(64, 1.5, 0.25))  # F
bass.notes.append(Note(62, 1.875, 0.25)) # D
bass.notes.append(Note(61, 2.25, 0.25))  # Eb
bass.notes.append(Note(59, 2.625, 0.25)) # E

# Bar 3: Chromatic approach down to A
bass.notes.append(Note(69, 3.0, 0.25))  # A
bass.notes.append(Note(67, 3.375, 0.25)) # G
bass.notes.append(Note(65, 3.75, 0.25))  # F
bass.notes.append(Note(64, 4.125, 0.25)) # E

# Bar 4: Chromatic approach down to C
bass.notes.append(Note(67, 4.5, 0.25))  # C
bass.notes.append(Note(65, 4.875, 0.25)) # Bb
bass.notes.append(Note(64, 5.25, 0.25))  # B
bass.notes.append(Note(62, 5.625, 0.25)) # A

# ===================
# PIANO: Diane
# 7th chords, comp on 2 and 4
# Dm7 = D, F, A, C
# Use 7th chords, rhythm on 2 and 4
# ===================

# Bar 1: Dm7 on beat 2 and 4
piano.notes.append(Note(62, 0.375, 0.25))  # D
piano.notes.append(Note(64, 0.375, 0.25))  # F
piano.notes.append(Note(69, 0.375, 0.25))  # A
piano.notes.append(Note(67, 0.375, 0.25))  # C
piano.notes.append(Note(62, 0.75, 0.25))  # D
piano.notes.append(Note(64, 0.75, 0.25))  # F
piano.notes.append(Note(69, 0.75, 0.25))  # A
piano.notes.append(Note(67, 0.75, 0.25))  # C

# Bar 2: Dm7 on beat 2 and 4
piano.notes.append(Note(62, 1.875, 0.25))  # D
piano.notes.append(Note(64, 1.875, 0.25))  # F
piano.notes.append(Note(69, 1.875, 0.25))  # A
piano.notes.append(Note(67, 1.875, 0.25))  # C
piano.notes.append(Note(62, 2.25, 0.25))  # D
piano.notes.append(Note(64, 2.25, 0.25))  # F
piano.notes.append(Note(69, 2.25, 0.25))  # A
piano.notes.append(Note(67, 2.25, 0.25))  # C

# Bar 3: Dm7 on beat 2 and 4
piano.notes.append(Note(62, 3.375, 0.25))  # D
piano.notes.append(Note(64, 3.375, 0.25))  # F
piano.notes.append(Note(69, 3.375, 0.25))  # A
piano.notes.append(Note(67, 3.375, 0.25))  # C
piano.notes.append(Note(62, 3.75, 0.25))  # D
piano.notes.append(Note(64, 3.75, 0.25))  # F
piano.notes.append(Note(69, 3.75, 0.25))  # A
piano.notes.append(Note(67, 3.75, 0.25))  # C

# Bar 4: Dm7 on beat 2 and 4
piano.notes.append(Note(62, 4.875, 0.25))  # D
piano.notes.append(Note(64, 4.875, 0.25))  # F
piano.notes.append(Note(69, 4.875, 0.25))  # A
piano.notes.append(Note(67, 4.875, 0.25))  # C
piano.notes.append(Note(62, 5.25, 0.25))  # D
piano.notes.append(Note(64, 5.25, 0.25))  # F
piano.notes.append(Note(69, 5.25, 0.25))  # A
piano.notes.append(Note(67, 5.25, 0.25))  # C

# ===================
# SAX: You
# One short motif — start it, leave it hanging, return and finish it
# D, F, G, D — Dm7 intervallic motion
# Start on beat 1 of bar 2, leave it on beat 3, return on beat 4
# ===================

# Bar 1: Rest
# Bar 2: Start the motif
sax.notes.append(Note(62, 1.5, 0.25))  # D
sax.notes.append(Note(64, 1.875, 0.25)) # F
sax.notes.append(Note(67, 2.25, 0.25))  # G

# Bar 3: Leave it hanging — rest
# Bar 4: Return and finish
sax.notes.append(Note(62, 5.25, 0.25))  # D

# Write the MIDI file
pm.write('dante_intro.mid')
