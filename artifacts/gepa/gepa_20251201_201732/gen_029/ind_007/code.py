
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=38, start=2.125, end=2.5),
    # Bar 3: A2 (fifth of D) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.125),
    pretty_midi.Note(velocity=100, pitch=43, start=3.125, end=3.5),
    # Bar 4: D2 (root) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=38, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=37, start=3.875, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    # Bar 5: A2 (fifth of D) with chromatic approach
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=43, start=5.125, end=5.5)
]
bass.notes.extend(bass_notes)

# Piano: Diane, open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.875),
    # Bar 4: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.875),
    # Bar 5: C#m7 (C#-E-G-B)
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875)
]
piano.notes.extend(piano_notes)

# Sax: Dante, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Melody starts
    pretty_midi.Note(velocity=110, pitch=69, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # G4
    # Bar 3: Let it hang, then return
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # G4
    # Bar 4: End the phrase
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # E4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 2.625, end=start + 3.0)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
