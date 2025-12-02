
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bar 2: Full ensemble (1.5 - 3.0s)
# Saxophone
sax_notes = [
    # Start motif - Fm7 -> Bb -> D -> F
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),  # F
]

sax.notes.extend(sax_notes)

# Bass - Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=2.0, end=2.25),  # A
]

bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Fm7 on beat 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # Ab
    # Fm7 on beat 4 (2.25 - 2.5)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),  # Ab
]

piano.notes.extend(piano_notes)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Saxophone - Continue motif, then resolve with a Bb phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),  # Bb
]

sax.notes.extend(sax_notes)

# Bass - Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=54, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=55, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.5),  # Db
    pretty_midi.Note(velocity=80, pitch=59, start=3.5, end=3.75),  # D
]

bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Fm7 on beat 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # Ab
    # Fm7 on beat 4 (3.75 - 4.0)
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),  # Ab
]

piano.notes.extend(piano_notes)

# Drums - Repeat pattern
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
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

# Bar 4: Full ensemble (4.5 - 6.0s)
# Saxophone - Resolve motif with a Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=5.0),  # Bb
]

sax.notes.extend(sax_notes)

# Bass - Continue walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0),  # F
]

bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Fm7 on beat 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # Ab
    # Fm7 on beat 4 (5.25 - 5.5)
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),  # Ab
]

piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
