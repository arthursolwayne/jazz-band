
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

# Bass: Walking line, chromatic approaches, never the same note twice
# Fm bass line: F, Eb, D, C, Bb, A, G, F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),    # F
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),   # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),   # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),    # C
    pretty_midi.Note(velocity=80, pitch=57, start=3.0, end=3.375),    # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=3.375, end=3.75),   # A
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.125),   # G
    pretty_midi.Note(velocity=80, pitch=64, start=4.125, end=4.5),    # F
    pretty_midi.Note(velocity=80, pitch=66, start=4.5, end=4.875),    # F#
    pretty_midi.Note(velocity=80, pitch=64, start=4.875, end=5.25),   # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625),   # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),    # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7 = F, Ab, C, Eb
# Bb7 = Bb, D, F, Ab
piano_notes = [
    # Bar 2, beat 2 (2.25s)
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.375),    # F
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.375),    # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=2.25, end=2.375),    # C
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.375),    # Eb
    # Bar 2, beat 4 (3.0s)
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.125),     # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.125),     # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.125),     # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.125),     # Ab
    # Bar 3, beat 2 (3.75s)
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.875),    # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=3.875),    # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=3.75, end=3.875),    # C
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=3.875),    # Eb
    # Bar 3, beat 4 (4.5s)
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.625),     # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.625),     # D
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.625),     # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.625),     # Ab
    # Bar 4, beat 2 (5.25s)
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.375),    # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.375),    # Ab
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.375),    # C
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.375),    # Eb
    # Bar 4, beat 4 (6.0s)
    pretty_midi.Note(velocity=80, pitch=60, start=6.0, end=6.125),     # Bb
    pretty_midi.Note(velocity=80, pitch=65, start=6.0, end=6.125),     # D
    pretty_midi.Note(velocity=80, pitch=64, start=6.0, end=6.125),     # F
    pretty_midi.Note(velocity=80, pitch=69, start=6.0, end=6.125),     # Ab
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Fm motif: F, Eb, D, C, F, Eb, D, C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),    # F
    pretty_midi.Note(velocity=100, pitch=63, start=1.625, end=1.75),   # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),    # C
    pretty_midi.Note(velocity=100, pitch=63, start=2.375, end=2.5),    # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),    # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=2.875),   # F
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.125),    # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.375),   # C
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.5),    # F#
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=3.625),    # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75),   # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.875),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),    # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
