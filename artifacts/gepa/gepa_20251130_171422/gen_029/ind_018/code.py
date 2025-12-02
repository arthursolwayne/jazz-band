
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1 (0.0 to 1.5)
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # G#
]

bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4 (Bar 2: 2nd beat)
piano_notes = [
    # Bar 2, beat 2: F7 chord (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=2.25, end=2.625),  # E
]

piano.notes.extend(piano_notes)

# Sax: Dante's motif (Bar 2, beat 1)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),   # E
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),   # G
]

sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # C
]

bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4 (Bar 3: 2nd beat)
piano_notes = [
    # Bar 3, beat 2: F7 chord (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=3.75, end=4.125),  # E
]

piano.notes.extend(piano_notes)

# Sax: Dante's motif (Bar 3, beat 1)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),   # F#
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),   # G
]

sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),   # C#
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),   # E
]

bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords on 2 and 4 (Bar 4: 2nd beat)
piano_notes = [
    # Bar 4, beat 2: F7 chord (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=82, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=80, start=5.25, end=5.625),  # E
]

piano.notes.extend(piano_notes)

# Sax: Dante's motif (Bar 4, beat 1)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.5, end=4.875),   # G
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),   # G (resting on the last beat)
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dantes_intro.mid")
