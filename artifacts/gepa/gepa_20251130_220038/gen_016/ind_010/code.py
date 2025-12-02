
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1: 0.0 - 1.5s
# 0.0s (beat 0) = kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.375))
# 0.75s (beat 1) = snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=0.75, end=1.125))
# 1.125s (beat 1.5) = hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=1.125, end=1.5))
# 1.5s (beat 2) = kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=1.5, end=1.875))
# 2.25s (beat 3) = snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=2.25, end=2.625))
# 2.625s (beat 3.5) = hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=2.625, end=3.0))
# 3.0s (beat 4) = kick
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=3.0, end=3.375))
# 3.75s (beat 4.5) = snare
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=3.75, end=4.125))
# 4.125s (beat 5) = hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=4.125, end=4.5))
# 4.5s (beat 5.5) = hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=4.5, end=4.875))
# 4.875s (beat 6) = hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=4.875, end=5.25))
# 5.25s (beat 6.5) = hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=5.25, end=5.625))
# 5.625s (beat 7) = hihat
drums.notes.append(pretty_midi.Note(velocity=100, pitch=HIHAT, start=5.625, end=6.0))

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: Fm7 -> Bb7 -> Eb7 -> Ab7 (Fm7 in F minor)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=pretty_midi.note_number_to_name(65, 'F'), start=1.5, end=1.75))  # F (Fm7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=pretty_midi.note_number_to_name(60, 'Bb'), start=1.75, end=2.0))  # Bb (Bb7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=pretty_midi.note_number_to_name(57, 'Eb'), start=2.0, end=2.25))  # Eb (Eb7)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=pretty_midi.note_number_to_name(55, 'Ab'), start=2.25, end=2.5))  # Ab (Ab7)

# Bass: Walking line in Fm (F -> Gb -> A -> Bb -> C -> Db -> Eb -> F)
bass.notes.append(pretty_midi.Note(velocity=70, pitch=53, start=1.5, end=1.625))  # F
bass.notes.append(pretty_midi.Note(velocity=70, pitch=51, start=1.625, end=1.75))  # Gb
bass.notes.append(pretty_midi.Note(velocity=70, pitch=50, start=1.75, end=1.875))  # A
bass.notes.append(pretty_midi.Note(velocity=70, pitch=52, start=1.875, end=2.0))  # Bb
bass.notes.append(pretty_midi.Note(velocity=70, pitch=55, start=2.0, end=2.125))  # C
bass.notes.append(pretty_midi.Note(velocity=70, pitch=50, start=2.125, end=2.25))  # Db
bass.notes.append(pretty_midi.Note(velocity=70, pitch=50, start=2.25, end=2.375))  # Eb
bass.notes.append(pretty_midi.Note(velocity=70, pitch=53, start=2.375, end=2.5))  # F

# Piano: 7th chords on 2 and 4 (Fm7, Bb7, Eb7, Ab7)
# Bar 2: Fm7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=58, start=1.75, end=2.0))  # Db
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0))  # F

# Bar 3: Bb7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=2.75, end=3.0))  # D
piano.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=3.0))  # F
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=2.75, end=3.0))  # Ab

# Bar 4: Eb7 on 2 and 4
piano.notes.append(pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0))  # Eb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.0))  # G
piano.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.0))  # Bb
piano.notes.append(pretty_midi.Note(velocity=100, pitch=47, start=3.75, end=4.0))  # Db

# Bar 4: Sax melody (Ab -> G -> F -> Eb)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.75))  # Ab
sax.notes.append(pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.0))  # G
sax.notes.append(pretty_midi.Note(velocity=100, pitch=52, start=4.0, end=4.25))  # F
sax.notes.append(pretty_midi.Note(velocity=100, pitch=50, start=4.25, end=4.5))  # Eb

# Add instruments to the MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_4bar_intro.mid")
