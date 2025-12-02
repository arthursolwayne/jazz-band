
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: C - B - Bb - A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=3.0),
    # Bar 3: G - F# - F - E
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),
    # Bar 4: C - B - Bb - A (repeat)
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),
    # Bar 3: G7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=78, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: C - Bb - B - C (first bar), then repeat with slight variation
sax_notes = [
    # Bar 2: C - Bb - B - C
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=63, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=60, start=2.625, end=3.0),
    # Bar 3: Bb - B - C - Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),
    # Bar 4: C - Bb - B - C (finish the motif)
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=63, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=60, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 4):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for bar in range(2, 4):
    start = bar * 1.5
    for offset in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:
        pretty_midi.Note(velocity=90, pitch=42, start=start + offset, end=start + offset + 0.1875)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
