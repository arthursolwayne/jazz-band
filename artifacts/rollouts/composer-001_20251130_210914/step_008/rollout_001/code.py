
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

# Bass line: walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.75, end=2.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=50, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=2.75, end=3.0),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=54, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=56, start=3.5, end=3.75),  # C#
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=58, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=59, start=4.25, end=4.5),  # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=4.75, end=5.0),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=63, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.75, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - F7 on 2
    pretty_midi.Note(velocity=100, pitch=48, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # F
    # Bar 3 (3.0 - 4.5s) - F7 on 4
    pretty_midi.Note(velocity=100, pitch=48, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.0, end=4.25),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),  # F
    # Bar 4 (4.5 - 6.0s) - F7 on 2
    pretty_midi.Note(velocity=100, pitch=48, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s) - Motif introduction
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # Bb
    # Bar 3 (3.0 - 4.5s) - Leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # Bb
    # Bar 4 (4.5 - 6.0s) - Come back and finish it
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
