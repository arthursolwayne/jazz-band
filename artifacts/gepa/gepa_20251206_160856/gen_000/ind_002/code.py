
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]

drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (38)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (43)
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.125),
    pretty_midi.Note(velocity=100, pitch=43, start=2.125, end=2.5),
    # Bar 3: G2 (43)
    pretty_midi.Note(velocity=100, pitch=43, start=2.5, end=2.875),
    # Chromatic approach to A2 (45)
    pretty_midi.Note(velocity=80, pitch=44, start=2.875, end=3.125),
    pretty_midi.Note(velocity=100, pitch=45, start=3.125, end=3.5),
    # Bar 4: A2 (45)
    pretty_midi.Note(velocity=100, pitch=45, start=3.5, end=3.875),
    # Chromatic approach to D3 (50)
    pretty_midi.Note(velocity=80, pitch=49, start=3.875, end=4.125),
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),
]

bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dmaj7 (D, F#, A, C#)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=61, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=55, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=64, start=2.5, end=2.875),
    # Bar 4: Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=57, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=60, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=64, start=3.5, end=3.875),
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.875),
]

piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# D (62), F# (66), G (67), D (62)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.625),
    pretty_midi.Note(velocity=110, pitch=66, start=1.625, end=1.75),
    pretty_midi.Note(velocity=110, pitch=67, start=1.75, end=1.875),
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.625),
    pretty_midi.Note(velocity=110, pitch=66, start=2.625, end=2.75),
    pretty_midi.Note(velocity=110, pitch=67, start=2.75, end=2.875),
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.625),
    pretty_midi.Note(velocity=110, pitch=66, start=3.625, end=3.75),
    pretty_midi.Note(velocity=110, pitch=67, start=3.75, end=3.875),
]

sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
