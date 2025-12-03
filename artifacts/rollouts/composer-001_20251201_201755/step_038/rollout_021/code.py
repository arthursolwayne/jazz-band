
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

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Fm root (D2, MIDI 38) with chromatic approach from C#2 (MIDI 37)
    pretty_midi.Note(velocity=90, pitch=37, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.6875, end=2.0),
    # Fm fifth (A2, MIDI 43) with chromatic approach from G#2 (MIDI 42)
    pretty_midi.Note(velocity=90, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=100, pitch=43, start=2.1875, end=2.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=1.5, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=1.5, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # First note: F (MIDI 53)
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),
    # Leave it hanging
    # Second note: Ab (MIDI 51)
    pretty_midi.Note(velocity=110, pitch=51, start=2.5, end=2.875),
    # Third note: D (MIDI 58)
    pretty_midi.Note(velocity=110, pitch=58, start=3.0, end=3.375),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Fm root (D2, MIDI 38) with chromatic approach from C#2 (MIDI 37)
    pretty_midi.Note(velocity=90, pitch=37, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=100, pitch=38, start=3.1875, end=3.5),
    # Fm fifth (A2, MIDI 43) with chromatic approach from G#2 (MIDI 42)
    pretty_midi.Note(velocity=90, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=100, pitch=43, start=3.6875, end=4.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 3: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=53, start=3.0, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=3.0, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=3.0, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Sax: Continue the motif
sax_notes = [
    # Fourth note: F (MIDI 53)
    pretty_midi.Note(velocity=110, pitch=53, start=3.375, end=3.75),
    # Fifth note: Ab (MIDI 51)
    pretty_midi.Note(velocity=110, pitch=51, start=4.0, end=4.375),
    # Sixth note: D (MIDI 58)
    pretty_midi.Note(velocity=110, pitch=58, start=4.5, end=4.875),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Fm root (D2, MIDI 38) with chromatic approach from C#2 (MIDI 37)
    pretty_midi.Note(velocity=90, pitch=37, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.6875, end=5.0),
    # Fm fifth (A2, MIDI 43) with chromatic approach from G#2 (MIDI 42)
    pretty_midi.Note(velocity=90, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=100, pitch=43, start=5.1875, end=5.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 4: Fm7 (F, Ab, C, D)
    pretty_midi.Note(velocity=100, pitch=53, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=51, start=4.5, end=6.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=58, start=4.5, end=6.0),  # D
]
piano.notes.extend(piano_notes)

# Sax: Finish the motif
sax_notes = [
    # Seventh note: F (MIDI 53)
    pretty_midi.Note(velocity=110, pitch=53, start=4.875, end=5.25),
    # Eighth note: Ab (MIDI 51)
    pretty_midi.Note(velocity=110, pitch=51, start=5.5, end=5.875),
    # Ninth note: D (MIDI 58)
    pretty_midi.Note(velocity=110, pitch=58, start=6.0, end=6.375),
]
sax.notes.extend(sax_notes)

# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    # Bar 2: Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=2.0, end=2.125),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Bar 2: Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0, end=2.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.1875, end=2.375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.375, end=2.5),
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0),
    # Bar 3: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    # Bar 3: Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.5, end=3.625),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Bar 3: Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5, end=3.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.6875, end=3.875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.875, end=4.0),
    pretty_midi.Note(velocity=80, pitch=42, start=4.0, end=4.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.1875, end=4.375),
    pretty_midi.Note(velocity=80, pitch=42, start=4.375, end=4.5),
    # Bar 4: Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.75, end=6.0),
    # Bar 4: Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.0, end=5.125),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Bar 4: Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5, end=5.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.6875, end=5.875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.875, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
