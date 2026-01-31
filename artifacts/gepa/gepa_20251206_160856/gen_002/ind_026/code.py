
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),
]

for note in drum_notes:
    drums.notes.append(note)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line (Marcus): Walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F#2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),  # A2
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),  # C3
    pretty_midi.Note(velocity=90, pitch=47, start=3.0, end=3.375),  # D3
    pretty_midi.Note(velocity=90, pitch=50, start=3.375, end=3.75),  # F#3
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.125),  # A3
    pretty_midi.Note(velocity=90, pitch=55, start=4.125, end=4.5),  # C4
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=90, pitch=60, start=4.875, end=5.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.625),  # A4
    pretty_midi.Note(velocity=90, pitch=65, start=5.625, end=6.0),  # C5
]

for note in bass_notes:
    bass.notes.append(note)

# Piano (Diane): Open voicings, different chord each bar, resolve on the last
# Bar 2: D7 (D F# A C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=2.25),
]

# Bar 3: Gm7 (G Bb D F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=76, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=78, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=81, start=2.25, end=3.0),
])

# Bar 4: Cmaj7 (C E G B)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),
])

# Bar 4 resolve: Bm7 (B D F# A)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=73, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=76, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=78, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=81, start=3.75, end=4.5),
])

for note in piano_notes:
    piano.notes.append(note)

# Sax (Dante): One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D4 (62) -> F#4 (66) -> A4 (69) -> D5 (72) -> D4 (62)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums (Little Ray): Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Bar 2 (1.5 - 3.0s)
for i in range(2):
    start = 1.5 + i * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),

# Bar 3 (3.0 - 4.5s)
for i in range(2):
    start = 3.0 + i * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),

# Bar 4 (4.5 - 6.0s)
for i in range(2):
    start = 4.5 + i * 1.5
    pretty_midi.Note(velocity=100, pitch=36, start=start, end=start + 0.375),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 0.75, end=start + 1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=start, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=36, start=start + 1.125, end=start + 1.5),
    pretty_midi.Note(velocity=100, pitch=38, start=start + 1.5, end=start + 1.875),

midi.instruments.extend([sax, bass, piano, drums])
