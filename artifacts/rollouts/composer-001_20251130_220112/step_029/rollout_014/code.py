
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
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Saxophone: Simple motif, start on F (65), G (67), A (69), Bb (70)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.75),  # F (47)
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # G (49)
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # Ab (50)
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # Bb (52)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 on beat 2 (0.75s into the bar)
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.375),  # F

    # Bar 3: A7 on beat 2 (0.75s into bar 3)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=3.875),  # E
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=3.875),  # G
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Saxophone: Repeat motif, but with slight variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=52, start=3.0, end=3.25),  # Bb (52)
    pretty_midi.Note(velocity=80, pitch=53, start=3.25, end=3.5),  # Bb (53)
    pretty_midi.Note(velocity=80, pitch=55, start=3.5, end=3.75),  # C (55)
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.0),  # D (57)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: A7 on beat 2 (0.75s into the bar)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=3.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=3.875),  # E
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=3.875),  # G

    # Bar 4: D7 on beat 2 (0.75s into bar 4)
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.625),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.625),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Saxophone: Repeat motif, but with slight variation and a resolution
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.5),
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F minor
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=57, start=4.5, end=4.75),  # D (57)
    pretty_midi.Note(velocity=80, pitch=59, start=4.75, end=5.0),  # Eb (59)
    pretty_midi.Note(velocity=80, pitch=61, start=5.0, end=5.25),  # F (61)
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.5),  # Ab (64)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: D7 on beat 2 (0.75s into the bar)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.375),  # C

    # Bar 4: F7 on beat 4 (0.75s into bar 4)
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=5.75),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=71, start=5.625, end=5.75),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=5.625, end=5.75),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
