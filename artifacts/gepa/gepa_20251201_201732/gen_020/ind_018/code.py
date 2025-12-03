
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

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Marcus: Walking line on F7 - Bb7 - Eb7 - Ab7
# Roots: F2, Bb2, Eb2, Ab2
# Fifths: C3, F3, A3, D3
# Chromatic approaches: E2, Bb2, D3, G3
bass_notes = [
    # Bar 2 (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=100, pitch=76, start=1.875, end=2.25), # C3
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625), # E2
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),  # F2

    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),  # Bb2
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75), # F3
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125), # Bb2
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.5),  # Bb2

    # Bar 4 (Eb7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),  # Eb2
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25), # A3
    pretty_midi.Note(velocity=100, pitch=66, start=5.25, end=5.625), # G3
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # Eb2
]
bass.notes.extend(bass_notes)

# Diane: Open voicings, different chord each bar, resolve on the last
# Bar 2: F7 (F, A, C, E)
# Bar 3: Bb7 (Bb, D, F, Ab)
# Bar 4: Eb7 (Eb, G, Bb, D)
piano_notes = [
    # Bar 2 (F7)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875), # F3
    pretty_midi.Note(velocity=100, pitch=76, start=1.5, end=1.875), # A3
    pretty_midi.Note(velocity=100, pitch=74, start=1.5, end=1.875), # C4
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.875), # E4

    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375), # Bb3
    pretty_midi.Note(velocity=100, pitch=72, start=3.0, end=3.375), # D4
    pretty_midi.Note(velocity=100, pitch=74, start=3.0, end=3.375), # F4
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=3.375), # Ab4

    # Bar 4 (Eb7)
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875), # Eb3
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875), # G4
    pretty_midi.Note(velocity=100, pitch=72, start=4.5, end=4.875), # Bb4
    pretty_midi.Note(velocity=100, pitch=76, start=4.5, end=4.875), # D5
]
piano.notes.extend(piano_notes)

# Dante: Tenor sax, one short motif, make it sing
# Start it, leave it hanging. Come back and finish it.
sax_notes = [
    # Bar 2 (F7)
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.875),  # Bb4
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25), # C5
    pretty_midi.Note(velocity=110, pitch=64, start=2.25, end=2.625), # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # Bb4

    # Bar 3 (Bb7)
    pretty_midi.Note(velocity=110, pitch=67, start=3.0, end=3.375),  # C5
    pretty_midi.Note(velocity=110, pitch=65, start=3.375, end=3.75), # Bb4
    pretty_midi.Note(velocity=110, pitch=69, start=3.75, end=4.125), # Bb4
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # D5

    # Bar 4 (Eb7)
    pretty_midi.Note(velocity=110, pitch=67, start=4.5, end=4.875),  # C5
    pretty_midi.Note(velocity=110, pitch=71, start=4.875, end=5.25), # D5
    pretty_midi.Note(velocity=110, pitch=69, start=5.25, end=5.625), # Bb4
    pretty_midi.Note(velocity=110, pitch=64, start=5.625, end=6.0),  # G4
]
sax.notes.extend(sax_notes)

# Drums: Bars 2-4
# Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=2.0),
]
drums.notes.extend(drum_notes)

# Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.5),
]
drums.notes.extend(drum_notes)

# Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375), # Snare
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=5.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
