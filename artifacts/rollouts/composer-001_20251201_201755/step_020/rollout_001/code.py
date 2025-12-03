
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in F, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0),  # Ab2
    pretty_midi.Note(velocity=90, pitch=40, start=2.0, end=2.25),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.5),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.75),  # Bb2
    pretty_midi.Note(velocity=90, pitch=41, start=2.75, end=3.0),  # Ab2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.5),  # Ab2
    pretty_midi.Note(velocity=90, pitch=40, start=3.5, end=3.75),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.0),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=4.0, end=4.25),  # Bb2
    pretty_midi.Note(velocity=90, pitch=41, start=4.25, end=4.5),  # Ab2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.0),  # Ab2
    pretty_midi.Note(velocity=90, pitch=40, start=5.0, end=5.25),  # G2
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.5),  # Bb2
    pretty_midi.Note(velocity=90, pitch=43, start=5.5, end=5.75),  # Bb2
    pretty_midi.Note(velocity=90, pitch=41, start=5.75, end=6.0),  # Ab2
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Fmaj7
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F5
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # A5
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=2.0),  # Bb5
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=2.0),  # D6
    # Bar 3 (3.0 - 4.5s) - Dm7
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # A5
    # Bar 4 (4.5 - 6.0s) - G7
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # F4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.0),  # A4
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=5.0),  # C5
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),  # A5
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.0),  # Bb5
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),  # A5
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.5),  # Bb5
    pretty_midi.Note(velocity=110, pitch=76, start=3.5, end=3.75),  # C6
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=74, start=4.5, end=4.875),  # Bb5
    pretty_midi.Note(velocity=110, pitch=76, start=4.875, end=5.0),  # C6
    pretty_midi.Note(velocity=110, pitch=72, start=5.0, end=5.25),  # A5
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.5),  # Bb5
    pretty_midi.Note(velocity=110, pitch=76, start=5.5, end=5.75),  # C6
    pretty_midi.Note(velocity=110, pitch=79, start=5.75, end=6.0),  # D6
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 (1.5 - 3.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),  # End at 6.0s
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
