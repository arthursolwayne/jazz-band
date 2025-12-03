
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line (F2 - C3), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2 (F2, Ab, Bb, C)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=2.625, end=3.0),  # C

    # Bar 3 (F2, Ab, Bb, C)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # C

    # Bar 4 (F2, Ab, Bb, C)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=55, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=90, pitch=55, start=5.625, end=6.0),  # C
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: Open voicings, resolve on the last bar
# Bar 2: Fm7 (F, Ab, C, D)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # D

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),  # Ab

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=3.0),

    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.5),

    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Dante: Tenor sax — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Fm (F, Ab, Bb, C) – short motif
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),     # F
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),     # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),     # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.5),     # C

    # Bar 3: Let it hang, then resolve
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),     # F
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5),     # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75),     # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.0),     # C

    # Bar 4: Resolution with a twist
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.75),     # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0),     # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),     # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),     # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),     # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),     # Bb
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
