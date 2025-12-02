
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.375, end=2.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.75, end=2.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.875, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: Diane
# 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),  # D7
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=2.875),
]
piano.notes.extend(piano_notes)

# Sax: Dante
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # E
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # E
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
