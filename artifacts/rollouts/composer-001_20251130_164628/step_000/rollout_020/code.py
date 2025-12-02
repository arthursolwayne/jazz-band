
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: All instruments in
# SAX: Melody starts
# Dm7 = D F A C
# Motif: D - F# - A - G (with a chromatic approach to G from F#)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.5),  # G
]
sax.notes.extend(sax_notes)

# BASS: Walking line in Dm
# D - C - B - A - G - F - E - D
# Bar 2: D - C - B - A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0),   # A
]
bass.notes.extend(bass_notes)

# PIANO: Comp on 2 and 4 with 7th chords
# Dm7 = D F A C
# Bar 2: Dm7 on beat 2, A7 on beat 4
piano_notes = [
    # Dm7 on beat 2 (0.75s into bar 2)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),  # C
    # A7 on beat 4 (1.5s into bar 2)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75),  # C#
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=2.75),  # E
]
piano.notes.extend(piano_notes)

# Bar 3: Sax continues the motif (starts at 2.5s)
# D - F# - A - G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5),  # G
]
sax.notes.extend(sax_notes)

# BASS: Walks on Dm again
# D - C - B - A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=2.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=2.75, end=2.875),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=2.875, end=3.0),   # A
]
bass.notes.extend(bass_notes)

# PIANO: Comp on 2 and 4 with 7th chords
# Bar 3: Dm7 on beat 2, A7 on beat 4
piano_notes = [
    # Dm7 on beat 2 (0.75s into bar 3)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375),  # C
    # A7 on beat 4 (1.5s into bar 3)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.875),  # C#
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=3.875),  # E
]
piano.notes.extend(piano_notes)

# Bar 4: Sax finishes the motif (starts at 3.5s)
# D - F# - A - G (repeat of Bar 2 motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=4.25, end=4.5),  # G
]
sax.notes.extend(sax_notes)

# BASS: Walks on Dm again
# D - C - B - A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.625, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=80, pitch=67, start=3.875, end=4.0),   # A
]
bass.notes.extend(bass_notes)

# PIANO: Comp on 2 and 4 with 7th chords
# Bar 4: Dm7 on beat 2, A7 on beat 4
piano_notes = [
    # Dm7 on beat 2 (0.75s into bar 4)
    pretty_midi.Note(velocity=90, pitch=62, start=4.25, end=4.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.25, end=4.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.375),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.375),  # C
    # A7 on beat 4 (1.5s into bar 4)
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=4.875),  # E
]
piano.notes.extend(piano_notes)

# Bar 4: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
