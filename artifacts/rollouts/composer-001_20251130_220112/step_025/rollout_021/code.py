
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
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=0.0, end=0.375))  # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5))    # Hihat on every eighth

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches
bass_notes = [
    (pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875)),   # D (root)
    (pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25)),  # C (chromatic approach)
    (pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625)),  # Eb (3rd)
    (pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0)),   # F (chromatic approach)
    (pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375)),   # G (5th)
    (pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75)),  # F# (chromatic approach)
    (pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125)),  # A (7th)
    (pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5)),   # Bb (chromatic approach)
    (pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875)),   # D (root)
    (pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25)),  # C (chromatic approach)
    (pretty_midi.Note(velocity=90, pitch=63, start=5.25, end=5.625)),  # Eb (3rd)
    (pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0)),   # F (chromatic approach)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # F
    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # F
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # F
]
piano.notes.extend(piano_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.25))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=3.0))    # Hihat on every eighth
drums.notes.append(pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25)) # Snare on 2
drums.notes.append(pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625)) # Kick on 1
drums.notes.append(pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5))     # Hihat on every eighth

# Sax: Motif in Dm, one short phrase, sing it, leave it hanging, come back and finish it
# Motif: D - Eb - F - G (Dm scale, melodic)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),   # F
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),   # F#
    pretty_midi.Note(velocity=110, pitch=67, start=2.25, end=2.5),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.0, end=3.25),   # F (return)
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),   # D
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.0, end=4.25),   # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
