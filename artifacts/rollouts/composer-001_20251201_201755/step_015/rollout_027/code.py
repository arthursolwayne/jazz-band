
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (38) -> C (43) chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.5),
    # Bar 3: A (40) -> D (38) chromatic approach
    pretty_midi.Note(velocity=80, pitch=40, start=2.5, end=2.875),
    pretty_midi.Note(velocity=80, pitch=39, start=2.875, end=3.125),
    pretty_midi.Note(velocity=80, pitch=38, start=3.125, end=3.5),
    # Bar 4: C (43) -> F (38) chromatic approach
    pretty_midi.Note(velocity=80, pitch=43, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.125),
    pretty_midi.Note(velocity=80, pitch=38, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=2.0),  # E
]
# Bar 3: Am7 (A, C, E, G)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.0, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=77, start=2.0, end=2.5),  # E
    pretty_midi.Note(velocity=90, pitch=76, start=2.0, end=2.5),  # G
])
# Bar 4: F7 (F, A, C, E♭)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=3.0),  # E♭
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (65), A (72), D (62), F (65)
# Play first note at 1.5s, hold through 2.0s
# Play third note at 2.5s, hold through 3.0s
# Play final note at 3.5s, hold through 4.5s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=3.0),
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=4.5),
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
