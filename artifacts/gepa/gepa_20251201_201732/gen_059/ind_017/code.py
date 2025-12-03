
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
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: Fm (F, C, Ab) -> root F (MIDI 53)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    # Chromatic approach to C (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=56, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=57, start=2.125, end=2.5),
    # Bar 3: Bb7 (Bb, F, D, Ab) -> root Bb (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.875),
    # Chromatic approach to F (MIDI 57)
    pretty_midi.Note(velocity=100, pitch=55, start=2.875, end=3.125),
    pretty_midi.Note(velocity=100, pitch=57, start=3.125, end=3.5),
    # Bar 4: Eb7 (Eb, Bb, G, Db) -> root Eb (MIDI 48)
    pretty_midi.Note(velocity=100, pitch=48, start=3.5, end=3.875),
    # Chromatic approach to Bb (MIDI 50)
    pretty_midi.Note(velocity=100, pitch=49, start=3.875, end=4.125),
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=50, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.875),
    # Bar 4: Eb7 (Eb, G, Bb, Db)
    pretty_midi.Note(velocity=100, pitch=48, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=52, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=50, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=55, start=3.5, end=3.875),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - F (MIDI 53 - 56 - 58 - 53)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=56, start=1.625, end=1.875),
    pretty_midi.Note(velocity=110, pitch=58, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=53, start=2.0, end=2.125),
    # Leave it hanging, return to finish
    pretty_midi.Note(velocity=110, pitch=53, start=3.5, end=3.625),
    pretty_midi.Note(velocity=110, pitch=56, start=3.625, end=3.875),
    pretty_midi.Note(velocity=110, pitch=58, start=3.875, end=4.0),
    pretty_midi.Note(velocity=110, pitch=53, start=4.0, end=4.125),
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.625, end=4.0)
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.875, end=4.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.625),
    pretty_midi.Note(velocity=100, pitch=42, start=4.625, end=5.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
