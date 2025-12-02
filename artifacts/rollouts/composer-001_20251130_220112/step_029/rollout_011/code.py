
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
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=95, pitch=53, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=85, pitch=48, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),  # C
    # Bar 3: Bb7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=85, pitch=57, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
]
piano.notes.extend(piano_notes)

# Sax: Motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=51, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=54, start=4.125, end=4.5),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=85, pitch=57, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),  # F
    # Bar 4: E7 on beat 4
    pretty_midi.Note(velocity=95, pitch=66, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=85, pitch=61, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),  # B
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=54, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=56, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=90, pitch=57, start=5.625, end=6.0),  # Db
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: E7 on beat 2
    pretty_midi.Note(velocity=95, pitch=66, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=85, pitch=61, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=68, start=5.25, end=5.625),  # B
    # Bar 4: End on Bb7 on beat 4
    pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=85, pitch=57, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=64, start=5.625, end=6.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
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

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
