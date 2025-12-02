
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=59, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0),  # F#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=70, start=4.125, end=4.5),  # B
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=73, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=80, pitch=75, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=5.625, end=6.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # F
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # F
]
piano.notes.extend(piano_notes)

# Sax: Melody with one short motif, leave it hanging
sax_notes = [
    # Bar 2: Motif begins
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Bb
    # Bar 3: Let it hang
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # Bb
    # Bar 4: Return and finish
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # Eb
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
