
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
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: Walking line in Dm
bass_notes = [
    # Dm: D F A C
    # Walking line with chromatic approaches
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.125),  # E
    pretty_midi.Note(velocity=90, pitch=63, start=2.125, end=2.25),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=2.375, end=2.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=2.625, end=2.75),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=2.75, end=2.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=2.875, end=3.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Dm7 = D F A C
piano_notes = [
    # Bar 2: 2nd beat (0.75s into bar)
    pretty_midi.Note(velocity=95, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=2.25, end=2.5),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=2.25, end=2.5),  # Bb
    # Bar 3: 2nd beat (0.75s into bar)
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.0),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Short motif, start it, leave it hanging, come back and finish it
# Dm scale: D F G A Bb C D
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.0),  # Bb
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=2.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=2.875, end=3.0),  # Bb
    # Bar 4: Come back and finish
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Drums (3.0 - 4.5s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 4: Full quartet (3.0 - 6.0s)

# Bass: Walking line in Dm
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=3.125, end=3.25),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.625),  # E
    pretty_midi.Note(velocity=90, pitch=63, start=3.625, end=3.75),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=3.875, end=4.0),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.125, end=4.25),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=4.25, end=4.375),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.375, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=4.625, end=4.75),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.125),  # E
    pretty_midi.Note(velocity=90, pitch=63, start=5.125, end=5.25),  # D#
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=90, pitch=60, start=5.375, end=5.5),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=5.625),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=5.75),  # C#
    pretty_midi.Note(velocity=90, pitch=60, start=5.75, end=5.875),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=5.875, end=6.0),  # D
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Dm7 = D F A C
piano_notes = [
    # Bar 3: 2nd beat (0.75s into bar)
    pretty_midi.Note(velocity=95, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=3.75, end=4.0),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=3.75, end=4.0),  # Bb
    # Bar 4: 2nd beat (0.75s into bar)
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=95, pitch=64, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=95, pitch=67, start=4.5, end=4.75),  # G
    pretty_midi.Note(velocity=95, pitch=69, start=4.5, end=4.75),  # Bb
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Completion of motif
# Dm scale: D F G A Bb C D
sax_notes = [
    # Bar 4: End with a resolution
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.125, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.375, end=5.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.625),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Drums (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.75, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
