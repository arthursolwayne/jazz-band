
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
    # Hihat on every eighth
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

# Bass line (Marcus)
bass_notes = [
    # Dm7 walking bass line: D - C - Bb - A (bar 2)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.25), # C
    pretty_midi.Note(velocity=100, pitch=59, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),  # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7: D - F - A - C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.25),  # C
    # Dm7 again: D - F - A - C
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): 4-note motif, starts with D, ends with G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.0),   # A
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=2.125, end=2.25), # D
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.375), # C
    pretty_midi.Note(velocity=110, pitch=67, start=2.375, end=2.5),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.625),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=2.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=2.75, end=2.875), # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.875, end=3.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass line: C - Bb - A - G
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=59, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),   # G
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7: D - F - A - C
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.75),  # C
    # Fm7: F - A - C - Eb
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=4.5, end=5.25),  # Eb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Continue the motif, resolve to G
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.5),   # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=3.625, end=3.75), # D
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=3.875), # C
    pretty_midi.Note(velocity=110, pitch=67, start=3.875, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.125),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.25), # A
    pretty_midi.Note(velocity=110, pitch=64, start=4.25, end=4.375), # G
    pretty_midi.Note(velocity=110, pitch=62, start=4.375, end=4.5),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass line: G - F - D - C
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7: D - F - A - C
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.25),  # C
    # Dm7 again: D - F - A - C
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),  # D
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.0),   # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.125),  # E
    pretty_midi.Note(velocity=110, pitch=62, start=5.125, end=5.25), # D
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.375), # C
    pretty_midi.Note(velocity=110, pitch=67, start=5.375, end=5.5),  # A
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.625),  # B
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=5.75), # A
    pretty_midi.Note(velocity=110, pitch=64, start=5.75, end=5.875), # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.875, end=6.0),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 3 and 4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
