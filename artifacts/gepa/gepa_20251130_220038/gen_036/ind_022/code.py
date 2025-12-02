
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875), # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125), # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.6875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=40, start=1.5, end=1.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=39, start=1.75, end=2.0),  # Eb (b9)
    pretty_midi.Note(velocity=90, pitch=38, start=2.0, end=2.25),  # D (b7)
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.5),  # G (5)
    pretty_midi.Note(velocity=90, pitch=41, start=2.5, end=2.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=39, start=2.75, end=3.0),  # Eb (b9)
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=63, start=1.5, end=1.75),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=60, start=1.5, end=1.75),  # F7 (F)
    pretty_midi.Note(velocity=95, pitch=61, start=1.5, end=1.75),  # F7 (G)
    pretty_midi.Note(velocity=95, pitch=64, start=1.5, end=1.75),  # F7 (A)
    pretty_midi.Note(velocity=95, pitch=59, start=2.25, end=2.5),  # F7 (Eb)
    pretty_midi.Note(velocity=95, pitch=63, start=2.25, end=2.5),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=60, start=2.25, end=2.5),  # F7 (F)
    pretty_midi.Note(velocity=95, pitch=61, start=2.25, end=2.5),  # F7 (G)
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.5),  # F7 (A)
]
piano.notes.extend(piano_notes)

# Dante: Sax melody - start with a whisper, build to a cry
sax_notes = [
    pretty_midi.Note(velocity=80, pitch=65, start=1.5, end=1.6875),  # C (Fm)
    pretty_midi.Note(velocity=80, pitch=68, start=1.6875, end=1.875), # Eb (b9)
    pretty_midi.Note(velocity=80, pitch=66, start=1.875, end=2.0),    # D (b7)
    pretty_midi.Note(velocity=80, pitch=70, start=2.0, end=2.1875),  # G (5)
    pretty_midi.Note(velocity=80, pitch=72, start=2.1875, end=2.375), # A (6)
    pretty_midi.Note(velocity=80, pitch=68, start=2.375, end=2.5),   # Eb (b9)
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.6875), # C (Fm)
    pretty_midi.Note(velocity=100, pitch=68, start=2.6875, end=2.875), # Eb (b9)
    pretty_midi.Note(velocity=100, pitch=66, start=2.875, end=3.0),   # D (b7)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.25),  # G (5)
    pretty_midi.Note(velocity=90, pitch=41, start=3.25, end=3.5),   # F (root)
    pretty_midi.Note(velocity=90, pitch=39, start=3.5, end=3.75),  # Eb (b9)
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.0),  # D (b7)
    pretty_midi.Note(velocity=90, pitch=42, start=4.0, end=4.25),  # G (5)
    pretty_midi.Note(velocity=90, pitch=41, start=4.25, end=4.5),   # F (root)
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=63, start=3.0, end=3.25),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.25),  # F7 (F)
    pretty_midi.Note(velocity=95, pitch=61, start=3.0, end=3.25),  # F7 (G)
    pretty_midi.Note(velocity=95, pitch=64, start=3.0, end=3.25),  # F7 (A)
    pretty_midi.Note(velocity=95, pitch=59, start=3.75, end=4.0),  # F7 (Eb)
    pretty_midi.Note(velocity=95, pitch=63, start=3.75, end=4.0),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=60, start=3.75, end=4.0),  # F7 (F)
    pretty_midi.Note(velocity=95, pitch=61, start=3.75, end=4.0),  # F7 (G)
    pretty_midi.Note(velocity=95, pitch=64, start=3.75, end=4.0),  # F7 (A)
]
piano.notes.extend(piano_notes)

# Dante: Continue the melody, slightly more intense
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.1875), # D (b7)
    pretty_midi.Note(velocity=100, pitch=70, start=3.1875, end=3.375), # G (5)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.5625), # A (6)
    pretty_midi.Note(velocity=100, pitch=68, start=3.5625, end=3.75), # Eb (b9)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.9375), # C (Fm)
    pretty_midi.Note(velocity=100, pitch=68, start=3.9375, end=4.125), # Eb (b9)
    pretty_midi.Note(velocity=100, pitch=66, start=4.125, end=4.3125), # D (b7)
    pretty_midi.Note(velocity=100, pitch=70, start=4.3125, end=4.5),  # G (5)
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Fm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.75),  # D (b7)
    pretty_midi.Note(velocity=90, pitch=40, start=4.75, end=5.0),   # F (root)
    pretty_midi.Note(velocity=90, pitch=39, start=5.0, end=5.25),  # Eb (b9)
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.5),  # G (5)
    pretty_midi.Note(velocity=90, pitch=41, start=5.5, end=5.75),  # F (root)
    pretty_midi.Note(velocity=90, pitch=39, start=5.75, end=6.0),  # Eb (b9)
]
bass.notes.extend(bass_notes)

# Diane: Comping on 2 and 4 with 7th chords
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=63, start=4.5, end=4.75),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=60, start=4.5, end=4.75),  # F7 (F)
    pretty_midi.Note(velocity=95, pitch=61, start=4.5, end=4.75),  # F7 (G)
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.75),  # F7 (A)
    pretty_midi.Note(velocity=95, pitch=59, start=5.25, end=5.5),  # F7 (Eb)
    pretty_midi.Note(velocity=95, pitch=63, start=5.25, end=5.5),  # F7 (Bb)
    pretty_midi.Note(velocity=95, pitch=60, start=5.25, end=5.5),  # F7 (F)
    pretty_midi.Note(velocity=95, pitch=61, start=5.25, end=5.5),  # F7 (G)
    pretty_midi.Note(velocity=95, pitch=64, start=5.25, end=5.5),  # F7 (A)
]
piano.notes.extend(piano_notes)

# Dante: Continue the melody, ending on an unresolved note
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.6875), # A (6)
    pretty_midi.Note(velocity=100, pitch=68, start=4.6875, end=4.875), # Eb (b9)
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.0),    # D (b7)
    pretty_midi.Note(velocity=100, pitch=70, start=5.0, end=5.1875),  # G (5)
    pretty_midi.Note(velocity=100, pitch=72, start=5.1875, end=5.375), # A (6)
    pretty_midi.Note(velocity=100, pitch=68, start=5.375, end=5.5625), # Eb (b9)
    pretty_midi.Note(velocity=100, pitch=66, start=5.5625, end=5.75),  # D (b7)
    pretty_midi.Note(velocity=100, pitch=70, start=5.75, end=5.9375),  # G (5)
    pretty_midi.Note(velocity=100, pitch=69, start=5.9375, end=6.0),   # Ab (b6)
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.75, end=5.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.6875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=42, start=4.75, end=4.9375),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.875),  # Snare on 4
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.4375),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=42, start=5.5, end=5.6875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("fm_jazz_intro.mid")
