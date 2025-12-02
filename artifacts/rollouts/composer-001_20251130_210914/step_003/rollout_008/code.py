
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

# Bass: Walking line in Dm, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: D (root), F (b7), E (chromatic), G (b5)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G

    # Bar 3: C (b9), B (b13), A (chromatic), D (root)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=61, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D

    # Bar 4: F (b7), E (chromatic), D (root), C (b9)
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),   # F
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),   # C
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4, keep it moving
piano_notes = [
    # Bar 2: Dm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # C

    # Bar 2: comp on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D

    # Bar 3: Dm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # C

    # Bar 3: comp on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D

    # Bar 4: Dm7 on beat 1
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # C

    # Bar 4: comp on beat 2
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E (Dm7)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # D (Dm7)

    # Bar 3: Continue the motif
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G (Dm7)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # Bb (Dm7)

    # Bar 4: Finish the motif
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),  # C (Dm7)
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # E (Dm7)
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.625),  # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G (Dm7)
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
