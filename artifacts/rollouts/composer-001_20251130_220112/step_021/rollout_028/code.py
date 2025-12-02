
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus, walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625), # E
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # F

    # Bar 3
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125), # E
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # F

    # Bar 4
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=47, start=4.875, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625), # F
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano: Diane, 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # F7: F, A, C, E
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),

    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # F7
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),

    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G7: G, B, D, F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.375),

    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # G7
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=4.125),

    # Bar 4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # A7: A, C#, E, G
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),

    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),  # A7
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (65) -> G (67) -> A (69) -> G (67) -> F (65)
# First phrase (Bar 2)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=67, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.4375),

    # Bar 3: leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=67, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=3.9375),

    # Bar 4: finish it
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=67, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.4375),
]
sax.notes.extend(sax_notes)

# Add drum notes for bars 2-4
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat on every eighth
    for i in range(0, 8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
