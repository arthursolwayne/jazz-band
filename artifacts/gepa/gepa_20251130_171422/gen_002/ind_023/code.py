
import pretty_midi

# Initialize the MIDI file with tempo and time signature
midi = pretty_midi.PrettyMIDI(initial_tempo=160)
time_signature = pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)
midi.time_signature_changes.append(time_signature)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# The beat: kick on 1 and 3, snare on 2 and 4, hihat on every 8th

# Bar 1: Just drums (0.0 - 1.5s)
# Kick on 1 and 3 (beat 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125))
# Snare on 2 and 4 (beat 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5))
# Hi-hat on every eighth (start at 0.0, 0.375, 0.75, 1.125)
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=i * 0.375, end=(i + 1) * 0.375))

# Bar 2: Full ensemble (1.5 - 3.0s)
# Sax: Simple, haunting motif in Fm (F, Ab, Bb, D)
# Motif: F (beat 1), Ab (beat 2), Bb (beat 3), D (beat 4)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875))   # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.25)) # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625)) # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0))  # D

# Bass: Walking line with chromatic approaches in Fm
# Fm: F, Ab, Bb, D
# Chromatic approach to Ab from G#, Bb from A, D from C#
# Notes: F (beat 1), G# (beat 2), A (beat 3), C# (beat 4)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875))   # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25)) # G#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625)) # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0))  # C#

# Piano: 7th chords on 2 and 4, comp on 2 and 4
# Fm7: F, Ab, Bb, D
# Root on 2 and 4 (beat 1.875 and 2.625)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25)) # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25)) # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25)) # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25)) # D

piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0)) # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=3.0)) # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0)) # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0)) # D

# Bar 3: Full ensemble (3.0 - 4.5s)
# Sax: Repeat motif with slight variation
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375))   # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75)) # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125)) # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5))  # D

# Bass: Walking line again
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375))   # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.75)) # G#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125)) # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.5))  # C#

# Piano: Comp on 2 and 4 again
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75)) # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75)) # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75)) # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75)) # D

piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5)) # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.5)) # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5)) # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5)) # D

# Bar 4: Full ensemble (4.5 - 6.0s)
# Sax: Repeat motif, but end on D with a slight sustain to leave it hanging
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875))   # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.25)) # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625)) # Bb
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0))  # D (with a little sustain)

# Bass: Walking line again
bass.notes.append(pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875))   # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=4.875, end=5.25)) # G#
bass.notes.append(pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625)) # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=6.0))  # C#

# Piano: Comp on 2 and 4 again
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25)) # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25)) # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25)) # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25)) # D

piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0)) # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0)) # Ab
piano.notes.append(pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0)) # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0)) # D

# Drums in bar 4
# Kick on 1 and 3 (4.5 and 5.25)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625))
# Snare on 2 and 4 (4.875 and 5.625)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0))
# Hi-hat on every eighth
for i in range(4):
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=4.5 + i * 0.375, end=4.5 + (i + 1) * 0.375))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
