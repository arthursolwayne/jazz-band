
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
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in F (D2 - G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Bar 2: F (40), D (38) as chromatic approach
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=40, start=1.75, end=2.0),
    # Bar 3: C (43), B (42) as chromatic approach
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.25),
    pretty_midi.Note(velocity=90, pitch=43, start=2.25, end=2.5),
    # Bar 4: G (45), F# (44) as chromatic approach
    pretty_midi.Note(velocity=90, pitch=44, start=2.5, end=2.75),
    pretty_midi.Note(velocity=90, pitch=45, start=2.75, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E♭)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.75),  # A4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=1.75),  # C5
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # E♭4
]
# Bar 3: B♭7 (B♭, D, F, A♭)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=62, start=2.0, end=2.25),  # B♭4
    pretty_midi.Note(velocity=100, pitch=65, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=100, pitch=69, start=2.0, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.25),  # A♭4
])
# Bar 4: E7 (E, G#, B, D)
piano_notes.extend([
    pretty_midi.Note(velocity=100, pitch=69, start=2.5, end=2.75),  # E4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=2.75),  # G#4
    pretty_midi.Note(velocity=100, pitch=74, start=2.5, end=2.75),  # B4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # D4
])
piano.notes.extend(piano_notes)

# Sax: One short motif, start it, leave it hanging, come back and finish it
# Motif: F (65), A (68), D (62), F (65)
# Start on 1.5s, leave D (62) hanging, come back with F (65) at 2.75s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),
    pretty_midi.Note(velocity=110, pitch=65, start=2.75, end=3.0),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
