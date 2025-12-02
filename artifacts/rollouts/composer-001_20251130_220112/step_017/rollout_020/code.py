
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Sax: short motif, start on F (65), Bb (62), D (67), G (67)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # G
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=48, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.5),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: C7 (C, E, G, B)
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.75),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Sax: repeat motif, but vary slightly
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # G#
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.25),  # G#
    pretty_midi.Note(velocity=80, pitch=50, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=80, pitch=52, start=3.5, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=4.0),  # B#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: C7 (C, E, G, B)
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=80, pitch=71, start=3.0, end=3.25),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=80, pitch=65, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Sax: finish the motif, resolve
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),  # G#
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.75),  # B#
    pretty_midi.Note(velocity=80, pitch=52, start=4.75, end=5.0),  # B
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=80, pitch=49, start=5.25, end=5.5),  # G#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: C7 (C, E, G, B)
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=80, pitch=71, start=4.5, end=4.75),
    # Bar 4: G7 (G, B, D, F)
    pretty_midi.Note(velocity=80, pitch=67, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=80, pitch=65, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [2, 3, 4]:
    start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.1875, end=start + 0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.375, end=start + 0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.5625, end=start + 0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.75, end=start + 0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 0.9375, end=start + 1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.125, end=start + 1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=start + 1.3125, end=start + 1.5),
    drums.notes.extend([

    ])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
