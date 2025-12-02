
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
    # Hi-hats on every eighth
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

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=2.25, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=2.5, end=2.75),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=2.75, end=3.0),  # E
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=3.5, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.5),  # F
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=57, start=5.0, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=55, start=5.25, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=57, start=5.5, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=59, start=5.75, end=6.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=95, pitch=74, start=1.5, end=1.75),  # G
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=95, pitch=74, start=3.0, end=3.25),  # G
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=95, pitch=74, start=4.5, end=4.75),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.375),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=3.0),  # Ab
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.875),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.5),  # Ab
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0),  # Ab
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.375),  # F
    pretty_midi.Note(velocity=110, pitch=69, start=5.375, end=5.5),  # D
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=6.0),  # Ab
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for Bars 2-4 (1.5 - 6.0s)
drum_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=1.75, end=1.875),  # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),  # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.75, end=4.875),  # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
