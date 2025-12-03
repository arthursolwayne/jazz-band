
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): D2-G2, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Bar 2: chromatic approach to G2 (F#2)
    pretty_midi.Note(velocity=90, pitch=37, start=1.875, end=2.25),
    # Bar 2: G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    # Bar 2: chromatic approach to D2 (C#2)
    pretty_midi.Note(velocity=90, pitch=35, start=2.625, end=3.0),
    # Bar 3: D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    # Bar 3: chromatic approach to G2 (F#2)
    pretty_midi.Note(velocity=90, pitch=37, start=3.375, end=3.75),
    # Bar 3: G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=3.75, end=4.125),
    # Bar 3: chromatic approach to D2 (C#2)
    pretty_midi.Note(velocity=90, pitch=35, start=4.125, end=4.5),
    # Bar 4: D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Bar 4: chromatic approach to G2 (F#2)
    pretty_midi.Note(velocity=90, pitch=37, start=4.875, end=5.25),
    # Bar 4: G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=5.25, end=5.625),
    # Bar 4: chromatic approach to D2 (C#2)
    pretty_midi.Note(velocity=90, pitch=35, start=5.625, end=6.0),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7sus4 (D, G, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=3.0),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),
    # Bar 4: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=6.0),
]

for note in piano_notes:
    piano.notes.append(note)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(2, 5):
    bar_start = (bar - 1) * 1.5
    # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start, end=bar_start + 0.375)
    # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 0.75, end=bar_start + 1.125)
    # Kick on 3
    pretty_midi.Note(velocity=100, pitch=36, start=bar_start + 1.5, end=bar_start + 1.875)
    # Snare on 4
    pretty_midi.Note(velocity=100, pitch=38, start=bar_start + 2.25, end=bar_start + 2.625)
    # Hihat on every eighth
    for i in range(0, 4):
        pretty_midi.Note(velocity=80, pitch=42, start=bar_start + i * 0.375, end=bar_start + i * 0.375 + 0.1875)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D (62), F# (67), A (69) — short, ascending, then repeat on the third bar to resolve
sax_notes = [
    # Bar 2: D, F#, A
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.0625),
    # Bar 3: D, F#, A
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=110, pitch=67, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=110, pitch=69, start=3.375, end=3.5625),
    # Bar 4: D, F#, A
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=110, pitch=67, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=110, pitch=69, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=110, pitch=67, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=110, pitch=62, start=5.4375, end=5.625),
]

for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
