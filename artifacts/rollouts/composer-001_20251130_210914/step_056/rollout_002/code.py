
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Fm root (F) on 1
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    # Bb on 2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.125),
    # Ab on 3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=59, start=2.125, end=2.5),
    # D on 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Fm7 on 2 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=1.875, end=2.125),
    pretty_midi.Note(velocity=90, pitch=59, start=1.875, end=2.125),
    pretty_midi.Note(velocity=85, pitch=60, start=1.875, end=2.125),
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.125),
    # Fm7 on 4 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=2.5, end=2.875),
    pretty_midi.Note(velocity=90, pitch=59, start=2.5, end=2.875),
    pretty_midi.Note(velocity=85, pitch=60, start=2.5, end=2.875),
    pretty_midi.Note(velocity=80, pitch=61, start=2.5, end=2.875),
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm, short and hanging
sax_notes = [
    # F (F) on 1
    pretty_midi.Note(velocity=105, pitch=65, start=1.5, end=1.6875),
    # Ab (Ab) on 2
    pretty_midi.Note(velocity=100, pitch=59, start=1.875, end=2.0),
    # D (D) on 3
    pretty_midi.Note(velocity=105, pitch=62, start=2.125, end=2.3125),
    # F (F) on 4, leave it hanging
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.6875),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Fm root (F) on 1
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),
    # Bb on 2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.625),
    # Ab on 3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=59, start=3.625, end=4.0),
    # D on 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Fm7 on 2 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=3.375, end=3.625),
    pretty_midi.Note(velocity=90, pitch=59, start=3.375, end=3.625),
    pretty_midi.Note(velocity=85, pitch=60, start=3.375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.625),
    # Fm7 on 4 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=4.0, end=4.375),
    pretty_midi.Note(velocity=90, pitch=59, start=4.0, end=4.375),
    pretty_midi.Note(velocity=85, pitch=60, start=4.0, end=4.375),
    pretty_midi.Note(velocity=80, pitch=61, start=4.0, end=4.375),
]
piano.notes.extend(piano_notes)

# Sax: Motif variation, resolving the hanging note
sax_notes = [
    # F (F) on 1
    pretty_midi.Note(velocity=105, pitch=65, start=3.0, end=3.1875),
    # Ab (Ab) on 2
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.5),
    # D (D) on 3
    pretty_midi.Note(velocity=105, pitch=62, start=3.625, end=3.8125),
    # F (F) on 4, resolved
    pretty_midi.Note(velocity=100, pitch=65, start=4.0, end=4.1875),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line in Fm, chromatic approaches
bass_notes = [
    # Fm root (F) on 1
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),
    # Bb on 2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=61, start=4.875, end=5.125),
    # Ab on 3 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=59, start=5.125, end=5.5),
    # D on 4
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.875),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comping
piano_notes = [
    # Fm7 on 2 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=4.875, end=5.125),
    pretty_midi.Note(velocity=90, pitch=59, start=4.875, end=5.125),
    pretty_midi.Note(velocity=85, pitch=60, start=4.875, end=5.125),
    pretty_midi.Note(velocity=80, pitch=61, start=4.875, end=5.125),
    # Fm7 on 4 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=95, pitch=65, start=5.5, end=5.875),
    pretty_midi.Note(velocity=90, pitch=59, start=5.5, end=5.875),
    pretty_midi.Note(velocity=85, pitch=60, start=5.5, end=5.875),
    pretty_midi.Note(velocity=80, pitch=61, start=5.5, end=5.875),
]
piano.notes.extend(piano_notes)

# Sax: Motif variation, with a slight twist
sax_notes = [
    # F (F) on 1
    pretty_midi.Note(velocity=105, pitch=65, start=4.5, end=4.6875),
    # Ab (Ab) on 2
    pretty_midi.Note(velocity=100, pitch=59, start=4.875, end=5.0),
    # D (D) on 3
    pretty_midi.Note(velocity=105, pitch=62, start=5.125, end=5.3125),
    # F (F) on 4, with a slight chromatic twist
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.6875),
]
sax.notes.extend(sax_notes)

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
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
