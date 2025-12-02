
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

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),   # E

    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=2.125, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),  # E
    pretty_midi.Note(velocity=90, pitch=63, start=2.375, end=2.5),   # Eb

    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=2.75),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.0),   # D
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.625),  # B
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.625),  # D7

    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=80, start=1.875, end=2.0),  # B
    pretty_midi.Note(velocity=90, pitch=82, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=1.875, end=2.0),  # F#

    # Bar 3 (2.0 - 2.5)
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=2.0, end=2.125),  # B
    pretty_midi.Note(velocity=90, pitch=81, start=2.0, end=2.125),  # D7

    pretty_midi.Note(velocity=90, pitch=76, start=2.375, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=80, start=2.375, end=2.5),  # B
    pretty_midi.Note(velocity=90, pitch=82, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=2.375, end=2.5),  # F#

    # Bar 4 (2.5 - 3.0)
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=2.5, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=81, start=2.5, end=2.625),  # D7

    pretty_midi.Note(velocity=90, pitch=76, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=80, start=2.875, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=82, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=84, start=2.875, end=3.0),  # F#
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax. One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 2.0)
    pretty_midi.Note(velocity=110, pitch=74, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=77, start=1.75, end=2.0),  # A

    # Bar 3 (2.0 - 2.5)
    pretty_midi.Note(velocity=110, pitch=77, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.5),  # F

    # Bar 4 (2.5 - 3.0)
    pretty_midi.Note(velocity=110, pitch=74, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=110, pitch=77, start=2.75, end=3.0),  # A
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4 (1.5 - 3.0)
for bar in range(2, 4):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.3125, end=start + 1.5)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
