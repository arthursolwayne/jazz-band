
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0),
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

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: Dm7 - D F A C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.6875, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.0625, end=2.25),  # G
    # Bar 3: Dm7 - D F A C
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.4375, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=2.8125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.8125, end=3.0),  # G
    # Bar 4: Dm7 - D F A C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.1875, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.5625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.5625, end=3.75),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 - D F A C
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.6875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.6875),  # D
    # Bar 3: Dm7 - D F A C
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.4375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.4375),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.4375),  # D
    # Bar 4: Dm7 - D F A C
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.1875),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Dm7 - D F A C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A
    # Bar 3: Dm7 - D F A C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A
    # Bar 4: Dm7 - D F A C
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=95, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=95, pitch=38, start=4.125, end=4.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
