
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=63, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=61, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=63, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=63, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=61, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D7
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=82, start=1.5, end=1.875),
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=79, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=82, start=3.0, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=79, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=82, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, make it sing
# Start on Bb (62), then F (65), then G (67), then Bb (62) again, leaving it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=1.6875, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.0625, end=2.25),  # Bb
    # Rest
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.6875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=2.6875, end=2.875),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # Bb
    # End of phrase
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),  # Bb
    pretty_midi.Note(velocity=110, pitch=65, start=3.1875, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5625),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.5625, end=3.75),  # Bb
    # No resolution
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums continue with same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
