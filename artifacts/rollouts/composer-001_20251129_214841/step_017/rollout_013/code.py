
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Everyone in (1.5 - 3.0s)
# Sax motif: C - E - G - Bb (C7 arpeggio, one note per beat)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in C (C - B - Bb - A - G - F - E - D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=63, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=62, start=4.125, end=4.5),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (C7 on 2, F7 on 4)
piano_notes = [
    # C7 (C - E - Bb - G) on beat 2 (1.875s)
    pretty_midi.Note(velocity=90, pitch=60, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),
    # F7 (F - A - E - C) on beat 4 (2.625s)
    pretty_midi.Note(velocity=90, pitch=65, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=2.625, end=3.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Everyone in (3.0 - 4.5s)
# Sax: Repeat the motif but transpose up a half step (Db - F - Ab - B)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=61, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=68, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Chromatic walking line (C - C# - D - D# - E - F - F# - G)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=61, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=63, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=65, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=67, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (F7 on 2, Bb7 on 4)
piano_notes = [
    # F7 (F - A - E - C) on beat 2 (3.375s)
    pretty_midi.Note(velocity=90, pitch=65, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=60, start=3.375, end=3.75),
    # Bb7 (Bb - D - Ab - F) on beat 4 (4.125s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=65, start=4.125, end=4.5),
]
for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Everyone in (4.5 - 6.0s)
# Sax: Repeat motif but transpose up a half step (Eb - G - Bb - C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=63, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

# Bass: Chromatic walking line (G - G# - A - A# - B - C - C# - D)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=68, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=70, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=71, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=72, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=73, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=74, start=7.125, end=7.5),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4 (Bb7 on 2, Eb7 on 4)
piano_notes = [
    # Bb7 (Bb - D - Ab - F) on beat 2 (4.875s)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=65, start=4.875, end=5.25),
    # Eb7 (Eb - G - Db - Bb) on beat 4 (5.625s)
    pretty_midi.Note(velocity=90, pitch=63, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=61, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),
]
for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2: 1.5 - 3.0s
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]

# Bar 3: 3.0 - 4.5s
drum_notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
])

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
