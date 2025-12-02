
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

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=65, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=2.625, end=3.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, in D
piano_notes = [
    # Bar 2: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # D
    # Bar 3: D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.625, end=3.0),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - start it, leave it hanging, return to finish it
# D (62) -> F (65) -> B (69) -> D (62) - start on beat 1
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=105, pitch=65, start=1.875, end=2.25),
    pretty_midi.Note(velocity=105, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=105, pitch=62, start=2.625, end=3.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums continue
# Kick on 1 and 3 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    # Hi-hat on every eighth (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5)
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Continue full quartet (3.0 - 6.0s)
# Bass line: walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),   # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, in D
piano_notes = [
    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # D
    # Bar 4: D7 on beat 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # G
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=90, pitch=71, start=4.125, end=4.5),   # D
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - return and finish it
# D (62) -> F (65) -> B (69) -> D (62) - start on beat 1
sax_notes = [
    pretty_midi.Note(velocity=105, pitch=62, start=3.0, end=3.375),
    pretty_midi.Note(velocity=105, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=105, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=105, pitch=62, start=4.125, end=4.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Drums continue
# Kick on 1 and 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hi-hat on every eighth (3.0 - 4.5s)
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

midi.write("dante_russo_intro.mid")
