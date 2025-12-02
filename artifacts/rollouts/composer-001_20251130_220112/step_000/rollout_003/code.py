
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=73, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=1.875, end=2.25),  # D
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: Short motif, make it sing
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.875),  # E
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=73, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=3.375, end=3.75),  # D
    # Bar 4: F7 on beat 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=66, start=4.875, end=5.25),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=45, start=5.625, end=6.0),   # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=73, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: End on F
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_russo_intro.mid')
