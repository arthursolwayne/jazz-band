
import pretty_midi

# Initialize the MIDI file with tempo (160 BPM)
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments for each player
sax = pretty_midi.Instrument(program=66)       # Tenor saxophone
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drums: kick=36, snare=38, hihat=42
# Constants for instrument notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray (drums) alone (0.0 to 1.5s)
# A question in rhythm, with dynamic tension and space
drum_notes = [
    # Kick on beat 1, snare on beat 2
    pretty_midi.Note(velocity=80, pitch=KICK, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=0.75, end=1.125),

    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.0, end=0.375),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.375, end=0.75),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=0.75, end=1.125),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2-4 (1.5 to 6.0s) - Full quartet, with sax motif, tension, and emotional depth

# Marcus: Walking bass line in D minor, chromatic approaches
bass_notes = [
    # Dm7 - D F A C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # C
]

bass.notes.extend(bass_notes)

# Diane: Piano comping with 7th chords on 2 and 4, in D minor
# Dm7 = D F A C
# G7 = G B D F
# A7 = A C# E G
# Bm7 = B D F# A
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # C

    # Bar 3: G7 on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F

    # Bar 4: A7 on beat 2
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # G
]

piano.notes.extend(piano_notes)

# Dante: Tenor sax motif - open, searching, incomplete, but with emotional weight
# Start with a chromatic motif: D, Eb, E, F, rest, then resolve with A
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),   # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),   # A (resolution)
]

sax.notes.extend(sax_notes)

# Drums continue in bars 2-4, maintaining rhythm with dynamic tension
drum_notes = [
    # Bar 2 (1.5-3.0s)
    pretty_midi.Note(velocity=80, pitch=KICK, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.5, end=1.875),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=1.875, end=2.25),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=2.25, end=2.625),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=2.625, end=3.0),

    # Bar 3 (3.0-4.5s)
    pretty_midi.Note(velocity=80, pitch=KICK, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=3.75, end=4.125),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=3.0, end=3.375),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=3.375, end=3.75),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=3.75, end=4.125),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=4.125, end=4.5),

    # Bar 4 (4.5-6.0s)
    pretty_midi.Note(velocity=80, pitch=KICK, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=SNARE, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=4.5, end=4.875),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=4.875, end=5.25),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=5.25, end=5.625),
    pretty_midi.Note(velocity=60, pitch=HIHAT, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
