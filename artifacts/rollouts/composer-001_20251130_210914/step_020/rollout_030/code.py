
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

# Bass line: Walking line, chromatic approaches, no repeated notes
bass_notes = [
    # Bar 2: D - C# - B - C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=61, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=59, start=2.0, end=2.25),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.5),
    # Bar 3: D - C# - B - A
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.75),
    pretty_midi.Note(velocity=100, pitch=61, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=57, start=3.25, end=3.5),
    # Bar 4: D - C# - B - A
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),
    pretty_midi.Note(velocity=100, pitch=61, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=59, start=4.0, end=4.25),
    pretty_midi.Note(velocity=100, pitch=57, start=4.25, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=74, start=2.0, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=2.0, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=2.0, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=2.0, end=2.25),  # C#
    # Bar 3: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=3.0, end=3.25),  # C#
    # Bar 4: D7 on 2 and 4
    pretty_midi.Note(velocity=100, pitch=74, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=100, pitch=76, start=4.0, end=4.25),  # F#
    pretty_midi.Note(velocity=100, pitch=79, start=4.0, end=4.25),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=4.0, end=4.25),  # C#
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start motif
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.6875),  # D
    pretty_midi.Note(velocity=110, pitch=76, start=1.6875, end=1.875), # F#
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.0),   # A
    # Bar 3: Leave it hanging
    # No notes in bar 3
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=76, start=3.5, end=3.6875),  # F#
    pretty_midi.Note(velocity=110, pitch=74, start=3.6875, end=3.875), # A
    pretty_midi.Note(velocity=110, pitch=72, start=3.875, end=4.0),   # D
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.5, end=3.875),  # Kick on 1
    pretty_midi.Note(velocity=110, pitch=38, start=4.0, end=4.125),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
