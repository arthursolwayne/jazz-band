
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Dm (D2-G2, MIDI 38-43)
# Roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Ab2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),  # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),  # G#2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),  # D2
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25),  # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=44, start=5.25, end=5.625),  # Bb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chords each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C5
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Bb4
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # F5
])
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # Eb5
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # Bb5
])
piano.notes.extend(piano_notes)

# Sax: short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D, F, G, D (hanging on G)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.125),  # D4 (come back)
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25),  # G4 (finish)
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.375),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.75),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # D4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
