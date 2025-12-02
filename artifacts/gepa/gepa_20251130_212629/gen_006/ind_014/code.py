
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line (walking line, chromatic approaches)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),  # D#
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),  # D#
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # E
]
bass.notes.extend(bass_notes)

# Diane - Piano comping (7th chords, on 2 and 4)
piano_notes = []
# Bar 2 (on 2 and 4)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # D7 - C
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # D7 - E
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),  # D7 - F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # D7 - A
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),   # D7 - C
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),   # D7 - E
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # D7 - F#
])
# Bar 3 (on 2 and 4)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # D7 - C
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D7 - E
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # D7 - F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # D7 - A
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),   # D7 - C
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),   # D7 - E
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),   # D7 - F#
])
# Bar 4 (on 2 and 4)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # D7 - A
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # D7 - C
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # D7 - E
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),  # D7 - F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # D7 - A
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # D7 - C
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),   # D7 - E
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),   # D7 - F#
])
piano.notes.extend(piano_notes)

# Dante - Sax melody (one short motif, make it sing. Start it, leave it hanging. Come back and finish it.)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.125, end=4.5),   # A
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),   # D
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
