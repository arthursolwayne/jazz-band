
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
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
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Gb (chromatic)
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625),  # G (3rd)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # A (5th)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # D
    # Bar 2: comp on beat 2
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=2.25, end=2.625),  # F
    # Bar 2: comp on beat 4
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=2.625, end=3.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # D
    # Bar 3: comp on beat 2
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=3.75, end=4.125),  # F
    # Bar 3: comp on beat 4
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # A
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
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

# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # D
    # Bar 4: comp on beat 2
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=78, start=5.25, end=5.625),  # F
    # Bar 4: comp on beat 4
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=74, start=5.625, end=6.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # A
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_intro.mid")
