
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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
# Sax: motif starting on Fm7 (F, Ab, Bb, D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # D
]

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=51, start=2.625, end=3.0),  # G
]

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # D
    # Fm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # D
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: repeat motif, but shift to Ab7 (Ab, C, Db, F)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # Db
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),   # F
])

# Bass: walking line in Ab
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=4.125, end=4.5),   # C
])

# Piano: 7th chords on 2 and 4
piano_notes.extend([
    # Ab7 on beat 2
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=61, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # F
    # Ab7 on beat 4
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=61, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # Db
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),   # F
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: repeat motif but resolve to Bb7 (Bb, D, Eb, G)
sax_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # G
])

# Bass: walking line in Bb
bass_notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # Db
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0),   # D
])

# Piano: 7th chords on 2 and 4
piano_notes.extend([
    # Bb7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # G
    # Bb7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),   # G
])

sax.notes.extend(sax_notes)
bass.notes.extend(bass_notes)
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
