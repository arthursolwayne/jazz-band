
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
])

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: D2 (MIDI 38), walking line with chromatic approaches
bass.notes.extend([
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),   # F#2 (chromatic)
])

# Diane: Open voicings, different chord each bar, resolve on the last
piano.notes.extend([
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # Dm7 (F#)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # (A)
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # (D)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # (Bb)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # Dm7 (F#)
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # (A)
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # (D)
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # (Bb)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),  # Dm7 (F#)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # (A)
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625),  # (D)
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # (C)
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # Dm7 (F#)
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # (A)
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # (D)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # (Bb)
])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
])

# Dante: Melody - one short motif, start it, leave it hanging, come back and finish it
# Dm7 -> Gm7 -> Cm7 -> F7 - a simple but clear motion
sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (root)
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # G (3rd of Gm7)
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25),   # E (5th of Cm7)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),   # Bb (7th of F7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),   # D (root again)
])

# Bar 3: (3.0 - 4.5s)
# Marcus: D2 (MIDI 38), walking line with chromatic approaches
bass.notes.extend([
    pretty_midi.Note(velocity=90, pitch=38, start=3.0, end=3.375),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=3.375, end=3.75),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=3.75, end=4.125),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # F#2 (chromatic)
])

# Diane: Open voicings, different chord each bar, resolve on the last
piano.notes.extend([
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # Gm7 (Bb)
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.375),  # (D)
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # (G)
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # (F)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),  # Gm7 (Bb)
    pretty_midi.Note(velocity=90, pitch=70, start=3.375, end=3.75),  # (D)
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # (G)
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # (F)
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # Gm7 (Bb)
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),  # (D)
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125),  # (G)
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # (F)
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),   # Gm7 (Bb)
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # (D)
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # (G)
    pretty_midi.Note(velocity=90, pitch=72, start=4.125, end=4.5),   # (F)
])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
])

# Dante: Melody - continue the motif, build the phrase
sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # G (3rd of Gm7)
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),   # E (5th of Cm7)
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),   # Bb (7th of F7)
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),   # D (root again)
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),   # G (3rd of Gm7)
])

# Bar 4: (4.5 - 6.0s)
# Marcus: D2 (MIDI 38), walking line with chromatic approaches
bass.notes.extend([
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=40, start=4.875, end=5.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=43, start=5.25, end=5.625),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # F#2 (chromatic)
])

# Diane: Open voicings, different chord each bar, resolve on the last
piano.notes.extend([
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Cm7 (Eb)
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # (G)
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # (C)
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # (Bb)
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # Cm7 (Eb)
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # (G)
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),  # (C)
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # (Bb)
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # Cm7 (Eb)
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.625),  # (G)
    pretty_midi.Note(velocity=90, pitch=77, start=5.25, end=5.625),  # (C)
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # (Bb)
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # Cm7 (Eb)
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),   # (G)
    pretty_midi.Note(velocity=90, pitch=77, start=5.625, end=6.0),   # (C)
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),   # (Bb)
])

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
])

# Dante: Melody - resolve the motif, leave space at the end
sax.notes.extend([
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),  # E (5th of Cm7)
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),   # Bb (7th of F7)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),   # D (root again)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.5),   # G (3rd of Gm7)
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),   # E (5th of Cm7)
    pretty_midi.Note(velocity=100, pitch=69, start=5.75, end=6.0),   # Bb (7th of F7)
])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
