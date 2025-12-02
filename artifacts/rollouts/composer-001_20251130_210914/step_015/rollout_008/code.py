
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
# Sax: short motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # F (resting)
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=47, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.625),  # F7: F
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # F7: A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F7: C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625),  # F7: Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation of the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # Bb (resting)
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=59, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),  # G7: G
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # G7: B
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),  # G7: D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # G7: F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.375),  # G
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: resolution of the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.0),  # F (resting)
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # A7: A
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # A7: C
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625),  # A7: E
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),  # A7: G
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=4.875),  # B
]
piano.notes.extend(piano_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
