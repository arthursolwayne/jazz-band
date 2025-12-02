
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=80, pitch=60, start=2.625, end=3.0),  # C
    # Bar 3
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=80, pitch=62, start=3.375, end=3.75), # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),  # D
    # Bar 4
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25), # Eb
    pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=80, pitch=60, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),  # D7: A
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),  # D7: C#
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # D7: F#
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),  # D7: A
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.375),  # D7: C#
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # D7: F#
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D7: D
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.875),  # D7: A
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.875),  # D7: C#
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # D7: F#
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]
for note in drum_notes:
    drums.notes.append(note)

# Sax (Dante): One short motif, make it sing
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.6875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=1.6875, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0625), # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.0625, end=2.25), # G
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.4375), # A
    pretty_midi.Note(velocity=100, pitch=69, start=2.4375, end=2.625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.8125), # A
    pretty_midi.Note(velocity=100, pitch=65, start=2.8125, end=3.0),   # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.1875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.1875, end=3.375), # E
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.5625), # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.5625, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=3.9375),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.9375, end=4.125), # E
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.3125), # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.3125, end=4.5),   # C
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.6875),  # A
    pretty_midi.Note(velocity=100, pitch=69, start=4.6875, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.0625), # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.0625, end=5.25), # G
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.4375), # A
    pretty_midi.Note(velocity=100, pitch=69, start=5.4375, end=5.625), # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.8125), # A
    pretty_midi.Note(velocity=100, pitch=65, start=5.8125, end=6.0),   # G
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
