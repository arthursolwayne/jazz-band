
import pretty_midi

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
sax_instrument = pretty_midi.Instrument(program=64)
bass_instrument = pretty_midi.Instrument(program=33)
piano_instrument = pretty_midi.Instrument(program=0)
drums_instrument = pretty_midi.Instrument(program=9)

# Add instruments to the MIDI
midi.instruments.append(sax_instrument)
midi.instruments.append(bass_instrument)
midi.instruments.append(piano_instrument)
midi.instruments.append(drums_instrument)

# Set tempo to 160 BPM
midi.tempo_changes[0].tempo = 160

# Define note durations and timing (160 BPM -> 0.375 seconds per beat)
beat = 0.375
bar = beat * 4
note_duration = 0.375  # quarter note

# Bar 1: Drums only - rhythmic intrigue, tension, space
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time signature: 4/4, Bar 1: 0.0 to 1.5 seconds

# Kick on beat 1 (0.0)
drums_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.0 + 0.125))
# Kick on beat 3 (1.125)
drums_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.125 + 0.125))

# Snare on beat 2 (0.75)
drums_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.75 + 0.125))
# Snare on beat 4 (1.5)
drums_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.5 + 0.125))

# Hi-hats on every eighth note
for i in range(8):
    start = i * 0.125
    end = start + 0.125
    drums_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=end))

# Bar 2: Saxophone motif, concise, emotional, memorable
# Start at 1.5 seconds

# Note sequence: D (D4, 62) -> E (64) -> B (66) -> D (62)
# Rest at the end to leave it hanging

sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375))  # D4
sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=1.875 + 0.375))  # E4
sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.25 + 0.375))  # B4
sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.625 + 0.375))  # D4

# Bar 2: Bass line - chromatic, melodic, not just walking
# Start at 1.5 seconds

# Chromatic line: D (62) -> C# (61) -> D (62) -> C# (61)
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.25))
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=1.75 + 0.25))
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.0 + 0.25))
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.25 + 0.25))

# Bar 2: Piano - comping with emotion, 7th chords on 2 and 4
# Start at 1.5 seconds

# D7 chord: D (62), F# (67), A (69), C# (61)
# On beat 2 (1.75 - 2.0)
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=1.75, end=2.0))

# D7 chord again on beat 4 (2.25 - 2.5)
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.5))

# Bar 3: Saxophone repeats the motif, but ends on a rest
# Start at 2.5 seconds

sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.5 + 0.375))  # D4
sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=2.875, end=2.875 + 0.375))  # E4
sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.25 + 0.375))  # B4
# Leave it hanging — no note on D4 this time
# sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.625 + 0.375))

# Bar 3: Bass line - continues the chromatic line
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.5 + 0.25))
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=2.75, end=2.75 + 0.25))
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.25))
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.25 + 0.25))

# Bar 3: Piano - continues comping, same pattern
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.75))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=2.5, end=2.75))

piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=3.25))

# Bar 4: Saxophone ends with a resolution — D4, full note
# Start at 3.5 seconds

sax_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.5 + 0.75))  # D4 full note

# Bar 4: Bass line — resolves to D with a chromatic approach
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=3.5, end=3.5 + 0.25))  # C#
bass_instrument.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.75 + 0.25))  # D

# Bar 4: Piano — resolves with a D7 chord, full quarter
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.5 + 0.5))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.5 + 0.5))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.5 + 0.5))
piano_instrument.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=3.5, end=3.5 + 0.5))

# Bar 4: Drums — similar to bar 1, but slightly more dynamic
# Kick on 1 (3.5)
drums_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=3.5, end=3.5 + 0.125))
# Kick on 3 (4.375)
drums_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=36, start=4.375, end=4.375 + 0.125))

# Snare on 2 (4.0)
drums_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.0 + 0.125))
# Snare on 4 (4.75)
drums_instrument.notes.append(pretty_midi.Note(velocity=110, pitch=38, start=4.75, end=4.75 + 0.125))

# Hi-hats on every eighth note
for i in range(8):
    start = 3.5 + i * 0.125
    end = start + 0.125
    drums_instrument.notes.append(pretty_midi.Note(velocity=95, pitch=42, start=start, end=end))

# Write MIDI to file
midi.write("jazz_intro.mid")
