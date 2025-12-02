
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),    # Snare on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),     # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),      # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),     # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),     # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),      # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),      # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),     # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),     # B
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),      # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),      # D
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),     # Eb
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),     # F
    pretty_midi.Note(velocity=90, pitch=81, start=5.625, end=6.0),      # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),     # G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),    # A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),    # G7 again
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),     # G7 again
    pretty_midi.Note(velocity=100, pitch=76, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),     # G7 again
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),    # G7 again
    pretty_midi.Note(velocity=100, pitch=76, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
]
piano.notes.extend(piano_notes)

# Drums continue: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),     # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),     # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),     # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),     # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),     # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),     # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),     # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),     # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),    # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),    # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),     # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),     # Hihat on 4
]
drums.notes.extend(drum_notes)

# Saxophone: Whisper at first, then a cry. Make it sing.
sax_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),      # F (first note)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),     # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),      # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),     # G (return)
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),      # F (return)
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),     # Eb (cry)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),      # D (resolve)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
