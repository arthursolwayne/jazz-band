
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
drums_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drums_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line in Fm, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # E
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=45, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=90, pitch=46, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # E
]
bass.notes.extend(bass_notes)

# Diane: 7th chords on 2 and 4, comp on 2 and 4
# Fm7 (F, Ab, C, Eb) on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=58, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.625),  # Eb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=58, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # Eb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=53, start=5.625, end=6.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=58, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # Eb
]
piano.notes.extend(piano_notes)

# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
drums_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]

# Bar 3 (3.0 - 4.5s)
drums_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5)
])

# Bar 4 (4.5 - 6.0s)
drums_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.125, end=6.25),  # Out of range, remove this
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0)
])
drums.notes.extend(drums_notes)

# Dante: Tenor saxophone, one short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: F (Eb), Gb (F#), G (Ab), E (D#) -> F, Gb, G, E (Fm motif)
# Bar 2: Start motif (F, Gb, G)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.6875),  # Gb
    pretty_midi.Note(velocity=100, pitch=55, start=1.6875, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.0625),  # F
    pretty_midi.Note(velocity=100, pitch=53, start=2.0625, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=2.4375),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=2.4375, end=2.625),  # F
    # Bar 3: Leave it hanging, no notes
    # Bar 4: Come back and finish it (G, F, E)
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.4375),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=5.4375, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=5.625, end=5.8125),  # E
    pretty_midi.Note(velocity=100, pitch=52, start=5.8125, end=6.0)    # F
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
