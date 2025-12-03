
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

# Bass line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25), # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625), # G#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # A2
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75), # A2
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125), # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # A2
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=4.875, end=5.25), # A2
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625), # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2 (1.5 - 3.0s) - D7sus4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875),  # D5
    # Bar 3 (3.0 - 4.5s) - Bm7
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # B4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),  # D5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.375),  # F#5
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.375),  # A5
    # Bar 4 (4.5 - 6.0s) - G9
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),  # D5
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=4.875),  # B5
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.875),  # A5
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> F#4 (66) -> D4 (62) -> F#4 (66) -> G4 (67)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=1.6875, end=1.875), # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625), # D4
    pretty_midi.Note(velocity=110, pitch=66, start=2.0625, end=2.25),  # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625), # D4
    pretty_midi.Note(velocity=110, pitch=66, start=3.5625, end=3.75),  # F#4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=3.9375),  # D4
    pretty_midi.Note(velocity=110, pitch=66, start=3.9375, end=4.125), # F#4
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),   # G4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + (i * 0.1875), end=start + (i * 0.1875) + 0.1875),

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
