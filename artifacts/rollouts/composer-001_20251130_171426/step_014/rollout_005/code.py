
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
kick = pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5)
drums.notes.extend([kick, snare, hihat])

# Bar 2: Full quartet (1.5 - 3.0s)
# Drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0)
drums.notes.extend([kick, snare, hihat])

# Bass (Marcus) - walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D7 (D, F#, A, C)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Motif: D (62), F# (67), Bb (66), D (62) - leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375)
snare = pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5)
drums.notes.extend([kick, snare, hihat])

# Bass (Marcus) - walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75), # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Repeat motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums
kick = pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875)
snare = pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625)
hihat = pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0)
drums.notes.extend([kick, snare, hihat])

# Bass (Marcus) - walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.25),  # D7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax (Dante) - Resolve motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
