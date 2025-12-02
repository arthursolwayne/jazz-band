
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
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus (Bass): Walking line, chromatic approaches, never the same note twice.
bass_notes = [
    # Bar 2: Dm7 - C, Bb, A, B
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=2.25, end=2.625),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),  # B
    # Bar 3: Dm7 - C, Bb, A, G
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=90, pitch=57, start=4.125, end=4.5),  # G
    # Bar 4: Dm7 - C, Bb, A, B
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=59, start=5.25, end=5.625),  # A
    pretty_midi.Note(velocity=90, pitch=60, start=5.625, end=6.0),  # B
]
for note in bass_notes:
    bass.notes.append(note)

# Diane (Piano): 7th chords, comp on 2 and 4.
piano_notes = [
    # Bar 2: Dm7 - F (2) and C (4)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.625, end=3.0),  # C
    # Bar 3: Dm7 - F (2) and C (4)
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C
    # Bar 4: Dm7 - F (2) and C (4)
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Dante (Sax): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Dm7 - F (2), Bb (3), D (1), C (4)
    pretty_midi.Note(velocity=110, pitch=64, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75),  # D
    # Bar 3: Dm7 - F (2), Bb (3), D (1), C (4)
    pretty_midi.Note(velocity=110, pitch=64, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=3.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.25),  # D
    # Bar 4: Dm7 - F (2), Bb (3), D (1), C (4)
    pretty_midi.Note(velocity=110, pitch=64, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=110, pitch=60, start=5.25, end=5.375),  # Bb
    pretty_midi.Note(velocity=110, pitch=62, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=110, pitch=60, start=5.75, end=6.0),  # C (finish the motif)
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=2.875, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.375, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
