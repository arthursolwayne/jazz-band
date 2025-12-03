
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
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),    # Hihat on every 8th
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
])

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: F2 (D2) on 1, Bb2 (F2) on 2, Ab2 (G2) on 3, Eb2 (D2) on 4
bass.notes.extend([
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # F2 on 1
    pretty_midi.Note(velocity=90, pitch=40, start=1.875, end=2.25), # Bb2 on 2
    pretty_midi.Note(velocity=90, pitch=39, start=2.25, end=2.625), # Ab2 on 3
    pretty_midi.Note(velocity=90, pitch=38, start=2.625, end=3.0),  # F2 on 4
])

# Piano: Fm7 (F, Ab, Bb, Db) on bar 2 (comp on 2 and 4)
piano.notes.extend([
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.875),  # Db
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.625), # Ab
    pretty_midi.Note(velocity=90, pitch=52, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=90, pitch=48, start=2.25, end=2.625), # Db
])

# Sax: Motif - F Ab Bb (1.5 - 2.0s), leave it hanging (2.0 - 2.625s), return and finish (2.625 - 3.0s)
sax.notes.extend([
    pretty_midi.Note(velocity=110, pitch=64, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25), # Ab
    pretty_midi.Note(velocity=110, pitch=63, start=2.25, end=2.625), # Bb
    pretty_midi.Note(velocity=110, pitch=64, start=2.625, end=3.0),  # F
])

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Ab2 (G2) on 1, Eb2 (D2) on 2, F2 (D2) on 3, Bb2 (F2) on 4
bass.notes.extend([
    pretty_midi.Note(velocity=90, pitch=39, start=3.0, end=3.375),  # Ab2 on 1
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75), # Eb2 on 2
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # F2 on 3
    pretty_midi.Note(velocity=90, pitch=40, start=4.125, end=4.5),  # Bb2 on 4
])

# Piano: Ab7 (Ab, C, Db, F) on bar 3 (comp on 2 and 4)
piano.notes.extend([
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=3.0, end=3.375),  # Db
    pretty_midi.Note(velocity=90, pitch=53, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.125), # Ab
    pretty_midi.Note(velocity=90, pitch=55, start=3.75, end=4.125), # C
    pretty_midi.Note(velocity=90, pitch=48, start=3.75, end=4.125), # Db
    pretty_midi.Note(velocity=90, pitch=53, start=3.75, end=4.125), # F
])

# Sax: Motif variation - Ab C Db (3.0 - 3.5s), leave it hanging (3.5 - 4.125s), return and finish (4.125 - 4.5s)
sax.notes.extend([
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.125), # Db
    pretty_midi.Note(velocity=110, pitch=62, start=4.125, end=4.5),  # Ab
])

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Bb2 (F2) on 1, F2 (D2) on 2, Ab2 (G2) on 3, Eb2 (D2) on 4
bass.notes.extend([
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),  # Bb2 on 1
    pretty_midi.Note(velocity=90, pitch=38, start=4.875, end=5.25), # F2 on 2
    pretty_midi.Note(velocity=90, pitch=39, start=5.25, end=5.625), # Ab2 on 3
    pretty_midi.Note(velocity=90, pitch=38, start=5.625, end=6.0),  # Eb2 on 4
])

# Piano: Bb7 (Bb, D, Eb, F) on bar 4 (comp on 2 and 4)
piano.notes.extend([
    pretty_midi.Note(velocity=90, pitch=52, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=52, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=90, pitch=57, start=5.25, end=5.625), # D
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=90, pitch=53, start=5.25, end=5.625), # F
])

# Sax: Motif resolution - Bb D Eb (4.5 - 5.0s), leave it hanging (5.0 - 5.625s), return and finish (5.625 - 6.0s)
sax.notes.extend([
    pretty_midi.Note(velocity=110, pitch=63, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.25), # D
    pretty_midi.Note(velocity=110, pitch=61, start=5.25, end=5.625), # Eb
    pretty_midi.Note(velocity=110, pitch=63, start=5.625, end=6.0),  # Bb
])

# Drums: kick on 1, snare on 2, kick on 3, snare on 4 (Bar 2)
drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),  # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # Snare on 2
    pretty_midi.Note(velocity=100, pitch=36, start=4.875, end=5.25), # Kick on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),  # Snare on 4
])

# Hihat on every eighth
for i in range(1, 5):
    start = 1.5 + (i - 1) * 0.375
    end = 1.5 + i * 0.375
    if i % 2 == 1:
        end = 1.5 + i * 0.375
    else:
        end = 1.5 + i * 0.375
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(dr)

# Add hihat in bar 3
for i in range(1, 5):
    start = 3.0 + (i - 1) * 0.375
    end = 3.0 + i * 0.375
    if i % 2 == 1:
        end = 3.0 + i * 0.375
    else:
        end = 3.0 + i * 0.375
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(dr)

# Add hihat in bar 4
for i in range(1, 5):
    start = 4.5 + (i - 1) * 0.375
    end = 4.5 + i * 0.375
    if i % 2 == 1:
        end = 4.5 + i * 0.375
    else:
        end = 4.5 + i * 0.375
    dr = pretty_midi.Note(velocity=100, pitch=42, start=start, end=end)
    drums.notes.append(dr)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
