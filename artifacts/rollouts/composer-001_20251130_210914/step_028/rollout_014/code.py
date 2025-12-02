
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

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=43, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=90, pitch=44, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=45, start=2.25, end=2.5),  # G#
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=90, pitch=47, start=3.25, end=3.5),  # A#
    pretty_midi.Note(velocity=90, pitch=48, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.0),  # B
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=90, pitch=52, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.5),  # C#
    pretty_midi.Note(velocity=90, pitch=54, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=5.75, end=6.0),  # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=54, start=1.5, end=1.75),  # D (F7)
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=54, start=2.25, end=2.5),  # D (F7)
    pretty_midi.Note(velocity=90, pitch=57, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=54, start=3.0, end=3.25),  # D (F7)
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.0),  # D (F7)
    pretty_midi.Note(velocity=90, pitch=57, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=54, start=4.5, end=4.75),  # D (F7)
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=54, start=5.25, end=5.5),  # D (F7)
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # Bb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Additional drum fills for bar 3 and 4
drum_notes = [
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625),  # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_introduction.mid')
