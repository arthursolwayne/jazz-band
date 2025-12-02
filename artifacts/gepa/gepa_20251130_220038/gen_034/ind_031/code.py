
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
    # Hi-hat on every eighth
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

# Bass: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=70, pitch=63, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=70, pitch=64, start=1.75, end=1.875),  # E
    pretty_midi.Note(velocity=70, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=70, pitch=69, start=2.125, end=2.25),  # A
    pretty_midi.Note(velocity=70, pitch=71, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=70, pitch=72, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=70, pitch=71, start=2.5, end=2.625),  # B
    pretty_midi.Note(velocity=70, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=70, pitch=67, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=70, pitch=65, start=2.875, end=3.0),  # F
    pretty_midi.Note(velocity=70, pitch=64, start=3.0, end=3.125),  # E
    pretty_midi.Note(velocity=70, pitch=63, start=3.125, end=3.25),  # Eb
    pretty_midi.Note(velocity=70, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=70, pitch=61, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=70, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=70, pitch=63, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=70, pitch=64, start=3.75, end=3.875),  # E
    pretty_midi.Note(velocity=70, pitch=65, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=4.0, end=4.125),  # G
    pretty_midi.Note(velocity=70, pitch=69, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=70, pitch=71, start=4.25, end=4.375),  # B
    pretty_midi.Note(velocity=70, pitch=72, start=4.375, end=4.5),  # C
    pretty_midi.Note(velocity=70, pitch=69, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=70, pitch=67, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=70, pitch=65, start=4.75, end=4.875),  # F
    pretty_midi.Note(velocity=70, pitch=64, start=4.875, end=5.0),  # E
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G7: G, B, D, F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=71, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=2.75),
    # Bar 4 (3.0 - 3.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),  # D7: D, F#, A, C
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),
    # Bar 4 (3.5 - 4.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),
    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.25),
    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.25),
    # Bar 4 (4.5 - 5.0s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Melody
sax_notes = [
    # Bar 2 (1.5 - 2.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=95, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=1.875, end=2.0),  # A
    # Bar 3 (2.0 - 2.5s)
    pretty_midi.Note(velocity=95, pitch=67, start=2.0, end=2.125),  # G
    pretty_midi.Note(velocity=95, pitch=64, start=2.125, end=2.25),  # E
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=95, pitch=65, start=2.375, end=2.5),  # F
    # Bar 4 (2.5 - 3.0s)
    pretty_midi.Note(velocity=95, pitch=67, start=2.5, end=2.625),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=2.625, end=2.75),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=2.75, end=2.875),  # B
    pretty_midi.Note(velocity=95, pitch=72, start=2.875, end=3.0),  # C
    # Bar 4 (3.0 - 3.5s)
    pretty_midi.Note(velocity=95, pitch=69, start=3.0, end=3.125),  # A
    pretty_midi.Note(velocity=95, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=95, pitch=64, start=3.25, end=3.375),  # E
    pretty_midi.Note(velocity=95, pitch=62, start=3.375, end=3.5),  # D
    # Bar 4 (3.5 - 4.0s)
    pretty_midi.Note(velocity=95, pitch=65, start=3.5, end=3.625),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=3.625, end=3.75),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=95, pitch=71, start=3.875, end=4.0),  # B
    # Bar 4 (4.0 - 4.5s)
    pretty_midi.Note(velocity=95, pitch=72, start=4.0, end=4.125),  # C
    pretty_midi.Note(velocity=95, pitch=69, start=4.125, end=4.25),  # A
    pretty_midi.Note(velocity=95, pitch=67, start=4.25, end=4.375),  # G
    pretty_midi.Note(velocity=95, pitch=64, start=4.375, end=4.5),  # E
    # Bar 4 (4.5 - 5.0s)
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=95, pitch=65, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=95, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=4.875, end=5.0),  # A
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
