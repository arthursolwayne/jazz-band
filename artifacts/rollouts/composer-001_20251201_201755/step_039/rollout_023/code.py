
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on 1
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # F (MIDI 41) on 2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.125),
    # G2 (MIDI 43) on 3
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.5),
    # D2 (MIDI 38) on 4
    pretty_midi.Note(velocity=80, pitch=38, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # C5
]
piano.notes.extend(piano_notes)

# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=3.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - G4 - D4 (start on 1, leave it hanging on G4 at the end of bar 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.125),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.5),   # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # G4 (leave it hanging)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # F (MIDI 41) on 1
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375),
    # G2 (MIDI 43) on 2
    pretty_midi.Note(velocity=80, pitch=43, start=3.375, end=3.625),
    # A (MIDI 45) on 3
    pretty_midi.Note(velocity=80, pitch=45, start=3.625, end=4.0),
    # D2 (MIDI 38) on 4
    pretty_midi.Note(velocity=80, pitch=38, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # F4
]
piano.notes.extend(piano_notes)

# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=4.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=4.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on 1
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),
    # F (MIDI 41) on 2
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.125),
    # G2 (MIDI 43) on 3
    pretty_midi.Note(velocity=80, pitch=43, start=5.125, end=5.5),
    # D2 (MIDI 38) on 4
    pretty_midi.Note(velocity=80, pitch=38, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last. Comp on 2 and 4.
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=5.0),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, finish the motif (return to D4 at the end of bar 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.375),  # D4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
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
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
