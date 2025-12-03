
import pretty_midi
from pretty_midi import Note, Instrument, MidiFile

# Set up the MIDI file
midi = pretty_midi.PrettyMidi(initial_tempo=160)

# Define time signature: 4/4
midi.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define key: F minor
key = 'F minor'
key_number = 21  # F minor is MIDI key 21

# Set up instruments
drums = Instrument(program=0, is_drum=True, name='Drums')
bass = Instrument(program=33, name='Bass')
piano = Instrument(program=0, name='Piano')
sax = Instrument(program=64, name='Saxophone')

# Add instruments to the MIDI file
midi.instruments = [drums, bass, piano, sax]

# Define note durations in seconds (based on 160 BPM = 0.375s per beat)
beat = 0.375
bar = 4 * beat  # 1.5s per bar

# Bar 1: Little Ray on drums only
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Dynamic contrast: soft hihat, punchy kick/snare

# Kick on 1 and 3
drums.notes.append(Note(36, 60, 0.0, 0.15))  # Kick on beat 1
drums.notes.append(Note(36, 60, 1.125, 0.15))  # Kick on beat 3

# Snare on 2 and 4
drums.notes.append(Note(38, 60, 0.375, 0.15))  # Snare on beat 2
drums.notes.append(Note(38, 60, 1.5, 0.15))    # Snare on beat 4

# Hihat on every eighth (soft)
drums.notes.append(Note(42, 60, 0.0, 0.05))   # 1
drums.notes.append(Note(42, 60, 0.1875, 0.05)) # 1&
drums.notes.append(Note(42, 60, 0.375, 0.05))  # 2
drums.notes.append(Note(42, 60, 0.5625, 0.05)) # 2&
drums.notes.append(Note(42, 60, 0.75, 0.05))   # 3
drums.notes.append(Note(42, 60, 0.9375, 0.05)) # 3&
drums.notes.append(Note(42, 60, 1.125, 0.05))  # 4
drums.notes.append(Note(42, 60, 1.3125, 0.05)) # 4&

# Bar 2: Full band enters
# Bass: Walking line in Fm, roots and fifths with chromatic approaches
# Fm root = F (70), fifth = C (60), chromatic approaches
# Bar 2: F, F#, C, B

# Bar 2: F (beat 1), F# (beat 2), C (beat 3), B (beat 4)
bass.notes.append(Note(70, 60, 1.5, 0.15))
bass.notes.append(Note(71, 60, 1.875, 0.15))
bass.notes.append(Note(60, 60, 2.25, 0.15))
bass.notes.append(Note(61, 60, 2.625, 0.15))

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, Eb) -> open voicing
# Play on beat 2 and 4 (comping)
piano.notes.append(Note(87, 60, 1.875, 0.15))  # F
piano.notes.append(Note(84, 60, 1.875, 0.15))  # Ab
piano.notes.append(Note(79, 60, 1.875, 0.15))  # C
piano.notes.append(Note(82, 60, 1.875, 0.15))  # Eb

piano.notes.append(Note(87, 60, 2.625, 0.15))  # F
piano.notes.append(Note(84, 60, 2.625, 0.15))  # Ab
piano.notes.append(Note(79, 60, 2.625, 0.15))  # C
piano.notes.append(Note(82, 60, 2.625, 0.15))  # Eb

# Sax: Melody — short motif, haunting, incomplete
# Motif: F, Eb, D, rest
# Start bar 2, beat 1
sax.notes.append(Note(87, 60, 1.5, 0.2))
sax.notes.append(Note(83, 60, 1.875, 0.2))  # Eb
sax.notes.append(Note(82, 60, 2.25, 0.2))   # D
sax.notes.append(Note(87, 60, 2.625, 0.0))  # Rest

# Bar 3: Continue bass line and piano comp
# Bass: F, Gb, C, Bb
bass.notes.append(Note(70, 60, 3.0, 0.15))
bass.notes.append(Note(69, 60, 3.375, 0.15))
bass.notes.append(Note(60, 60, 3.75, 0.15))
bass.notes.append(Note(62, 60, 4.125, 0.15))

# Piano: Bbmaj7 (Bb, D, F, Ab) on beat 2 and 4
piano.notes.append(Note(83, 60, 3.375, 0.15))  # Bb
piano.notes.append(Note(79, 60, 3.375, 0.15))  # D
piano.notes.append(Note(76, 60, 3.375, 0.15))  # F
piano.notes.append(Note(84, 60, 3.375, 0.15))  # Ab

piano.notes.append(Note(83, 60, 4.125, 0.15))  # Bb
piano.notes.append(Note(79, 60, 4.125, 0.15))  # D
piano.notes.append(Note(76, 60, 4.125, 0.15))  # F
piano.notes.append(Note(84, 60, 4.125, 0.15))  # Ab

# Sax: Echo the motif, leave it hanging
# F, Eb, rest, rest
sax.notes.append(Note(87, 60, 3.0, 0.2))
sax.notes.append(Note(83, 60, 3.375, 0.2))
sax.notes.append(Note(87, 60, 3.75, 0.0))  # Rest
sax.notes.append(Note(87, 60, 4.125, 0.0))  # Rest

# Bar 4: Continue bass and piano, leave sax unresolved
# Bass: F, Gb, C, B
bass.notes.append(Note(70, 60, 4.5, 0.15))
bass.notes.append(Note(69, 60, 4.875, 0.15))
bass.notes.append(Note(60, 60, 5.25, 0.15))
bass.notes.append(Note(61, 60, 5.625, 0.15))

# Piano: Fm7 again on beat 2 and 4, but with tension
piano.notes.append(Note(87, 60, 4.875, 0.15))  # F
piano.notes.append(Note(84, 60, 4.875, 0.15))  # Ab
piano.notes.append(Note(79, 60, 4.875, 0.15))  # C
piano.notes.append(Note(86, 60, 4.875, 0.15))  # Eb/Bb

piano.notes.append(Note(87, 60, 5.625, 0.15))  # F
piano.notes.append(Note(84, 60, 5.625, 0.15))  # Ab
piano.notes.append(Note(79, 60, 5.625, 0.15))  # C
piano.notes.append(Note(86, 60, 5.625, 0.15))  # Eb/Bb

# Sax: End on a question — leave it open
# F, rest, rest, rest
sax.notes.append(Note(87, 60, 4.5, 0.2))
sax.notes.append(Note(87, 60, 4.875, 0.0))  # Rest
sax.notes.append(Note(87, 60, 5.25, 0.0))   # Rest
sax.notes.append(Note(87, 60, 5.625, 0.0))  # Rest

# Write the MIDI file
# midi.write disabled
