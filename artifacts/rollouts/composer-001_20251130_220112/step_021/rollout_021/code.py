
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.1875),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=60, start=2.1875, end=2.375), # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=2.375, end=2.5625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.5625, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=2.75, end=2.9375),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=63, start=2.9375, end=3.125), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=3.125, end=3.3125), # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.3125, end=3.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=61, start=3.5, end=3.6875),   # C
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.6875),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.4375), # D7
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.4375), # A
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.4375), # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.4375), # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875),  # C
]
piano.notes.extend(piano_notes)

# Sax (Dante) - 4-bar motif
# Bar 2: Start of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.6875), # F (Dm7)
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875), # A (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),   # G (Dm7)
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.1875),  # F (Dm7)
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.4375), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.4375, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.8125), # F
    # Bar 4: Return to finish the motif
    pretty_midi.Note(velocity=100, pitch=66, start=2.8125, end=2.9375), # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.9375, end=3.125), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.3125), # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.3125, end=3.5),   # F
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4375), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.75, end=2.9375), # Snare
    # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=2.8125, end=2.9375), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.3125), # Snare
    # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
