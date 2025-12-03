
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
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # Bb2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # A2
    pretty_midi.Note(velocity=80, pitch=43, start=4.125, end=4.5),  # Bb2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25),  # F2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # A2
    pretty_midi.Note(velocity=80, pitch=43, start=5.625, end=6.0),  # Bb2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.5 + 0.375),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.5 + 0.375),  # F#4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.5 + 0.375),  # A4
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.5 + 0.375),  # C4
]
# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.375),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.0 + 0.375),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.0 + 0.375),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.0 + 0.375),  # F4
])
# Bar 4: Cmaj7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.5 + 0.375),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.5 + 0.375),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.5 + 0.375),  # G4
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.5 + 0.375),  # B4
])
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + i * 0.1875 + 0.1875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # G4
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # A4
]
# Bar 3: Leave it hanging
sax_notes.append(pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25))
# Bar 4: Come back and finish it
sax_notes.extend([
    pretty_midi.Note(velocity=110, pitch=66, start=4.5, end=4.75),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=4.75, end=5.0),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # D4
])
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
