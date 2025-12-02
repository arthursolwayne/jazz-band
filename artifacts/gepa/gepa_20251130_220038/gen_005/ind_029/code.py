
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=110, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=110, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=110, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=110, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=110, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=110, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=110, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=110, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=1.75, end=1.875),  # D#
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=2.125, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=2.625, end=2.75),  # D#
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # D
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.125, end=3.25),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),  # C
    # Bar 6
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.625, end=3.75),  # D#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.875, end=4.0),  # C
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4. Stay out of your way but keep it moving.
piano_notes = [
    # Bar 2: D7 (D F# A C)
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.625),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # C
    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.125),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # F
    # Bar 4: C7 (C E G B)
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.625),  # B
    # Bar 5: F7 (F A C E)
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # E
    # Bar 6: G7 (G B D F)
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.625),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625),  # F
]
piano.notes.extend(piano_notes)

# Dante: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.625),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=1.625, end=1.75),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.125),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.375, end=2.5),  # A
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.75, end=2.875),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=2.875, end=3.0),  # A
    # Bar 5
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5),  # A
    # Bar 6
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.625),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=3.625, end=3.75),  # A
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=110, pitch=69, start=3.875, end=4.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-6
for bar in range(2, 6):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=110, pitch=42, start=start + i*0.1875, end=start + (i+1)*0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
