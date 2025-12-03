
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
    # Hi-hat on every eighth
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

# Bass: Walking line in D (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (38), F# (41), G (43), A (45)
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=45, start=2.625, end=3.0),
    # Bar 3: B (46), D (38), F# (41), G (43)
    pretty_midi.Note(velocity=90, pitch=46, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=41, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=43, start=4.125, end=4.5),
    # Bar 4: A (45), C# (44), D (38), F# (41)
    pretty_midi.Note(velocity=90, pitch=45, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),
]
for note in bass_notes:
    bass.notes.append(note)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),
]
for note in piano_notes:
    piano.notes.append(note)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start of motif
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # E (Dorian)
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.625),  # E (leave it hanging)
    # Bar 3: Continue motif
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=3.375, end=3.75),  # E
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.125),  # F#
    # Bar 4: Finish motif
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),  # G
]
for note in sax_notes:
    sax.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
