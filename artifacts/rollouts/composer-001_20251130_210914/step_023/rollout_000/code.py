
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2: Fm7 - Bb7
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F#
    # Bar 3: E7 - Am7
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5),  # A
    # Bar 4: Dm7 - G7
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=63, start=4.25, end=4.5),  # Eb
    # Bar 5: Cm7 - F7 (extra bar for resolution)
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),  # Db
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=5.75, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (2 and 4)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    # Bar 3: E7 (2 and 4)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A#
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.5),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),  # A#
    # Bar 4: Dm7 (2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=59, start=4.25, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # F
]
piano.notes.extend(piano_notes)

# Sax: motif, one short phrase, make it sing
sax_notes = [
    # Bar 2: Motif starts on Fm
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # A
    # Bar 3: Answer to the motif
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0),  # F#
    # Bar 4: Resolution
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=4.25, end=4.5),  # C
    # Bar 5: Final resolution
    pretty_midi.Note(velocity=110, pitch=59, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
])
# Snare on 2 and 4
drum_notes.extend([
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
])
# Hihat on every eighth
drum_notes.extend([
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
