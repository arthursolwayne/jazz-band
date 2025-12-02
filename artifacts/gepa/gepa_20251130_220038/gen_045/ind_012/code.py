
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking bass line in Fm (F, Gb, Ab, Bb)
bass_notes = [
    # Bar 2: F, Gb, Ab, Bb
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),
    # Bar 3: Bb, F, Gb, Ab
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),
    # Bar 4: Ab, Bb, F, Gb
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),  # D
    # Bar 3: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # D
    # Bar 4: F7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax melody — one short motif, make it sing. Start it, leave it hanging. Come back and finish it.

# Bar 2: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=1.6875, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0625),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=2.0625, end=2.25),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.4375),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=2.4375, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.8125),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=2.8125, end=3.0),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=3.1875, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5625),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=3.5625, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=4.6875, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0625),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=5.0625, end=5.25),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.4375),  # Ab
    pretty_midi.Note(velocity=110, pitch=64, start=5.4375, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.8125),  # Ab
    pretty_midi.Note(velocity=110, pitch=60, start=5.8125, end=6.0),  # F
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
