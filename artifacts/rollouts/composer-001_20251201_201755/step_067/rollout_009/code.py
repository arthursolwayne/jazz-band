
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

# Bar 2: Everyone in. Sax takes melody
# Dmaj7 -> G7 -> A7 -> Dmaj7
# Piano: Open voicings
piano_notes = [
    # Bar 2: Dmaj7 (D-F#-A-C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=2.0),  # C#5
    # Bar 3: G7 (G-B-D-F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=81, start=2.0, end=2.5),  # F5
    # Bar 4: A7 (A-C#-E-G)
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=2.5, end=3.0),  # C#5
    pretty_midi.Note(velocity=100, pitch=81, start=2.5, end=3.0),  # E5
    pretty_midi.Note(velocity=100, pitch=86, start=2.5, end=3.0),  # G5
    # Bar 4: Dmaj7 resolution
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # A4
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # C#5
]
piano.notes.extend(piano_notes)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (MIDI 38) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=37, start=1.875, end=2.0),
    # Bar 3: G (MIDI 43) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=43, start=2.0, end=2.375),
    pretty_midi.Note(velocity=80, pitch=44, start=2.375, end=2.5),
    # Bar 4: A (MIDI 45) with chromatic approach
    pretty_midi.Note(velocity=90, pitch=45, start=2.5, end=2.875),
    pretty_midi.Note(velocity=80, pitch=44, start=2.875, end=3.0),
    # Bar 4: D (MIDI 38) resolution
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.5),
]
bass.notes.extend(bass_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif (D4 - F#4 - A4)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),  # A4
    # Bar 3: Leave it hanging (rest)
    # Bar 4: Come back and finish it (D4 - F#4 - A4)
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),  # F#4
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.25),  # A4
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
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
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
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
