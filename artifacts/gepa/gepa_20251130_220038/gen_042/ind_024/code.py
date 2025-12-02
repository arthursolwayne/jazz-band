
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5)    # hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),   # F
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=80, pitch=51, start=4.5, end=4.875),   # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, sparse comping
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=70, start=4.375, end=4.75),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=4.375, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=4.375, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),   # B
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=6.0),   # F
]
piano.notes.extend(piano_notes)

# Saxophone - short motif with rests and dynamic contour
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),   # D
    # Bar 3: Repeat with higher dynamics
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25), # E
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625), # D
    # Bar 4: End on a high note with space
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums in Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # hihat on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # hihat on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),   # hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
