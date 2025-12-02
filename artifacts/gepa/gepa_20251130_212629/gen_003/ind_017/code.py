
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new MIDI file
pm = pretty_midi.PrettyMIDIClass()
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0.0)]
pm.midi_file.header.time_division = 480  # 480 ticks per quarter note

# Set tempo (160 BPM)
pm.tempos = [pretty_midi.TempoChange(tempo=160, time=0.0)]

# Define the 4 bars (6 seconds total)
# Each bar is 1.5 seconds
# 160 BPM = 160 beats per minute = 160/60 = 2.666 beats per second

# Define instruments
drums = Instrument(program=0, is_drum=True, name='Drums')
bass = Instrument(program=33, name='Bass')
piano = Instrument(program=0, name='Piano')
sax = Instrument(program=64, name='Saxophone')

# Add instruments to the MIDI file
pm.instruments = [drums, bass, piano, sax]

# Define the note durations and times
# 1 beat = 0.375 seconds at 160 BPM
beat_duration = 0.375
bar_duration = 1.5  # 4 beats per bar

# Bar 1: Drums only
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth

# Bar 1: 0.0 to 1.5 seconds
# Time in seconds: 0.0, 0.375, 0.75, 1.125, 1.5

# Kick (C1) on 1 and 3 (0.0 and 0.75)
drums.notes.append(Note(velocity=100, pitch=36, start=0.0, end=0.125))
drums.notes.append(Note(velocity=100, pitch=36, start=0.75, end=0.875))

# Snare (C2) on 2 and 4 (0.375 and 1.125)
drums.notes.append(Note(velocity=100, pitch=42, start=0.375, end=0.5))
drums.notes.append(Note(velocity=100, pitch=42, start=1.125, end=1.25))

# Hi-hat (C7) on every eighth: 0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125
for t in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:
    drums.notes.append(Note(velocity=70, pitch=60, start=t, end=t + 0.0625))

# Bar 2: Everyone in. Saxophone starts the melody

# Bar 2: 1.5 to 3.0 seconds
# Time in seconds: 1.5, 1.875, 2.25, 2.625, 3.0

# Bass: Walking line in D
# D - C# - B - A - G - F# - E - D
# Notes: D2=50, C#2=49, B2=47, A2=45, G2=43, F#2=42, E2=41, D2=50

bass_notes = [50, 49, 47, 45, 43, 42, 41, 50]
bass_times = [1.5, 1.875, 2.25, 2.625, 3.0, 3.375, 3.75, 4.125]
for note, time in zip(bass_notes, bass_times):
    bass.notes.append(Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords on 2 and 4 (2.25 and 3.0)
# D7 chord = D, F#, A, C
# D=50, F#=42, A=45, C=48
piano.notes.append(Note(velocity=100, pitch=50, start=2.25, end=2.375))
piano.notes.append(Note(velocity=100, pitch=42, start=2.25, end=2.375))
piano.notes.append(Note(velocity=100, pitch=45, start=2.25, end=2.375))
piano.notes.append(Note(velocity=100, pitch=48, start=2.25, end=2.375))

piano.notes.append(Note(velocity=100, pitch=50, start=3.0, end=3.125))
piano.notes.append(Note(velocity=100, pitch=42, start=3.0, end=3.125))
piano.notes.append(Note(velocity=100, pitch=45, start=3.0, end=3.125))
piano.notes.append(Note(velocity=100, pitch=48, start=3.0, end=3.125))

# Drums continue with same pattern (Bar 2)
for t in [1.5, 1.6875, 1.875, 2.0625, 2.25, 2.4375, 2.625, 2.8125]:
    drums.notes.append(Note(velocity=70, pitch=60, start=t, end=t + 0.0625))

drums.notes.append(Note(velocity=100, pitch=36, start=1.5, end=1.625))
drums.notes.append(Note(velocity=100, pitch=36, start=2.25, end=2.375))
drums.notes.append(Note(velocity=100, pitch=42, start=1.875, end=2.0))
drums.notes.append(Note(velocity=100, pitch=42, start=2.625, end=2.75))

# Saxophone: Melody - D - F# - B (rest on 2), then F# - D (rest on 4)

# D4 = 62, F#4 = 64, B4 = 67
sax.notes.append(Note(velocity=100, pitch=62, start=1.5, end=1.625))
sax.notes.append(Note(velocity=100, pitch=64, start=1.875, end=2.0))
sax.notes.append(Note(velocity=100, pitch=67, start=2.25, end=2.375))

sax.notes.append(Note(velocity=100, pitch=64, start=2.625, end=2.75))
sax.notes.append(Note(velocity=100, pitch=62, start=3.0, end=3.125))

# Bar 3: Continue the pattern (similar to Bar 2, but with variation)

# Make it feel like a story, not a loop. So let's just repeat similar structure but with a slight variation in bass and piano

# Bar 3: 3.0 to 4.5 seconds
# Bass again: D - C# - B - A - G - F# - E - D
# But vary the timing a bit

bass_notes_bar3 = [50, 49, 47, 45, 43, 42, 41, 50]
bass_times_bar3 = [3.0, 3.375, 3.75, 4.125, 4.5, 4.875, 5.25, 5.625]
for note, time in zip(bass_notes_bar3, bass_times_bar3):
    bass.notes.append(Note(velocity=80, pitch=note, start=time, end=time + 0.125))

# Piano: 7th chords again
piano.notes.append(Note(velocity=100, pitch=50, start=3.375, end=3.5))
piano.notes.append(Note(velocity=100, pitch=42, start=3.375, end=3.5))
piano.notes.append(Note(velocity=100, pitch=45, start=3.375, end=3.5))
piano.notes.append(Note(velocity=100, pitch=48, start=3.375, end=3.5))

piano.notes.append(Note(velocity=100, pitch=50, start=4.125, end=4.25))
piano.notes.append(Note(velocity=100, pitch=42, start=4.125, end=4.25))
piano.notes.append(Note(velocity=100, pitch=45, start=4.125, end=4.25))
piano.notes.append(Note(velocity=100, pitch=48, start=4.125, end=4.25))

# Bar 4: 4.5 to 6.0 seconds
# Saxophone: Finish the motif and leave it hanging

sax.notes.append(Note(velocity=100, pitch=62, start=4.5, end=4.625))
sax.notes.append(Note(velocity=100, pitch=64, start=4.875, end=5.0))
sax.notes.append(Note(velocity=100, pitch=67, start=5.25, end=5.375))

# End the piece
pm.write('dante_intro.mid')
print("MIDI file 'dante_intro.mid' created successfully.")
