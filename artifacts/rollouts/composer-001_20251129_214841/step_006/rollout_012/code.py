
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
    # Hihat on every eighth
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

# Bars 2-4 (1.5 - 6.0s)
# Bass: Walking line, chromatic approaches, never the same note twice
bass_line = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=63, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=61, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=58, start=4.25, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=61, start=5.0, end=5.25),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=63, start=5.5, end=5.75),
    pretty_midi.Note(velocity=100, pitch=63, start=5.75, end=6.0),
]
bass.notes.extend(bass_line)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=70, start=1.75, end=2.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=70, start=4.75, end=5.0),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (1.5 - 3.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),
    pretty_midi.Note(velocity=100, pitch=60, start=2.75, end=3.0),
    # Bar 3 (3.0 - 4.5s)
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=60, start=4.25, end=4.5),
    # Bar 4 (4.5 - 6.0s)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 2-4
# Kick on 1 and 3
for bar in range(2, 5):
    start = bar * 1.5
    kick1 = pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    kick2 = pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    drums.notes.extend([kick1, kick2])
# Snare on 2 and 4
for bar in range(2, 5):
    start = bar * 1.5
    snare1 = pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 0.875)
    snare2 = pretty_midi.Note(velocity=100, pitch=38, start=start + 1.875, end=start + 2.0)
    drums.notes.extend([snare1, snare2])
# Hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    for i in range(8):
        hihat = pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.1875, end=start + (i + 1) * 0.1875)
        drums.notes.append(hihat)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
