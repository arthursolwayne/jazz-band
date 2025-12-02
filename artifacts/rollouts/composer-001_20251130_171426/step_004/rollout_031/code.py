
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.875, end=2.25),
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

# Bass: Walking line in Dm, chromatic approaches, no same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: Dm7 (F, A, C, D)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    # Bar 3: G7 (B, D, F, G)
    pretty_midi.Note(velocity=90, pitch=73, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # G
    # Bar 4: Cm7 (Eb, G, Bb, C)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif: E-F-G-F, then leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=66, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # F
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: Walking line in Dm, chromatic approaches, no same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: G7 (B, D, F, G)
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # G
    # Bar 4: Cm7 (Eb, G, Bb, C)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]
for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: Walking line in Dm, chromatic approaches, no same note twice
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),   # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: Cm7 (Eb, G, Bb, C)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.875),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=38, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
for note in drum_notes:
    drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
