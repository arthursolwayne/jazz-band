
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
# Marcus: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.5),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # Dm7 on 1
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=1.5, end=1.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),  # F
    # F7 on 2
    pretty_midi.Note(velocity=95, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    # Dm7 on 3
    pretty_midi.Note(velocity=95, pitch=62, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # F
    # G7 on 4
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=85, pitch=74, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=70, start=2.25, end=2.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, one short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: D (62) to F (65) to Bb (67) on beat 1
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=65, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),
    # Bar 3: G (67) to Bb (67) to D (69) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=67, start=2.125, end=2.25),
    pretty_midi.Note(velocity=110, pitch=69, start=2.25, end=2.5),
    # Bar 4: F (65) to D (62) on beat 3
    pretty_midi.Note(velocity=110, pitch=65, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=62, start=2.625, end=2.75),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # G7 on 1
    pretty_midi.Note(velocity=95, pitch=67, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.25),  # B
    pretty_midi.Note(velocity=85, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=90, pitch=70, start=3.0, end=3.25),  # F
    # Dm7 on 2
    pretty_midi.Note(velocity=95, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F
    # F7 on 3
    pretty_midi.Note(velocity=95, pitch=65, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=3.75),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=3.5, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=3.75),  # G
    # G7 on 4
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=3.75, end=4.0),  # B
    pretty_midi.Note(velocity=85, pitch=74, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=70, start=3.75, end=4.0),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, continue motif
sax_notes = [
    # Bar 3: F (65) to D (62) to Bb (67) on beat 1
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=62, start=3.125, end=3.25),
    pretty_midi.Note(velocity=110, pitch=67, start=3.25, end=3.5),
    # Bar 4: Bb (67) to F (65) on beat 2
    pretty_midi.Note(velocity=110, pitch=67, start=3.5, end=3.625),
    pretty_midi.Note(velocity=110, pitch=65, start=3.625, end=3.75),
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking line
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),  # A
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),  # F
]

for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords, comp on 2 and 4
piano_notes = [
    # G7 on 1
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.75),  # B
    pretty_midi.Note(velocity=85, pitch=74, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=90, pitch=70, start=4.5, end=4.75),  # F
    # Dm7 on 2
    pretty_midi.Note(velocity=95, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=85, pitch=69, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    # F7 on 3
    pretty_midi.Note(velocity=95, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=85, pitch=72, start=5.0, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.25),  # G
    # G7 on 4
    pretty_midi.Note(velocity=95, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=85, pitch=74, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=70, start=5.25, end=5.5),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Dante: Tenor sax, finish the motif
sax_notes = [
    # Bar 4: G (67) to C (69) on beat 3
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.625),
    pretty_midi.Note(velocity=110, pitch=69, start=4.625, end=4.75),
    # Bar 4: F (65) on beat 4
    pretty_midi.Note(velocity=110, pitch=65, start=4.75, end=5.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=2.75),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 6
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
