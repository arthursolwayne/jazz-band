
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line in Dm, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D - C - Eb - F
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=40, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    # Bar 3: G - F - A - Bb
    pretty_midi.Note(velocity=100, pitch=43, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=45, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=46, start=4.125, end=4.5),
    # Bar 4: D - C - Eb - F (resolve)
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=37, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=40, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),
]
# Bar 3: G7 (G, B, D, F)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.375),
])
# Bar 4: Cm7 (C, Eb, G, Bb)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=59, start=4.5, end=4.875),
])
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# Motif: D - Eb - F - E (half note, quarter note, eighth note, eighth note)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=50, start=1.5, end=3.0),
    pretty_midi.Note(velocity=110, pitch=51, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=52, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=51, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=52, start=4.5, end=6.0),
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
