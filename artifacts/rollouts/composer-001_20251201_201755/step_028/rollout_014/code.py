
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

# Marcus - Bass line (F2, C2, Gb2, D2, F2, C2, Gb2, D2)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25),  # C2
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Gb2
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),  # C2
    pretty_midi.Note(velocity=100, pitch=51, start=3.75, end=4.125),  # Gb2
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # D2
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=100, pitch=48, start=4.875, end=5.25),  # C2
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # Gb2
    pretty_midi.Note(velocity=100, pitch=47, start=5.625, end=6.0),  # D2
]
bass.notes.extend(bass_notes)

# Diane - Piano (Open voicings, resolve on last beat)
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # D
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.5),  # Ab
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # Bb
])
piano.notes.extend(piano_notes)

# Dante - Tenor Sax (One short motif, sing it, leave it hanging)
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),   # G4
    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.625),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.875),  # E4
    # Bar 4: Resolve the motif
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.625),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=3.625, end=3.875),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=3.875, end=4.125),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=4.125, end=4.375),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=4.375, end=4.625),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.875),  # E4
    pretty_midi.Note(velocity=110, pitch=65, start=4.875, end=5.125),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=5.125, end=5.375),  # G4
    pretty_midi.Note(velocity=110, pitch=64, start=5.375, end=5.625),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.875),  # D4
    pretty_midi.Note(velocity=110, pitch=60, start=5.875, end=6.0),    # C4
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar_start in [1.5, 3.0, 4.5]:
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 0.0, end=bar_start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.0, end=bar_start + 0.1875),
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
