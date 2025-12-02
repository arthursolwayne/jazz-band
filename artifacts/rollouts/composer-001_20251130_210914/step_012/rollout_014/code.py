
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif: D (D4) -> F# (F#4) -> B (B4) -> D (D5), then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5)
]
sax.notes.extend(sax_notes)

# Bass: walking line in D
bass_notes = [
    # Bar 2: D (D3) -> E (E3) -> F# (F#3) -> G (G3)
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=52, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 in bar 2
piano_notes = [
    # D7 chord on 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=90, pitch=74, start=1.75, end=2.0),
    # D7 chord on 4 (2.25 - 2.5)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.5)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: return and finish the motif from bar 2
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0)
]
sax.notes.extend(sax_notes)

# Bass: walking line in D
bass_notes = [
    # Bar 3: A (A3) -> B (B3) -> C# (C#4) -> D (D4)
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=59, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=61, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 in bar 3
piano_notes = [
    # D7 chord on 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),
    pretty_midi.Note(velocity=90, pitch=74, start=3.25, end=3.5),
    # D7 chord on 4 (3.75 - 4.0)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.0)
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: variation of the motif, inverted, ends on D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5)
]
sax.notes.extend(sax_notes)

# Bass: walking line in D
bass_notes = [
    # Bar 4: F# (F#3) -> G (G3) -> A (A3) -> B (B3)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=55, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=57, start=5.0, end=5.25),
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.5)
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4 in bar 4
piano_notes = [
    # D7 chord on 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=90, pitch=74, start=4.75, end=5.0),
    # D7 chord on 4 (5.25 - 5.5)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=74, start=5.25, end=5.5)
]
piano.notes.extend(piano_notes)

# Drums: Bar 3
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Drums: Bar 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.375),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
