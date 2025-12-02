
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone: Motif - Fm7 (F, Ab, Bb, D) -> F, Ab, Bb, D
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm - F, Gb, Ab, Bb, Bb, C, D, Eb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.625, end=1.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=1.75, end=1.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=2.0, end=2.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=2.125, end=2.25),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=80, pitch=66, start=2.375, end=2.5),  # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 2 (1.5-3.0s): 2nd beat (2.0-2.5s) - Fm7 (F, Ab, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=2.0, end=2.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=2.0, end=2.5),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: Repeat motif, but with a chromatic approach to Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=70, start=3.5, end=3.75),  # Bb (chromatic from A)
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.0, end=4.25),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm - F, Gb, Ab, Bb, Bb, C, D, Eb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.125),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=3.125, end=3.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=3.25, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.5, end=3.625),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=3.625, end=3.75),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=80, pitch=66, start=3.875, end=4.0),  # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 3 (3.0-4.5s): 2nd beat (3.5-4.0s) - Fm7 (F, Ab, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=3.5, end=4.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=3.5, end=4.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=3.5, end=4.0),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: Finish the motif, resolve to Bb
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # D
]

for note in sax_notes:
    sax.notes.append(note)

# Bass: Walking line in Fm - F, Gb, Ab, Bb, Bb, C, D, Eb
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=70, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=4.625, end=4.75),  # Gb
    pretty_midi.Note(velocity=80, pitch=67, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=69, start=4.875, end=5.0),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=5.0, end=5.125),  # Bb
    pretty_midi.Note(velocity=80, pitch=68, start=5.125, end=5.25),  # C
    pretty_midi.Note(velocity=80, pitch=64, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=80, pitch=66, start=5.375, end=5.5),  # Eb
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: 7th chords on 2 and 4
# Bar 4 (4.5-6.0s): 2nd beat (5.0-5.5s) - Fm7 (F, Ab, Bb, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=70, start=5.0, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.0, end=5.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=69, start=5.0, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=64, start=5.0, end=5.5),  # D
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
    pretty_midi.Note(velocity=80, pitch=42, start=6.75, end=7.125),
    pretty_midi.Note(velocity=80, pitch=42, start=7.125, end=7.5),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
