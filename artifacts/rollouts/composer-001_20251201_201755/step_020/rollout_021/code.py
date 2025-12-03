
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus - Bass: Walking line in Fm (F, Ab, D, C)
# Bar 2: F (root), Ab (b9), D (5), C (b7)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.6875),  # F2
    pretty_midi.Note(velocity=90, pitch=68, start=1.6875, end=1.875), # Ab2
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.0625), # D2
    pretty_midi.Note(velocity=90, pitch=72, start=2.0625, end=2.25), # C2
]
bass.notes.extend(bass_notes)

# Diane - Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=2.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.25),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),   # Eb
]
piano.notes.extend(piano_notes)

# Dante - Sax: Motif (F, Ab, G, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus - Bass: Walking line in Fm (Bb, F, Ab, D)
# Bar 3: Bb (b7), F (root), Ab (b9), D (5)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),  # Bb2
    pretty_midi.Note(velocity=90, pitch=71, start=3.1875, end=3.375), # F2
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.5625), # Ab2
    pretty_midi.Note(velocity=90, pitch=74, start=3.5625, end=3.75), # D2
]
bass.notes.extend(bass_notes)

# Diane - Piano: Open voicings, different chord each bar
# Bar 3: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.75),   # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.75),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),   # Eb
]
piano.notes.extend(piano_notes)

# Dante - Sax: Motif (F, Ab, G, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=3.75, end=4.125), # G
    pretty_midi.Note(velocity=110, pitch=65, start=4.125, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus - Bass: Walking line in Fm (C, Bb, F, Ab)
# Bar 4: C (b7), Bb (b7), F (root), Ab (b9)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.6875),  # C2
    pretty_midi.Note(velocity=90, pitch=67, start=4.6875, end=4.875), # Bb2
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.0625), # F2
    pretty_midi.Note(velocity=90, pitch=68, start=5.0625, end=5.25), # Ab2
]
bass.notes.extend(bass_notes)

# Diane - Piano: Open voicings, different chord each bar
# Bar 4: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.25),   # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=5.25),   # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=5.25),   # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.25),   # Eb
]
piano.notes.extend(piano_notes)

# Dante - Sax: Motif (F, Ab, G, F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=5.8125),
    # Hihat on every eighth
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
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
