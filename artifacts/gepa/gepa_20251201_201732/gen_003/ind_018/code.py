
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

# Bass: Walking line, D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.0),
    # Bar 3: G2 (fifth) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.375),
    pretty_midi.Note(velocity=90, pitch=44, start=2.375, end=2.625),
    # Bar 4: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=37, start=2.875, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # E
    # Bar 3: Bm7 (B, D, F, A)
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.375),  # A
    # Bar 4: Em7 (E, G, B, D)
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.875),  # E
    pretty_midi.Note(velocity=100, pitch=78, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=2.875),  # B
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=2.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, finish it
# Motif: F (65), Bb (62), D (67), C (69)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.375),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.875),  # C (late return)
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hi-hat
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.625)
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375)
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75)
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
