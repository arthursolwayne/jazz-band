
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=0.375, end=0.75),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.75),    # Hihat on 1 & 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),  # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=1.125, end=1.5),   # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)

# Marcus: Walking bass line in D (D F# A C)
# Bar 2: D (1), F# (2), A (3), C (4)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625), # A
    pretty_midi.Note(velocity=90, pitch=64, start=2.625, end=3.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (D7 on 2, Bm7 on 4)
# D7 = D F# A C (root on 1), Bm7 = B D F# A (root on 2)
piano_notes = [
    # D7 on 2 (1.875 - 2.25)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=1.875, end=2.25),  # C

    # Bm7 on 4 (2.625 - 3.0)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=90, pitch=62, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=90, pitch=66, start=2.625, end=3.0),   # F#
    pretty_midi.Note(velocity=90, pitch=67, start=2.625, end=3.0),   # A
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Motif in D (D - F# - B - C) ascending, then repeat on next bar
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=1.625, end=1.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=2.125, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.375),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus: Walking bass line (D F# A C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.125, end=4.5),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (D7 on 2, Bm7 on 4)
piano_notes = [
    # D7 on 2 (3.375 - 3.75)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=3.375, end=3.75),  # C

    # Bm7 on 4 (4.125 - 4.5)
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=90, pitch=62, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.125, end=4.5),   # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.125, end=4.5),   # A
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Repeat motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.125, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=3.625, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=3.875),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus: Walking bass line (D F# A C)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25), # F#
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.625), # A
    pretty_midi.Note(velocity=90, pitch=64, start=5.625, end=6.0),  # C
]
for note in bass_notes:
    bass.notes.append(note)

# Diane: 7th chords on 2 and 4 (D7 on 2, Bm7 on 4)
piano_notes = [
    # D7 on 2 (4.875 - 5.25)
    pretty_midi.Note(velocity=90, pitch=62, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=90, pitch=66, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=64, start=4.875, end=5.25),  # C

    # Bm7 on 4 (5.625 - 6.0)
    pretty_midi.Note(velocity=90, pitch=69, start=5.625, end=6.0),   # B
    pretty_midi.Note(velocity=90, pitch=62, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=90, pitch=66, start=5.625, end=6.0),   # F#
    pretty_midi.Note(velocity=90, pitch=67, start=5.625, end=6.0),   # A
]
for note in piano_notes:
    piano.notes.append(note)

# Dante: Repeat motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=4.625, end=4.75),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.0),   # C
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),  # D
    pretty_midi.Note(velocity=100, pitch=66, start=5.125, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.375),  # B
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.5),   # C
]
for note in sax_notes:
    sax.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.25),    # Hihat on 1 & 2
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),   # Hihat on 4
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),   # Snare on 4
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
