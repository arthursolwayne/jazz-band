
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
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Bar 2: F#2 (fifth)
    pretty_midi.Note(velocity=100, pitch=41, start=1.875, end=2.25),
    # Bar 2: chromatic approach to G2
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    # Bar 3: G2 (fifth)
    pretty_midi.Note(velocity=100, pitch=43, start=2.625, end=2.875),
    # Bar 3: B2 (seventh)
    pretty_midi.Note(velocity=100, pitch=45, start=2.875, end=3.25),
    # Bar 3: chromatic approach to A2
    pretty_midi.Note(velocity=100, pitch=44, start=3.25, end=3.625),
    # Bar 4: A2 (root)
    pretty_midi.Note(velocity=100, pitch=44, start=3.625, end=4.0),
    # Bar 4: C#3 (fifth)
    pretty_midi.Note(velocity=100, pitch=47, start=4.0, end=4.375),
    # Bar 4: chromatic approach to D3
    pretty_midi.Note(velocity=100, pitch=46, start=4.375, end=4.75),
    # Bar 4: D3 (root)
    pretty_midi.Note(velocity=100, pitch=47, start=4.75, end=5.125)
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: D7sus4 (D, G, A, C#)
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=55, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=2.25),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=58, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),
    # Bar 4: A7 (A, C#, E, G)
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.75),
    # Bar 4: Resolving to Dmaj7
    pretty_midi.Note(velocity=100, pitch=50, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=53, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=57, start=3.75, end=4.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.5)
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif begins
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875),
    # Bar 4: Return and finish the motif
    pretty_midi.Note(velocity=100, pitch=65, start=4.375, end=4.75),
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.125)
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Bar 2: Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=38, start=2.875, end=3.0),
    # Bar 2: Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    # Bar 3: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=3.875),
    # Bar 3: Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=38, start=3.875, end=4.0),
    # Bar 3: Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=2.875),
    pretty_midi.Note(velocity=100, pitch=42, start=2.875, end=3.25),
    pretty_midi.Note(velocity=100, pitch=42, start=3.25, end=3.625),
    pretty_midi.Note(velocity=100, pitch=42, start=3.625, end=4.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.375),
    pretty_midi.Note(velocity=100, pitch=42, start=4.375, end=4.75),
    # Bar 4: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=36, start=4.625, end=4.875),
    # Bar 4: Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Bar 4: Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.625, end=3.875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.875, end=4.25),
    pretty_midi.Note(velocity=100, pitch=42, start=4.25, end=4.625),
    pretty_midi.Note(velocity=100, pitch=42, start=4.625, end=5.0),
    pretty_midi.Note(velocity=100, pitch=42, start=5.0, end=5.375),
    pretty_midi.Note(velocity=100, pitch=42, start=5.375, end=5.75)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
