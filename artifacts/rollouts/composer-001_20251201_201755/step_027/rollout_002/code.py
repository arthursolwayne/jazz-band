
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

# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) -> F#2 (41) chromatic approach to G2 (43)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    # Bar 3: G2 (43) -> A2 (45) chromatic approach to B2 (47)
    pretty_midi.Note(velocity=90, pitch=43, start=2.375, end=2.75),
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),
    # Bar 4: B2 (47) -> C#3 (49) chromatic approach to D3 (50)
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=49, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=50, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D-F#-A-C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C#4
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # F4
])
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # Bb4
])
piano.notes.extend(piano_notes)

# You: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62), F#4 (67), A4 (71), D5 (72)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5),  # D5
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=3.25, end=3.5),  # D5
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=4.0, end=4.25),  # A4
    pretty_midi.Note(velocity=110, pitch=72, start=4.25, end=4.5),  # D5
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.9375, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.3125, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
