
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=100, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),   # D
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=100, pitch=52, start=4.125, end=4.5),   # F
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # C#
    pretty_midi.Note(velocity=100, pitch=51, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=6.0),   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (F, A, C, D)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),  # C
    # Bar 3: G7 (B, D, F, G)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),  # G
    # Bar 4: Cm7 (Eb, G, Bb, C)
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Motif - start it, leave it hanging, return and finish it
# Dm scale: D, Eb, F, G, A, Bb, C
sax_notes = [
    # Bar 2: D, Eb, F, G
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=100, pitch=51, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.0625), # F
    pretty_midi.Note(velocity=100, pitch=55, start=2.0625, end=2.25), # G
    # Bar 3: A, Bb, C, D
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.1875),  # A
    pretty_midi.Note(velocity=100, pitch=55, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.375, end=3.5625), # C
    pretty_midi.Note(velocity=100, pitch=50, start=3.5625, end=3.75), # D
    # Bar 4: Eb, F, G, A, Bb, C, D
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=4.6875),  # Eb
    pretty_midi.Note(velocity=100, pitch=53, start=4.6875, end=4.875), # F
    pretty_midi.Note(velocity=100, pitch=55, start=4.875, end=5.0625), # G
    pretty_midi.Note(velocity=100, pitch=58, start=5.0625, end=5.25), # A
    pretty_midi.Note(velocity=100, pitch=55, start=5.25, end=5.4375), # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=5.4375, end=5.625), # C
    pretty_midi.Note(velocity=100, pitch=50, start=5.625, end=5.8125), # D
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
