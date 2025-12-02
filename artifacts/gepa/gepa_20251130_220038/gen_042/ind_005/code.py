
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody: Fm7 -> Gb -> Ab -> Bb -> F
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.6875),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=1.6875, end=1.875), # Gb
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0625), # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=2.0625, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),     # F
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.6875, end=1.875), # Eb
    pretty_midi.Note(velocity=80, pitch=48, start=1.875, end=2.0625), # F#
    pretty_midi.Note(velocity=80, pitch=49, start=2.0625, end=2.25),  # G
    pretty_midi.Note(velocity=80, pitch=50, start=2.25, end=2.5),     # G#
    pretty_midi.Note(velocity=80, pitch=51, start=2.5, end=2.6875),   # A
    pretty_midi.Note(velocity=80, pitch=50, start=2.6875, end=2.875), # G#
    pretty_midi.Note(velocity=80, pitch=49, start=2.875, end=3.0),    # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords: 7th chords, comp on 2 and 4
# Bar 2: Fm7 on beat 1
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6875),   # F
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.6875),   # Ab
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6875),   # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=1.5, end=1.6875),   # D

    # Bar 3: Bb7 on beat 2
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.4375),  # Bb
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.4375),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.4375),  # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.4375),  # Ab

    # Bar 4: Ab7 on beat 4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=3.9375),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=3.9375),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.9375),  # F
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Ab -> Bb -> F -> F#
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.1875),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=3.1875, end=3.375), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5625), # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.5625, end=3.75),  # F#
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=3.0, end=3.1875),   # G
    pretty_midi.Note(velocity=80, pitch=50, start=3.1875, end=3.375), # G#
    pretty_midi.Note(velocity=80, pitch=51, start=3.375, end=3.5625), # A
    pretty_midi.Note(velocity=80, pitch=52, start=3.5625, end=3.75),  # A#
    pretty_midi.Note(velocity=80, pitch=53, start=3.75, end=3.9375),  # B
    pretty_midi.Note(velocity=80, pitch=51, start=3.9375, end=4.125), # A#
    pretty_midi.Note(velocity=80, pitch=50, start=4.125, end=4.3125), # G#
    pretty_midi.Note(velocity=80, pitch=49, start=4.3125, end=4.5),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords: 7th chords, comp on 2 and 4
# Bar 3: Ab7 on beat 1
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1875),   # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.1875),   # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1875),   # D
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1875),   # F

    # Bar 4: D7 on beat 2
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=90, pitch=58, start=3.75, end=3.9375),  # F
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=3.9375),  # G
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=3.9375),  # A
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: F -> Bb -> Ab -> Gb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.6875),  # F
    pretty_midi.Note(velocity=100, pitch=57, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0625), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=5.0625, end=5.25),  # Gb
]

for note in sax_notes:
    sax.notes.append(note)

# Bass line: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=49, start=4.5, end=4.6875),   # G
    pretty_midi.Note(velocity=80, pitch=50, start=4.6875, end=4.875), # G#
    pretty_midi.Note(velocity=80, pitch=51, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=80, pitch=52, start=5.0625, end=5.25),  # A#
    pretty_midi.Note(velocity=80, pitch=53, start=5.25, end=5.4375),  # B
    pretty_midi.Note(velocity=80, pitch=51, start=5.4375, end=5.625), # A#
    pretty_midi.Note(velocity=80, pitch=50, start=5.625, end=5.8125), # G#
    pretty_midi.Note(velocity=80, pitch=49, start=5.8125, end=6.0),   # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano chords: 7th chords, comp on 2 and 4
# Bar 4: G7 on beat 3
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.0625),  # G
    pretty_midi.Note(velocity=90, pitch=63, start=4.875, end=5.0625),  # Bb
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.0625),  # C
    pretty_midi.Note(velocity=90, pitch=69, start=4.875, end=5.0625),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.875, end=bar_start + 2.0)
    # Hi-hats on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=90, pitch=42, start=bar_start + i * 0.1875, end=bar_start + (i + 1) * 0.1875)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_introduction.mid")
