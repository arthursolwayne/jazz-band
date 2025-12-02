
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# BAR 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.125),
    pretty_midi.Note(velocity=80, pitch=42, start=0.125, end=0.25),
    pretty_midi.Note(velocity=80, pitch=42, start=0.25, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5, end=0.625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.875, end=1.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.0, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.25),
    pretty_midi.Note(velocity=80, pitch=42, start=1.25, end=1.375),
    pretty_midi.Note(velocity=80, pitch=42, start=1.375, end=1.5),
]
drums.notes.extend(drum_notes)

# BAR 2: Full quartet (1.5 - 3.0s)
# Sax: Motif - F (G7), A (Bb7), Bb (C7), F (G7)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # G7
    pretty_midi.Note(velocity=100, pitch=74, start=1.75, end=2.0),  # A (Bb7)
    pretty_midi.Note(velocity=100, pitch=72, start=2.0, end=2.25),  # Bb (C7)
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # F (G7)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (F, G, A, Bb)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=66, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=68, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=1.75, end=2.0),  # F
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=2.75),  # F
]
piano.notes.extend(piano_notes)

# BAR 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif, but with a slight variation (E instead of F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),  # E (F7)
    pretty_midi.Note(velocity=100, pitch=74, start=3.25, end=3.5),  # A (Bb7)
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # Bb (C7)
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # G (G7)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (C, D, E, F)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0),  # F
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=3.25, end=3.5),  # F
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=65, start=4.0, end=4.25),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.0, end=4.25),  # F
]
piano.notes.extend(piano_notes)

# BAR 4: Full quartet (4.5 - 6.0s)
# Sax: Return to original motif, but with a trill on the final note (F)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # G7
    pretty_midi.Note(velocity=100, pitch=74, start=4.75, end=5.0),  # A (Bb7)
    pretty_midi.Note(velocity=100, pitch=72, start=5.0, end=5.25),  # Bb (C7)
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # F (G7)
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # F (trill)
    pretty_midi.Note(velocity=100, pitch=72, start=5.75, end=6.0),  # F (trill)
]
sax.notes.extend(sax_notes)

# Bass: Walking line in F (Bb, C, D, E)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=60, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),  # E
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=4.75, end=5.0),  # F
    # F7 on beat 4
    pretty_midi.Note(velocity=90, pitch=65, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=72, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=76, start=5.5, end=5.75),  # F
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.125, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
