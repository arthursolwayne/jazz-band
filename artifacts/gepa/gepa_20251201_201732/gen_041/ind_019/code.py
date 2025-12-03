
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (43)
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=43, start=2.0, end=2.25),
    # Bar 3: G2 (43)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),
    # Chromatic approach to C3 (48)
    pretty_midi.Note(velocity=80, pitch=47, start=2.625, end=2.875),
    pretty_midi.Note(velocity=80, pitch=48, start=2.875, end=3.125),
    # Bar 4: C3 (48)
    pretty_midi.Note(velocity=80, pitch=48, start=3.125, end=3.5),
    # Chromatic approach to F3 (53)
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75),
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, resolve on the last chord
piano_notes = [
    # Bar 2: Dmaj7 (D4, F#4, A4, C#5)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),
    # Bar 3: G7 (G4, B4, D5, F5)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=2.625),
    # Bar 4: Cmaj7 (C4, E4, G4, B4)
    pretty_midi.Note(velocity=100, pitch=60, start=3.125, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.125, end=3.5),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging
sax_notes = [
    # Bar 2: Start motif (D4, F4, G4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=65, start=2.375, end=2.5),
    # Bar 4: Finish the motif with a twist (F4 to E4)
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
