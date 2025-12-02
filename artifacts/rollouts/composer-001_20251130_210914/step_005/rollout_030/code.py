
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0)   # F
]
sax.notes.extend(sax_notes)

# Bass line (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0)   # G#
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=1.875, end=2.25),  # D7
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),  # F7
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),  # A7
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # C7

    pretty_midi.Note(velocity=80, pitch=59, start=3.0, end=3.375),  # D7
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # A7
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375)   # C7
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif (reprise with variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5)   # Bb
]
sax.notes.extend(sax_notes)

# Bass line (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # G#
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5)   # B
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.75),  # D7
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # F7
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # A7
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # C7

    pretty_midi.Note(velocity=80, pitch=59, start=4.5, end=4.875),  # D7
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # A7
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875)   # C7
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif (resolve)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)   # Bb
]
sax.notes.extend(sax_notes)

# Bass line (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=51, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0)   # D
]
bass.notes.extend(bass_notes)

# Piano comping on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.25),  # D7
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # F7
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),  # A7
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # C7

    pretty_midi.Note(velocity=80, pitch=59, start=6.0, end=6.375),  # D7
    pretty_midi.Note(velocity=80, pitch=62, start=6.0, end=6.375),  # F7
    pretty_midi.Note(velocity=80, pitch=67, start=6.0, end=6.375),  # A7
    pretty_midi.Note(velocity=80, pitch=71, start=6.0, end=6.375)   # C7
]
piano.notes.extend(piano_notes)

# Drums: Bar 3-4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.75),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.save('dante_russo_4bar.mid')
