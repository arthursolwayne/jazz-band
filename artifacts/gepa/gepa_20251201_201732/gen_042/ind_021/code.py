
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
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)
# Bass: walking line with roots and fifths, chromatic approaches
bass_notes = [
    # Bar 2: D2 (root), F2 (fifth), Eb2 (chromatic approach), D2 (root)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),
    # Bar 3: G2 (root), Bb2 (fifth), A2 (chromatic approach), G2 (root)
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
    # Bar 4: C2 (root), E2 (fifth), D2 (chromatic approach), C2 (root)
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=40, start=5.625, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
]
# Bar 3: G7 (G B D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
])
# Bar 4: Cmaj7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
])
piano.notes.extend(piano_notes)

# Sax: one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62) -> F (65) -> Eb (64) -> D (62)
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),
    # Bar 4: Finish it
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat
    for i in range(0, 8):
        pretty_midi.Note(velocity=90, pitch=42, start=start + (i * 0.1875), end=start + (i * 0.1875) + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI
# midi.write disabled
