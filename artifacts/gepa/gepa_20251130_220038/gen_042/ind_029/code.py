
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5)
drums.notes.extend([drum_kick, drum_snare, drum_hihat])

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=58, start=2.625, end=3.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.375),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.375),
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.375),
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.95)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2, drum_hihat])

# Dante: Motif in Dm
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),   # Eb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=58, start=4.125, end=4.5),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.875),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.875),
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2, drum_hihat])

# Dante: Motif repeat and resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),   # Eb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=58, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.375),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.375),
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.375),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.375),
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
drum_kick2 = pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0)
drum_snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
drum_snare2 = pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375)
drum_hihat = pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0)
drums.notes.extend([drum_kick, drum_kick2, drum_snare, drum_snare2, drum_hihat])

# Dante: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # Eb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
