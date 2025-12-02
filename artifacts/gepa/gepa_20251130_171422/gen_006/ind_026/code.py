
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
    # Hihat on every 8th
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
    # Bar 2: D (Dm root) on 1, chromatic approach to C on 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.0),  # C
    # Bar 2: chromatic approach to Bb on 3, Bb on 4
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.1875),  # Bb
    pretty_midi.Note(velocity=80, pitch=59, start=2.1875, end=2.375),  # A
    pretty_midi.Note(velocity=80, pitch=58, start=2.375, end=2.5625),  # Ab
    pretty_midi.Note(velocity=80, pitch=57, start=2.5625, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=57, start=2.75, end=3.0),  # G
    # Bar 3: F on 1, chromatic approach to E on 2
    pretty_midi.Note(velocity=80, pitch=58, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=3.375, end=3.5625),  # E
    pretty_midi.Note(velocity=80, pitch=56, start=3.5625, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=3.9375, end=4.25),  # D
    # Bar 4: F on 1, chromatic approach to E on 2
    pretty_midi.Note(velocity=80, pitch=58, start=4.25, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=57, start=4.625, end=4.8125),  # E
    pretty_midi.Note(velocity=80, pitch=56, start=4.8125, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=55, start=5.0, end=5.1875),  # D
    pretty_midi.Note(velocity=80, pitch=55, start=5.1875, end=5.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 on 1
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # C
    # Bar 2: comp on 2
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.0),  # C
    # Bar 3: comp on 4
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.9375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.9375),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=3.9375),  # C
    # Bar 4: comp on 2
    pretty_midi.Note(velocity=90, pitch=60, start=4.625, end=4.8125),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.625, end=4.8125),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=4.625, end=4.8125),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=4.625, end=4.8125),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - short motif, make it sing
sax_notes = [
    # Bar 2 (1.5 - 2.0s): motif starts
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.625),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=1.875),  # Bb
    # Bar 3 (2.0 - 2.5s): leave it hanging
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),  # Bb
    # Bar 4 (3.0 - 3.5s): come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),  # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.875, end=4.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
