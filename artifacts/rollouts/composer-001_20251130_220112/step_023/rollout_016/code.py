
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),   # Gb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),  # F7 - E
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F7 - Eb
    # Bar 2, beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0),  # F7 - E
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # F7 - Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif (start on beat 2, finish on beat 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.125),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.375),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),    # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),   # Gb
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # F7 - E
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # F7 - Eb
    # Bar 3, beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # F7 - F
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),   # F7 - E
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # F7 - Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation (start on beat 2, finish on beat 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.625, end=3.875),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),    # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),   # D
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),   # Gb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # F7 - F
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),  # F7 - E
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # F7 - Eb
    # Bar 4, beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # F7 - F
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),   # F7 - Bb
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0),   # F7 - E
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # F7 - Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif completion (start on beat 2, finish on beat 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.125, end=5.375),  # E
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),    # Bb
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('fm_intro.mid')
