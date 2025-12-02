
import pretty_midi

# Create a new MIDI file at 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Saxophone
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define note pitches based on F major scale
F_major = [65, 67, 69, 72, 74, 76, 77]  # F, G, A, Bb, B, C, D

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),
    # Hi-hat on every 8th
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
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]

# Bass: Walking line with chromatic passing notes, in F major
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=0.0, end=0.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=0.375, end=0.75),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=0.75, end=1.125),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.125, end=1.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=81, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=83, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=85, start=4.5, end=4.875),   # B
    pretty_midi.Note(velocity=90, pitch=87, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=89, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=91, start=5.625, end=6.0),   # E
]

# Piano: 7th chords on the "and" of 2 and 4
piano_notes = [
    # Bar 1: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=65, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=68, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=72, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=76, start=0.75, end=1.125),
    # Bar 2: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),
    # Bar 3: A7 (A, C, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    # Bar 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),
]

# Sax: Motif in F major
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=0.0, end=0.25),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=0.25, end=0.5),   # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=0.5, end=0.75),   # B
    pretty_midi.Note(velocity=110, pitch=76, start=0.75, end=1.0),   # C
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),   # Bb
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0),   # B
    pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=110, pitch=77, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=110, pitch=74, start=3.0, end=3.25),   # B
    pretty_midi.Note(velocity=110, pitch=76, start=3.25, end=3.5),   # C
    pretty_midi.Note(velocity=110, pitch=79, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=110, pitch=81, start=3.75, end=4.0),   # E
    pretty_midi.Note(velocity=110, pitch=76, start=4.5, end=4.75),   # C
    pretty_midi.Note(velocity=110, pitch=77, start=4.75, end=5.0),   # D
    pretty_midi.Note(velocity=110, pitch=79, start=5.0, end=5.25),   # E
    pretty_midi.Note(velocity=110, pitch=81, start=5.25, end=5.5),   # F
]

# Assign notes to instruments
drums.notes.extend(drum_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Add all instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("jazz_in_f.mid")
