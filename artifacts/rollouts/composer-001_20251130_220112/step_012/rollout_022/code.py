
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Start of the melody (1.5 - 3.0s)
# Saxophone: Fm7 -> Ab -> G -> Eb -> F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),  # Eb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm (1.5 - 3.0s)
# F -> Gb -> G -> Ab -> A -> Bb -> B -> C
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (1.5 - 3.0s)
# Fm7 on 2, Ab7 on 4
piano_notes = [
    # Fm7 on beat 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=47, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # Db
    # Ab7 on beat 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=90, pitch=59, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # Db
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # Eb
]
piano.notes.extend(piano_notes)

# Bar 3: Continue the melody (3.0 - 4.5s)
# Saxophone: D -> Eb -> F -> G -> Ab -> G -> F -> Eb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),  # Eb
]
sax.notes.extend(sax_notes)

# Bass: Walking line continuation (3.0 - 4.5s)
# C -> Db -> D -> Eb -> E -> F -> F# -> G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=51, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.75),  # Db
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=54, start=4.125, end=4.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625),  # F#
    pretty_midi.Note(velocity=80, pitch=58, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (3.0 - 4.5s)
# Dm7 on 2, F7 on 4
piano_notes = [
    # Dm7 on beat 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=90, pitch=51, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=47, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # C
    # F7 on beat 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=90, pitch=54, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # A
    pretty_midi.Note(velocity=90, pitch=59, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),  # Eb
]
piano.notes.extend(piano_notes)

# Bar 4: Continue the melody (4.5 - 6.0s)
# Saxophone: D -> Eb -> F -> G -> Ab -> G -> F -> Eb (same motif, resolves)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Bass: Walking line continuation (4.5 - 6.0s)
# G -> Ab -> A -> Bb -> B -> C -> C# -> D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=58, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=59, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=80, pitch=61, start=5.625, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 (4.5 - 6.0s)
# Gm7 on 2, Bb7 on 4
piano_notes = [
    # Gm7 on beat 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=90, pitch=58, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=54, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=57, start=4.875, end=5.25),  # F
    # Bb7 on beat 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),  # Ab
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.625, end=6.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
