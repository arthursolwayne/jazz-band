
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

# Marcus (bass): Walking line, chromatic approaches
bass_notes = [
    # Dm7 - F - G - Bb - D
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=3.75, end=4.125),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Diane (piano): 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 on 1
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # Bb

    # Comp on 2
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),  # Bb

    # Comp on 3
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # Bb

    # Comp on 4
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # Bb
]
piano.notes.extend(piano_notes)

# Dante (sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=105, pitch=67, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=105, pitch=69, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=105, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=2.625, end=3.0),  # E

    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=105, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=105, pitch=67, start=3.75, end=4.125),  # G

    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=105, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=105, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=105, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=105, pitch=62, start=5.625, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
