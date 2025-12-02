
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
    pretty_midi.Note(velocity=80, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=60, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=60, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=60, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=60, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=60, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=60, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=60, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=60, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=60, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=60, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=60, pitch=42, start=1.375, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: motif in Fm
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),     # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),     # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),     # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),     # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),     # Bb
]
sax.notes.extend(sax_notes)

# Bass: walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=36, start=1.5, end=1.75),     # F
    pretty_midi.Note(velocity=60, pitch=35, start=1.75, end=2.0),     # Eb
    pretty_midi.Note(velocity=60, pitch=34, start=2.0, end=2.25),     # D
    pretty_midi.Note(velocity=60, pitch=36, start=2.25, end=2.5),     # F
    pretty_midi.Note(velocity=60, pitch=39, start=2.5, end=2.75),     # G
    pretty_midi.Note(velocity=60, pitch=38, start=2.75, end=3.0),     # Gb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s): F7 chord on beat 2
    pretty_midi.Note(velocity=90, pitch=44, start=1.75, end=2.0),     # F
    pretty_midi.Note(velocity=90, pitch=48, start=1.75, end=2.0),     # A
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),     # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=1.75, end=2.0),     # D
    # Bar 3 (2.5 - 3.0s): F7 chord on beat 4
    pretty_midi.Note(velocity=90, pitch=44, start=2.75, end=3.0),     # F
    pretty_midi.Note(velocity=90, pitch=48, start=2.75, end=3.0),     # A
    pretty_midi.Note(velocity=90, pitch=50, start=2.75, end=3.0),     # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=3.0),     # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: continuation, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),     # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),     # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.75),     # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),     # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.0, end=4.25),     # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),     # Eb
]
sax.notes.extend(sax_notes)

# Bass: chromatic walking line
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=38, start=3.0, end=3.25),     # Gb
    pretty_midi.Note(velocity=60, pitch=39, start=3.25, end=3.5),     # G
    pretty_midi.Note(velocity=60, pitch=37, start=3.5, end=3.75),     # F#
    pretty_midi.Note(velocity=60, pitch=36, start=3.75, end=4.0),     # F
    pretty_midi.Note(velocity=60, pitch=34, start=4.0, end=4.25),     # D
    pretty_midi.Note(velocity=60, pitch=33, start=4.25, end=4.5),     # Db
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 3.5s): F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=44, start=3.25, end=3.5),     # F
    pretty_midi.Note(velocity=90, pitch=48, start=3.25, end=3.5),     # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.25, end=3.5),     # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=3.25, end=3.5),     # D
    # Bar 4 (4.0 - 4.5s): F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=44, start=4.25, end=4.5),     # F
    pretty_midi.Note(velocity=90, pitch=48, start=4.25, end=4.5),     # A
    pretty_midi.Note(velocity=90, pitch=50, start=4.25, end=4.5),     # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.25, end=4.5),     # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: return to the motif, but incomplete
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),     # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),     # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25),     # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),     # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.5, end=5.75),     # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),     # Bb
]
sax.notes.extend(sax_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=60, pitch=36, start=4.5, end=4.75),     # F
    pretty_midi.Note(velocity=60, pitch=35, start=4.75, end=5.0),     # Eb
    pretty_midi.Note(velocity=60, pitch=34, start=5.0, end=5.25),     # D
    pretty_midi.Note(velocity=60, pitch=36, start=5.25, end=5.5),     # F
    pretty_midi.Note(velocity=60, pitch=39, start=5.5, end=5.75),     # G
    pretty_midi.Note(velocity=60, pitch=38, start=5.75, end=6.0),     # Gb
]
bass.notes.extend(bass_notes)

# Piano: comp on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 5.0s): F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=44, start=4.75, end=5.0),     # F
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=5.0),     # A
    pretty_midi.Note(velocity=90, pitch=50, start=4.75, end=5.0),     # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=4.75, end=5.0),     # D
    # Bar 4 (5.5 - 6.0s): F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=44, start=5.75, end=6.0),     # F
    pretty_midi.Note(velocity=90, pitch=48, start=5.75, end=6.0),     # A
    pretty_midi.Note(velocity=90, pitch=50, start=5.75, end=6.0),     # Bb
    pretty_midi.Note(velocity=90, pitch=53, start=5.75, end=6.0),     # D
]
piano.notes.extend(piano_notes)

# Drums: continue pattern with subtle variation
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=80, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=60, pitch=42, start=3.0, end=3.125),
    pretty_midi.Note(velocity=60, pitch=42, start=3.125, end=3.25),
    pretty_midi.Note(velocity=60, pitch=42, start=3.25, end=3.375),
    pretty_midi.Note(velocity=60, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=60, pitch=42, start=3.5, end=3.625),
    pretty_midi.Note(velocity=60, pitch=42, start=3.625, end=3.75),
    pretty_midi.Note(velocity=60, pitch=42, start=3.75, end=3.875),
    pretty_midi.Note(velocity=60, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=60, pitch=42, start=4.0, end=4.125),
    pretty_midi.Note(velocity=60, pitch=42, start=4.125, end=4.25),
    pretty_midi.Note(velocity=60, pitch=42, start=4.25, end=4.375),
    pretty_midi.Note(velocity=60, pitch=42, start=4.375, end=4.5),
    pretty_midi.Note(velocity=60, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=60, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=60, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=60, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=60, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=60, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=60, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=60, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=60, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=60, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=60, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=60, pitch=42, start=5.875, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_intro.mid")
