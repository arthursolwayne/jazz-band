
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # C (1.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),
    # D# (1.625s)
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),
    # E (1.75s)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),
    # F (1.875s)
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),
    # G (2.0s)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),
    # A# (2.125s)
    pretty_midi.Note(velocity=100, pitch=70, start=2.125, end=2.25),
    # B (2.25s)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375),
    # C (2.375s)
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # C7 (1.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.625),
    # E7 (2.0s)
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=68, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.125),
    # G7 (2.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=79, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=81, start=2.5, end=2.625)
]
piano.notes.extend(piano_notes)

# Sax: Melodic motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # C (1.5s)
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.625),
    # E (1.625s)
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),
    # G (1.75s)
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),
    # C (2.0s)
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.125),
    # D# (2.125s)
    pretty_midi.Note(velocity=110, pitch=63, start=2.125, end=2.25),
    # E (2.25s)
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.375),
    # G (2.375s)
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # D# (3.0s)
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.125),
    # E (3.125s)
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),
    # F (3.25s)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),
    # G (3.375s)
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),
    # A# (3.5s)
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.625),
    # B (3.625s)
    pretty_midi.Note(velocity=100, pitch=71, start=3.625, end=3.75),
    # C (3.75s)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.875),
    # D# (3.875s)
    pretty_midi.Note(velocity=100, pitch=63, start=3.875, end=4.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # D#7 (3.0s)
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.125),
    # F7 (3.5s)
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=77, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=79, start=3.5, end=3.625),
    # A#7 (4.0s)
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=82, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=84, start=4.0, end=4.125)
]
piano.notes.extend(piano_notes)

# Sax: Melody continuation
sax_notes = [
    # D# (3.0s)
    pretty_midi.Note(velocity=110, pitch=63, start=3.0, end=3.125),
    # F (3.125s)
    pretty_midi.Note(velocity=110, pitch=65, start=3.125, end=3.25),
    # G (3.25s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),
    # D# (3.5s)
    pretty_midi.Note(velocity=110, pitch=63, start=3.5, end=3.625),
    # E (3.625s)
    pretty_midi.Note(velocity=110, pitch=64, start=3.625, end=3.75),
    # G (3.75s)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=3.875),
    # F (3.875s)
    pretty_midi.Note(velocity=110, pitch=65, start=3.875, end=4.0)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # E (4.5s)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),
    # F (4.625s)
    pretty_midi.Note(velocity=100, pitch=65, start=4.625, end=4.75),
    # G (4.75s)
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),
    # A# (4.875s)
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0),
    # B (5.0s)
    pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.125),
    # C (5.125s)
    pretty_midi.Note(velocity=100, pitch=60, start=5.125, end=5.25),
    # D# (5.25s)
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.375),
    # E (5.375s)
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # E7 (4.5s)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.625),
    # G7 (5.0s)
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=71, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=79, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=81, start=5.0, end=5.125),
    # C7 (5.5s)
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=71, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.625)
]
piano.notes.extend(piano_notes)

# Sax: Melody resolution
sax_notes = [
    # E (4.5s)
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.625),
    # G (4.625s)
    pretty_midi.Note(velocity=110, pitch=67, start=4.625, end=4.75),
    # A# (4.75s)
    pretty_midi.Note(velocity=110, pitch=70, start=4.75, end=4.875),
    # B (4.875s)
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.0),
    # C (5.0s)
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.125),
    # D# (5.125s)
    pretty_midi.Note(velocity=110, pitch=63, start=5.125, end=5.25),
    # E (5.25s)
    pretty_midi.Note(velocity=110, pitch=64, start=5.25, end=5.375),
    # G (5.375s)
    pretty_midi.Note(velocity=110, pitch=67, start=5.375, end=5.5)
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.875, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
