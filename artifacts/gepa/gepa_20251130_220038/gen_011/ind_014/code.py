
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875)   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),   # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),   # G#
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=75, start=5.625, end=6.0),   # D#
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # E (7th chord Dm7: D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),   # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),   # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),   # Bb
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Motif in Dm, one short phrase, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),   # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # A
]
sax.notes.extend(sax_notes)

# Drums: continue filling the bar with hihat and snare
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=2.25),  # Kick on 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 2
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),   # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),  # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),   # Kick on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),   # Hihat on 2
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
