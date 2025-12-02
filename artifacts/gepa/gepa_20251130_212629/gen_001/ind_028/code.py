
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bar 2: Full quartet (1.5 - 3.0s)
# D7 chord for Diane (D F# A C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.75),  # C#
    # Chromatic approach on bass (C# to D)
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.75),  # C#
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D
    # Sax motif (D Bb G D)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
]

# Bar 3: Full quartet (3.0 - 4.5s)
# D7 chord again
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # C#
    # Chromatic bass line (D to Eb)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=63, start=3.25, end=3.5),  # Eb
    # Sax motif (G Bb D G)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),  # G
])

# Bar 4: Full quartet (4.5 - 6.0s)
# D7 chord again
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.75),  # C#
    # Chromatic bass line (Eb to E)
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # E
    # Sax motif (D Bb G D) again, with slight variation
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
])

piano.notes.extend(piano_notes)
bass.notes.extend(piano_notes[4:6] + piano_notes[13:15] + piano_notes[22:24])
sax.notes.extend(piano_notes[17:21] + piano_notes[27:31])

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
