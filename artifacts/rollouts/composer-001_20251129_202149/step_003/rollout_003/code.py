
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=63, start=2.25, end=2.5),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=63, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=58, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=57, start=4.25, end=4.5),
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=58, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=59, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.5),
    # Bar 6
    pretty_midi.Note(velocity=100, pitch=60, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=61, start=5.75, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=2.0),  # Bb
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=3.0),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=4.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=3.5, end=4.0),  # Bb
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=5.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=4.5, end=5.0),  # Bb
    # Bar 6
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=6.0),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=74, start=5.5, end=6.0),  # Bb
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=1.75, end=2.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),  # G
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=3.75),  # G#
    pretty_midi.Note(velocity=100, pitch=71, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.0, end=4.25),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),  # G
    # Bar 5
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.75),  # G#
    pretty_midi.Note(velocity=100, pitch=71, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.25, end=5.5),  # G
    # Bar 6
    pretty_midi.Note(velocity=100, pitch=69, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums for bars 2-6
for bar in range(2, 6):
    start_time = bar * 1.5
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=start_time, end=start_time + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start_time + 1.125, end=start_time + 1.5)
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 0.75, end=start_time + 0.875)
    pretty_midi.Note(velocity=100, pitch=38, start=start_time + 1.875, end=start_time + 2.0)
    # Hi-hat on every eighth
    for i in range(8):
        start = start_time + i * 0.1875
        end = start + 0.1875
        pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
