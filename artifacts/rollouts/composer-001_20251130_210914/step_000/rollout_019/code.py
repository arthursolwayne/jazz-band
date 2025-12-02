
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

# Bass line - Marcus - chromatic walking line with approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=61, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=63, start=2.25, end=2.625),  # D#
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),   # E
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=68, start=4.125, end=4.5),   # G#
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=70, start=4.875, end=5.25),  # A#
    pretty_midi.Note(velocity=90, pitch=71, start=5.25, end=5.625),  # B
    pretty_midi.Note(velocity=90, pitch=72, start=5.625, end=6.0),   # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano - Diane - 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=90, pitch=74, start=2.25, end=2.625),  # B
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),  # C
    # Bar 3: G7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125),  # G
    pretty_midi.Note(velocity=90, pitch=76, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=73, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # F
    # Bar 4: C7 on 2 and 4
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625),  # E
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625),  # Bb
]
for note in piano_notes:
    piano.notes.append(note)

# Sax - Dante - short motif, start it, leave it hanging, finish it
sax_notes = [
    # Bar 2: motif starts
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # C
    # Bar 3: motif continues
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # D
    # Bar 4: motif resolves
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),   # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),   # Snare on 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare on 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
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
