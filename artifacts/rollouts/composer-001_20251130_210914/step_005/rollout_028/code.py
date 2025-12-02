
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax motif: D - F# - B - D (one bar)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=105, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=105, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=105, pitch=62, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=45, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=3.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2 (1.875)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # C
    # D7 on beat 4 (2.625)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=2.625, end=3.0),  # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax motif starts again, but ends on F# on beat 3
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=105, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=105, pitch=71, start=3.75, end=4.125),
    pretty_midi.Note(velocity=105, pitch=67, start=4.125, end=4.5),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=80, pitch=76, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2 (3.375)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # C
    # D7 on beat 4 (4.125)
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),  # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax motif: F# - B - D - F# (ending on a question)
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=105, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=105, pitch=62, start=5.25, end=5.625),
    pretty_midi.Note(velocity=105, pitch=67, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # D7 on beat 2 (4.875)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # C
    # D7 on beat 4 (5.625)
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=76, start=5.625, end=6.0),  # C
]
piano.notes.extend(piano_notes)

# Drums: continue with same pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('wayne_intro.mid')
