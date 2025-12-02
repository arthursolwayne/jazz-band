
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=47, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=49, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif that sings, starts, leaves it hanging, finishes
# Dm scale: D, Eb, F, G, A, Bb, C
# Motif: D - Eb - F - G (1st bar), leave it hanging, then return to complete the phrase

sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # G
    # Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=2.5, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.75),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=2.875),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=2.875, end=3.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
