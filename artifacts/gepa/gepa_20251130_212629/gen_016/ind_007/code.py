
import pretty_midi

# Initialize MIDI file with D minor key and 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Saxophone
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Acoustic Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes (kick, snare, hi-hat)
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
    
    # Hi-hat on every 8th note
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
]

# Bass line: walking bass in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # E (3rd)
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=3.0),   # F (4th)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F# (chromatic)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # G (5th)
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125),  # G# (6th)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # A (7th)
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),  # Bb (chromatic)
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # B (octave)
]

# Piano: comping with 7th chords
piano_notes = [
    # Dm7 (D F A C) on 2 and 4
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # C
]

# Sax: Motif starting in bar 2, finishes in bar 4
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # E (3rd)
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # G (5th)
    # Bar 3: Let it hang
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),  # E
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=4.75, end=5.0),  # Bb (7th)
]

# Add notes to instruments
drums.notes.extend(drum_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save to file
midi.write("dminor_intro.mid")
