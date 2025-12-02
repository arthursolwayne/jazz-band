
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

# Drums - Bar 1 (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full ensemble (1.5 - 3.0s)
# Sax: C (60) - E (64) - G (67) - B (71) - E (64)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=2.25, end=2.5),  # B
    pretty_midi.Note(velocity=110, pitch=64, start=2.5, end=2.75),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in C minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.5, end=2.75),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=60, start=1.75, end=2.0),  # C7 (C, E, B)
    pretty_midi.Note(velocity=95, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=71, start=1.75, end=2.0),
    pretty_midi.Note(velocity=95, pitch=60, start=2.5, end=2.75),  # C7 (C, E, B)
    pretty_midi.Note(velocity=95, pitch=64, start=2.5, end=2.75),
    pretty_midi.Note(velocity=95, pitch=71, start=2.5, end=2.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full ensemble (3.0 - 4.5s)
# Sax: Repeat the motif, but with a half-step lower
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=59, start=3.0, end=3.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=63, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=110, pitch=66, start=3.5, end=3.75),  # F
    pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.0),  # A
    pretty_midi.Note(velocity=110, pitch=63, start=4.0, end=4.25),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in C minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.0, end=4.25),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=59, start=3.25, end=3.5),  # Bb7 (Bb, D, F, A)
    pretty_midi.Note(velocity=95, pitch=63, start=3.25, end=3.5),
    pretty_midi.Note(velocity=95, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=95, pitch=70, start=3.25, end=3.5),
    pretty_midi.Note(velocity=95, pitch=59, start=4.0, end=4.25),  # Bb7 (Bb, D, F, A)
    pretty_midi.Note(velocity=95, pitch=63, start=4.0, end=4.25),
    pretty_midi.Note(velocity=95, pitch=67, start=4.0, end=4.25),
    pretty_midi.Note(velocity=95, pitch=70, start=4.0, end=4.25),
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full ensemble (4.5 - 6.0s)
# Sax: Bring the motif back up, resolve to C
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=110, pitch=64, start=4.75, end=5.0),  # E
    pretty_midi.Note(velocity=110, pitch=67, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=71, start=5.25, end=5.5),  # B
    pretty_midi.Note(velocity=110, pitch=64, start=5.5, end=5.75),  # E
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in C minor
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),  # C
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.5, end=5.75),  # G
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=60, start=4.75, end=5.0),  # C7 (C, E, B)
    pretty_midi.Note(velocity=95, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=95, pitch=71, start=4.75, end=5.0),
    pretty_midi.Note(velocity=95, pitch=60, start=5.5, end=5.75),  # C7 (C, E, B)
    pretty_midi.Note(velocity=95, pitch=64, start=5.5, end=5.75),
    pretty_midi.Note(velocity=95, pitch=71, start=5.5, end=5.75),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums - Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=3.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Drums - Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Drums - Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=6.0),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
