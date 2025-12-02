
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

# Marcus: Walking line, chromatic approaches, never the same note twice. D minor
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.6875, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.0625),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.0625, end=2.25),  # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.4375),  # G
    pretty_midi.Note(velocity=80, pitch=64, start=2.4375, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.8125, end=3.0),  # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=61, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=3.1875, end=3.375),  # B
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.5625),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.5625, end=3.75),  # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4. D minor 7
piano_notes = [
    # Bar 2: Dm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875),  # D
    # Bar 3: Dm7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.8125),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=2.8125),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.8125),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.5625, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.5625, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.5625, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.5625, end=3.75),  # D
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=38, start=2.0625, end=2.25),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=110, pitch=38, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=110, pitch=38, start=2.8125, end=3.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=3.5625, end=3.75),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D (Down)
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875),  # G (Up)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0625),  # D (Down)
    pretty_midi.Note(velocity=100, pitch=60, start=2.0625, end=2.25),  # C (Hold)
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.4375),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.4375, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.8125),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.8125, end=3.0),  # C
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.1875, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.5625, end=3.75),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
