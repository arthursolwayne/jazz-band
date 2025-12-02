
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bars 2-4: 1.5s to 6.0s (4 bars total)

# Bass line: walking line in F, chromatic approach to F7
bass_notes = [
    # Bar 2: F -> Bb -> B -> C
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=61, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # C
    # Bar 3: D -> Eb -> F -> G
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # G
    # Bar 4: A -> Bb -> B -> C (resolve)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=61, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Bar 2: F7 on beat 2
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.25),  # D
    # Bar 3: F7 on beat 4
    pretty_midi.Note(velocity=80, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),  # D
]
piano.notes.extend(piano_notes)

# Sax: 4-bar motif, start with a phrase, leave it hanging, then return and finish
# Phrase: F -> A -> B -> C (intervallic movement, not scale)
sax_notes = [
    # Bar 2: Start the phrase
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=1.75, end=2.0),   # A
    pretty_midi.Note(velocity=110, pitch=71, start=2.0, end=2.25),   # B
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.5),   # C
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.25),   # A
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),   # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.75),   # A
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.0),   # C
    # Bar 4: Return and finish the phrase
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=110, pitch=69, start=4.75, end=5.0),   # A
    pretty_midi.Note(velocity=110, pitch=71, start=5.0, end=5.25),   # B
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.5),   # C
    pretty_midi.Note(velocity=110, pitch=72, start=5.5, end=6.0),    # C (hold)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
