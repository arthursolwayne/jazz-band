
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
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

# Marcus on bass (walking line, chromatic approaches)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # F
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=53, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=2.75, end=3.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=80, pitch=51, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=80, pitch=52, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=53, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=80, pitch=54, start=5.25, end=5.5),  # A
    pretty_midi.Note(velocity=80, pitch=52, start=5.5, end=5.75),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=85, pitch=62, start=1.75, end=2.0),  # F7 (Bb)
    pretty_midi.Note(velocity=85, pitch=67, start=1.75, end=2.0),  # F7 (E)
    pretty_midi.Note(velocity=85, pitch=71, start=1.75, end=2.0),  # F7 (A)
    pretty_midi.Note(velocity=85, pitch=76, start=1.75, end=2.0),  # F7 (D)
    pretty_midi.Note(velocity=85, pitch=62, start=2.25, end=2.5),  # F7 (Bb)
    pretty_midi.Note(velocity=85, pitch=67, start=2.25, end=2.5),  # F7 (E)
    pretty_midi.Note(velocity=85, pitch=71, start=2.25, end=2.5),  # F7 (A)
    pretty_midi.Note(velocity=85, pitch=76, start=2.25, end=2.5),  # F7 (D)
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=85, pitch=62, start=2.75, end=3.0),  # F7 (Bb)
    pretty_midi.Note(velocity=85, pitch=67, start=2.75, end=3.0),  # F7 (E)
    pretty_midi.Note(velocity=85, pitch=71, start=2.75, end=3.0),  # F7 (A)
    pretty_midi.Note(velocity=85, pitch=76, start=2.75, end=3.0),  # F7 (D)
    pretty_midi.Note(velocity=85, pitch=62, start=3.25, end=3.5),  # F7 (Bb)
    pretty_midi.Note(velocity=85, pitch=67, start=3.25, end=3.5),  # F7 (E)
    pretty_midi.Note(velocity=85, pitch=71, start=3.25, end=3.5),  # F7 (A)
    pretty_midi.Note(velocity=85, pitch=76, start=3.25, end=3.5),  # F7 (D)
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=85, pitch=62, start=3.75, end=4.0),  # F7 (Bb)
    pretty_midi.Note(velocity=85, pitch=67, start=3.75, end=4.0),  # F7 (E)
    pretty_midi.Note(velocity=85, pitch=71, start=3.75, end=4.0),  # F7 (A)
    pretty_midi.Note(velocity=85, pitch=76, start=3.75, end=4.0),  # F7 (D)
    pretty_midi.Note(velocity=85, pitch=62, start=4.25, end=4.5),  # F7 (Bb)
    pretty_midi.Note(velocity=85, pitch=67, start=4.25, end=4.5),  # F7 (E)
    pretty_midi.Note(velocity=85, pitch=71, start=4.25, end=4.5),  # F7 (A)
    pretty_midi.Note(velocity=85, pitch=76, start=4.25, end=4.5),  # F7 (D)
]
piano.notes.extend(piano_notes)

# Dante on sax (melody)
sax_notes = [
    # Bar 2: first motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    # Bar 3: silence (let it breathe)
    # Bar 4: return and finish the motif
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
