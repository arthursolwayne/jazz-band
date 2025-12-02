
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
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25), # Gb
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.625), # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=45, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75), # F
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=90, pitch=45, start=4.125, end=4.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: Diane
piano_notes = [
    # Bar 2: 7th chords on 2 and 4
    pretty_midi.Note(velocity=95, pitch=59, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=95, pitch=59, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),  # D
    # Bar 3: 7th chords on 2 and 4
    pretty_midi.Note(velocity=95, pitch=57, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=95, pitch=60, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=95, pitch=65, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=95, pitch=57, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=95, pitch=60, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=95, pitch=65, start=4.875, end=5.25),  # C
    # Bar 4: 7th chords on 2 and 4
    pretty_midi.Note(velocity=95, pitch=55, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=95, pitch=58, start=5.625, end=6.0),  # Eb
    pretty_midi.Note(velocity=95, pitch=60, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=95, pitch=63, start=5.625, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: Dante
sax_notes = [
    # Bar 2: Motif starts here
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=2.0),  # G
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # A
    # Bar 4: Come back and finish
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.5),  # G
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Add all instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("wayne_intro.mid")
