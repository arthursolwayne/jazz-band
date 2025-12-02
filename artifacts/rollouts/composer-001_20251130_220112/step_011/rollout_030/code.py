
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in. Sax melody starts
# Melody: Fm scale, but with a twist. One motif, sing it
# Fm: F, Gb, Ab, Bb, C, Db, Eb
# Motif: F, Ab, Bb, Db (descending minor third, then whole step)
# Start at 1.5s
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F (tenor sax middle C is 62, so +9)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),  # Db
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # Bb again
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # Db
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # F
]
sax.notes.extend(sax_notes)

# Marcus (bass): Walking line, chromatic approaches
# Fm7: F, Ab, Bb, Db
# Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F (bass)
    pretty_midi.Note(velocity=80, pitch=44, start=1.75, end=2.0),  # Eb (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=2.25, end=2.5),  # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),  # Gb
]
bass.notes.extend(bass_notes)

# Diane (piano): 7th chords, comp on 2 and 4
# Fm7 = F, Ab, Bb, Db
# Comp on 2 and 4
piano_notes = [
    # Bar 2, measure 2 (beat 2)
    pretty_midi.Note(velocity=80, pitch=64, start=1.75, end=2.0),  # F (root)
    pretty_midi.Note(velocity=80, pitch=76, start=1.75, end=2.0),  # Ab (3rd)
    pretty_midi.Note(velocity=80, pitch=78, start=1.75, end=2.0),  # Bb (5th)
    pretty_midi.Note(velocity=80, pitch=74, start=1.75, end=2.0),  # Db (7th)
    # Bar 2, measure 4 (beat 4)
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=2.25, end=2.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=78, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=2.25, end=2.5),  # Db
    # Bar 3, measure 2
    pretty_midi.Note(velocity=80, pitch=64, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=78, start=2.75, end=3.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=2.75, end=3.0),  # Db
    # Bar 3, measure 4
    pretty_midi.Note(velocity=80, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=78, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=3.25, end=3.5),  # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.125, end=3.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75)
]
drums.notes.extend(drum_notes)

# Bar 4: Sax continues motif
# Repeat and resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=4.25, end=4.5),  # Db
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # Db
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # F
]
sax.notes.extend(sax_notes)

# Marcus (bass): Walking line continues
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=4.25, end=4.5),  # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.5),  # Gb
]
bass.notes.extend(bass_notes)

# Diane (piano): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4, measure 2
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=3.75, end=4.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=78, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=3.75, end=4.0),  # Db
    # Bar 4, measure 4
    pretty_midi.Note(velocity=80, pitch=64, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=80, pitch=78, start=4.25, end=4.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=4.25, end=4.5),  # Db
    # Bar 4, measure 4 (again)
    pretty_midi.Note(velocity=80, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=76, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=80, pitch=78, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=74, start=4.75, end=5.0),  # Db
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.375, end=4.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.75, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
