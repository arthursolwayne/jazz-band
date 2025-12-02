
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

# Bass line (Marcus): Walking line in F, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.6875, end=1.875),  # F#
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.0625, end=2.25),  # G#
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.4375),  # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.4375, end=2.625),  # A#
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=2.8125),  # B
    pretty_midi.Note(velocity=80, pitch=52, start=2.8125, end=3.0),  # C
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.1875),  # C#
    pretty_midi.Note(velocity=80, pitch=54, start=3.1875, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=3.375, end=3.5625),  # D#
    pretty_midi.Note(velocity=80, pitch=56, start=3.5625, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=80, pitch=58, start=3.9375, end=4.125),  # F#
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.3125),  # G
    pretty_midi.Note(velocity=80, pitch=60, start=4.3125, end=4.5),  # G#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=61, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=80, pitch=62, start=4.6875, end=4.875),  # A#
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.0625),  # B
    pretty_midi.Note(velocity=80, pitch=64, start=5.0625, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.4375),  # C#
    pretty_midi.Note(velocity=80, pitch=66, start=5.4375, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=5.8125),  # D#
    pretty_midi.Note(velocity=80, pitch=68, start=5.8125, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - 2nd beat
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.375),  # F7: F, A, C, E
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.375),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),  # E
    # Bar 2 (1.5 - 3.0s) - 4th beat
    pretty_midi.Note(velocity=90, pitch=53, start=2.875, end=3.0),  # F7
    pretty_midi.Note(velocity=90, pitch=58, start=2.875, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.875, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=2.875, end=3.0),  # E
    # Bar 3 (3.0 - 4.5s) - 2nd beat
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=3.875),  # F7: F, A, C, E
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=3.875),  # E
    # Bar 3 (3.0 - 4.5s) - 4th beat
    pretty_midi.Note(velocity=90, pitch=57, start=4.375, end=4.5),  # F7
    pretty_midi.Note(velocity=90, pitch=62, start=4.375, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.375, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=4.375, end=4.5),  # E
    # Bar 4 (4.5 - 6.0s) - 2nd beat
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.375),  # F7
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.375),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.375),  # E
    # Bar 4 (4.5 - 6.0s) - 4th beat
    pretty_midi.Note(velocity=90, pitch=57, start=5.875, end=6.0),  # F7
    pretty_midi.Note(velocity=90, pitch=62, start=5.875, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=5.875, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=68, start=5.875, end=6.0),  # E
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (65), G (67), Bb (62), F (65)

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.75),  # F (return)
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
