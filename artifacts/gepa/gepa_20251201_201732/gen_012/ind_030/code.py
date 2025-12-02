
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=100, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=100, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=39, start=2.25, end=2.625),  # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=40, start=2.625, end=3.0),   # E2 (resolution)
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),   # F2 (resolution)
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # D2 (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # F2 (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # G2 (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),   # G2 (resolution)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F Ab C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # Ab4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # C5
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # B4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # F4
])
# Bar 4: Cm7 (C Eb G Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.75),  # Eb4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),  # Bb4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - G4 - Bb4 (Dm7), then resolve on the last bar
sax_notes = [
    # Bar 2: D4
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),
    # Bar 2: F4
    pretty_midi.Note(velocity=100, pitch=65, start=1.625, end=1.75),
    # Bar 2: G4
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    # Bar 2: Bb4 (leave hanging)
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),
    # Bar 3: D4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),
    # Bar 3: F4
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),
    # Bar 3: G4
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),
    # Bar 3: Bb4 (leave hanging)
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),
    # Bar 4: D4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    # Bar 4: F4
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),
    # Bar 4: G4
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),
    # Bar 4: Bb4 (resolve)
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),    # Hihat on every eighth
]
for i in range(1.5, 2.0, 0.125):
    if i != 1.875:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.125))

# Bar 3
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.5),    # Hihat on every eighth
])
for i in range(3.0, 3.5, 0.125):
    if i != 3.375:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.125))

# Bar 4
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.0),    # Hihat on every eighth
])
for i in range(4.5, 5.0, 0.125):
    if i != 4.875:
        drum_notes.append(pretty_midi.Note(velocity=100, pitch=42, start=i, end=i + 0.125))

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
