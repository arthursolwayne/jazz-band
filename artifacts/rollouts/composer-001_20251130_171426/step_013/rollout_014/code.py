
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F# (3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # A (5th)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B (7th)
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # C (chromatic)
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # B (7th)
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # A (5th)
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # F# (3rd)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F (chromatic)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D (root)
    pretty_midi.Note(velocity=100, pitch=63, start=5.625, end=6.0),  # Eb (chromatic)
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 with 7th chords
piano_notes = [
    # Bar 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # Bar 3: Bm7 (B, D, F#, A)
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif in D, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums in Bars 2-4
drum_notes = [
    # Kick on 1 and 3 in each bar
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4 in each bar
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5),
    # Hi-hat on every eighth
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
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
