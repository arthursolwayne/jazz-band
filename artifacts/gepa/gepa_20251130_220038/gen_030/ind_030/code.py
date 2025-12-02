
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: walking line in Fm, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=37, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=36, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=35, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=34, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=33, start=3.0, end=3.375),   # Bb
    pretty_midi.Note(velocity=100, pitch=32, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=31, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=100, pitch=30, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=100, pitch=29, start=4.5, end=4.875),   # E
    pretty_midi.Note(velocity=100, pitch=28, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=27, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=26, start=5.625, end=6.0),   # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, Eb) on beat 2
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=51, start=1.875, end=2.25),  # Eb

    # Bar 3: Bbm7 (Bb, Db, F, Ab) on beat 2
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # Ab

    # Bar 4: Dm7 (D, F, A, C) on beat 2
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # C
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing
# Motif: F - Bb - Eb - F (intervallic: 4 - 3 - 4)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=50, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=48, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0),   # F
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_jazz_intro.mid")
