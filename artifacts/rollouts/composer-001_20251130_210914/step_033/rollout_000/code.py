
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

# Marcus on bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=53, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.375, end=2.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=50, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.875, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),  # D7 (A)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625),  # D7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.625),  # D7 (F#)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # D7 (A)
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),  # D7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375),  # D7 (F#)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.0),  # D7 (D)
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),  # D7 (A)
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),  # D7 (C)
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),  # D7 (F#)
]
piano.notes.extend(piano_notes)

# Little Ray on drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.375, end=2.5),
    pretty_midi.Note(velocity=110, pitch=38, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=38, start=2.5, end=2.625),
    # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0625, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.8125, end=4.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.625, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.8125, end=5.0),
]
drums.notes.extend(drum_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
# Melody: Dm7 -> G7 -> Cm7 -> F7 (Dorian mode)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.6875, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.6875),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.6875, end=2.875),  # D
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.1875),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.save("jazz_intro.mid")
