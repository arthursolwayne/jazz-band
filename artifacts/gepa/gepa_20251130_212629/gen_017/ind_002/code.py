
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus on bass: Walking line, chromatic approaches, no same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=2.875),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.875),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=4.0, end=4.125),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.375),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=4.375, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=80, pitch=67, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=80, pitch=62, start=5.375, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=62, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.625, end=5.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=64, start=5.75, end=5.875),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=5.875, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Diane on piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # A
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D7: D
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # A
]
piano.notes.extend(piano_notes)

# Dante on sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875),  # E
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.625),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875),  # E
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=3.875),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.125),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.25, end=4.375),  # A
]
sax.notes.extend(sax_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_introduction.mid")
