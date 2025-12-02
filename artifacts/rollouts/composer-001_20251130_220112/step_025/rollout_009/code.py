
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
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Walking line, chromatic approaches, never the same note twice
bass_notes = [
    # Bar 2
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.875, end=2.25),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.625, end=3.0),  # D
    # Bar 3
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=49, start=3.375, end=3.75),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=90, pitch=51, start=4.125, end=4.5),  # Eb
    # Bar 4
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=5.25, end=5.625),  # C#
    pretty_midi.Note(velocity=90, pitch=50, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),  # D7 - D
    pretty_midi.Note(velocity=80, pitch=67, start=1.5, end=1.875),  # D7 - A
    pretty_midi.Note(velocity=80, pitch=69, start=1.5, end=1.875),  # D7 - C
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.875),  # D7 - F
    # Bar 3 (comp on 2 and 4)
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),  # D7 - D
    pretty_midi.Note(velocity=80, pitch=67, start=3.0, end=3.375),  # D7 - A
    pretty_midi.Note(velocity=80, pitch=69, start=3.0, end=3.375),  # D7 - C
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.375),  # D7 - F
    # Bar 4 (comp on 2 and 4)
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),  # D7 - D
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),  # D7 - A
    pretty_midi.Note(velocity=80, pitch=69, start=4.5, end=4.875),  # D7 - C
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),  # D7 - F
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
sax_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),  # G
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # Bb
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),  # G
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),  # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare 4
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),  # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),  # Snare 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),  # Snare 4
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick 1
    pretty_midi.Note(velocity=110, pitch=38, start=5.875, end=6.0),  # Snare 2
]
drums.notes.extend(drum_notes)

# Add hi-hats on every eighth for all bars 2-4
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    for i in range(8):
        note_start = start + i * 0.1875
        note_end = note_start + 0.1875
        if note_end > 6.0:
            break
        pretty_midi.Note(velocity=80, pitch=42, start=note_start, end=note_end)

drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
