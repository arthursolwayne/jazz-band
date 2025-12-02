
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
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking line (roots and fifths with chromatic approaches)
# Dm7: D, A, C, F (MIDI 43, 50, 40, 45)
# Walking bass line: D -> C -> A -> D -> F -> E -> D -> C
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=45, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=40, start=4.125, end=4.5),
]

bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
# Bar 3: Gm7 (G, Bb, D, F)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2: Dm7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=40, start=1.5, end=1.875),
    # Bar 3: Gm7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=47, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    # Bar 4: Cm7 (open voicing)
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=47, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=40, start=3.0, end=3.375),
]

piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
]
# Bar 3
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.125),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.125),
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.625),
]
# Bar 4
drum_notes += [
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.125),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=4.875),
]

drums.notes.extend(drum_notes)

# Dante: Melody (bar 2-4)
# Short motif: Dm scale with chromatic approach, start on D, end on F
# D -> Eb -> D -> F
# Bar 2 (1.5 - 3.0s)
# D (43), Eb (44), D (43), F (45)
# Bar 3 (3.0 - 4.5s)
# D (43), Eb (44), D (43), F (45)
# Bar 4 (4.5 - 6.0s)
# D (43), D (43), Eb (44), F (45) (end on F)
# Wait between bar 2-3, resolve on F
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=110, pitch=43, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=44, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=43, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=45, start=1.875, end=2.25),
    # Bar 3
    pretty_midi.Note(velocity=110, pitch=43, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=44, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=43, start=2.875, end=3.0),
    pretty_midi.Note(velocity=110, pitch=45, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=110, pitch=43, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=43, start=4.625, end=4.75),
    pretty_midi.Note(velocity=110, pitch=44, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=45, start=4.875, end=5.25),
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
