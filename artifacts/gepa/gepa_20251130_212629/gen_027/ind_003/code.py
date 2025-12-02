
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drum notes: kick=36, snare=38, hihat=42

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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.6875),  # Fm7: F
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),   # Eb
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.1875),  # F again
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=36, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=70, pitch=34, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=70, pitch=32, start=1.875, end=2.0),   # Db
    pretty_midi.Note(velocity=70, pitch=35, start=2.0, end=2.1875),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2, beat 2 (1.6875 - 1.875): Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.6875, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=1.6875, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=1.6875, end=1.875),  # C
    # Bar 2, beat 4 (2.0 - 2.1875): Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.1875),    # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.0, end=2.1875),    # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=2.0, end=2.1875),    # D
    pretty_midi.Note(velocity=90, pitch=55, start=2.0, end=2.1875),    # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 2
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.75, end=2.875),
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif with variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # Eb
    pretty_midi.Note(velocity=110, pitch=60, start=3.1875, end=3.375), # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.5625, end=3.75),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=52, start=3.0, end=3.1875),   # G
    pretty_midi.Note(velocity=70, pitch=50, start=3.1875, end=3.375), # Ab
    pretty_midi.Note(velocity=70, pitch=48, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=70, pitch=53, start=3.5625, end=3.75),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3, beat 2 (3.1875 - 3.375): Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=3.1875, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.1875, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=3.1875, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=3.1875, end=3.375),  # C
    # Bar 3, beat 4 (3.5625 - 3.75): Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=3.5625, end=3.75),   # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.5625, end=3.75),   # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=3.5625, end=3.75),   # D
    pretty_midi.Note(velocity=90, pitch=55, start=3.5625, end=3.75),   # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: End with a question, not a statement
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.6875),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0),   # Eb
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.1875),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=48, start=4.5, end=4.6875),   # D
    pretty_midi.Note(velocity=70, pitch=50, start=4.6875, end=4.875), # Ab
    pretty_midi.Note(velocity=70, pitch=52, start=4.875, end=5.0),   # G
    pretty_midi.Note(velocity=70, pitch=53, start=5.0, end=5.1875),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4, beat 2 (4.6875 - 4.875): Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=4.6875, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.6875, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=4.6875, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=4.6875, end=4.875),  # C
    # Bar 4, beat 4 (5.0 - 5.1875): Fm7
    pretty_midi.Note(velocity=90, pitch=53, start=5.0, end=5.1875),    # F
    pretty_midi.Note(velocity=90, pitch=50, start=5.0, end=5.1875),    # Ab
    pretty_midi.Note(velocity=90, pitch=48, start=5.0, end=5.1875),    # D
    pretty_midi.Note(velocity=90, pitch=55, start=5.0, end=5.1875),    # C
]
piano.notes.extend(piano_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
