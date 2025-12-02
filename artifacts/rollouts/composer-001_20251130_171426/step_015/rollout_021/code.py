
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    # Hi-hats on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line with chromatic approaches
bass_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=49, start=2.0, end=2.25),  # G#
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.5),  # A
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.75),  # A#
    pretty_midi.Note(velocity=90, pitch=53, start=2.75, end=3.0),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=50, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=47, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=90, pitch=46, start=4.25, end=4.5),  # Eb
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.5),  # A#
    pretty_midi.Note(velocity=90, pitch=53, start=5.5, end=5.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=51, start=5.75, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s) - Comp on 2 and 4
    pretty_midi.Note(velocity=95, pitch=62, start=2.0, end=2.25),  # D7
    pretty_midi.Note(velocity=95, pitch=66, start=2.0, end=2.25),
    pretty_midi.Note(velocity=95, pitch=60, start=2.0, end=2.25),
    pretty_midi.Note(velocity=95, pitch=65, start=2.0, end=2.25),
    pretty_midi.Note(velocity=95, pitch=62, start=3.0, end=3.25),  # D7
    pretty_midi.Note(velocity=95, pitch=66, start=3.0, end=3.25),
    pretty_midi.Note(velocity=95, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=95, pitch=65, start=3.0, end=3.25),
    # Bar 3 (3.0 - 4.5s) - Comp on 2 and 4
    pretty_midi.Note(velocity=95, pitch=62, start=4.0, end=4.25),  # D7
    pretty_midi.Note(velocity=95, pitch=66, start=4.0, end=4.25),
    pretty_midi.Note(velocity=95, pitch=60, start=4.0, end=4.25),
    pretty_midi.Note(velocity=95, pitch=65, start=4.0, end=4.25),
    pretty_midi.Note(velocity=95, pitch=62, start=5.0, end=5.25),  # D7
    pretty_midi.Note(velocity=95, pitch=66, start=5.0, end=5.25),
    pretty_midi.Note(velocity=95, pitch=60, start=5.0, end=5.25),
    pretty_midi.Note(velocity=95, pitch=65, start=5.0, end=5.25),
    # Bar 4 (4.5 - 6.0s) - Comp on 2 and 4
    pretty_midi.Note(velocity=95, pitch=62, start=5.5, end=5.75),  # D7
    pretty_midi.Note(velocity=95, pitch=66, start=5.5, end=5.75),
    pretty_midi.Note(velocity=95, pitch=60, start=5.5, end=5.75),
    pretty_midi.Note(velocity=95, pitch=65, start=5.5, end=5.75),
]
piano.notes.extend(piano_notes)

# Sax (Dante): One short motif, make it sing.
# Start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=110, pitch=68, start=2.25, end=2.5),  # Bb
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=110, pitch=68, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),  # G#
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.75),  # G#
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=110, pitch=66, start=5.0, end=5.25),  # A
    pretty_midi.Note(velocity=110, pitch=68, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=110, pitch=67, start=5.5, end=5.75),  # A#
    pretty_midi.Note(velocity=110, pitch=68, start=5.75, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4 (1.5 - 6.0s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hi-hats on every eighth
    for i in range(8):
        pretty_midi.Note(velocity=80, pitch=42, start=start + (i * 0.1875), end=start + (i * 0.1875) + 0.1875)

drums.notes.extend([note for note in drums.notes if note.start >= 1.5])

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
