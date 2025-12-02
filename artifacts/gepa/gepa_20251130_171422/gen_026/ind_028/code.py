
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Start of the melody (1.5 - 3.0s)
# Saxophone motif: Fm7 -> Ab -> Bb -> D (Fm scale)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # D
    # Rest for the rest of the bar
]
sax.notes.extend(sax_notes)

# Bass line: walking line with chromatic approaches
# Fm7 -> Ab -> Bb -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=2.375, end=2.5),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=80, pitch=46, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=2.875, end=3.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Fm7 on 2, Bb7 on 4
piano_notes = [
    # Fm7 on 2 (beat 2)
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # Bb
    # Bb7 on 4 (beat 4)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=2.75),  # Db
]
piano.notes.extend(piano_notes)

# Bar 3: Continue the melody (3.0 - 4.5s)
# Saxophone continues the motif, now with resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=3.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.375, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=4.0, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=80, pitch=46, start=4.25, end=4.375),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=4.375, end=4.5),  # F
]
bass.notes.extend(bass_notes)

# Piano follows with 7th chords
piano_notes = [
    # Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=3.875, end=4.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=3.875, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.875, end=4.0),  # Bb
    # Bb7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.625, end=4.75),  # Db
]
piano.notes.extend(piano_notes)

# Bar 4: Continue the melody (4.5 - 6.0s)
# Saxophone resolves with a rest and hint of the next phrase
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),  # F
]
sax.notes.extend(sax_notes)

# Bass continues the walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.125, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=5.375, end=5.5),  # G
    pretty_midi.Note(velocity=80, pitch=46, start=5.5, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=5.625, end=5.75),  # A
    pretty_midi.Note(velocity=80, pitch=46, start=5.75, end=5.875),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=5.875, end=6.0),  # F
]
bass.notes.extend(bass_notes)

# Piano follows with 7th chords
piano_notes = [
    # Fm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=5.875, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=61, start=5.875, end=6.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=67, start=5.875, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.875, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Drums continue in bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
