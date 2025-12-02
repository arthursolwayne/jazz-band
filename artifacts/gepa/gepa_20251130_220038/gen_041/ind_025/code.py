
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in D, chromatic approach to C# on beat 3
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.625),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F#
    # Bar 3: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F#
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F#
]
piano.notes.extend(piano_notes)

# Sax: Short motif, sing it, leave it hanging
# D (62) -> F# (64) -> C# (61) -> D (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=61, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0625, end=2.25),
    # Return to finish the motif
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=3.75),
    # Final phrase to finish it
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=61, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (1.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=90, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=36, start=4.875, end=5.25),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625)
]
drums.notes.extend(drum_notes)

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
