
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

# Bar 2: Full quartet (1.5 - 3.0s)
# SAX: Melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Dm7
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # Cm7
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Dm7
]
sax.notes.extend(sax_notes)

# BASS: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=80, pitch=51, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.25),   # C
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),   # D
    pretty_midi.Note(velocity=80, pitch=51, start=2.5, end=2.75),   # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0),   # C
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: 7th chord on 2 (start=2.0)
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),   # D
    # Bar 3: 7th chord on 2 (start=3.0)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),   # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# SAX: Melody (repeat with variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Dm7
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # Cm7
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # Dm7
]
sax.notes.extend(sax_notes)

# BASS: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=80, pitch=51, start=3.25, end=3.5),   # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=80, pitch=50, start=3.75, end=4.0),   # D
    pretty_midi.Note(velocity=80, pitch=51, start=4.0, end=4.25),   # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: 7th chord on 2 (start=3.5)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),   # D
    # Bar 4: 7th chord on 2 (start=4.5)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),   # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# SAX: Melody (finish motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Dm7
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # Cm7
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # Dm7
]
sax.notes.extend(sax_notes)

# BASS: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=80, pitch=51, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=5.0, end=5.25),   # C
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.5),   # D
    pretty_midi.Note(velocity=80, pitch=51, start=5.5, end=5.75),   # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=5.75, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# PIANO: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: 7th chord on 2 (start=5.0)
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),   # D
    # Bar 4: 7th chord on 4 (start=5.75)
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.75, end=6.0),   # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.75, end=6.0),   # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
