
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

# Bass line (Marcus)
bass_notes = [
    # Bar 2: walking line in F
    pretty_midi.Note(velocity=100, pitch=47, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=1.875, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=49, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # Bb
    # Bar 3: chromatic approach
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=49, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=48, start=4.125, end=4.5),  # G
    # Bar 4: resolution
    pretty_midi.Note(velocity=100, pitch=47, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=46, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=47, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=48, start=5.625, end=6.0),  # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane)
piano_notes = [
    # Bar 2: C7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=74, start=3.875, end=4.25),
    pretty_midi.Note(velocity=100, pitch=74, start=4.875, end=5.25),
    # Bar 4: F7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=76, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=76, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Tenor sax (Dante) - motif in F
sax_notes = [
    # Bar 2: start the motif
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A
    # Bar 3: leave it hanging
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F
    # Bar 4: come back and finish
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
