
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
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

# Bass line (Marcus): Walking line in Dm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=95, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=95, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=95, pitch=62, start=2.625, end=3.0),   # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.25s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # D
    # Bar 3 (2.25 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625), # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): Short motif starting on beat 1 of bar 2 (1.5s)
# Melody: D - Eb - C - D (half note on D, quarter on Eb, eighth on C, eighth on D)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=2.25),  # D (half note)
    pretty_midi.Note(velocity=110, pitch=63, start=2.25, end=2.625), # Eb (eighth note)
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=2.8125), # C (eighth note)
    pretty_midi.Note(velocity=110, pitch=62, start=2.8125, end=3.0), # D (eighth note)
]
sax.notes.extend(sax_notes)

# Bar 3 and Bar 4: continuation of the pattern

# Bar 3 (3.0 - 4.5s)
# Drums
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
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

# Bass (Marcus): Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=95, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=95, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=95, pitch=62, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=95, pitch=60, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=95, pitch=62, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano (Diane): Continue 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 3.75s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # D
    # Bar 4 (3.75 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125), # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125), # D
    # Bar 4 (4.5 - 5.25s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax (Dante): Continue the motif, ending on D
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.75),   # D (quarter note)
    pretty_midi.Note(velocity=110, pitch=63, start=3.75, end=4.125), # Eb (eighth note)
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.3125), # C (eighth note)
    pretty_midi.Note(velocity=110, pitch=62, start=4.3125, end=4.5), # D (eighth note)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=5.25),   # D (quarter note)
    pretty_midi.Note(velocity=110, pitch=63, start=5.25, end=5.625), # Eb (eighth note)
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=5.8125), # C (eighth note)
    pretty_midi.Note(velocity=110, pitch=62, start=5.8125, end=6.0), # D (eighth note)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
