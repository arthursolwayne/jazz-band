
import pretty_midi

# Initialize the MIDI file with a tempo of 160 BPM (4/4 time)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax (Dante)
bass = pretty_midi.Instrument(program=33)      # Double bass (Marcus)
piano = pretty_midi.Instrument(program=0)      # Piano (Diane)
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums (Little Ray)

# Drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Time in seconds for each bar
BAR_DURATION = 1.5
BEAT_DURATION = 0.375
EIGHTH_NOTE = BEAT_DURATION / 2

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Build tension with dynamic variation and subtle space

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=90, pitch=KICK, start=0.0, end=0.25))
drums.notes.append(pretty_midi.Note(velocity=80, pitch=KICK, start=0.75, end=1.0))
# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=85, pitch=SNARE, start=0.375, end=0.5))
drums.notes.append(pretty_midi.Note(velocity=85, pitch=SNARE, start=1.125, end=1.25))
# Hi-hat on every eighth
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.0, end=0.125))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.125, end=0.25))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.25, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=65, pitch=HIHAT, start=0.375, end=0.5))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.5, end=0.625))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.625, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=65, pitch=HIHAT, start=0.75, end=0.875))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.875, end=1.0))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.0, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=65, pitch=HIHAT, start=1.125, end=1.25))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.25, end=1.375))
drums.notes.append(pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.375, end=1.5))

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Key: Fm (F, Ab, Bb, C, Eb)
# Time signature: 4/4

# Bass line: chromatic walking line with melodic intent
bass_notes = [
    (1.5, 72),   # G (Ab), Bb, C, Eb
    (1.75, 71),  # F (Ab)
    (2.0, 73),   # Ab
    (2.25, 72),  # G
    (2.5, 71),   # F
    (2.75, 69),  # Eb
    (3.0, 71),   # F
    (3.25, 72),  # G
    (3.5, 73),   # Ab
    (3.75, 74),  # Bb
    (4.0, 72),   # G
    (4.25, 72),  # G
    (4.5, 71),   # F
    (4.75, 69),  # Eb
    (5.0, 71),   # F
    (5.25, 72),  # G
    (5.5, 73),   # Ab
    (5.75, 74),  # Bb
]

for start, pitch in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=pitch, start=start, end=start + BEAT_DURATION))

# Piano: comping with 7th chords on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
# Eb7 = Eb, G, Bb, Db
# C7 = C, E, G, Bb

# Comp on 2 and 4 in each bar
piano_notes = [
    # Bar 2: Fm7 on 2 (2.0-2.25), Bb7 on 4 (2.5-2.75)
    (2.0, 76, 100), (2.0, 83, 100), (2.0, 72, 100), (2.0, 74, 100),
    (2.5, 81, 100), (2.5, 84, 100), (2.5, 76, 100), (2.5, 83, 100),
    # Bar 3: Eb7 on 2 (3.5-3.75), C7 on 4 (4.0-4.25)
    (3.5, 74, 100), (3.5, 79, 100), (3.5, 81, 100), (3.5, 82, 100),
    (4.0, 72, 100), (4.0, 77, 100), (4.0, 79, 100), (4.0, 81, 100),
    # Bar 4: Fm7 on 2 (5.0-5.25), Bb7 on 4 (5.5-5.75)
    (5.0, 76, 100), (5.0, 83, 100), (5.0, 72, 100), (5.0, 74, 100),
    (5.5, 81, 100), (5.5, 84, 100), (5.5, 76, 100), (5.5, 83, 100),
]

for start, pitch, vel in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + BEAT_DURATION))

# Saxophone: short, memorable motif (start at 1.5s)
# Motif: F, Bb, Ab, G
# F (76), Bb (79), Ab (82), G (81)
# Let it sing — leave it hanging, then resolve

# First phrase: F, Bb, Ab, G (1.5-2.5s)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=2.5))

# Second phrase: repeat with slight variation (2.5-3.5s)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=2.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=79, start=2.75, end=3.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=81, start=3.25, end=3.5))

# Third phrase: resolve with a whisper (3.5-4.5s)
sax.notes.append(pretty_midi.Note(velocity=70, pitch=76, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=70, pitch=79, start=3.75, end=4.0))
sax.notes.append(pretty_midi.Note(velocity=70, pitch=82, start=4.0, end=4.25))
sax.notes.append(pretty_midi.Note(velocity=70, pitch=81, start=4.25, end=4.5))

# Fourth phrase: final resolution (4.5-5.5s)
sax.notes.append(pretty_midi.Note(velocity=80, pitch=76, start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=80, pitch=79, start=4.75, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=80, pitch=82, start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=80, pitch=81, start=5.25, end=5.5))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
