
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bass line: Marcus, walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),   # D#
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=54, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),   # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),  # A#
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4 (Bar 2: 2 and 4, Bar 3: 2 and 4, Bar 4: 2 and 4)
piano_notes = [
    # Bar 2 (Beat 2)
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),  # Bb
    # Bar 2 (Beat 4)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # Bb
    # Bar 3 (Beat 2)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # Bb
    # Bar 3 (Beat 4)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # Bb
    # Bar 4 (Beat 2)
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # Bb
    # Bar 4 (Beat 4)
    pretty_midi.Note(velocity=100, pitch=60, start=6.0, end=6.375),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=6.0, end=6.375),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.375),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=6.0, end=6.375),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Dante, short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # E
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # E
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
