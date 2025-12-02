
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: start a motif - Fm7 -> Bb -> Ab -> G
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F (Fm7)
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0)   # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=55, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=56, start=2.625, end=3.0)   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on 2 (bar 2, beat 2)
    pretty_midi.Note(velocity=90, pitch=53, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # Db
    # Fm7 on 4 (bar 2, beat 4)
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=2.625, end=3.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0)    # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif but end on Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5)   # Eb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (Bb, C, D, Eb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.5)   # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on 2 (bar 3, beat 2)
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # Db
    # Fm7 on 4 (bar 3, beat 4)
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.125, end=4.5)    # Db
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: return to motif, resolve to F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0)   # F
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (F, Gb, Ab, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=55, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=56, start=5.625, end=6.0)   # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on 2 (bar 4, beat 2)
    pretty_midi.Note(velocity=90, pitch=53, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=49, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # Db
    # Fm7 on 4 (bar 4, beat 4)
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=49, start=5.625, end=6.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=51, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0)    # Db
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=6.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
