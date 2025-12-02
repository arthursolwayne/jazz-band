
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches, never the same note twice
# Dm7 = D F A C
# Walking bass line: D -> Eb -> F -> G -> A -> Bb -> B -> C -> D
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=2.625, end=2.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=3.875, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.375),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=4.375, end=4.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=4.625, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.125),  # A
    pretty_midi.Note(velocity=90, pitch=68, start=5.125, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.375),  # B
    pretty_midi.Note(velocity=90, pitch=70, start=5.375, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=5.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=5.75, end=5.875),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=5.875, end=6.0),  # G
]
bass.notes.extend(bass_notes)

# Diane: 7th chords, comp on 2 and 4
# Dm7 = D F A C
# Comp on beat 2 and 4 of each bar
# Bar 2: Dm7 on beat 2
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.125),
    # Bar 3: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.125),
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.125),
    # Bar 4: Dm7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.125),
    pretty_midi.Note(velocity=90, pitch=70, start=4.0, end=4.125),
    # Bar 4: Dm7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.125),
    pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.125),
]
piano.notes.extend(piano_notes)

# Dante: Motif in Dm
# Dm = D F A C
# Short motif: D -> F -> A -> C (start at bar 2)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0),  # C
    # Rest for a moment, leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.375, end=2.5),  # C
    # Full motif again with some variation
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=2.875, end=3.0),  # C
    # Repeat with a slight delay
    pretty_midi.Note(velocity=100, pitch=62, start=3.125, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.625),  # C
    # End with a sustained note
    pretty_midi.Note(velocity=100, pitch=70, start=3.625, end=6.0),  # C
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('dante_intro.mid')
