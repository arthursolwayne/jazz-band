
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),# Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line in F, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=2.75, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=73, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=80, pitch=71, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=74, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=5.75, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # F7
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=77, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=81, start=1.75, end=2.0),

    # Bar 3 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),  # F7
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=77, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=81, start=2.75, end=3.0),

    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=71, start=4.25, end=4.5),  # F7
    pretty_midi.Note(velocity=90, pitch=74, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=77, start=4.25, end=4.5),
    pretty_midi.Note(velocity=90, pitch=81, start=4.25, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - motif in F
# Bar 2: Start motif at 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),  # A
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.0, end=2.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.1875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.4375),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.6875), # Hihat on 4

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=3.6875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=3.9375),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.1875), # Hihat on 4

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.0, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.1875), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),# Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=5.6875), # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
