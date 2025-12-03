
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
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # D2 (MIDI 38) on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # F (MIDI 41) on 2
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    # G2 (MIDI 43) on 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    # D2 (MIDI 38) on 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    # Chromatic approach on 3 (C#2, MIDI 37)
    pretty_midi.Note(velocity=80, pitch=37, start=2.125, end=2.25),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C4
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # D4 (MIDI 62) on 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    # F4 (MIDI 65) on 2
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),
    # G4 (MIDI 67) on 3
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
    # D4 (MIDI 62) on 4
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # G2 (MIDI 43) on 1
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    # Bb (MIDI 46) on 2
    pretty_midi.Note(velocity=100, pitch=46, start=3.375, end=3.75),
    # C3 (MIDI 48) on 3
    pretty_midi.Note(velocity=100, pitch=48, start=3.75, end=4.125),
    # G2 (MIDI 43) on 4
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),
    # Chromatic approach on 3 (B, MIDI 45)
    pretty_midi.Note(velocity=80, pitch=45, start=3.875, end=3.75),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: G7 (G-B-D-F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F4
]
piano.notes.extend(piano_notes)

# Sax: Continue motif
sax_notes = [
    # G4 (MIDI 67) on 1
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),
    # B4 (MIDI 71) on 2
    pretty_midi.Note(velocity=110, pitch=71, start=3.375, end=3.75),
    # D5 (MIDI 74) on 3
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.125),
    # G4 (MIDI 67) on 4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # C3 (MIDI 48) on 1
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=4.875),
    # D (MIDI 50) on 2
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),
    # F (MIDI 52) on 3
    pretty_midi.Note(velocity=100, pitch=52, start=5.25, end=5.625),
    # C3 (MIDI 48) on 4
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=6.0),
    # Chromatic approach on 3 (E, MIDI 51)
    pretty_midi.Note(velocity=80, pitch=51, start=5.375, end=5.25),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cmaj7 (C-E-G-B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B4
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # C5 (MIDI 72) on 1
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),
    # E5 (MIDI 76) on 2
    pretty_midi.Note(velocity=110, pitch=76, start=4.875, end=5.25),
    # G5 (MIDI 79) on 3
    pretty_midi.Note(velocity=110, pitch=79, start=5.25, end=5.625),
    # C5 (MIDI 72) on 4
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
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
