
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
    # Hihat on every eighth note
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=54, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=48, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D
    # Bar 3: G7
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=78, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.625),  # F
    # Bar 4: Cm7
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Motif in Dm
# 1st note: D (62), 2nd: F (65), 3rd: Bb (67), 4th: D (62) - leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),   # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D
]
sax.notes.extend(sax_notes)

# Add drum fill in bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.75),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=2.875),  # Snare
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.75),   # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.875),   # Hihat
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
