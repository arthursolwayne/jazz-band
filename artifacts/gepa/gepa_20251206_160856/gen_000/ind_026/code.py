
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F2 (chromatic), G2 (fifth), D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=39, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875),
    # Bar 3: D2 (root), F2 (chromatic), G2 (fifth), D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=39, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.25),
    # Bar 4: D2 (root), F2 (chromatic), G2 (fifth), D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=4.25, end=4.625),
    pretty_midi.Note(velocity=100, pitch=39, start=4.625, end=4.875),
    pretty_midi.Note(velocity=100, pitch=43, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),
]
# Bar 3: Bb7 (Bb-D-F-A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=57, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=3.0),
])
# Bar 4: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=4.0),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: Dm - F - Dm - G - Dm
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.875),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat
]
# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=2.5, end=3.0),    # Hihat
])
# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),  # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0),  # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.5, end=4.0),    # Hihat
])
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
