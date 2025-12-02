
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

# Bar 2: Full ensemble starts here (1.5 - 3.0s)
# Sax: motif starts
# F7, G7, A7, Bb7 (F major scale)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F7
    pretty_midi.Note(velocity=100, pitch=72, start=1.75, end=2.0),  # G7
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # A7
    pretty_midi.Note(velocity=100, pitch=73, start=2.25, end=2.5),  # Bb7
]
sax.notes.extend(sax_notes)

# Bass: walking line in F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.75),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=78, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=77, start=2.5, end=2.75),
    # Bar 4: A7 (A, C, E, G)
    pretty_midi.Note(velocity=90, pitch=74, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=76, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=79, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=78, start=3.5, end=3.75),
]
piano.notes.extend(piano_notes)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Sax: repeat the motif, but shift up a half step
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.25),  # G7
    pretty_midi.Note(velocity=100, pitch=73, start=3.25, end=3.5),  # A7
    pretty_midi.Note(velocity=100, pitch=75, start=3.5, end=3.75),  # Bb7
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.0),  # C7
]
sax.notes.extend(sax_notes)

# Bass: walking line in G
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=49, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=78, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.25),
    # Bar 4: A7 (A, C, E, G)
    pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=76, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=79, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=78, start=4.0, end=4.25),
]
piano.notes.extend(piano_notes)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Sax: finish the motif with a surprise
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.75),  # A7
    pretty_midi.Note(velocity=100, pitch=76, start=4.75, end=5.0),  # B7
    pretty_midi.Note(velocity=100, pitch=78, start=5.0, end=5.25),  # C7
    pretty_midi.Note(velocity=100, pitch=77, start=5.25, end=5.5),  # D7
    pretty_midi.Note(velocity=100, pitch=76, start=5.5, end=5.75),  # C7
    pretty_midi.Note(velocity=100, pitch=74, start=5.75, end=6.0),  # A7
]
sax.notes.extend(sax_notes)

# Bass: walking line in A
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=50, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=80, pitch=47, start=5.75, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: A7 (A, C, E, G)
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=78, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
