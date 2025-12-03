
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking line in D, roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D2 (root) with chromatic approach from C#2
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=37, start=1.125, end=1.5),  # chromatic
    # Bar 3: A2 (fifth) with chromatic approach from Bb2
    pretty_midi.Note(velocity=100, pitch=43, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),  # chromatic
    # Bar 4: D2 (root) with chromatic approach from C#2
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=37, start=2.625, end=3.0),  # chromatic
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.25),
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=2.25),
    # Bar 3: G7 (G, B, D, F)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=3.0),
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=3.0),
    # Bar 4: Cmaj7 (C, E, G, B)
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.75),
]
piano.notes.extend(piano_notes)

# Sax: short motif, start it, leave it hanging, come back and finish it
sax_notes = [
    # Bar 2: Start motif on D4 (62) with a grace note on C#4 (61)
    pretty_midi.Note(velocity=110, pitch=61, start=1.5, end=1.55),
    pretty_midi.Note(velocity=110, pitch=62, start=1.55, end=1.75),
    # Bar 3: Continue motif, leave it hanging
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),
    # Bar 4: Return and finish the motif on D4 (62)
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),
]
sax.notes.extend(sax_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
