
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet starts (1.5 - 3.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=1.5, end=1.875),  # D (root)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),  # B (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=3.0),   # D (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # F#
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.0),  # C
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: First motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),   # F#
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),  # D (root)
    pretty_midi.Note(velocity=100, pitch=41, start=3.375, end=3.75),  # B (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=3.75, end=4.125),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=4.125, end=4.5),   # D (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: C7 (C E G B)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.5),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.5),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),   # E
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=43, start=4.5, end=4.875),  # D (root)
    pretty_midi.Note(velocity=100, pitch=41, start=4.875, end=5.25),  # B (fifth)
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625),  # Bb (chromatic approach)
    pretty_midi.Note(velocity=100, pitch=43, start=5.625, end=6.0),   # D (root)
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=5.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=5.0),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=5.0),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: Finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),   # E
]
for note in sax_notes:
    sax.notes.append(note)

# Add the drum fill for the last bar (4.5 - 6.0s)
# Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.125),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=100, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=100, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=100, pitch=42, start=7.125, end=7.5),
]
for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
