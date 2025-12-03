
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
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
    # Bar 2: D2 (root), F#2 (fifth), chromatic approach to G2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.125, end=2.5),
    # Bar 3: G2 (root), B2 (fifth), chromatic approach to A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=43, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=46, start=2.875, end=3.125),
    pretty_midi.Note(velocity=90, pitch=45, start=3.125, end=3.5),
    # Bar 4: A2 (fifth), D3 (root), chromatic approach to C#3 (fifth)
    pretty_midi.Note(velocity=90, pitch=45, start=3.5, end=3.875),
    pretty_midi.Note(velocity=90, pitch=49, start=3.875, end=4.125),
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # C
]
# Bar 3: G7 (G-B-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # B
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # F
])
# Bar 4: Cm7 (C-Eb-G-Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=3.5, end=4.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.5, end=4.0),  # Bb
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (E4) - F4 (G4) - A4 (B4) - C5 (D5) (D4 - F4 - A4 - C5, with a chromatic passing tone)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=1.875, end=2.0),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.1875),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.1875, end=2.375),  # A4
    pretty_midi.Note(velocity=110, pitch=71, start=2.375, end=2.5),  # B4
    pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=2.6875),  # C5
    pretty_midi.Note(velocity=110, pitch=74, start=2.6875, end=2.875),  # D5
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.6875),  # C5
    pretty_midi.Note(velocity=110, pitch=69, start=3.6875, end=3.875),  # A4
    pretty_midi.Note(velocity=110, pitch=67, start=3.875, end=4.0),  # G4
    pretty_midi.Note(velocity=110, pitch=65, start=4.0, end=4.1875),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=4.1875, end=4.375),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=4.375, end=4.5),  # E4
]
sax.notes.extend(sax_notes)

# Drums: Continue for bars 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.0, end=start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.3125, end=start + 1.5),
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
