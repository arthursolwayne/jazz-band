
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
    # Hihat on every eighth
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line - Marcus (walking line, chromatic approaches, no repeated notes)
# D minor scale: D, Eb, F, G, Ab, Bb, C
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),  # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),  # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Piano - Diane (7th chords, comp on 2 and 4)
# Bar 2 (1.5 - 3.0s)
piano_notes = [
    # Bar 2, beat 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),
    # Bar 2, beat 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=69, start=2.625, end=3.0),
    # Bar 3, beat 2: Ab7 (Ab, C, Eb, Gb)
    pretty_midi.Note(velocity=80, pitch=68, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=65, start=3.375, end=3.75),
    # Bar 3, beat 4: C7 (C, E, G, Bb)
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=74, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=69, start=4.125, end=4.5),
    # Bar 4, beat 2: D7 (D, F#, A, C)
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.25),
    # Bar 4, beat 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=69, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Saxophone - Dante (melody, one short motif, start it, leave it hanging, come back)
# Motif: D, F#, Bb, B (saxophone transposed up a major third)
# Bar 2 (1.5 - 3.0s)
sax_notes = [
    # Bar 2, beat 1: D (E)
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),
    # Bar 2, beat 2: F# (A)
    pretty_midi.Note(velocity=110, pitch=72, start=1.875, end=2.25),
    # Bar 2, beat 3: Bb (C)
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.625),
    # Bar 2, beat 4: B (D)
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),
    # Bar 3, beat 1: F# (A) - repeat motif
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),
    # Bar 3, beat 2: Bb (C)
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.75),
    # Bar 3, beat 3: B (D)
    pretty_midi.Note(velocity=110, pitch=71, start=3.75, end=4.125),
    # Bar 3, beat 4: D (E)
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),
    # Bar 4, beat 1: G (Bb)
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),
    # Bar 4, beat 2: Bb (C)
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),
    # Bar 4, beat 3: D (E)
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.625),
    # Bar 4, beat 4: F# (A) - finish the motif
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
