
import pretty_midi

# Create a MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define the instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
kick = 36
snare = 38
hihat = 42

# Bar 1: 0.0 - 1.5s
# Little Ray on drums only
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=kick, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=snare, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=snare, start=1.875, end=2.25),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=hihat, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=hihat, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=hihat, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=hihat, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=hihat, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=hihat, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2-4: 1.5 - 6.0s (3 bars, 4.5 seconds)
# Start with the saxophone motif
sax_notes = [
    # Your motif: F (65) on beat 1, Bb (70) on beat 2, D (62) on beat 3, F (65) on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),  # F
    # Repeat the motif with a slight rhythmic variation
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.5),  # F
    # End with F on the last beat, but leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F
]

sax.notes.extend(sax_notes)

# Marcus on bass: walking line with chromatic approaches
# In F, walking bass line: F, G, Ab, A, Bb, B, C, Db, D, Eb, E, F
# Let's use a chromatic approach to F and Bb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),   # Db
    pretty_midi.Note(velocity=80, pitch=73, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=80, pitch=74, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=75, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=5.625, end=6.0),   # F
]

bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
# In F7: F, A, C, Eb
piano_notes = [
    # Bar 2 (1.5 - 3.0s): F7
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=1.5, end=1.875),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),   # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),   # Eb
    # Bar 3 (3.0 - 4.5s): F7 again
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),   # C
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),   # Eb
    # Bar 4 (4.5 - 6.0s): F7 again
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),   # Eb
]

piano.notes.extend(piano_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("jazz_intro.mid")
