
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=0.1875, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.9375, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.3125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=1.5, end=1.875),  # D2
    pretty_midi.Note(velocity=90, pitch=39, start=1.875, end=2.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=40, start=2.25, end=2.625),  # E2
    pretty_midi.Note(velocity=90, pitch=43, start=2.625, end=3.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolving on the last
# Bar 2: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=1.5, end=3.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=3.0),  # A4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=3.0),  # C4
]
piano.notes.extend(piano_notes)

# Sax: Melody - short motif, sing, leave it hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # A4
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=3.0),   # G4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=43, start=3.0, end=3.375),  # G2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # F2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=40, start=3.75, end=4.125),  # E2
    pretty_midi.Note(velocity=90, pitch=38, start=4.125, end=4.5),   # D2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolving on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=59, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=4.5),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5),  # F4
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=4.5),  # Ab4
]
piano.notes.extend(piano_notes)

# Sax: Melody - continuation of the motif, resolved
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.375),  # F4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # E4
    pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.125),  # D4
    pretty_midi.Note(velocity=100, pitch=60, start=4.125, end=4.5),   # C4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: D2 (MIDI 38) walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=38, start=4.5, end=4.875),  # D2
    pretty_midi.Note(velocity=90, pitch=39, start=4.875, end=5.25),  # Eb2 (chromatic)
    pretty_midi.Note(velocity=90, pitch=40, start=5.25, end=5.625),  # E2
    pretty_midi.Note(velocity=90, pitch=43, start=5.625, end=6.0),   # G2
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolving on the last
# Bar 4: Dm7 (D, F, A, C)
piano_notes = [
    pretty_midi.Note(velocity=95, pitch=62, start=4.5, end=6.0),  # D4
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # F4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # A4
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # C4
]
piano.notes.extend(piano_notes)

# Sax: Melody - resolution, return to the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # E4
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=6.0),   # G4
]
sax.notes.extend(sax_notes)

# Drums: Bar 4 (4.5 - 6.0s)
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
# midi.write disabled
