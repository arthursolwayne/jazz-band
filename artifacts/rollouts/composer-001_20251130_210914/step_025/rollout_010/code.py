
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drums_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F (65)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # A (67)
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # E (64)
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # A (67)
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F (45)
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25),  # G (47)
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.625),  # E (44)
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),  # D (42)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2: F7
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F (64)
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # A (69)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G (67)
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # C (71)
    # Bar 2, beat 4: A7
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),  # A (69)
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # C (71)
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),  # E (74)
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # G (76)
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.625),
    pretty_midi.Note(velocity=80, pitch=42, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.125, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=3.0),
]
drums.notes.extend(drums_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D (62)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F (64)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D (62)
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # F (64)
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=40, start=3.0, end=3.375),  # C (40)
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),  # D (42)
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.125),  # E (44)
    pretty_midi.Note(velocity=80, pitch=45, start=4.125, end=4.5),  # F (45)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2: D7
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D (62)
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G (67)
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F (64)
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # A (69)
    # Bar 3, beat 4: F7
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # F (64)
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),  # A (69)
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # G (67)
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # C (71)
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.25, end=4.5),
]
drums.notes.extend(drums_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # A (67)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F (65)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # A (67)
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # E (64)
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # G (47)
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),  # F (45)
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # E (44)
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # D (42)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2: A7
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # A (69)
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # C (71)
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # E (74)
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # G (76)
    # Bar 4, beat 4: D7
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D (62)
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # G (67)
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F (64)
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # A (69)
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=6.0),
]
drums.notes.extend(drums_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
