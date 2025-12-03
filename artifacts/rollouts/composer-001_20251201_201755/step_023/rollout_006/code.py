
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
    # Hihat on every eighth
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38) to F2 (41) chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=41, start=2.125, end=2.5),
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=2.875),
    # Bar 3: G2 (43) to A2 (45) chromatic approach
    pretty_midi.Note(velocity=80, pitch=43, start=2.875, end=3.25),
    pretty_midi.Note(velocity=80, pitch=44, start=3.25, end=3.5),
    pretty_midi.Note(velocity=80, pitch=45, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=47, start=3.875, end=4.25),
    # Bar 4: D2 (38) to F2 (41) chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=4.25, end=4.625),
    pretty_midi.Note(velocity=80, pitch=40, start=4.625, end=4.875),
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=85, pitch=52, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=75, pitch=57, start=1.5, end=2.0),  # C
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.5),  # G
    pretty_midi.Note(velocity=85, pitch=57, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=75, pitch=62, start=2.0, end=2.5),  # F
])
# Bar 4: Dm7 (D F A C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=50, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=85, pitch=52, start=2.5, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=55, start=2.5, end=3.0),  # A
    pretty_midi.Note(velocity=75, pitch=57, start=2.5, end=3.0),  # C
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm motif: D F A D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),  # D
    # Finish it
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
