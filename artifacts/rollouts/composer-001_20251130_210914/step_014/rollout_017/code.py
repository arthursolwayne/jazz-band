
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

for note in drum_notes:
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line, chromatic approaches, never the same note twice
# Dm7 = D F A C
# Walking line: D -> C -> B -> A -> G -> F -> E -> D -> C -> B -> A -> G -> F -> E -> D
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=2.125, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=2.25, end=2.375),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=2.625, end=2.75),  # B
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=59, start=2.875, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.75),  # C
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D -> F -> A -> D (with a slight chromatic twist)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # E (chromatic)
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=1.875, end=2.0),  # A
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=2.75),  # E (chromatic)
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875),  # F
    pretty_midi.Note(velocity=110, pitch=71, start=2.875, end=3.0),  # A
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
