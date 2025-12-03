
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
# Bass: Walking line (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25), # G2
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=54, start=2.625, end=3.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: First motif, start it, leave it hanging
# F - Ab - Bb - C (Fm scale, but not a scale)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625), # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=2.0625, end=2.25),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75), # G2
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125), # Ab2
    pretty_midi.Note(velocity=90, pitch=54, start=4.125, end=4.5),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Bar 3: Bbm7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Sax: Continue motif, leave it hanging
# F - Ab - Bb - C (Fm scale, but not a scale)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375), # C
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.5625, end=3.75),  # Ab
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2, G2, Ab2, A2, Bb2, B2, C2, Db2)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25), # G2
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625), # Ab2
    pretty_midi.Note(velocity=90, pitch=54, start=5.625, end=6.0),  # A2
]
bass.notes.extend(bass_notes)

# Piano: Bar 4: C7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=6.0),  # B
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
# F - Ab - Bb - C (Fm scale, but not a scale)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0625), # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.0625, end=5.25),  # C
]
sax.notes.extend(sax_notes)

# Drums: Bar 4 (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
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
