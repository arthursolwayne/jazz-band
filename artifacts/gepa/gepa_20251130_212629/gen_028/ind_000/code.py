
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

# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=95, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),
]

drums.notes.extend(drum_notes)

# Bar 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus - walking line, chromatic approaches
# D D# C# D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=62, start=1.5, end=1.875),     # D
    pretty_midi.Note(velocity=80, pitch=63, start=1.875, end=2.25),    # D#
    pretty_midi.Note(velocity=80, pitch=61, start=2.25, end=2.625),    # C#
    pretty_midi.Note(velocity=80, pitch=62, start=2.625, end=3.0),     # D
    pretty_midi.Note(velocity=80, pitch=62, start=3.0, end=3.375),     # D
    pretty_midi.Note(velocity=80, pitch=63, start=3.375, end=3.75),    # D#
    pretty_midi.Note(velocity=80, pitch=61, start=3.75, end=4.125),    # C#
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),     # D
    pretty_midi.Note(velocity=80, pitch=62, start=4.5, end=4.875),     # D
    pretty_midi.Note(velocity=80, pitch=63, start=4.875, end=5.25),    # D#
    pretty_midi.Note(velocity=80, pitch=61, start=5.25, end=5.625),    # C#
    pretty_midi.Note(velocity=80, pitch=62, start=5.625, end=6.0),     # D
]
bass.notes.extend(bass_notes)

# Piano: Diane - 7th chords, comp on 2 and 4
# D7 - G7 - C7 - F7
piano_notes = [
    # D7 (Bar 2)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),     # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),     # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),     # B
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),     # F# (7th)

    # G7 (Bar 3)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),     # G
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),     # B
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375),     # D
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),     # F# (7th)

    # C7 (Bar 4)
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),     # C
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.875),     # E
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),     # G
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),     # B (7th)
]
piano.notes.extend(piano_notes)

# Drums: Bar 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.75, end=start + 1.125)
    # Snare
    pretty_midi.Note(velocity=90, pitch=38, start=start + 0.375, end=start + 0.75)
    pretty_midi.Note(velocity=90, pitch=38, start=start + 1.125, end=start + 1.5)
    # Hihat
    pretty_midi.Note(velocity=95, pitch=42, start=start, end=start + 1.5)

# Sax: Dante - motif, start it, leave it hanging, come back and finish it
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=66, start=1.5, end=1.75),      # E (D7 chord)
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=2.0),      # F (chromatic)
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),      # D (back down)
    pretty_midi.Note(velocity=110, pitch=66, start=2.25, end=2.5),      # E (rest)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.25),      # F (return)
    pretty_midi.Note(velocity=110, pitch=65, start=3.25, end=3.5),      # D
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),      # C#
    pretty_midi.Note(velocity=110, pitch=66, start=3.75, end=4.0),      # E
    pretty_midi.Note(velocity=110, pitch=67, start=4.0, end=4.25),      # F
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),      # D
    pretty_midi.Note(velocity=110, pitch=64, start=4.5, end=4.75),      # C#
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),      # E
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),      # F
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),      # D
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),      # C#
    pretty_midi.Note(velocity=110, pitch=66, start=5.75, end=6.0),      # E
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
