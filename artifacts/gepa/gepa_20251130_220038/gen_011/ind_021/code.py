
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

# Drums in Bar 1
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

# Bass line (Marcus)
bass_notes = [
    # Bar 2: F - Gb - G - Ab (walking line)
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=72, start=2.625, end=3.0),  # Ab
    # Bar 3: Bb - B - C - Db
    pretty_midi.Note(velocity=80, pitch=74, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=75, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=77, start=4.125, end=4.5),  # Db
    # Bar 4: Eb - E - F - Gb
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # Gb
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 (G, Bb, C, E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=78, start=1.875, end=2.25),  # E
    # Bar 3: Bb7 on 2 (D, F, G, Bb)
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # Bb
    # Bar 4: Eb7 on 2 (G, Bb, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # Eb
]
piano.notes.extend(piano_notes)

# Saxophone (Dante) - Melody in Bar 2-4
sax_notes = [
    # Bar 2: F - Bb - G - F (Motif)
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=3.0),  # F
    # Bar 3: Rest
    pretty_midi.Note(velocity=110, pitch=70, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=70, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=110, pitch=70, start=4.125, end=4.5),  # F
    # Bar 4: Return to motif
    pretty_midi.Note(velocity=110, pitch=70, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=70, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums in Bars 2-4
drum_notes = [
    # Kick on 1 and 3 (Bars 2, 3, 4)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4 (Bars 2, 3, 4)
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
