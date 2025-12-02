
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5)   # Kick on 3
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=3.375, end=3.75), # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, comping in Dm
piano_notes = [
    # Bar 2: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # F
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # F
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # F
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0),     # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),  # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
]
drums.notes.extend(drum_notes)

# Dante: Tenor sax motif (start at bar 2)
# Motif: D (62) -> Eb (64) -> D (62) -> C (60) -> D (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),   # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_in_the_cellar.mid")
