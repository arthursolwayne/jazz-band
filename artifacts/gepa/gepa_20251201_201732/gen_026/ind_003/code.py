
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Bar 2: F2 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),
    # Bar 3: G2 (root of next chord)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    # Bar 3: Bb2 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),
    # Bar 4: D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    # Bar 4: F2 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75),
    # Bar 4: G2 (root of next chord)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),
    # Bar 4: Bb2 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),
    # Bar 5: D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Bar 5: F2 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25),
    # Bar 5: G2 (root of next chord)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),
    # Bar 5: Bb2 (fifth with chromatic approach)
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (F, A, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # D5
]
# Bar 3: G7 (B, D, F#, G)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.5),  # B4
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # D5
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.5),  # F#5
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # G5
])
# Bar 4: Cmaj7 (E, G, B, C)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # E5
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G5
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # B5
    pretty_midi.Note(velocity=100, pitch=72, start=2.5, end=3.0),  # C6
])
# Bar 5: F7 (A, C, E, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.5),  # A5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # C6
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # E6
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # F6
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Melody: Dm7 -> G7 -> Cmaj7 -> F7
# Motif: D4 (62), F4 (65), G4 (67), D5 (67)
sax_notes = [
    # Bar 2: D4 (62), F4 (65)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.25),
    # Bar 3: G4 (67), leave it hanging
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),
    # Bar 4: D5 (67) return to finish the motif
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.125),
]
sax.notes.extend(sax_notes)

# Drums continue for bars 2-4
# Bar 2: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 3: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75)
]
drums.notes.extend(drum_notes)

# Bar 4: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
