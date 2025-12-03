
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

# Bass line (Marcus)
# Walking line: D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),  # D2 (root)
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25), # Eb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=43, start=2.25, end=2.625),  # G2 (fifth)
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # F2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=3.375, end=3.75), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # F2
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=80, pitch=40, start=4.875, end=5.25), # Eb2
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # F2
]
bass.notes.extend(bass_notes)

# Piano (Diane)
# Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.25),  # A4
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),  # C#5

    # Bar 3: Gm7 (G, Bb, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=3.0),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=3.0),  # F4

    # Bar 4: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),  # D5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.75),  # F5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),  # Ab4

    # Bar 4: Resolution (Cmaj7)
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.5),  # C4
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.5),  # E4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.5),  # G4
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.5),  # B4
]
piano.notes.extend(piano_notes)

# Saxophone (Dante)
# One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),   # A4
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),  # C#5 (hanging)
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),  # A4
    pretty_midi.Note(velocity=110, pitch=66, start=2.75, end=3.0),  # F4
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # E4
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # F4
]
sax.notes.extend(sax_notes)

# Drums for Bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start, end=bar_start + 0.1875)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125)
    pretty_midi.Note(velocity=90, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5)
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
