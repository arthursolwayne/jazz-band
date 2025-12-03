
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (1.5s - 3.0s): F (D2), C (E2), Bb (D2), Eb (F2)
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),

    # Bar 3 (3.0s - 4.5s): G (F2), D (G2), C (F2), F (A2)
    pretty_midi.Note(velocity=80, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=46, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=43, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=48, start=4.125, end=4.5),

    # Bar 4 (4.5s - 6.0s): A (G2), Eb (A2), D (G2), G (B2)
    pretty_midi.Note(velocity=80, pitch=46, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=46, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=53, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, resolve on the last chord
piano_notes = [
    # Bar 2 (1.5s - 3.0s): Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),

    # Bar 3 (3.0s - 4.5s): G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=73, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),

    # Bar 4 (4.5s - 6.0s): Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5s - 3.0s): Motif
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=74, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=76, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=74, start=2.25, end=2.5),
    # Leave it hanging
    pretty_midi.Note(velocity=110, pitch=72, start=2.5, end=2.75),
    pretty_midi.Note(velocity=110, pitch=74, start=2.75, end=3.0),
    # Bar 3 (3.0s - 4.5s): Repeat the motif
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.25),
    pretty_midi.Note(velocity=110, pitch=74, start=3.25, end=3.5),
    pretty_midi.Note(velocity=110, pitch=76, start=3.5, end=3.75),
    pretty_midi.Note(velocity=110, pitch=74, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=72, start=4.0, end=4.25),
    pretty_midi.Note(velocity=110, pitch=74, start=4.25, end=4.5),
    # Bar 4 (4.5s - 6.0s): Resolve the motif
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.75),
    pretty_midi.Note(velocity=110, pitch=74, start=4.75, end=5.0),
    pretty_midi.Note(velocity=110, pitch=76, start=5.0, end=5.25),
    pretty_midi.Note(velocity=110, pitch=74, start=5.25, end=5.5),
    pretty_midi.Note(velocity=110, pitch=72, start=5.5, end=5.75),
    pretty_midi.Note(velocity=110, pitch=74, start=5.75, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    kick_start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start, end=kick_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=kick_start + 0.75, end=kick_start + 1.125)

# Snare on 2 and 4
for bar in range(2, 5):
    snare_start = (bar - 1) * 1.5
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 0.75, end=snare_start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=snare_start + 1.875, end=snare_start + 2.0)

# Hihat on every eighth
for bar in range(2, 5):
    snare_start = (bar - 1) * 1.5
    for i in range(8):
        hihat_start = snare_start + i * 0.1875
        pretty_midi.Note(velocity=90, pitch=42, start=hihat_start, end=hihat_start + 0.1875)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
