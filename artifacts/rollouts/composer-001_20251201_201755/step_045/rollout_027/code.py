
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
#ONLY drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
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
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.125),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.125, end=2.5),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=2.5, end=2.875),  # F2 (chromatic approach)
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.625),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=3.625, end=4.0),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=4.0, end=4.375),  # F2 (chromatic approach)
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.125),  # E2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=5.125, end=5.5),  # G2
    pretty_midi.Note(velocity=90, pitch=41, start=5.5, end=5.875),  # F2 (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # D5
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F5
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=4.5),  # Ab4
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # Eb5
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # G5
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # Bb5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F4, Ab4, C5, F4 (start on bar 2, leave it hanging on Ab4, come back on bar 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.25),  # Ab4
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.625),  # C5
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # F4
    # Leave it hanging on Ab4
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.375),  # Ab4
    # Come back and finish it on bar 4
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.25),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.1875, end=bar_start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.5625, end=bar_start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.9375, end=bar_start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.3125, end=bar_start + 1.5),
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
