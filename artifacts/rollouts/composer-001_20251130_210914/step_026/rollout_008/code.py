
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

# Bass line: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=90, pitch=72, start=2.625, end=3.0),   # G#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=73, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # A#
    pretty_midi.Note(velocity=90, pitch=75, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=76, start=4.125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # C#
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),  # D#
    pretty_midi.Note(velocity=90, pitch=80, start=5.625, end=6.0),   # E
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # E
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # E
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Motif - start it, leave it hanging, come back and finish it
# F - G - Bb - F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # G
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),   # G
    pretty_midi.Note(velocity=100, pitch=68, start=2.5, end=2.625),   # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=3.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),   # G
    pretty_midi.Note(velocity=100, pitch=68, start=4.0, end=4.125),   # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.375),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5),   # G
    pretty_midi.Note(velocity=100, pitch=68, start=5.5, end=5.625),   # Bb
]
for note in sax_notes:
    sax.notes.append(note)

# Drums in bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),   # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),   # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),   # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),  # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),   # Snare on 4
]
for note in drum_notes:
    drums.notes.append(note)

# Add hi-hat on every eighth in bars 2-4
for i in range(2, 6):
    start = i * 1.5
    for j in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)
    start = i * 1.5
    for j in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=start + j * 0.375, end=start + j * 0.375 + 0.375)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
