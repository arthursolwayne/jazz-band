
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
# Bass line: walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625), # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # E
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=95, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=95, pitch=72, start=1.875, end=2.25),  # C
    # D7 on 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=95, pitch=64, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=2.625, end=3.0),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=2.625, end=3.0),  # B
    pretty_midi.Note(velocity=95, pitch=72, start=2.625, end=3.0),  # C
]

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2 - start the motif
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    # Bar 3 - continuation
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),  # D
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # A
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=95, pitch=64, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=95, pitch=72, start=3.375, end=3.75),  # C
    # D7 on 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=95, pitch=64, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=4.125, end=4.5),  # B
    pretty_midi.Note(velocity=95, pitch=72, start=4.125, end=4.5),  # C
]

# Sax: continuation of motif and resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # D
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # A
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=95, pitch=64, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=95, pitch=72, start=4.875, end=5.25),  # C
    # D7 on 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=95, pitch=64, start=5.625, end=6.0),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=5.625, end=6.0),  # G
    pretty_midi.Note(velocity=95, pitch=71, start=5.625, end=6.0),  # B
    pretty_midi.Note(velocity=95, pitch=72, start=5.625, end=6.0),  # C
]

# Sax: resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # D
]

bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2: 1.5 - 3.0
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

# Bar 3: 3.0 - 4.5
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
])

# Bar 4: 4.5 - 6.0
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
])

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
