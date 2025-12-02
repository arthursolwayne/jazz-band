
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # F
]

sax.notes.extend(sax_notes)

# Bass line (walking, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=40, start=2.625, end=3.0),   # G
]

bass.notes.extend(bass_notes)

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7 (F A C E)
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=78, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=81, start=1.875, end=2.25),  # F
    # Bar 2, beat 4: F7
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=80, pitch=78, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=80, pitch=81, start=2.625, end=3.0),  # F
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody (reprise)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # F
]

sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),   # G
]

bass.notes.extend(bass_notes)

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: F7
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=78, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=81, start=3.375, end=3.75),  # F
    # Bar 3, beat 4: F7
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=80, pitch=78, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=80, pitch=81, start=4.125, end=4.5),  # F
]

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody (variation)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # Bb
]

sax.notes.extend(sax_notes)

# Bass line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=39, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=38, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),   # G#
]

bass.notes.extend(bass_notes)

# Piano comp: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: F7
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=78, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=81, start=4.875, end=5.25),  # F
    # Bar 4, beat 4: F7
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),  # E
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=80, pitch=78, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=80, pitch=81, start=5.625, end=6.0),  # F
]

piano.notes.extend(piano_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
