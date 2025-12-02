
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=40, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=39, start=2.625, end=3.0),   # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 chord
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # Db
    # Bar 2, beat 4: Bb7 chord
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=54, start=2.625, end=3.0),   # Gb
]
piano.notes.extend(piano_notes)

# Sax: Motif (Bar 2 - start, Bar 3 - continuation, Bar 4 - resolution)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=3.0),   # A
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=3.0, end=3.375),   # D
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),   # E
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),   # F#
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),    # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3, beat 2: G7 chord
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),   # G
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),   # B
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),   # C
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),   # D
    # Bar 3, beat 4: C7 chord
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),    # C
    pretty_midi.Note(velocity=90, pitch=58, start=4.125, end=4.5),    # E
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),    # G
    pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.5),    # Ab
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation, ends on resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.75),   # B
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.125),   # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),    # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),   # F#
    pretty_midi.Note(velocity=80, pitch=40, start=5.25, end=5.625),   # E
    pretty_midi.Note(velocity=80, pitch=39, start=5.625, end=6.0),    # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, beat 2: D7 chord
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),   # D
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),   # F
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),   # G
    pretty_midi.Note(velocity=90, pitch=56, start=4.875, end=5.25),   # Ab
    # Bar 4, beat 4: F7 chord
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),    # F
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0),    # A
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),    # C
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),    # Db
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.25),   # G
    pretty_midi.Note(velocity=110, pitch=66, start=5.25, end=5.625),   # A
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=6.0),    # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
