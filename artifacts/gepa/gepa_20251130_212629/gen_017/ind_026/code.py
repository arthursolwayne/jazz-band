
import pretty_midi

# Create the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Saxophone
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define MIDI note pitch values
# Dm7: D (62), F (64), A (69), C (60)
# Dm9: D (62), F (64), A (69), C (60), E (67)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    # Add variation
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
]
drums.notes.extend(drum_notes)

# Bass: Walking line with chromatic passing tones
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 & 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # C
    # Bar 3: Dm7
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # C
    # Bar 4: Dm9
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # B
]
piano.notes.extend(piano_notes)

# Sax: Motif: D -> F -> A -> G (on beat 1 of bar 2), with a return in bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),   # A
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),   # G
    # Repeat in bar 4 (building tension)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),   # A
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),   # G
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dm_jazz_intro.mid")
