
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody - F7, G7, A7, Bb7 (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=1.875),  # F7
    pretty_midi.Note(velocity=100, pitch=87, start=1.875, end=2.25), # G7
    pretty_midi.Note(velocity=100, pitch=89, start=2.25, end=2.625), # A7
    pretty_midi.Note(velocity=100, pitch=86, start=2.625, end=3.0),  # Bb7
]
sax.notes.extend(sax_notes)

# Bass - walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=2.625, end=3.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=78, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.375),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax - repeat motif, slightly altered
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=3.0, end=3.375),  # F7
    pretty_midi.Note(velocity=100, pitch=87, start=3.375, end=3.75), # G7
    pretty_midi.Note(velocity=100, pitch=89, start=3.75, end=4.125), # A7
    pretty_midi.Note(velocity=100, pitch=86, start=4.125, end=4.5),  # Bb7
]
sax.notes.extend(sax_notes)

# Bass - walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.5),   # Bb
]
bass.notes.extend(bass_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax - repeat motif, ending on a suspended note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=4.875),  # F7
    pretty_midi.Note(velocity=100, pitch=87, start=4.875, end=5.25), # G7
    pretty_midi.Note(velocity=100, pitch=89, start=5.25, end=5.625), # A7
    pretty_midi.Note(velocity=100, pitch=86, start=5.625, end=6.0),  # Bb7
]
sax.notes.extend(sax_notes)

# Bass - walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=4.875),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and Bar 4
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('intro.mid')
