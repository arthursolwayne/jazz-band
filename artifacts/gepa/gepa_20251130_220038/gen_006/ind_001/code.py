
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (1.5 - 3.0s)
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),  # F#
    # Bar 2: A7 on beat 4
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=100, pitch=81, start=2.625, end=3.0),   # E
    pretty_midi.Note(velocity=100, pitch=83, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=85, start=2.625, end=3.0),   # A
]
piano.notes.extend(piano_notes)

# Sax: motif (1.5 - 3.0s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),   # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (3.0 - 4.5s)
piano_notes = [
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),  # F#
    # Bar 3: A7 on beat 4
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=81, start=4.125, end=4.5),   # E
    pretty_midi.Note(velocity=100, pitch=83, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=85, start=4.125, end=4.5),   # A
]
piano.notes.extend(piano_notes)

# Sax: motif continuation (3.0 - 4.5s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),   # A
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line in D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=5.625, end=6.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (4.5 - 6.0s)
piano_notes = [
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),  # F#
    # Bar 4: A7 on beat 4
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),   # B
    pretty_midi.Note(velocity=100, pitch=81, start=5.625, end=6.0),   # E
    pretty_midi.Note(velocity=100, pitch=83, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=85, start=5.625, end=6.0),   # A
]
piano.notes.extend(piano_notes)

# Sax: motif resolution (4.5 - 6.0s)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=110, pitch=76, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=110, pitch=76, start=5.625, end=6.0),   # F#
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
