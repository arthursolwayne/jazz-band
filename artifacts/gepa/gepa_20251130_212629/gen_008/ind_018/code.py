
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=52, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),   # D#
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0),   # G#
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # F
    # Bar 3: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # F
    # Bar 4: F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # F
]

piano.notes.extend(piano_notes)

# Sax: Motif starts in bar 2, leaves it hanging, comes back in bar 4
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),   # D
    # Bar 3: Silence to leave it hanging
    # Bar 4: Return to finish the motif
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=110, pitch=74, start=5.625, end=6.0),   # F
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
