
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=45, start=2.625, end=3.0),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=45, start=3.375, end=3.75),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.625),  # Bb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0),  # G2 (fifth)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D5
]
# Bar 3: G7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625),  # F5
])
# Bar 4: Cm7
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # C4
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # E4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # Bb4
])
# Bar 2: Comp on beat 2
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # Bb4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D5
])
# Bar 4: Comp on beat 4
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125),  # C4
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # E4
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # G4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Eb4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
