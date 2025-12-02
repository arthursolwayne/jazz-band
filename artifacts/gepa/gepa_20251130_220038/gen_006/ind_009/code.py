
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # Fm7
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # Fm7
]
sax.notes.extend(sax_notes)

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=39, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=37, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.5),  # Gb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=100, pitch=59, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # Ab
    # Bar 2, beat 4 (2.25 - 2.5)
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.5),  # Db
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # G
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=61, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),
]
sax.notes.extend(sax_notes)

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=40, start=3.25, end=3.5),  # Gb
    pretty_midi.Note(velocity=100, pitch=39, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=37, start=3.75, end=4.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # Ab
    # Bar 3, beat 4 (3.75 - 4.0)
    pretty_midi.Note(velocity=100, pitch=66, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.0),  # Db
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # G
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=61, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),
]
sax.notes.extend(sax_notes)

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=39, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=40, start=5.0, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.5),  # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=100, pitch=59, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # Ab
    # Bar 4, beat 4 (5.25 - 5.5)
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.5),  # Db
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # G
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
