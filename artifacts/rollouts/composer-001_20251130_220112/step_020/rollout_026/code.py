
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
# Sax: motif starts here
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.75),  # F (66)
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),  # A (69)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # G (67)
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.5),  # A (69)
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # C (71)
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # A (69)
]
sax.notes.extend(sax_notes)

# Bass: walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F (45)
    pretty_midi.Note(velocity=80, pitch=47, start=1.75, end=2.0),  # G (47)
    pretty_midi.Note(velocity=80, pitch=46, start=2.0, end=2.25),  # F# (46)
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5),  # E (44)
    pretty_midi.Note(velocity=80, pitch=45, start=2.5, end=2.75),  # F (45)
    pretty_midi.Note(velocity=80, pitch=47, start=2.75, end=3.0),  # G (47)
]
bass.notes.extend(bass_notes)

# Piano: 7th chord on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, E)
    pretty_midi.Note(velocity=90, pitch=66, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=66, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Drums continue
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
]
drums.notes.extend(drum_notes)

# Bar 3: Sax continues motif (1.5 - 3.0s)
# Already added in bar 2

# Bar 3: Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.25),  # E (44)
    pretty_midi.Note(velocity=80, pitch=45, start=3.25, end=3.5),  # F (45)
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.75),  # G (47)
    pretty_midi.Note(velocity=80, pitch=49, start=3.75, end=4.0),  # A (49)
    pretty_midi.Note(velocity=80, pitch=47, start=4.0, end=4.25),  # G (47)
    pretty_midi.Note(velocity=80, pitch=45, start=4.25, end=4.5),  # F (45)
]
bass.notes.extend(bass_notes)

# Bar 3: Piano continues 7th chords
piano_notes = [
    # Bar 3: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.25),
]
piano.notes.extend(piano_notes)

# Bar 4: Drums continue
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Sax concludes motif
# Return to F, resolve the tension
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.75),  # F (66)
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # A (69)
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # G (67)
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),  # A (69)
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=5.75),  # C (71)
    pretty_midi.Note(velocity=100, pitch=66, start=5.75, end=6.0),  # F (66)
]
sax.notes.extend(sax_notes)

# Bar 4: Bass continues walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.75),  # A (49)
    pretty_midi.Note(velocity=80, pitch=51, start=4.75, end=5.0),  # B (51)
    pretty_midi.Note(velocity=80, pitch=49, start=5.0, end=5.25),  # A (49)
    pretty_midi.Note(velocity=80, pitch=47, start=5.25, end=5.5),  # G (47)
    pretty_midi.Note(velocity=80, pitch=45, start=5.5, end=5.75),  # F (45)
    pretty_midi.Note(velocity=80, pitch=47, start=5.75, end=6.0),  # G (47)
]
bass.notes.extend(bass_notes)

# Bar 4: Piano resolves with F7
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=66, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),
]
piano.notes.extend(piano_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
