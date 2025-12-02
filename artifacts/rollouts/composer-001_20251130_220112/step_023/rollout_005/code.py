
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=73, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # D
]

bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # D7: D
    pretty_midi.Note(velocity=90, pitch=79, start=1.875, end=2.25),  # D7: A
    pretty_midi.Note(velocity=90, pitch=81, start=1.875, end=2.25),  # D7: C
    pretty_midi.Note(velocity=90, pitch=83, start=1.875, end=2.25),  # D7: D
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # D7: D
    pretty_midi.Note(velocity=90, pitch=79, start=3.375, end=3.75),  # D7: A
    pretty_midi.Note(velocity=90, pitch=81, start=3.375, end=3.75),  # D7: C
    pretty_midi.Note(velocity=90, pitch=83, start=3.375, end=3.75),  # D7: D
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # D7: D
    pretty_midi.Note(velocity=90, pitch=79, start=4.875, end=5.25),  # D7: A
    pretty_midi.Note(velocity=90, pitch=81, start=4.875, end=5.25),  # D7: C
    pretty_midi.Note(velocity=90, pitch=83, start=4.875, end=5.25),  # D7: D
]

piano.notes.extend(piano_notes)

# Dante: Melody - one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A
    # Bar 3 (3.0 - 4.5)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # G
    # Bar 4 (4.5 - 6.0)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),  # D
]

sax.notes.extend(sax_notes)

# Drums: Bar 2 (1.5 - 3.0)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),      # Hihat
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),   # Snare
]

# Bar 3 (3.0 - 4.5)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
])

# Bar 4 (4.5 - 6.0)
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
])

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
