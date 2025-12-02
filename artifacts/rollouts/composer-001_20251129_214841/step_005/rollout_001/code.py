
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0),   # D#
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.125),  # F#
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),   # G
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=68, start=4.5, end=4.875),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=70, start=5.25, end=5.625),  # A#
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),   # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 on beat 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.625),
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Motif start
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # G
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # G
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=5.625, end=6.0),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
