
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
    # Hihat on every eighth note
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Fm (F, Ab, D, C), chromatic approaches
bass_notes = [
    # Bar 2: F (root), Ab (b9), D (5th), C (b7)
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=47, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),  # C2

    # Bar 3: Ab (b9), G (b7), D (5th), C (b7)
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Ab2
    pretty_midi.Note(velocity=90, pitch=43, start=3.375, end=3.75),  # C2
    pretty_midi.Note(velocity=90, pitch=47, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),  # C2

    # Bar 4: F (root), Eb (b7), D (5th), C (b7)
    pretty_midi.Note(velocity=90, pitch=44, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # Eb2
    pretty_midi.Note(velocity=90, pitch=47, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),  # C2
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=44, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=43, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=47, start=1.5, end=1.875),

    # Bar 3: Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=44, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),

    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=43, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=41, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=46, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=40, start=4.5, end=4.875),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: First statement of motif (Ab - F - Eb)
    pretty_midi.Note(velocity=110, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=44, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=41, start=2.25, end=2.625),

    # Bar 3: Rest, leave it hanging

    # Bar 4: Return and finish the motif (Ab - F - Eb - D)
    pretty_midi.Note(velocity=110, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=44, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=41, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=47, start=5.625, end=6.0),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Bar 2-4
# Bar 2: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    start = bar * 1.5
    # Kick
    pretty_midi.Note(velocity=100, pitch=36, start=start + 0.0, end=start + 0.375)
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5)
    # Snare
    pretty_midi.Note(velocity=110, pitch=38, start=start + 0.75, end=start + 0.875)
    pretty_midi.Note(velocity=110, pitch=38, start=start + 1.875, end=start + 2.0)
    # Hihat
    for i in range(4):
        pretty_midi.Note(velocity=90, pitch=42, start=start + i * 0.375, end=start + i * 0.375 + 0.375)

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
