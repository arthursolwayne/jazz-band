
import pretty_midi

# Initialize the MIDI file with 160 BPM and 4/4 time
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Create time variables: 1 bar = 1.5 sec, 4 bars = 6 sec
bar_length = 1.5
beat_length = 0.375  # 160 BPM, 4/4 time

# BAR 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hi-hat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.5))

# Hi-hat on every eighth
for i in range(0, 6):
    start = i * beat_length
    end = start + beat_length
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=HIHAT, start=start, end=end))

# BAR 2: Full quartet (1.5 - 3.0s)

# Marcus on bass: walking line, chromatic approach to Dm7
# Dm7 = D F A C
# Chromatic approach on the 3rd (F) and 7th (C)

# Bar 2: D -> Eb -> F -> G -> A (walking line)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=2, start=1.5, end=1.875))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=3, start=1.875, end=2.25))  # Eb
bass.notes.append(pretty_midi.Note(velocity=80, pitch=5, start=2.25, end=2.625))  # F
bass.notes.append(pretty_midi.Note(velocity=80, pitch=7, start=2.625, end=3.0))  # G

# Diane on piano: comping on 2 and 4 with 7th chords
# Dm7 = D F A C

# 2nd beat (1.875 - 2.25)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=2, start=1.875, end=2.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=5, start=1.875, end=2.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=9, start=1.875, end=2.25))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=11, start=1.875, end=2.25))  # C

# 4th beat (2.625 - 3.0)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=2, start=2.625, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=5, start=2.625, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=9, start=2.625, end=3.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=11, start=2.625, end=3.0))  # C

# Dante on sax: motif — makes it sing, leaves it hanging
# Dm7: D F A C
# Motif: D -> F -> A -> (leave it hanging on A)

# D (start=1.5, end=1.6875)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=2, start=1.5, end=1.6875))
# F (start=1.6875, end=1.875)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=5, start=1.6875, end=1.875))
# A (start=1.875, end=2.0625)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=9, start=1.875, end=2.0625))

# BAR 3: Full quartet (3.0 - 4.5s)

# Marcus on bass: Dm -> C -> B -> A -> G
# Dm7 to G7
bass.notes.append(pretty_midi.Note(velocity=80, pitch=2, start=3.0, end=3.375))  # D
bass.notes.append(pretty_midi.Note(velocity=80, pitch=11, start=3.375, end=3.75))  # C
bass.notes.append(pretty_midi.Note(velocity=80, pitch=10, start=3.75, end=4.125))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=9, start=4.125, end=4.5))  # A

# Diane on piano: comping on 2 and 4 with G7
# G7 = G B D F

# 2nd beat (3.375 - 3.75)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=7, start=3.375, end=3.75))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=10, start=3.375, end=3.75))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=2, start=3.375, end=3.75))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=5, start=3.375, end=3.75))  # F

# 4th beat (4.125 - 4.5)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=7, start=4.125, end=4.5))  # G
piano.notes.append(pretty_midi.Note(velocity=90, pitch=10, start=4.125, end=4.5))  # B
piano.notes.append(pretty_midi.Note(velocity=90, pitch=2, start=4.125, end=4.5))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=5, start=4.125, end=4.5))  # F

# Dante on sax: continuation of the melody
# D -> F -> A -> G (completes the motif)

# G (start=3.0, end=3.1875)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=7, start=3.0, end=3.1875))

# BAR 4: Full quartet (4.5 - 6.0s)

# Marcus on bass: G -> A -> B -> C -> D (back to Dm)
bass.notes.append(pretty_midi.Note(velocity=80, pitch=7, start=4.5, end=4.875))  # G
bass.notes.append(pretty_midi.Note(velocity=80, pitch=9, start=4.875, end=5.25))  # A
bass.notes.append(pretty_midi.Note(velocity=80, pitch=10, start=5.25, end=5.625))  # B
bass.notes.append(pretty_midi.Note(velocity=80, pitch=11, start=5.625, end=6.0))  # C

# Diane on piano: comping on 2 and 4 with Dm7 again
# 2nd beat (4.875 - 5.25)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=2, start=4.875, end=5.25))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=5, start=4.875, end=5.25))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=9, start=4.875, end=5.25))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=11, start=4.875, end=5.25))  # C

# 4th beat (5.625 - 6.0)
piano.notes.append(pretty_midi.Note(velocity=90, pitch=2, start=5.625, end=6.0))  # D
piano.notes.append(pretty_midi.Note(velocity=90, pitch=5, start=5.625, end=6.0))  # F
piano.notes.append(pretty_midi.Note(velocity=90, pitch=9, start=5.625, end=6.0))  # A
piano.notes.append(pretty_midi.Note(velocity=90, pitch=11, start=5.625, end=6.0))  # C

# Dante on sax: resolves the motif and ends on D
sax.notes.append(pretty_midi.Note(velocity=100, pitch=2, start=4.5, end=4.875))  # D

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
