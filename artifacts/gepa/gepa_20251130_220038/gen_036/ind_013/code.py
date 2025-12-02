
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

# Bar 2: Sax enters with a motif in F minor (1.5 - 3.0s)
# F minor scale: F, Gb, G, Ab, A, Bb, B, C
# Motif: F, Ab, Bb, G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),   # G
]

sax.notes.extend(sax_notes)

# Bass line (Marcus): Walking line, chromatic approaches, no repeated notes
# F7 chord: F, A, C, Eb
# Walking bass in F minor: F, Gb, G, Ab, A, Bb, B, C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),   # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.25),   # G
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.5),   # Ab
]

bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# F7 chord: F, A, C, Eb
# Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),   # Eb
]

piano.notes.extend(piano_notes)

# Bar 3: Sax continues motif, twist it (3.0 - 4.5s)
# Motif variation: Ab, Bb, C, F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),   # F
]

sax.notes.extend(sax_notes)

# Bass line (Marcus): Continue walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=80, pitch=70, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=3.5, end=3.75),   # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),   # C
]

bass.notes.extend(bass_notes)

# Piano (Diane): Comp again
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=68, start=3.25, end=3.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),   # C
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),   # F
]

piano.notes.extend(piano_notes)

# Bar 4: Sax resolves, build to climax (4.5 - 6.0s)
# Motif resolution: F, Ab, Bb, G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0),   # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),   # G
]

sax.notes.extend(sax_notes)

# Bass line (Marcus): Continue walking
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),   # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=5.0, end=5.25),   # G
    pretty_midi.Note(velocity=80, pitch=68, start=5.25, end=5.5),   # Ab
]

bass.notes.extend(bass_notes)

# Piano (Diane): Comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),   # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),   # A
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),   # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),   # Eb
]

piano.notes.extend(piano_notes)

# Drums: repeat the pattern (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),
]

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
