
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
    # Bar 2: D2 (38) -> F2 (41) chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=41, start=2.125, end=2.5),
    # Bar 3: G2 (43) -> A2 (45) chromatic approach
    pretty_midi.Note(velocity=80, pitch=43, start=2.5, end=2.875),
    pretty_midi.Note(velocity=80, pitch=44, start=2.875, end=3.125),
    pretty_midi.Note(velocity=80, pitch=45, start=3.125, end=3.5),
    # Bar 4: D2 (38) -> F2 (41) chromatic approach
    pretty_midi.Note(velocity=80, pitch=38, start=3.5, end=3.875),
    pretty_midi.Note(velocity=80, pitch=40, start=3.875, end=4.125),
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D-F-A-C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C5
]
# Bar 3: Gm7 (G-Bb-D-F)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.875),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.875),  # Bb4
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.875),  # D4
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.875),  # F5
])
# Bar 4: Dm7 (D-F-A-C)
piano_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.875),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.875),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.875),  # A4
    pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.875),  # C5
])
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 - F4 - A4 - G4 (Dm7 arpeggio with a twist on G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=1.6875, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0625, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.6875),  # D4 (repeat)
    pretty_midi.Note(velocity=100, pitch=65, start=3.6875, end=3.875),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=3.875, end=4.0625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=4.0625, end=4.25),  # G4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hihat on every eighth
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

midi.write("dante_intro.mid")
