
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with roots and fifths
bass_notes = [
    # Fm root (F) on beat 1
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # D (fifth of Fm) on beat 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.875, end=2.25),
    # Ab (chromatic approach) on beat 3
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625),
    # F (root) on beat 4
    pretty_midi.Note(velocity=90, pitch=53, start=2.625, end=3.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 2: Fm7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0)   # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif (F Bb D F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=55, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=2.625, end=3.0)   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with roots and fifths
bass_notes = [
    # Bb (chromatic approach) on beat 1
    pretty_midi.Note(velocity=90, pitch=52, start=3.0, end=3.375),
    # F (root) on beat 2
    pretty_midi.Note(velocity=90, pitch=53, start=3.375, end=3.75),
    # D (fifth of Fm) on beat 3
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),
    # Ab (chromatic approach) on beat 4
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 3: Bb7 (Bb D F Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5)   # Ab
]
piano.notes.extend(piano_notes)

# Sax: Motif variation (F Bb D F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=55, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=4.125, end=4.5)   # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with roots and fifths
bass_notes = [
    # F (root) on beat 1
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),
    # Ab (chromatic approach) on beat 2
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),
    # D (fifth of Fm) on beat 3
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625),
    # Bb (chromatic approach) on beat 4
    pretty_midi.Note(velocity=90, pitch=52, start=5.625, end=6.0)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar
# Bar 4: Fm7 (F A C Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0)   # Eb
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution (F Bb D F)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=50, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=55, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=110, pitch=53, start=5.625, end=6.0)   # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
