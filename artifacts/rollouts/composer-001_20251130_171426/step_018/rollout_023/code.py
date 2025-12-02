
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=54, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),   # B
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=56, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=90, pitch=58, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=5.625, end=6.0),   # D#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 2 - F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=81, start=1.5, end=1.875),  # E
    # Bar 3 - Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=80, start=3.0, end=3.375),  # Ab
    # Bar 4 - D7 (D, F#, A, C)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 - Motif starts
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),   # E
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),   # E
    # Bar 3 - Leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),   # E
    # Bar 4 - Come back and finish it
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),   # E
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),   # D
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.5),   # E
    pretty_midi.Note(velocity=110, pitch=71, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=110, pitch=72, start=5.75, end=6.0),   # F#
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
