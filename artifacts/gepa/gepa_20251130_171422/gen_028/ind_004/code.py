
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
    # Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D F A C)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=72, start=1.5, end=1.875),  # C

    # Bar 3: G7 (G B D F)
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=76, start=3.0, end=3.375),  # F

    # Bar 4: Cm7 (C Eb G Bb)
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=63, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Bass: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2: D -> C -> B -> A
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=59, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),

    # Bar 3: A -> G -> F -> Eb
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.5),

    # Bar 4: D -> C -> B -> A
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=59, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Sax: Tenor motif — short, singable, mysterious
# Bar 2: Introduce the motif (D - F - A - rest)
# Bar 3: Development (G - B - D - rest)
# Bar 4: Return (C - Eb - G - rest), but with a delay on the last note

sax_notes = [
    # Bar 2: D (62), F (64), A (67)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625),

    # Bar 3: G (67), B (71), D (69)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=71, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5625),

    # Bar 4: C (60), Eb (63), G (67) - last note delayed
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=63, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.1875),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: continue for bars 2-4
drum_notes = [
    # Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),

    # Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),

    # Bar 4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
