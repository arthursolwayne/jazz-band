
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: Marcus (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.25), # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),  # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),  # F (root)
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.75), # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),  # Bb (chromatic)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),  # F (root)
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.25), # Ab (chromatic)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625), # C (fifth)
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),  # Bb (chromatic)
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Diane (Open voicings, different chord each bar, resolve on the last)
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),  # Ab
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),  # Eb

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.25, end=2.625),  # Ab

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Eb
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # Bb

    # Resolutions on 2 and 4
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),  # C
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: Dante (Melody - one short motif, make it sing)
# Motif: F - Bb - C - Eb
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=2.625, end=3.0),   # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.375),  # F (return)
    pretty_midi.Note(velocity=110, pitch=62, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=110, pitch=65, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=62, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=110, pitch=67, start=5.625, end=6.0),   # Eb
]

for note in sax_notes:
    sax.notes.append(note)

# Drums for bars 2-4
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875)
    # Hihat on every eighth
    for i in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=start + i * 0.375, end=start + (i + 1) * 0.375)

drums.notes.extend([
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),
])

# Add hihat fills
for i in range(0, 6, 1.5):
    for j in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=i + j * 0.375, end=i + (j + 1) * 0.375)

for i in range(1.5, 6, 1.5):
    for j in range(4):
        pretty_midi.Note(velocity=100, pitch=42, start=i + j * 0.375, end=i + (j + 1) * 0.375)

midi.instruments.extend([sax, bass, piano, drums])

midi.writeFile("dante_intro.mid")
