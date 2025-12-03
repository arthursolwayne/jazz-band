
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
    # Bar 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in Dm, roots and fifths with chromatic approaches
# Dm: D, F, A, C
# Bar 2 (1.5s - 3.0s): D - Eb - F - D
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=39, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=80, pitch=41, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=80, pitch=38, start=2.625, end=3.0), # D
    # Bar 3 (3.0s - 4.5s): F - G - A - F
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.375), # F
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # G
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125), # A
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5), # F
    # Bar 4 (4.5s - 6.0s): A - Bb - C - A
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.875), # A
    pretty_midi.Note(velocity=80, pitch=46, start=4.875, end=5.25), # Bb
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.625), # C
    pretty_midi.Note(velocity=80, pitch=45, start=5.625, end=6.0), # A
]
for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, one chord per bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=3.0), # D
    pretty_midi.Note(velocity=100, pitch=41, start=1.5, end=3.0), # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.5, end=3.0), # A
    pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=3.0), # C
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=4.5), # G
    pretty_midi.Note(velocity=100, pitch=46, start=3.0, end=4.5), # B
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=4.5), # D
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5), # F
    # Bar 4: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=48, start=4.5, end=6.0), # C
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0), # E
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0), # G
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=6.0), # B
]
for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): Short motif, sing it, leave it hanging
# Melody: D - Eb - F - D (Bar 2), then D - C - Bb - A (Bar 3), then D - C - Bb - A (Bar 4)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=38, start=1.5, end=1.875), # D
    pretty_midi.Note(velocity=110, pitch=39, start=1.875, end=2.25), # Eb
    pretty_midi.Note(velocity=110, pitch=41, start=2.25, end=2.625), # F
    pretty_midi.Note(velocity=110, pitch=38, start=2.625, end=3.0), # D

    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375), # D
    pretty_midi.Note(velocity=110, pitch=48, start=3.375, end=3.75), # C
    pretty_midi.Note(velocity=110, pitch=46, start=3.75, end=4.125), # Bb
    pretty_midi.Note(velocity=110, pitch=45, start=4.125, end=4.5), # A

    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875), # D
    pretty_midi.Note(velocity=110, pitch=48, start=4.875, end=5.25), # C
    pretty_midi.Note(velocity=110, pitch=46, start=5.25, end=5.625), # Bb
    pretty_midi.Note(velocity=110, pitch=45, start=5.625, end=6.0), # A
]
for note in sax_notes:
    sax.notes.append(note)

# Drums for Bars 2-4: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Hihat on every 8th
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start, end=bar_start + 0.375)
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.375, end=bar_start + 0.75)
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 0.75, end=bar_start + 1.125)
    pretty_midi.Note(velocity=80, pitch=42, start=bar_start + 1.125, end=bar_start + 1.5)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.125, end=bar_start + 1.5)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
])

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
