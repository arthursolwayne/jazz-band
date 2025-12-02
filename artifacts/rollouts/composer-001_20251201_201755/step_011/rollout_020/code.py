
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Piano: Cmaj7 (C E G B) in open voicing
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=3.0),  # E
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=3.0),  # B
]
for note in piano_notes:
    piano.notes.append(note)

# Bass: D (root) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25), # C#
    pretty_midi.Note(velocity=100, pitch=50, start=2.25, end=2.625), # D
    pretty_midi.Note(velocity=100, pitch=51, start=2.625, end=3.0),  # D#
]
for note in bass_notes:
    bass.notes.append(note)

# Sax: Motif (G A Bb B)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),  # B
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Piano: Bm7 (B D F# A)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),  # F#
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),  # A
]
for note in piano_notes:
    piano.notes.append(note)

# Bass: B (root) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=59, start=3.0, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=58, start=3.375, end=3.75), # A
    pretty_midi.Note(velocity=100, pitch=59, start=3.75, end=4.125), # B
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Sax: Repeat motif (G A Bb B)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),  # B
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Piano: G7 (G B D F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # B
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=6.0),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),  # F
]
for note in piano_notes:
    piano.notes.append(note)

# Bass: G (root) with chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),  # G#
]
for note in bass_notes:
    bass.notes.append(note)

# Sax: Repeat motif (G A Bb B)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=68, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),  # B
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_start = 4.5
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start, end=bar_start + 1.5),  # Hihat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.375, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 0.75, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 1.5, end=bar_start + 1.875),  # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
