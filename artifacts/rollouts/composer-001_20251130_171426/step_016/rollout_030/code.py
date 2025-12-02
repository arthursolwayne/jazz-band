
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone motif: Dm7 - F - G - Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # Bb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=2.625, end=3.0),   # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # C
    # Bar 3: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: repeat the motif, but shift up a half-step (Ebm)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Ebm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=80, pitch=54, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=80, pitch=52, start=4.125, end=4.5),   # F
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Ebm7 on 2 and 4
piano_notes = [
    # Bar 3: Ebm7 (Eb, F, Ab, Bb)
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # Bb
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: return to Dm, but end on a suspended note (G) to leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G (suspended)
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=6.0),   # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Dm7 on 2 and 4
piano_notes = [
    # Bar 4: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick=36, snare=38, hihat=42

# Bar 3: Full drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
