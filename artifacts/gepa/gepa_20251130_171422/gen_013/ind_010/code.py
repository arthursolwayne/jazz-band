
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=49, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=51, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.0),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.125),  # B
    pretty_midi.Note(velocity=100, pitch=55, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=56, start=3.25, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.5),  # E
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.625),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=57, start=1.75, end=1.875),  # E7
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=1.875),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.375),  # E7
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.25, end=3.375),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=4.875),  # E7
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=4.875),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.0),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # D
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.625),  # B
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0),  # C
]
sax.notes.extend(sax_notes)

# Drums (bars 2-4)
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.75, end=1.875),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hi-hat
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.125),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.25, end=3.375),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),    # Hi-hat
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=4.875),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),    # Hi-hat
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
