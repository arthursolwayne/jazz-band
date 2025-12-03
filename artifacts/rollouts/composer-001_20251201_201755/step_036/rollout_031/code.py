
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
    # Root (Fm) on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),
    # Chromatic approach to 3rd (Ab) on 2
    pretty_midi.Note(velocity=100, pitch=40, start=1.875, end=2.0),
    # 5th (C) on 3
    pretty_midi.Note(velocity=100, pitch=43, start=2.0, end=2.375),
    # Chromatic approach to root (F) on 4
    pretty_midi.Note(velocity=100, pitch=41, start=2.375, end=2.5),
    # Root (F) on 4
    pretty_midi.Note(velocity=100, pitch=38, start=2.5, end=2.875),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7
piano_notes = [
    # Fm7: F, Ab, D, C
    pretty_midi.Note(velocity=100, pitch=53, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=50, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=57, start=1.5, end=3.0),
    pretty_midi.Note(velocity=100, pitch=52, start=1.5, end=3.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging
sax_notes = [
    # F (Ab) on 1
    pretty_midi.Note(velocity=110, pitch=53, start=1.5, end=1.875),
    # Ab (Bb) on 2
    pretty_midi.Note(velocity=110, pitch=50, start=1.875, end=2.125),
    # Bb (B) on 3
    pretty_midi.Note(velocity=110, pitch=52, start=2.125, end=2.5),
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Root (F) on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.0, end=3.375),
    # Chromatic approach to 3rd (Ab) on 2
    pretty_midi.Note(velocity=100, pitch=40, start=3.375, end=3.5),
    # 5th (C) on 3
    pretty_midi.Note(velocity=100, pitch=43, start=3.5, end=3.875),
    # Chromatic approach to root (F) on 4
    pretty_midi.Note(velocity=100, pitch=41, start=3.875, end=4.0),
    # Root (F) on 4
    pretty_midi.Note(velocity=100, pitch=38, start=4.0, end=4.375),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Ab7
piano_notes = [
    # Ab7: Ab, C, Eb, Gb
    pretty_midi.Note(velocity=100, pitch=50, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=55, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=52, start=3.0, end=4.5),
    pretty_midi.Note(velocity=100, pitch=51, start=3.0, end=4.5),
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation
sax_notes = [
    # F (Ab) on 1
    pretty_midi.Note(velocity=110, pitch=53, start=3.0, end=3.375),
    # Ab (Bb) on 2
    pretty_midi.Note(velocity=110, pitch=50, start=3.375, end=3.625),
    # Bb (B) on 3
    pretty_midi.Note(velocity=110, pitch=52, start=3.625, end=4.0),
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D2-G2, MIDI 38-43), roots and fifths with chromatic approaches
bass_notes = [
    # Root (F) on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.5, end=4.875),
    # Chromatic approach to 3rd (Ab) on 2
    pretty_midi.Note(velocity=100, pitch=40, start=4.875, end=5.0),
    # 5th (C) on 3
    pretty_midi.Note(velocity=100, pitch=43, start=5.0, end=5.375),
    # Chromatic approach to root (F) on 4
    pretty_midi.Note(velocity=100, pitch=41, start=5.375, end=5.5),
    # Root (F) on 4
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: Cm7
piano_notes = [
    # Cm7: C, Eb, G, Bb
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=52, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=6.0),
    pretty_midi.Note(velocity=100, pitch=50, start=4.5, end=6.0),
]
piano.notes.extend(piano_notes)

# Sax: Motif finish
sax_notes = [
    # F (Ab) on 1
    pretty_midi.Note(velocity=110, pitch=53, start=4.5, end=4.875),
    # Ab (Bb) on 2
    pretty_midi.Note(velocity=110, pitch=50, start=4.875, end=5.125),
    # Bb (B) on 3
    pretty_midi.Note(velocity=110, pitch=52, start=5.125, end=5.5),
    # Resolution to F
    pretty_midi.Note(velocity=110, pitch=53, start=5.5, end=6.0),
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4
# Bar 3: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
