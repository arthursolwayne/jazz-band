
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in Fm, chromatic approach to Gb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=80, pitch=41, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=39, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=80, pitch=40, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.375),  # E
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=2.625),  # F#
    pretty_midi.Note(velocity=80, pitch=44, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.75, end=2.875),  # F#
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: 7th chord on 2 (Gbm7)
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=1.875),  # G
    # Bar 2: 7th chord on 4 (F7)
    pretty_midi.Note(velocity=100, pitch=53, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # A
    # Bar 3: 7th chord on 2 (Gbm7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.375),  # G
    # Bar 3: 7th chord on 4 (F7)
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.75, end=3.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # A
    # Bar 4: 7th chord on 2 (Gbm7)
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.375),  # Gb
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.375),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.375),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=4.25, end=4.375),  # G
    # Bar 4: 7th chord on 4 (F7)
    pretty_midi.Note(velocity=100, pitch=53, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # A
]
piano.notes.extend(piano_notes)

# Sax: Melody in Fm, single motif with space
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # Gb
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=1.75, end=1.875),  # Gb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=60, start=2.5, end=2.625),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75),  # Gb
    pretty_midi.Note(velocity=110, pitch=60, start=2.75, end=2.875),  # E
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.625),  # Gb
    pretty_midi.Note(velocity=110, pitch=65, start=3.625, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.875),  # Gb
    pretty_midi.Note(velocity=110, pitch=60, start=3.875, end=4.0),  # E
    pretty_midi.Note(velocity=110, pitch=58, start=4.0, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=55, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=53, start=4.25, end=4.375),  # F
]
sax.notes.extend(sax_notes)

# Bar 2: Drums continue (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Drums continue (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
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

# Bar 4: Drums continue (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
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

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_sax_intro.mid")
