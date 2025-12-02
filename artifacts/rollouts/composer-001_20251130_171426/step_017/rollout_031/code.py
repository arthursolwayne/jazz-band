
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: Fm7 - Bb7 - Eb7 - Am7
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # F#
    pretty_midi.Note(velocity=90, pitch=66, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=4.25, end=4.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),  # F#
    pretty_midi.Note(velocity=90, pitch=66, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=62, start=5.75, end=6.0),  # D
]

bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # D
    # Bar 3: Bb7
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=77, start=2.25, end=2.5),  # F#
    # Bar 4: Eb7
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25),  # C
    # Bar 4: Am7
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=80, start=3.75, end=4.0),  # C#
    pretty_midi.Note(velocity=90, pitch=82, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=90, pitch=84, start=3.75, end=4.0),  # F#
]

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),  # Eb
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
