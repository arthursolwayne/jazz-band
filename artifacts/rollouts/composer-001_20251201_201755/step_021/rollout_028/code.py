
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
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # F2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=1.5, end=1.875),
    # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=54, start=1.875, end=2.0),
    # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=57, start=2.0, end=2.375),
    # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=56, start=2.375, end=2.5),
    # F2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=2.5, end=2.875),
    # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=54, start=2.875, end=3.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, Eb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=61, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=3.0),  # Eb4
]
piano.notes.extend(piano_notes)

# Sax: Motif - start it, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # F4
    pretty_midi.Note(velocity=110, pitch=66, start=1.75, end=2.0),  # A4
    pretty_midi.Note(velocity=110, pitch=64, start=2.0, end=2.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=2.25, end=2.5),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=2.5, end=2.75),  # C5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=56, start=3.0, end=3.125),
    # F2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=3.125, end=3.5),
    # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=54, start=3.5, end=3.625),
    # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=57, start=3.625, end=4.0),
    # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=56, start=4.0, end=4.125),
    # F2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=4.125, end=4.5),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=4.5),  # Ab4
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.25),  # F4
    pretty_midi.Note(velocity=110, pitch=66, start=3.25, end=3.5),  # A4
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=3.75, end=4.0),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=4.0, end=4.25),  # C5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (F2-A2, MIDI 53-57), roots and fifths with chromatic approaches
bass_notes = [
    # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=57, start=4.5, end=4.875),
    # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=56, start=4.875, end=5.0),
    # F2 (root)
    pretty_midi.Note(velocity=90, pitch=53, start=5.0, end=5.375),
    # Gb2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=54, start=5.375, end=5.5),
    # A2 (fifth)
    pretty_midi.Note(velocity=90, pitch=57, start=5.5, end=5.875),
    # Ab2 (chromatic approach)
    pretty_midi.Note(velocity=80, pitch=56, start=5.875, end=6.0),
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 4: C7 (C, E, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=6.0),  # C5
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),  # E6
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=6.0),  # G5
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=6.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Motif conclusion
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # F4
    pretty_midi.Note(velocity=110, pitch=66, start=4.75, end=5.0),  # A4
    pretty_midi.Note(velocity=110, pitch=64, start=5.0, end=5.25),  # G4
    pretty_midi.Note(velocity=110, pitch=62, start=5.25, end=5.5),  # F4
    pretty_midi.Note(velocity=110, pitch=69, start=5.5, end=5.75),  # C5
    pretty_midi.Note(velocity=110, pitch=62, start=5.75, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums: Bar 3 and 4 (3.0 - 6.0s)
# Bar 3: Kick on 1 and 3, Snare on 2 and 4, Hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0, end=5.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=5.1875, end=5.375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.375, end=5.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.5625, end=5.75),
    pretty_midi.Note(velocity=80, pitch=42, start=5.75, end=5.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.9375, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
