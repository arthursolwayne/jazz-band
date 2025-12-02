
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth note
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): chromatic approach to Dm
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 - Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C
    # Bar 3 - G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F
    # Bar 4 - Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Saxophone (Dante): short motif in Dm, leave it hanging
sax_notes = [
    # Bar 2: Dm motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # D
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),  # C
    # Bar 4: Return and finish
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
