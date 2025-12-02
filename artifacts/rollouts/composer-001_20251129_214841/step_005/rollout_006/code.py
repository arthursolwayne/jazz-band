
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Marcus (walking line, chromatic approaches)
bass_notes = [
    # C (1.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    # D- (1.875s)
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.25),
    # Eb (2.25s)
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625),
    # F (2.625s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # C7 on 2 (1.875s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # B
    # F7 on 4 (2.625s)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Dante (melody)
sax_notes = [
    # C (1.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    # E (2.25s)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),
    # G (2.625s)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Marcus (walking line, chromatic approaches)
bass_notes = [
    # D (3.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    # Eb- (3.375s)
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75),
    # F (3.75s)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),
    # G (4.125s)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # D7 on 2 (3.375s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=73, start=3.375, end=3.75),  # C
    # G7 on 4 (4.125s)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),  # F
]
piano.notes.extend(piano_notes)

# Sax: Dante (melody)
sax_notes = [
    # D (3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # G (3.75s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
    # B (4.125s)
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),  # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bass: Marcus (walking line, chromatic approaches)
bass_notes = [
    # C (4.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    # D- (4.875s)
    pretty_midi.Note(velocity=90, pitch=59, start=4.875, end=5.25),
    # Eb (5.25s)
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625),
    # F (5.625s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Diane (7th chords, comp on 2 and 4)
piano_notes = [
    # C7 on 2 (4.875s)
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # B
    # F7 on 4 (5.625s)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Dante (melody)
sax_notes = [
    # C (4.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    # E (5.25s)
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),
    # G (5.625s)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
