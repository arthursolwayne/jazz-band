
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # F
]

sax.notes.extend(sax_notes)

# Bass line (walking with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),   # D
]

bass.notes.extend(bass_notes)

# Piano (7th chords on 2 and 4)
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - 7th chord on 2 (1.875)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # F
    # Bar 3 (3.0 - 4.5s) - 7th chord on 4 (3.375)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # F
]

piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone motif (rest, then repeat)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # F
]

sax.notes.extend(sax_notes)

# Bass line (walking with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # D
]

bass.notes.extend(bass_notes)

# Piano (7th chords on 2 and 4)
piano_notes = [
    # Bar 3 (3.0 - 4.5s) - 7th chord on 2 (3.375)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # F
    # Bar 4 (4.5 - 6.0s) - 7th chord on 4 (4.875)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # F
]

piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone motif (rest, then finish)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # F
]

sax.notes.extend(sax_notes)

# Bass line (walking with chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # D
]

bass.notes.extend(bass_notes)

# Drums: Bar 3 and 4
for i in range(3, 6):
    start = i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start+0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start+1.125, end=start+1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start+0.75, end=start+1.125)
    pretty_midi.Note(velocity=100, pitch=38, start=start+1.875, end=start+2.25)
    # Hi-hat on every eighth
    for j in range(0, 4):
        pretty_midi.Note(velocity=100, pitch=42, start=start+j*0.375, end=start+j*0.375+0.375)

drums.notes.extend([note for note in drum_notes if note not in drums.notes])

midi.instruments.extend([sax, bass, piano, drums])
