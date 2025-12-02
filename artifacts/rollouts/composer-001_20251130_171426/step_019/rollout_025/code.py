
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax: short motif, start on D (D4 = 62), then Bb (60), then A (57), then G (67)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.65),
    pretty_midi.Note(velocity=110, pitch=60, start=1.65, end=1.8),
    pretty_midi.Note(velocity=110, pitch=57, start=1.8, end=1.95),
    pretty_midi.Note(velocity=110, pitch=67, start=1.95, end=2.1),
]
sax.notes.extend(sax_notes)

# Bass: walking line in D, chromatic approaches
bass_notes = [
    # D (62) -> Eb (63) -> F (65) -> G (67)
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.65),
    pretty_midi.Note(velocity=80, pitch=63, start=1.65, end=1.8),
    pretty_midi.Note(velocity=80, pitch=65, start=1.8, end=1.95),
    pretty_midi.Note(velocity=80, pitch=67, start=1.95, end=2.1),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 2: D7 (D, F#, A, C)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.65),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.65),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.65),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.65),
    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.4),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.4),
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.4),
    pretty_midi.Note(velocity=90, pitch=68, start=2.25, end=2.4),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.15),
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.15),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.15),
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.15),
]
piano.notes.extend(piano_notes)

# Bar 3: Everyone in (3.0 - 4.5s)
# Sax: repeat the motif, but with a slight variation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.15),
    pretty_midi.Note(velocity=110, pitch=60, start=3.15, end=3.3),
    pretty_midi.Note(velocity=110, pitch=57, start=3.3, end=3.45),
    pretty_midi.Note(velocity=110, pitch=67, start=3.45, end=3.6),
]
sax.notes.extend(sax_notes)

# Bass: walking line in D, chromatic approaches
bass_notes = [
    # D (62) -> Eb (63) -> F (65) -> G (67)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.15),
    pretty_midi.Note(velocity=80, pitch=63, start=3.15, end=3.3),
    pretty_midi.Note(velocity=80, pitch=65, start=3.3, end=3.45),
    pretty_midi.Note(velocity=80, pitch=67, start=3.45, end=3.6),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.15),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.15),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.15),
    pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.15),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.9),
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.9),
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.9),
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=3.9),
]
piano.notes.extend(piano_notes)

# Bar 4: Everyone in (4.5 - 6.0s)
# Sax: finish the motif, resolve it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.65),
    pretty_midi.Note(velocity=110, pitch=60, start=4.65, end=4.8),
    pretty_midi.Note(velocity=110, pitch=57, start=4.8, end=4.95),
    pretty_midi.Note(velocity=110, pitch=67, start=4.95, end=5.1),
]
sax.notes.extend(sax_notes)

# Bass: walking line in D, chromatic approaches
bass_notes = [
    # D (62) -> Eb (63) -> F (65) -> G (67)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.65),
    pretty_midi.Note(velocity=80, pitch=63, start=4.65, end=4.8),
    pretty_midi.Note(velocity=80, pitch=65, start=4.8, end=4.95),
    pretty_midi.Note(velocity=80, pitch=67, start=4.95, end=5.1),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
# Bar 4: G7 (G, B, D, F)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.65),
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.65),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.65),
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.65),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4
# Bar 2: 1.5 - 3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
