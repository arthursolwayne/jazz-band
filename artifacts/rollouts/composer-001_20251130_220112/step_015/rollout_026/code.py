
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
# Sax melody: F, Ab, Bb, C (F7 chord)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.625, end=1.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F7 (F, G#, Bb, C)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=70, pitch=69, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=70, pitch=72, start=1.875, end=2.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (1.625 - 1.75)
    pretty_midi.Note(velocity=80, pitch=65, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.625, end=1.75),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=1.625, end=1.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=1.625, end=1.75),  # C
    # F7 on beat 4 (1.875 - 2.0)
    pretty_midi.Note(velocity=80, pitch=65, start=1.875, end=2.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=1.875, end=2.0),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=1.875, end=2.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody: G, Bb, C, D (G7 chord)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.125, end=3.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=74, start=3.375, end=3.5),  # D
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in G7 (G, A#, C, D)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=67, start=3.0, end=3.125),  # G
    pretty_midi.Note(velocity=70, pitch=69, start=3.125, end=3.25),  # A#
    pretty_midi.Note(velocity=70, pitch=72, start=3.25, end=3.375),  # C
    pretty_midi.Note(velocity=70, pitch=74, start=3.375, end=3.5),  # D
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # G7 on beat 2 (3.125 - 3.25)
    pretty_midi.Note(velocity=80, pitch=67, start=3.125, end=3.25),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.125, end=3.25),  # A#
    pretty_midi.Note(velocity=80, pitch=72, start=3.125, end=3.25),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=3.125, end=3.25),  # D
    # G7 on beat 4 (3.375 - 3.5)
    pretty_midi.Note(velocity=80, pitch=67, start=3.375, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5),  # A#
    pretty_midi.Note(velocity=80, pitch=72, start=3.375, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=76, start=3.375, end=3.5),  # D
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody: F, Ab, Bb, C (F7 chord)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.0),  # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in F7 (F, G#, Bb, C)
bass_notes = [
    pretty_midi.Note(velocity=70, pitch=65, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=70, pitch=67, start=4.625, end=4.75),  # G#
    pretty_midi.Note(velocity=70, pitch=69, start=4.75, end=4.875),  # Bb
    pretty_midi.Note(velocity=70, pitch=72, start=4.875, end=5.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # F7 on beat 2 (4.625 - 4.75)
    pretty_midi.Note(velocity=80, pitch=65, start=4.625, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.625, end=4.75),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.625, end=4.75),  # C
    # F7 on beat 4 (4.875 - 5.0)
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=80, pitch=67, start=4.875, end=5.0),  # G#
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=72, start=4.875, end=5.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: kicks on 1 and 3, snares on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
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
