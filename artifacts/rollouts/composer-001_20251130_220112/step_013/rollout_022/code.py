
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Start with the sax melody
# Motif: Dm7 -> G7 -> Cm7 -> F7

# Bar 2
# Dm7: D, F, A, C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3
# G7: G, B, D, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # D
]
sax.notes.extend(sax_notes)

# Bar 4
# Cm7: C, Eb, G, Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.625),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.625, end=3.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.375),  # Bb
]
sax.notes.extend(sax_notes)

# Bass line (walking line with chromatic approaches)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.75, end=2.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=2.5, end=2.75),  # G#
    pretty_midi.Note(velocity=80, pitch=67, start=2.75, end=3.0),  # G
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.625),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.625, end=3.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.875, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.375),  # B
]
bass.notes.extend(bass_notes)

# Piano comping (7th chords on 2 and 4)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=60, start=3.625, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.625, end=3.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.625, end=3.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.625, end=3.875),  # Bb
]
piano.notes.extend(piano_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
