
import pretty_midi

# Create a new MIDI file with tempo 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Initialize instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only

# Kick on 1 and 3 (0.0, 0.75, 1.5s)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=1.5, end=1.875))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hi-hat on every eighth note
hihat_times = [0.0, 0.375, 0.75, 1.125, 1.5, 1.875]
for t in hihat_times:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=t, end=t + 0.375))

# Bar 2 (1.5 - 3.0s): Full quartet
# Bass (Marcus) - walking line in F minor, chromatic approach to Bb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),   # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4 (Bb7, Eb7)
# Bar 2: Bb7 on beat 2 (start 2.0 - 2.375)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.375),  # Eb
]
piano.notes.extend(piano_notes)

# Bar 3 (3.0 - 4.5s): Sax (Dante) - motif
# F -> Ab -> Bb -> D (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # D
]
sax.notes.extend(sax_notes)

# Bass continues walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=4.125, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano adds more chords on beat 4 (Eb7)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.375),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.375),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.375),  # Eb
]
piano.notes.extend(piano_notes)

# Bar 4 (4.5 - 6.0s): Sax completes the motif and returns
# F -> Ab -> Bb -> D (return of motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=63, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # D
]
sax.notes.extend(sax_notes)

# Bass continues walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano resolves with F7 on beat 4 (F7)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.875),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.875),  # C
]
piano.notes.extend(piano_notes)

# Drums continue: Bar 3 and 4
# Kick on 1 and 3 (4.5, 5.25, 6.0)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=5.25, end=5.625))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=6.0, end=6.375))

# Snare on 2 and 4 (4.875, 5.5)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=5.5, end=5.875))

# Hi-hat on every eighth note
hihat_times = [4.5, 4.875, 5.25, 5.625, 6.0, 6.375]
for t in hihat_times:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=t, end=t + 0.375))

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
