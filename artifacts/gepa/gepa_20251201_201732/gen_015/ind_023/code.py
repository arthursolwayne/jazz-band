
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
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=100, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (MIDI 38)
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to G2 (MIDI 43)
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.375),
    # Bar 3: G2 (MIDI 43)
    pretty_midi.Note(velocity=100, pitch=43, start=2.375, end=2.75),
    # Chromatic approach to C3 (MIDI 48)
    pretty_midi.Note(velocity=90, pitch=47, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=48, start=3.0, end=3.375),
    # Bar 4: C3 (MIDI 48)
    pretty_midi.Note(velocity=100, pitch=48, start=3.375, end=3.75),
    # Chromatic approach to F3 (MIDI 53)
    pretty_midi.Note(velocity=90, pitch=52, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=53, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dm7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=71, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=74, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=76, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=77, start=2.375, end=2.75),
    # Bar 4: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Start the motif
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.0),
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=110, pitch=68, start=2.0, end=2.375),
    # Bar 4: Come back and finish it
    pretty_midi.Note(velocity=110, pitch=65, start=3.75, end=4.0),
    pretty_midi.Note(velocity=110, pitch=68, start=4.0, end=4.375),
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=2.1875, end=2.375),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=38, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=2.375, end=2.75),
    pretty_midi.Note(velocity=100, pitch=42, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=3.1875, end=3.375),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.0),
    pretty_midi.Note(velocity=100, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.1875, end=4.375),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
