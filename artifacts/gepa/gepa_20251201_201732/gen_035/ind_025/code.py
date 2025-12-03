
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
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

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) to F#2 (5th)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.25),
    # Bar 3: G2 (root) to Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    # Bar 4: C2 (root) to D2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=40, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    # Bar 4: A2 (root) to Bb2 (chromatic approach)
    pretty_midi.Note(velocity=90, pitch=45, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]

for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=71, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.625),
    # Bar 4: Cm7 (C, Eb, G, Bb)
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=63, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.375),
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125),
]

for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it. No scale runs
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),
]

for note in sax_notes:
    sax.notes.append(note)

# Drums: Fill the bar for bars 2-4
drum_notes = [
    # Bar 2: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Bar 2: Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    # Bar 2: Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 3: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Bar 3: Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    # Bar 3: Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    # Bar 4: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Bar 4: Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Bar 4: Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]

for note in drum_notes:
    drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
