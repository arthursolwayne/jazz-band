
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

# Bar 1 - Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.75),  # D (root)
    pretty_midi.Note(velocity=90, pitch=66, start=1.75, end=2.0),  # Eb (chromatic)
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),  # Bb (chromatic)
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2 - 2nd beat: D7
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),  # D
    # Bar 2 - 4th beat: G7
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.75, end=3.0),  # F
]
piano.notes.extend(piano_notes)

# Sax - Motif: D - F# - B - D (first four notes of the melody)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # B
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bass - Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=70, start=3.25, end=3.5),  # Ab (chromatic)
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=75, start=4.25, end=4.5),  # Eb (chromatic)
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 3 - 2nd beat: A7
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.0),  # A
    # Bar 3 - 4th beat: D7
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),  # D
]
piano.notes.extend(piano_notes)

# Sax - Motif continuation, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=4.0, end=4.25),  # B
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # D
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

# Bass - Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=4.75, end=5.0),  # Ab (chromatic)
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 4 - 2nd beat: B7
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.5),  # F#
    pretty_midi.Note(velocity=90, pitch=81, start=5.25, end=5.5),  # A
    # Bar 4 - 4th beat: G7
    pretty_midi.Note(velocity=90, pitch=67, start=6.0, end=6.25),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=6.0, end=6.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=6.0, end=6.25),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=6.0, end=6.25),  # F
]
piano.notes.extend(piano_notes)

# Sax - Finish the motif with a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
