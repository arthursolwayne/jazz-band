
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
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus)
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=1.875),  # Gb
    pretty_midi.Note(velocity=80, pitch=51, start=1.875, end=2.0),  # A
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=80, pitch=53, start=2.125, end=2.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=80, pitch=54, start=2.375, end=2.5),  # C
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=54, start=2.5, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=56, start=2.625, end=2.75),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=2.75, end=2.875),  # Db
    pretty_midi.Note(velocity=80, pitch=57, start=2.875, end=3.0),  # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - F7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.75),  # E
    # Bar 3 - rest
    pretty_midi.Note(velocity=80, pitch=71, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=70, pitch=76, start=2.0, end=2.125),  # A
    pretty_midi.Note(velocity=75, pitch=69, start=2.0, end=2.125),  # C
    pretty_midi.Note(velocity=70, pitch=74, start=2.0, end=2.125),  # E
    # Bar 4 - F7 again
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=95, pitch=69, start=2.5, end=2.75),  # C
    pretty_midi.Note(velocity=90, pitch=74, start=2.5, end=2.75),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante) - Motif in F
sax_notes = [
    # Bar 2 - Start the motif
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=105, pitch=68, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.375),  # F#
    # Bar 3 - Rest
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=95, pitch=66, start=2.75, end=3.0),  # F
    # Bar 4 - Finish the motif
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=110, pitch=69, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=105, pitch=68, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0),  # F
]
for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=38, start=1.625, end=1.75),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.625),
    pretty_midi.Note(velocity=100, pitch=36, start=4.0, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.25),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("wayne_moment.mid")
