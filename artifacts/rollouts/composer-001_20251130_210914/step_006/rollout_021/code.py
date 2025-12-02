
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
    # Hihat on every eighth note
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif starting at 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # Fm7 - F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Ab
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=2.75, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - 2nd beat (1.75 - 2.0s): Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # D
    # Bar 2 - 4th beat (2.75 - 3.0s): Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, shifted up by a half step
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=68, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=70, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=68, start=4.25, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.5),  # E
    pretty_midi.Note(velocity=80, pitch=46, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=4.25, end=4.5),  # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 - 2nd beat (3.25 - 3.5s): Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # D
    # Bar 3 - 4th beat (4.25 - 4.5s): Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Return to motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # Ab
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=5.0, end=5.25),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=80, pitch=44, start=5.75, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 - 2nd beat (4.75 - 5.0s): Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # D
    # Bar 4 - 4th beat (5.75 - 6.0s): Fm7
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
