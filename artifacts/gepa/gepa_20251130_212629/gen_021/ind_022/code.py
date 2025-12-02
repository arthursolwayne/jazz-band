
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double Bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Define MIDI note numbers for the instruments
# Sax: D4 (62), E4 (64), F#4 (66), G4 (67), A4 (69), B4 (71)
# Bass: D2 (50), E2 (52), F#2 (54), G2 (55), A2 (57), B2 (59)
# Piano: D3 (62), E3 (64), F#3 (66), G3 (67), A3 (69), B3 (71), C4 (60)
# Drums: Kick = 36, Snare = 38, Hihat = 42

# Bar 1: Drums only (0.0 - 1.5s)
# Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth with a bit of space

bar_length = 1.5  # seconds per bar at 160 BPM

# Kick on 1 and 3 (0.0 and 0.75s)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.05))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=36, start=0.75, end=0.8))

# Snare on 2 and 4, but with slight syncopation
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.25, end=0.275))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.0, end=1.025))

# Hihat on every eighth note (with slight variation in timing to give space)
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.025))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.15))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.275))
drums.notes.append(pretty_midi.Note(velocity=75, pitch=42, start=0.375, end=0.4))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.525))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.65))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.775))
drums.notes.append(pretty_midi.Note(velocity=75, pitch=42, start=0.875, end=0.9))

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, no repeated notes
# D2 -> E2 -> F#2 -> G2 -> A2 -> B2 -> C3 -> D3
# Each note is 1/4 note, played on beat 1, 2, 3, 4, etc.

note_values = [50, 52, 54, 55, 57, 59, 60, 62]
for i, note in enumerate(note_values):
    start_time = 1.5 + (i * 0.375)
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start_time, end=start_time + 0.375))

# Piano: 7th chords on 2 and 4, comping with space
# D7 chord: D (62), F# (66), A (69), C (60)
# B7 chord: B (71), D (62), F# (66), A (69)

# Bar 2: D7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 0.25, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.5 + 0.25, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 0.25, end=1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.5 + 0.25, end=1.5 + 0.375))

# Bar 3: D7 on beat 2
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 0.25 + 1.5, end=1.5 + 0.25 + 1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.5 + 0.25 + 1.5, end=1.5 + 0.25 + 1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 0.25 + 1.5, end=1.5 + 0.25 + 1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.5 + 0.25 + 1.5, end=1.5 + 0.25 + 1.5 + 0.375))

# Bar 4: B7 on beat 4
piano.notes.append(pretty_midi.Note(velocity=90, pitch=71, start=1.5 + 0.75 + 1.5, end=1.5 + 0.75 + 1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.5 + 0.75 + 1.5, end=1.5 + 0.75 + 1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=66, start=1.5 + 0.75 + 1.5, end=1.5 + 0.75 + 1.5 + 0.375))
piano.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.5 + 0.75 + 1.5, end=1.5 + 0.75 + 1.5 + 0.375))

# Saxophone: Melody (Dante's motif)
# D4 (62), E4 (64), F#4 (66), G4 (67) — start it, leave it hanging, come back and finish it
# Start at bar 2, first beat (1.5s)
# First phrase: D4 -> E4 -> F#4 -> G4 (start at 1.5s)
# Then leave it hanging by ending the phrase at 1.875s (beat 2)
# Then repeat the phrase, but ending at the end of the bar (6.0s)

# First phrase
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.55))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.55, end=1.6))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.6, end=1.65))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.65, end=1.875))

# Second phrase (repeat and finish the motif)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.05))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.05, end=3.1))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.1, end=3.15))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.15, end=6.0))

# Add all instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Save the MIDI file
midi.write("dante_intro.mid")
