
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

# Bar 2: Everyone in
# Bass: F2 (MIDI 53) -> G2 (MIDI 55) with chromatic approach
bass_notes = [
    # F2, chromatic approach from E2 (MIDI 52)
    pretty_midi.Note(velocity=90, pitch=52, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=53, start=1.625, end=1.875),
    # G2, chromatic approach from G#2 (MIDI 56)
    pretty_midi.Note(velocity=90, pitch=56, start=1.875, end=1.9375),
    pretty_midi.Note(velocity=100, pitch=55, start=1.9375, end=2.125),
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, Fm7 (F, Ab, C, Eb) -> Bb7 (Bb, D, F, Ab)
piano_notes = [
    # Fm7 (F, Ab, C, Eb) on bar 2
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=2.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=2.0),  # Ab4
    pretty_midi.Note(velocity=100, pitch=72, start=1.5, end=2.0),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=2.0),  # Eb5
    # Bb7 (Bb, D, F, Ab) on bar 4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.5),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.5),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # Ab4
]
piano.notes.extend(piano_notes)

# Sax: Motif in Fm - start with a G (MIDI 67), move to Ab (MIDI 68), then C (MIDI 72)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.125),  # Ab4
    pretty_midi.Note(velocity=110, pitch=72, start=2.125, end=2.5),  # C5
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet
# Bass: F2 (MIDI 53) -> Bb2 (MIDI 50) with chromatic approach
bass_notes = [
    # F2, chromatic approach from E2 (MIDI 52)
    pretty_midi.Note(velocity=90, pitch=52, start=2.5, end=2.625),
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=2.875),
    # Bb2, chromatic approach from A2 (MIDI 49)
    pretty_midi.Note(velocity=90, pitch=49, start=2.875, end=2.9375),
    pretty_midi.Note(velocity=100, pitch=50, start=2.9375, end=3.125),
]
bass.notes.extend(bass_notes)

# Piano: Open voicing, Bb7 (Bb, D, F, Ab) -> Cm7 (C, Eb, G, Bb)
piano_notes = [
    # Bb7 (Bb, D, F, Ab) on bar 3
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=2.5, end=3.0),  # D4
    pretty_midi.Note(velocity=100, pitch=71, start=2.5, end=3.0),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=3.0),  # Ab4
    # Cm7 (C, Eb, G, Bb) on bar 4
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.5),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.5),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=3.0, end=3.5),  # G5
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.5),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Motif continuation - move to Bb (MIDI 67), then resolve on C (MIDI 72)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=2.5, end=2.875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=72, start=2.875, end=3.25),  # C5
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet
# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=2.5, end=2.875),
    pretty_midi.Note(velocity=100, pitch=36, start=3.375, end=3.75),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    pretty_midi.Note(velocity=110, pitch=38, start=4.125, end=4.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=2.5, end=2.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.6875, end=2.875),
    pretty_midi.Note(velocity=80, pitch=42, start=2.875, end=3.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0625, end=3.25),
    pretty_midi.Note(velocity=80, pitch=42, start=3.25, end=3.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.4375, end=3.625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.625, end=3.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=3.8125, end=4.0),
]
drums.notes.extend(drum_notes)

# Bass: Bb2 (MIDI 50) -> F2 (MIDI 53) with chromatic approach
bass_notes = [
    # Bb2, chromatic approach from B2 (MIDI 51)
    pretty_midi.Note(velocity=90, pitch=51, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=50, start=3.625, end=3.875),
    # F2, chromatic approach from E2 (MIDI 52)
    pretty_midi.Note(velocity=90, pitch=52, start=3.875, end=3.9375),
    pretty_midi.Note(velocity=100, pitch=53, start=3.9375, end=4.125),
]
bass.notes.extend(bass_notes)

# Piano: Cm7 (C, Eb, G, Bb)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=72, start=3.5, end=4.0),  # C5
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=4.0),  # Eb5
    pretty_midi.Note(velocity=100, pitch=76, start=3.5, end=4.0),  # G5
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=4.0),  # Bb4
]
piano.notes.extend(piano_notes)

# Sax: Motif resolution - C (MIDI 72) and a final Ab (MIDI 68) to leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.5, end=3.875),  # C5
    pretty_midi.Note(velocity=110, pitch=68, start=3.875, end=4.125),  # Ab4
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
