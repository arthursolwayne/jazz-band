
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # F#2 (MIDI 41) chromatic approach to G2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.125),
    # G2 (MIDI 43)
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.5),
    # Bb2 (MIDI 42) chromatic approach to A2
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.75),
    # A2 (MIDI 41)
    pretty_midi.Note(velocity=80, pitch=41, start=2.75, end=3.0),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=90, pitch=73, start=1.5, end=1.75),  # C#4
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25),  # F4
    # Bar 4: A7 (A-C#-E-G)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),  # A4
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.75),  # C#4
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.75),  # E4
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.75),  # G4
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=90, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=90, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.125, end=2.5),
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),
    # F#2 (MIDI 41) chromatic approach to G2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.625),
    # G2 (MIDI 43)
    pretty_midi.Note(velocity=80, pitch=43, start=3.625, end=4.0),
    # Bb2 (MIDI 42) chromatic approach to A2
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.25),
    # A2 (MIDI 41)
    pretty_midi.Note(velocity=80, pitch=41, start=4.25, end=4.5),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25),
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=4.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    # F#2 (MIDI 41) chromatic approach to G2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.125),
    # G2 (MIDI 43)
    pretty_midi.Note(velocity=80, pitch=43, start=5.125, end=5.5),
    # Bb2 (MIDI 42) chromatic approach to A2
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.75),
    # A2 (MIDI 41)
    pretty_midi.Note(velocity=80, pitch=41, start=5.75, end=6.0),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 4: A7 (A-C#-E-G)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=81, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.6875, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

# Dante's sax line: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif (E4, G4, Bb4)
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # Bb4
    # Bar 3: Leave it hanging (hold Bb4)
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    # Bar 4: Resolve back to E4 and end the motif
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
