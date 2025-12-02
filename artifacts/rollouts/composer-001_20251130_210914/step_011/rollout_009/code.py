
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass - walking line with chromatic approaches
bass_notes = [
    # Dm7 - F, A, C, D
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=1.6875, end=1.875),  # F#
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.1875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.1875, end=2.375),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=2.6875),  # E
    pretty_midi.Note(velocity=90, pitch=59, start=2.6875, end=2.875),  # D#
    pretty_midi.Note(velocity=90, pitch=60, start=2.875, end=3.0),  # E
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.1875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.1875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.1875),  # G
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.875, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.875, end=3.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.875, end=3.0),  # G
]
piano.notes.extend(piano_notes)

# Sax - melody motif
sax_notes = [
    # Start the motif
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=1.875, end=2.0),  # E
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.1875),  # F
    # Come back and finish the motif
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.6875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=2.6875, end=2.875),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=3.1875, end=3.375),  # F#
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.5),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.6875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.6875, end=3.875),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.1875),  # E
    pretty_midi.Note(velocity=90, pitch=59, start=4.1875, end=4.375),  # D#
    pretty_midi.Note(velocity=90, pitch=60, start=4.375, end=4.5),  # E
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.6875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.6875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.6875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.6875),  # G
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.375, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.375, end=4.5),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=4.375, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.375, end=4.5),  # G
]
piano.notes.extend(piano_notes)

# Sax - continue the motif
sax_notes = [
    # Continue from the end of the previous motif
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.1875),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.1875, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=3.375, end=3.5),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.6875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=3.6875, end=3.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=3.875, end=4.0),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.1875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=4.1875, end=4.375),  # G
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass - walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=90, pitch=63, start=4.6875, end=4.875),  # F#
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.1875),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.1875, end=5.375),  # G
    pretty_midi.Note(velocity=90, pitch=62, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=5.6875),  # E
    pretty_midi.Note(velocity=90, pitch=59, start=5.6875, end=5.875),  # D#
    pretty_midi.Note(velocity=90, pitch=60, start=5.875, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Piano - 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.1875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.1875),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.0, end=5.1875),  # G
    # Dm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.875, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.875, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.875, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.875, end=6.0),  # G
]
piano.notes.extend(piano_notes)

# Sax - finish the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.6875),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.6875, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=4.875, end=5.0),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.1875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.1875, end=5.375),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.375, end=5.5),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.6875),  # F
    pretty_midi.Note(velocity=110, pitch=64, start=5.6875, end=5.875),  # G
    pretty_midi.Note(velocity=110, pitch=60, start=5.875, end=6.0),  # E
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('wayne_intro.mid')
