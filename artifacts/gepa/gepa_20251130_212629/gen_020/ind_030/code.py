
import pretty_midi

# Create a MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Saxophone
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Acoustic Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum note definitions (kick=36, snare=38, hihat=42)
drum_notes = [
    # Kick on beats 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),

    # Snare on beats 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),

    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
]

# Bass line in F minor (Fm7)
# Notes: F, Gb, Ab, A, Bb, B, C, Db, D, Eb, E, F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # Gb (chromatic)
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.625),  # Ab (b9)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # A (9)
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # Gb (chromatic)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # A (9)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # Bb (11)
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # Db (b13)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # D (root + 2)
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),  # C (13)
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # Db (b13)
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),   # F (root)
]

# Piano: Fm7 chord on 2 and 4
# Fm7 = F, Ab, C, Eb
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),

    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),

    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),
]

# Saxophone motif: A simple melodic line that returns and resolves
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # Ab (reprise)
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # Bb (reprise)
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # A (resolution)
]

# Add notes to instruments
drums.notes.extend(drum_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("f_minor_intro.mid")
