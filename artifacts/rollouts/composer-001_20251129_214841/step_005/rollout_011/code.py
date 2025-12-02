
import pretty_midi

midi = pretty_midi.PrettyMIDI()

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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=90, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=90, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=90, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: C (60) - E (64) - G (67) - Bb (62) - C (60)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.125),
    pretty_midi.Note(velocity=100, pitch=60, start=2.125, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=2.75),
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in C minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75),  # Db
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.125, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.375, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.5, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=2.75, end=3.0),  # B
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C - E - G - B)
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.625),
    # Bar 3: F7 (F - A - C - E)
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.375),
    # Bar 4: G7 (G - B - D - F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=74, start=2.75, end=3.0),
    pretty_midi.Note(velocity=90, pitch=77, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Drums (3.0 - 4.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=90, pitch=42, start=4.375, end=4.5)
]
drums.notes.extend(drum_notes)

# Bar 3: Sax (3.0 - 4.5s)
# Repeat the motif, but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=60, start=3.625, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.25),
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Bass (3.0 - 4.5s)
# Walking line in C minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=3.125, end=3.25),  # Db
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.75, end=3.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.875, end=4.0),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.25),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.25, end=4.5),  # B
]
bass.notes.extend(bass_notes)

# Bar 3: Piano (3.0 - 4.5s)
# 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 3: F7 (F - A - C - E)
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.125),
    # Bar 4: G7 (G - B - D - F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=77, start=3.75, end=3.875),
]
piano.notes.extend(piano_notes)

# Bar 4: Drums (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.25, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=90, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=90, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=90, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

# Bar 4: Sax (4.5 - 6.0s)
# Finish motif with a descending line
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75),
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=5.75),
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=5.875),
    pretty_midi.Note(velocity=100, pitch=64, start=5.875, end=6.0)
]
sax.notes.extend(sax_notes)

# Bar 4: Bass (4.5 - 6.0s)
# Walking line in C minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=4.625, end=4.75),  # Db
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.125, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=5.375, end=5.5),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=5.5, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=5.75),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.75, end=6.0),  # B
]
bass.notes.extend(bass_notes)

# Bar 4: Piano (4.5 - 6.0s)
# 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 4: G7 (G - B - D - F)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.625),
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.625),
    # Bar 4: C7 (C - E - G - B)
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.375),
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_russo_intro.mid")
