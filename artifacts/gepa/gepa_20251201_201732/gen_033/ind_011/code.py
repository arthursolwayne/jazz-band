
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
# Marcus - walking line in Fm (F, Ab, D, Eb, etc.)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=80, pitch=50, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=57, start=2.25, end=2.625),  # D3
    pretty_midi.Note(velocity=80, pitch=55, start=2.625, end=3.0),   # Eb3
]
bass.notes.extend(bass_notes)

# Diane - open voicings, different chord each bar, resolve on the last
# Bar 2: Fm7 (F, Ab, C, D)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=65, start=1.5, end=3.0),  # F4
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=3.0),  # Ab4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=3.0),  # C5
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=3.0),  # D5
]
piano.notes.extend(piano_notes)

# Bar 2: Sax - motif start
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=1.5, end=1.875),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625),  # G#4
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),  # F4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus - walking line in Fm (F, Ab, D, Eb, etc.)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=3.0, end=3.375),   # F2
    pretty_midi.Note(velocity=80, pitch=50, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=80, pitch=57, start=3.75, end=4.125),  # D3
    pretty_midi.Note(velocity=80, pitch=55, start=4.125, end=4.5),   # Eb3
]
bass.notes.extend(bass_notes)

# Diane - different chord, resolve on the last
# Bar 3: Bb7 (Bb, D, F, Ab)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=61, start=3.0, end=4.5),  # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=4.5),  # D5
    pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=4.5),  # F5
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=4.5),  # Ab4
]
piano.notes.extend(piano_notes)

# Bar 3: Sax - continue motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=3.0, end=3.375),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=3.75, end=4.125),  # G#4
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),  # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus - walking line in Fm (F, Ab, D, Eb, etc.)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=53, start=4.5, end=4.875),   # F2
    pretty_midi.Note(velocity=80, pitch=50, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=80, pitch=57, start=5.25, end=5.625),  # D3
    pretty_midi.Note(velocity=80, pitch=55, start=5.625, end=6.0),   # Eb3
]
bass.notes.extend(bass_notes)

# Diane - different chord, resolve on the last
# Bar 4: Cm7 (C, Eb, F, G)
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=6.0),  # C5
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=6.0),  # Eb5
    pretty_midi.Note(velocity=90, pitch=65, start=4.5, end=6.0),  # F5
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=6.0),  # G5
]
piano.notes.extend(piano_notes)

# Bar 4: Sax - finish motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=66, start=4.5, end=4.875),  # G4
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F4
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625),  # G#4
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),  # F4
]
sax.notes.extend(sax_notes)

# Drums for bars 2-4
# Bar 2: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=90, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=90, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Kick on 1 and 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=90, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=90, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Kick on 1 and 3
drum_notes = [
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
