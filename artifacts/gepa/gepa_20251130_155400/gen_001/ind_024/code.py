
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
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
])

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Dm7 -> F -> G -> Bb
sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5), # Bb
])

# Bass: Walking line in Dm
bass.notes.extend([
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75), # D
    pretty_midi.Note(velocity=80, pitch=53, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=80, pitch=55, start=2.0, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.5), # Bb
])

# Piano: Dm7 on 2 and 4
piano.notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0), # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0), # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5), # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5), # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5), # F
])

# Drums: kick=36, snare=38, hihat=42
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0), # Kick on 3
])

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Dm7 -> F -> G -> Bb
sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25), # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0), # Bb
])

# Bass: Walking line in Dm
bass.notes.extend([
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25), # D
    pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5), # F
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75), # G
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0), # Bb
])

# Piano: Dm7 on 2 and 4
piano.notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5), # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5), # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0), # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0), # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0), # F
])

# Drums: kick=36, snare=38, hihat=42
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # Kick on 3
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Dm7 -> F -> G -> Bb (again, but without resolving)
sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5), # Bb
])

# Bass: Walking line in Dm
bass.notes.extend([
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75), # D
    pretty_midi.Note(velocity=80, pitch=53, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.5), # Bb
])

# Piano: Dm7 on 2 and 4
piano.notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0), # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0), # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5), # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5), # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5), # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5), # F
])

# Drums: kick=36, snare=38, hihat=42
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
