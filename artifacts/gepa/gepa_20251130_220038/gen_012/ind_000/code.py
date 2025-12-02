
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in F, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=85, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=75, pitch=64, start=1.5, end=1.875),
    # Bar 3: B♭7 (B♭, D, F, A♭)
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=75, pitch=61, start=2.25, end=2.625),
    # Bar 4: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=85, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=75, pitch=65, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Your motif — short, singable, leaves it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # B♭
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # D
]
sax.notes.extend(sax_notes)

# Bar 3 and 4: Repeat the rhythm, vary the melody slightly
# Bar 3
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B♭
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # A
]
sax.notes.extend(sax_notes)

# Bass: Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # E♭
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # B♭
]
bass.notes.extend(bass_notes)

# Piano: Continue comping
piano_notes = [
    # Bar 3: F7
    pretty_midi.Note(velocity=85, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=75, pitch=64, start=3.0, end=3.375),
    # Bar 4: B♭7
    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=75, pitch=61, start=3.75, end=4.125),
]
piano.notes.extend(piano_notes)

# Drums: Continue same pattern
drum_notes = [
    # Kick on 1 and 3 (Bar 3: 3.0 - 3.375, 4.125 - 4.5)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4 (Bar 3: 3.375 - 3.5, 4.5 - 4.625)
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
