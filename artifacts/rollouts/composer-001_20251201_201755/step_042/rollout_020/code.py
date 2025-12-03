
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

# Bass line (Marcus): Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (38) -> F (41) chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=41, start=2.125, end=2.5),
    # Bar 3: A (45) -> G (43) chromatic approach
    pretty_midi.Note(velocity=90, pitch=45, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=44, start=2.875, end=3.125),
    pretty_midi.Note(velocity=90, pitch=43, start=3.125, end=3.5),
    # Bar 4: D (38) -> C (40) chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=39, start=3.875, end=4.125),
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes_bar2 = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # C4
]
# Bar 3: G7 (G, B, D, F)
piano_notes_bar3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),  # F4
]
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes_bar4 = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),  # B4
]
piano.notes.extend(piano_notes_bar2 + piano_notes_bar3 + piano_notes_bar4)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F4 (65), A4 (69), D5 (72)
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.125),
    pretty_midi.Note(velocity=110, pitch=69, start=2.125, end=2.5),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.875),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.875),
    pretty_midi.Note(velocity=110, pitch=69, start=3.875, end=4.125),
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=62, start=4.375, end=4.5),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2
drum_notes_bar2 = [
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
# Bar 3
drum_notes_bar3 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=3.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0625, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.8125, end=4.0),
]
# Bar 4
drum_notes_bar4 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.25, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=5.375, end=5.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0625, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.4375, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.8125, end=5.0),
]
drums.notes.extend(drum_notes_bar2 + drum_notes_bar3 + drum_notes_bar4)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
