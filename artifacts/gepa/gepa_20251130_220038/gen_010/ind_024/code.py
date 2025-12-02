
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
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, no repeating notes
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=49, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.625, end=3.0),   # Ab
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.375),   # A
    pretty_midi.Note(velocity=80, pitch=53, start=3.375, end=3.75),   # Bb
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125),   # B
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),    # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=56, start=4.5, end=4.875),    # C#
    pretty_midi.Note(velocity=80, pitch=57, start=4.875, end=5.25),    # D
    pretty_midi.Note(velocity=80, pitch=58, start=5.25, end=5.625),    # Eb
    pretty_midi.Note(velocity=80, pitch=59, start=5.625, end=6.0),     # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=59, start=1.5, end=1.875),  # E (7th)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # G (3rd)
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # Bb (7th)
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G (7th)
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # Bb (3rd)
    pretty_midi.Note(velocity=90, pitch=66, start=3.0, end=3.375),  # D (7th)
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # Bb (7th)
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.875),  # D (3rd)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # F (7th)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),   # G#
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),   # C
    pretty_midi.Note(velocity=100, pitch=81, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=83, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=85, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
