
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax melody starts
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # F
]
sax.notes.extend(sax_notes)

# Bass line (walking, chromatic approach)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # F
]
bass.notes.extend(bass_notes)

# Piano chords (7th chords, comp on 2 and 4)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # G7
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Everyone in (3.0 - 4.5s)
# Sax continues melody
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # F
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.5),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),  # F
]
bass.notes.extend(bass_notes)

# Piano chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # G7
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # G7
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Bar 4: Everyone in (4.5 - 6.0s)
# Sax completes melody
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),  # F
]
bass.notes.extend(bass_notes)

# Piano chords
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # G7
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # G7
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Drums continue (bar 3 and 4)
# Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
