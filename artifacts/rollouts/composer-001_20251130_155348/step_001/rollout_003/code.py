
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

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (start=2.25)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    # G7 on 4 (start=3.0)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # C
]
piano.notes.extend(piano_notes)

# Sax: Motif - start on D (62), move to F# (65), then to B (69)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25),  # D (resolve)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # A7 on 2 (start=3.75)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # C
    # D7 on 4 (start=4.5)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif variation - start on B (69), move to D (62), then to F# (65)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.1875),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=3.1875, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5625),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.5625, end=3.75),  # B (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 (3.0 - 4.5s)
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
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # B7 on 2 (start=5.25)
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # C
    # D7 on 4 (start=6.0)
    pretty_midi.Note(velocity=90, pitch=62, start=6.0, end=6.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=6.0, end=6.375),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=6.0, end=6.375),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif variation - start on D (62), move to F# (65), then to B (69)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.6875, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0625),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # D (resolve)
]
sax.notes.extend(sax_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_introduction.mid')
