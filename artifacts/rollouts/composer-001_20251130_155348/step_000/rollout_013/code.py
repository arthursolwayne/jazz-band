
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
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

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),   # F
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=3.375, end=3.75),  # G#
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # A#
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=6.0),   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),   # D
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),   # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),   # D
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=100, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),   # Bb
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),   # D
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - motif in D, one short phrase, make it sing
sax_notes = [
    # Start on D (62), ascending to G (67), then back to D (62), leave it hanging
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.0),
    # Repeat the motif with a slight variation in the second bar
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=65, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.375),
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.5),
    # Repeat again in the third bar
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=65, start=4.625, end=4.75),
    pretty_midi.Note(velocity=110, pitch=67, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.0),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_introduction.mid")
