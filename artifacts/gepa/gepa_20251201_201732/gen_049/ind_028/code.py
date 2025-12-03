
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> C#2 (37) -> G2 (43)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=75, pitch=37, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),

    # Bar 3: G2 (43) -> F#2 (42) -> D2 (38)
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=75, pitch=42, start=2.8125, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=38, start=3.1875, end=3.5625),

    # Bar 4: D2 (38) -> C#2 (37) -> G2 (43)
    pretty_midi.Note(velocity=80, pitch=38, start=3.5625, end=3.9375),
    pretty_midi.Note(velocity=75, pitch=37, start=3.9375, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=43, start=4.3125, end=4.6875),
]
bass.notes.extend(bass_notes)

# Piano (Dm7, Gm7, Amaj7, D7)
# Open voicings, resolve on the last bar
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=85, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=85, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),

    # Bar 4: Amaj7 (A, C#, E, G#)
    pretty_midi.Note(velocity=100, pitch=69, start=3.1875, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=74, start=3.1875, end=3.5625),
    pretty_midi.Note(velocity=85, pitch=72, start=3.1875, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=76, start=3.1875, end=3.5625),

    # Bar 4: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5625, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.5625, end=4.3125),
    pretty_midi.Note(velocity=85, pitch=69, start=3.5625, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=74, start=3.5625, end=4.3125),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4, F4, G4, (rest), then D4, F4, G4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=105, pitch=67, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=105, pitch=67, start=3.9375, end=4.125)
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.5625, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.1875, end=3.3125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
