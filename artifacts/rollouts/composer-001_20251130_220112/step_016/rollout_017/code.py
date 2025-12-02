
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus) - walking in Dm, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.625),  # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=63, start=3.0, end=3.375),  # D#
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=59, start=4.125, end=4.5),  # B
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=60, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane) - 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (F, A, C, D)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    # Bar 3: rest
    # Bar 4: Dm7 again
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante) - motif in Dm, short and singable
sax_notes = [
    # Bar 2: motif starts
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=1.875),  # D
    # Bar 3: rests
    # Bar 4: motif returns and resolves
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Add drum fills in bars 2-4
for i in range(2, 6):
    start = i * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0),
    # Append each note to drums
    for note in [pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
                 pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875),
                 pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0),
                 pretty_midi.Note(velocity=80, pitch=42, start=start, end=start + 0.375),
                 pretty_midi.Note(velocity=80, pitch=42, start=start + 0.375, end=start + 0.75),
                 pretty_midi.Note(velocity=80, pitch=42, start=start + 0.75, end=start + 1.125),
                 pretty_midi.Note(velocity=80, pitch=42, start=start + 1.125, end=start + 1.5),
                 pretty_midi.Note(velocity=80, pitch=42, start=start + 1.5, end=start + 1.875),
                 pretty_midi.Note(velocity=80, pitch=42, start=start + 1.875, end=start + 2.25),
                 pretty_midi.Note(velocity=80, pitch=42, start=start + 2.25, end=start + 2.625),
                 pretty_midi.Note(velocity=80, pitch=42, start=start + 2.625, end=start + 3.0)]:
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
