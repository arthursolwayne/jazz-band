
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in D, chromatic approaches
bass_notes = [
    # Bar 2: D - C# - D - E
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    # Bar 3: F - E - F - G
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    # Bar 4: A - G - A - B
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 & 4, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.625),
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.125),
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=95, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),
    pretty_midi.Note(velocity=95, pitch=69, start=5.25, end=5.625)
]
piano.notes.extend(piano_notes)

# Sax: Motif in D, short and singable, start and finish it
sax_notes = [
    # Bar 2: D (62) - F (65) - D (62) - E (64)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),
    # Bar 3: D (62) - F (65) - G (67) - E (64)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=64, start=4.125, end=4.5),
    # Bar 4: D (62) - F (65) - G (67) - B (71)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

# Add all instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
midi.write("wayne_intro.mid")
