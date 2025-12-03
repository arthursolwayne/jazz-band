
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

# Bass: Walking line in Fm (F2, Bb2, Ab2, Eb2, etc.) with chromatic approaches
bass_notes = [
    # Bar 2: F2 (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=70, start=1.5, end=1.875),
    # Bar 2: Ab2 (fifth) with chromatic approach from G
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    # Bar 3: Eb2 (b9) with chromatic approach from D
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625),
    # Bar 3: F2 (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),
    # Bar 4: Bb2 (b7) with chromatic approach from A
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    # Bar 4: Ab2 (fifth) with chromatic approach from G
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),
    # Bar 4: F2 (root) with chromatic approach from E
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),
    # Bar 4: Bb2 (b7) with chromatic approach from A
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=63, start=1.5, end=1.875),  # Eb
]
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Ab
]
# Bar 4: Eb7 (Eb, G, Bb, Db)
piano_notes += [
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # Db
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F - Ab - Bb - F (with some chromaticism)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=70, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.6875, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=70, start=2.625, end=2.8125),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=2.8125, end=3.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.1875),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=3.1875, end=3.375),  # F
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
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
        pretty_midi.Note(velocity=80, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
