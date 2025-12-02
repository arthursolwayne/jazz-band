
import pretty_midi

# Initialize MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Saxophone
bass = pretty_midi.Instrument(program=33)      # Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes (kick=36, snare=38, hihat=42)
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
    # Subtle variation
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
]

# Bass (walking line in D)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.875),  # Root (D)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # Chromatic
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # 7th (B)
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),   # Root + 2 (E)
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Chromatic
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # 9th (F#)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # 7th (B)
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),   # Root + 2 (E)
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),  # 11th (G)
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25),  # 9th (F#)
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # Root + 2 (E)
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),   # 7th (B)
]

# Piano (7th chords on 2 and 4)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # B (7th)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # F# (3rd)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A# (9th)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # D (7th)
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # B (3rd)
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # E (9th)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=68, start=4.875, end=5.25),  # D (7th)
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),  # F# (3rd)
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # G# (9th)
]

# Sax (simple motif)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # D (2nd octave)
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),  # F# (2nd octave)
    # Bar 3: Repeat first note, leave hanging
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.25),
    # Bar 4: Repeat second note, add resolution
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=5.0),  # E (2nd octave)
]

# Add notes to instruments
drums.notes.extend(drum_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
