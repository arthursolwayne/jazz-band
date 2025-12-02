
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

# Bass line: walking line in F, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),  # F#3
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E3
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F3
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G3
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # G#3
    pretty_midi.Note(velocity=90, pitch=66, start=3.75, end=4.125),  # F#3
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # G3
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A3
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),  # A#3
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),  # G#3
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # A3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.875),  # F3
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.875),  # A3
    pretty_midi.Note(velocity=95, pitch=71, start=1.5, end=1.875),  # C4
    pretty_midi.Note(velocity=95, pitch=72, start=1.5, end=1.875),  # C#4
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.625),  # F3
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.625),  # A3
    pretty_midi.Note(velocity=95, pitch=71, start=2.25, end=2.625),  # C4
    pretty_midi.Note(velocity=95, pitch=72, start=2.25, end=2.625),  # C#4
    # Bar 3
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.125),  # A3
    pretty_midi.Note(velocity=95, pitch=71, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=95, pitch=72, start=3.75, end=4.125),  # C#4
    pretty_midi.Note(velocity=95, pitch=76, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.875),   # A3
    pretty_midi.Note(velocity=95, pitch=71, start=4.5, end=4.875),   # C4
    pretty_midi.Note(velocity=95, pitch=72, start=4.5, end=4.875),   # C#4
    pretty_midi.Note(velocity=95, pitch=76, start=4.5, end=4.875),   # E4
    # Bar 4
    pretty_midi.Note(velocity=95, pitch=69, start=5.625, end=6.0),  # A#3
    pretty_midi.Note(velocity=95, pitch=72, start=5.625, end=6.0),  # C#4
    pretty_midi.Note(velocity=95, pitch=76, start=5.625, end=6.0),  # E4
    pretty_midi.Note(velocity=95, pitch=77, start=5.625, end=6.0),  # F4
]
piano.notes.extend(piano_notes)

# Saxophone: short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # F#3
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A3
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F#3
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A3
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.625),  # C4
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # A3
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
