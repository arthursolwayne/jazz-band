
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # Dm7 root
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=49, start=5.625, end=6.0)   # C
]
bass.notes.extend(bass_notes)

# Piano - Diane
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
    # Bar 3: Dm7 (D F A C) with chromatic passing tones
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625), # C#
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625), # C
    # Bar 4: Dm7 (D F A C) with diminished passing
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # C
    # Bar 4 continuation
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75), # C#
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Sax - Dante
sax_notes = [
    # Bar 2: Melody motif (D F A C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # C
    # Bar 3: Transpose up a third (F A C Eb)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),  # Eb
    # Bar 4: Return to D F A C, but with space
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
