
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
    pretty_midi.Note(velocity=90, pitch=38, start=0.0, end=0.375),  # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.75),   # hihat on 1
    pretty_midi.Note(velocity=90, pitch=36, start=0.75, end=1.125), # kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=2.0)     # hihat on 1 (next bar)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus (bass): walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=2.625, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Diane (piano): 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=85, pitch=72, start=1.5, end=1.875),  # D

    pretty_midi.Note(velocity=85, pitch=62, start=2.625, end=2.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=2.875),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=2.625, end=2.875),  # Bb
    pretty_midi.Note(velocity=85, pitch=72, start=2.625, end=2.875),  # D
]
piano.notes.extend(piano_notes)

# Dante (sax): short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # E
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus (bass): walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),  # E
]
bass.notes.extend(bass_notes)

# Diane (piano): 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=85, pitch=72, start=3.0, end=3.375),  # D

    pretty_midi.Note(velocity=85, pitch=62, start=4.125, end=4.375),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=4.125, end=4.375),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=4.125, end=4.375),  # Bb
    pretty_midi.Note(velocity=85, pitch=72, start=4.125, end=4.375),  # D
]
piano.notes.extend(piano_notes)

# Dante (sax): continuation of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # E
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75), # hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.125), # kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125), # hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),  # hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus (bass): walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Diane (piano): 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=85, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=85, pitch=72, start=4.5, end=4.875),  # D

    pretty_midi.Note(velocity=85, pitch=62, start=5.625, end=5.875),  # D
    pretty_midi.Note(velocity=85, pitch=67, start=5.625, end=5.875),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=5.625, end=5.875),  # Bb
    pretty_midi.Note(velocity=85, pitch=72, start=5.625, end=5.875),  # D
]
piano.notes.extend(piano_notes)

# Dante (sax): finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25), # snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25), # hihat on 2
    pretty_midi.Note(velocity=90, pitch=36, start=5.25, end=5.625), # kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),  # hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
