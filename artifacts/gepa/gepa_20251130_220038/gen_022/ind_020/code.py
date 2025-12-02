
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # E
    # Bar 3: Bb7 on beat 4 (but we're only doing 3 bars total)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Motif in F, one phrase that lingers
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # C
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.125),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Continuation of motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # F#
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # E
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),   # A
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hihat
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=100, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
