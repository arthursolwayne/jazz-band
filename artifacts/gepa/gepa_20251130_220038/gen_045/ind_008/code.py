
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus - Bass line
bass_notes = [
    # Bar 2: D (2) -> C# (11) chromatic approach, G (7)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D2
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75),  # C#2
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # G2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D2
    # Bar 3: A (5) -> Bb (6) chromatic approach, D (2)
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.125),  # A2
    pretty_midi.Note(velocity=90, pitch=70, start=2.125, end=2.25),  # Bb2
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D2
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5),  # A2
    # Bar 4: F# (4) -> G (7) chromatic approach, D (2)
    pretty_midi.Note(velocity=90, pitch=66, start=2.5, end=2.625),  # F#2
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),  # G2
    pretty_midi.Note(velocity=90, pitch=62, start=2.75, end=2.875),  # D2
    pretty_midi.Note(velocity=90, pitch=66, start=2.875, end=3.0),  # F#2
]
bass.notes.extend(bass_notes)

# Diane - Piano comping
piano_notes = [
    # Bar 2: D7 comp on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=1.875),  # A
    # Bar 3: D7 comp on beat 4
    pretty_midi.Note(velocity=90, pitch=67, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.875, end=3.0),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.875, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=2.875, end=3.0),  # A
    # Bar 4: D7 comp on beat 2
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.5, end=3.625),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.625),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625),  # A
]
piano.notes.extend(piano_notes)

# Little Ray - Drums continue
drum_notes = [
    # Bar 2: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    # Bar 3: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.0, end=2.375),
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=90, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.3125, end=3.5),
]
drums.notes.extend(drum_notes)

# Dante - Saxophone melody
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.6875),  # D5
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.1875),  # B5
    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875),  # D5
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
