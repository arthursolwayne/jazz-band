
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
    # Hi-hat on every eighth
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

# Bass line (Marcus): Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=51, start=2.25, end=2.625),  # Eb (3rd)
    pretty_midi.Note(velocity=80, pitch=52, start=2.625, end=3.0),  # E (chromatic)
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F (5th)
    pretty_midi.Note(velocity=80, pitch=54, start=3.375, end=3.75),  # F# (chromatic)
    pretty_midi.Note(velocity=80, pitch=51, start=3.75, end=4.125),  # Eb (3rd)
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.5),  # D (root)
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.875),  # C# (chromatic)
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # D (root)
    pretty_midi.Note(velocity=80, pitch=51, start=5.25, end=5.625),  # Eb (3rd)
    pretty_midi.Note(velocity=80, pitch=52, start=5.625, end=6.0),  # E (chromatic)
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D (7th)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D (7th)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # D (7th)
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.6875),  # E (3rd)
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875),  # D (root)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.1875),  # E (3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=3.1875, end=3.375),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625),  # E (3rd)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),  # D (root)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.6875),  # E (3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=4.6875, end=4.875),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0625),  # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # D (root)
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.4375),  # E (3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=5.4375, end=5.625),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.8125),  # Bb (7th)
    pretty_midi.Note(velocity=100, pitch=62, start=5.8125, end=6.0),  # D (root)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0),  # Hi-hat
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.5),  # Hi-hat
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0),  # Hi-hat
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
