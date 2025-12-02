
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick on 36, snare on 38, hihat on 42
kick = 36
snare = 38
hihat = 42

# Time for each bar (160 BPM = 60/160 = 0.375 seconds per beat, 1.5 seconds per bar)
bar_length = 1.5

# ------------------------------- DRUMS -------------------------------
# Bar 1: Little Ray alone
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=hihat, start=1.125, end=1.5))

# Bar 2: Kick on 1 and 3, snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=2.25, end=2.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=2.625, end=3.0))

# Bar 3: Kick on 1 and 3, snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=3.75, end=4.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.125, end=4.5))

# Bar 4: Kick on 1 and 3, snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=5.625, end=6.0))

# ------------------------------- BASS -------------------------------
# Marcus: walking line with chromatic approaches

# Bar 1 (setup)
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=0.0, end=0.375))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=0.375, end=0.75))  # Fb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=0.75, end=1.125))  # F#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.125, end=1.5))  # F

# Bar 2
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875))  # A
bass.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25))  # Ab
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625))  # A#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0))  # A

# Bar 3
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375))  # B
bass.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75))  # Bb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125))  # B#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5))  # B

# Bar 4
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875))  # F
bass.notes.append(pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25))  # Fb
bass.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625))  # F#
bass.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0))  # F

# ------------------------------- PIANO -------------------------------
# Diane: 7th chords, comp on 2 and 4

# F7 chord (F A C E)
# Bar 1: comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=0.75, end=1.125))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=0.75, end=1.125))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=0.75, end=1.125))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=0.75, end=1.125))  # F

piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=1.125, end=1.5))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=1.125, end=1.5))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=1.125, end=1.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.125, end=1.5))  # F

# Bar 2: comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625))  # F

piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=2.625, end=3.0))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0))  # F

# Bar 3: comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125))  # F

piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=4.125, end=4.5))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5))  # F

# Bar 4: comp on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625))  # F

piano.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=5.625, end=6.0))  # E
piano.notes.append(pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0))  # C
piano.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0))  # A
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0))  # F

# ------------------------------- SAX (Dante) -------------------------------
# 4-bar melody: one motif, simple but striking

# Bar 1: Wait, set the stage
# No notes here

# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=1.875, end=2.25))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625))  # B
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0))  # A

# Bar 3: Development
sax.notes.append(pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5))  # C

# Bar 4: Resolution, lingering
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875))  # B
sax.notes.append(pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25))  # A
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0))  # B

# Add instruments to the MIDI file
midi.instruments.append(sax)
midi.instruments.append(bass)
midi.instruments.append(piano)
midi.instruments.append(drums)

# Write the MIDI file
midi.write("dante_intro.mid")
