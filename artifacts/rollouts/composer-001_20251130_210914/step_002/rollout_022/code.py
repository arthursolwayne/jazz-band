
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane)
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=1.5, end=1.875),  # Eb
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # Ab
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.875),  # Eb
]
piano.notes.extend(piano_notes)

# Sax (Dante)
sax_notes = [
    # Bar 2: Motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # G
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
