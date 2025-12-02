
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line in Fm, chromatic approaches, no repeating notes
# Fm: F, Ab, Bb, D, Eb
bass_notes = [
    # Bar 2: F -> Gb -> Ab -> A
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=68, start=2.625, end=3.0),  # A
    # Bar 3: Bb -> B -> C -> C#
    pretty_midi.Note(velocity=80, pitch=68, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=70, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.5),  # C#
    # Bar 4: D -> Eb -> F -> F#
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=72, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=73, start=5.625, end=6.0),  # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
# Fm7: F, Ab, Bb, C
# Bb7: Bb, D, F, Ab
# Fm7: F, Ab, Bb, C
# Bb7: Bb, D, F, Ab
# Start on beat 2 and 4 of each bar
piano_notes = [
    # Bar 2: 2nd beat - Fm7
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),  # C
    # Bar 2: 4th beat - Bb7
    pretty_midi.Note(velocity=100, pitch=68, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # Ab
    # Bar 3: 2nd beat - Fm7
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),  # C
    # Bar 3: 4th beat - Bb7
    pretty_midi.Note(velocity=100, pitch=68, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # Ab
    # Bar 4: 2nd beat - Fm7
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),  # C
    # Bar 4: 4th beat - Bb7
    pretty_midi.Note(velocity=100, pitch=68, start=6.0, end=6.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=71, start=6.0, end=6.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=6.0, end=6.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=6.0, end=6.375),  # Ab
]
piano.notes.extend(piano_notes)

# Sax: Your moment. One short motif, make it sing.
# Fm: F, Ab, Bb
# Motif: F -> Bb -> Ab -> F (staccato)
# Start on beat 1 of bar 2, leave it hanging on beat 3
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=65, start=2.625, end=2.75),  # F
    # Repeat the motif on bar 4, starting on beat 1
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=65, start=5.625, end=5.75),  # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("jazz_intro.mid")
