
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: D (MIDI 38) with chromatic approach from C# (MIDI 37)
    pretty_midi.Note(velocity=80, pitch=37, start=1.5, end=1.625),
    pretty_midi.Note(velocity=90, pitch=38, start=1.625, end=1.75),
    # Bar 2: G (MIDI 43) with chromatic approach from F# (MIDI 42)
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),
    pretty_midi.Note(velocity=90, pitch=43, start=1.875, end=2.0),
    # Bar 3: A (MIDI 40) with chromatic approach from G# (MIDI 39)
    pretty_midi.Note(velocity=80, pitch=39, start=2.0, end=2.125),
    pretty_midi.Note(velocity=90, pitch=40, start=2.125, end=2.25),
    # Bar 3: D (MIDI 38) with chromatic approach from C# (MIDI 37)
    pretty_midi.Note(velocity=80, pitch=37, start=2.25, end=2.375),
    pretty_midi.Note(velocity=90, pitch=38, start=2.375, end=2.5),
    # Bar 4: B (MIDI 42) with chromatic approach from A# (MIDI 41)
    pretty_midi.Note(velocity=80, pitch=41, start=2.5, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.75),
    # Bar 4: F (MIDI 45) with chromatic approach from E (MIDI 44)
    pretty_midi.Note(velocity=80, pitch=44, start=2.75, end=2.875),
    pretty_midi.Note(velocity=90, pitch=45, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Dmaj7 (D, F#, A, C#)
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=2.0),  # D
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=2.0),  # F#
    pretty_midi.Note(velocity=80, pitch=57, start=1.5, end=2.0),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=2.0),  # C#
    # Bar 3: Amaj7 (A, C#, E, G)
    pretty_midi.Note(velocity=80, pitch=57, start=2.0, end=2.5),  # A
    pretty_midi.Note(velocity=80, pitch=60, start=2.0, end=2.5),  # C#
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.5),  # E
    pretty_midi.Note(velocity=80, pitch=67, start=2.0, end=2.5),  # G
    # Bar 4: Bm7b5 (B, D, F#, A)
    pretty_midi.Note(velocity=80, pitch=59, start=2.5, end=3.0),  # B
    pretty_midi.Note(velocity=80, pitch=62, start=2.5, end=3.0),  # D
    pretty_midi.Note(velocity=80, pitch=66, start=2.5, end=3.0),  # F#
    pretty_midi.Note(velocity=80, pitch=69, start=2.5, end=3.0),  # A
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2: Motif start (D, F#, G, A)
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F#
    # Bar 3: Leave it hanging
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # G
    # Bar 4: Return and finish (A, G, F#, D)
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # A
    pretty_midi.Note(velocity=100, pitch=66, start=2.75, end=3.0),  # G
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25),  # F#
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
]
sax.notes.extend(sax_notes)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save MIDI file
# midi.write disabled
