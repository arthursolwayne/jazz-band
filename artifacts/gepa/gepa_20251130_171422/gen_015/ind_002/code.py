
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drum kit (Little Ray)

# MIDI note numbers for drum kit
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth

bar_length = 1.5  # 1.5 seconds per bar

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5))

# Hi-hat on every eighth
for i in range(0, 8):
    start = i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=end))

# Bar 2: Everyone in. Start of the motif

# Sax (Dante) - Fm7 -> Cm7 -> Ab7 -> Dm7 (Fm key)
# Start motif on beat 1
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875))  # Fm7 - F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25))  # Cm7 - C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625))  # Ab7 - Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0))  # Dm7 - D

# Bass (Marcus) - Chromatic walking line
# F -> E -> D -> C -> B -> Bb -> A -> Ab -> G
bass_notes = [71, 70, 69, 68, 67, 66, 65, 64, 63]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano (Diane) - 7th chords, offbeat comping
# Fm7 on beat 1
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875))  # F

# Cm7 on beat 2 (offbeat)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=1.875, end=2.25))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25))  # C

# Drums continue
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=1.5, end=1.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=2.25, end=2.625))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.875, end=2.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=2.625, end=3.0))

# Hi-hat on every eighth
for i in range(0, 8):
    start = 1.5 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=end))

# Bar 3: Continue the motif

# Sax - Repeat motif but end on D (Dm7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375))  # Fm7 - F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75))  # Cm7 - C
sax.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125))  # Ab7 - Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5))  # Dm7 - D

# Bass (Marcus) - Chromatic walking line
# F -> E -> D -> C -> B -> Bb -> A -> Ab -> G
bass_notes = [71, 70, 69, 68, 67, 66, 65, 64, 63]
for i, note in enumerate(bass_notes):
    start = 3.0 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano (Diane) - 7th chords, offbeat comping
# Fm7 on beat 1
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375))  # F

# Cm7 on beat 2 (offbeat)
piano.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75))  # C
piano.notes.append(pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75))  # Eb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75))  # C

# Drums continue
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=3.0, end=3.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=3.75, end=4.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=3.375, end=3.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=4.125, end=4.5))

# Hi-hat on every eighth
for i in range(0, 8):
    start = 3.0 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=end))

# Bar 4: End of the motif (Dante leaves it hanging)

# Sax - End on D (Dm7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875))  # D

# Bass (Marcus) - Chromatic walking line
# F -> E -> D -> C -> B -> Bb -> A -> Ab -> G
bass_notes = [71, 70, 69, 68, 67, 66, 65, 64, 63]
for i, note in enumerate(bass_notes):
    start = 4.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Piano (Diane) - 7th chords, offbeat comping
# Fm7 on beat 1
piano.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875))  # Bb
piano.notes.append(pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875))  # F

# Drums continue
# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=5.25, end=5.625))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=5.625, end=6.0))

# Hi-hat on every eighth
for i in range(0, 8):
    start = 4.5 + i * 0.375
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=start, end=end))

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("fm_jazz_intro.mid")
