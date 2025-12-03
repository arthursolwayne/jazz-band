
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

# Bass: Walking line, roots and fifths with chromatic approaches
# Dm7 -> G7 -> Cmaj7 -> F7
# Bar 2: Dm7
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),  # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # D2
]
# Bar 3: G7
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),  # D3 (fifth)
    pretty_midi.Note(velocity=90, pitch=44, start=3.75, end=4.125),  # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # G2
])
# Bar 4: Cmaj7
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=47, start=4.5, end=4.875),  # C3
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.25),  # G3 (fifth)
    pretty_midi.Note(velocity=90, pitch=48, start=5.25, end=5.625),  # D3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=47, start=5.625, end=6.0),  # C3
])
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C5
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F5
])
# Bar 4: Cmaj7 (C, E, G, B)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # E4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # B4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Dm7 -> G7 -> Cmaj7
# Motif: D4 - F4 - D4 - Eb4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.5),  # Eb4
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # D4 (reprise)
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=4.0),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # Eb4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2 and 3
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
