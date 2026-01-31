
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),  # F#2
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),   # G2
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),  # A2
    pretty_midi.Note(velocity=80, pitch=41, start=3.375, end=3.75),  # F#2
    pretty_midi.Note(velocity=80, pitch=38, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.125, end=4.5),   # F2
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=40, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.25),  # D2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=80, pitch=41, start=5.625, end=6.0),   # F#2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F#4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),  # C4
]
# Bar 3: Bm7 (B D F# A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # A5
])
# Bar 4: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G5
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # F5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F#4 - A4 - G4 (first bar), then D4 - F#4 - A4 (last bar)
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # G4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # F#4
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # A4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),   # F#4
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25),  # A4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
