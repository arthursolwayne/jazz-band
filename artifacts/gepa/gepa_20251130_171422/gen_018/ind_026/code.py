
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=52, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=54, start=1.75, end=1.875),  # D#
    pretty_midi.Note(velocity=100, pitch=55, start=1.875, end=2.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=57, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=100, pitch=56, start=2.125, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=2.375),  # G#
    pretty_midi.Note(velocity=100, pitch=59, start=2.375, end=2.5),  # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=61, start=2.5, end=2.625),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.875, end=3.0),  # C#
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4) - D7
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875),  # D
    # Bar 3 (comp on 2 and 4) - D7
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.375),  # D
    # Bar 4 (comp on 2 and 4) - D7
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=2.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),  # B
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=2.875),  # D
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, short motif, start it, leave it hanging, return to finish
sax_notes = [
    # Bar 2 - Start of motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G
    # Bar 3 - Leave it hanging
    pretty_midi.Note(velocity=110, pitch=68, start=2.0, end=2.125),  # G#
    # Bar 4 - Return to finish the motif
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
