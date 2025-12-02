
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.1875),   # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.5625), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=0.5625, end=0.75), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.5625, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=0.9375),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.125, end=1.5),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass: walking line in F, roots and fifths with chromatic approaches
# F - G# - C - D - F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=32, start=1.5, end=1.875),   # F2
    pretty_midi.Note(velocity=80, pitch=35, start=1.875, end=2.25),  # G#2
    pretty_midi.Note(velocity=80, pitch=36, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=80, pitch=37, start=2.625, end=3.0),   # D3
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, comp on 2 and 4
# Bar 2: Fmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.875),   # F4
    pretty_midi.Note(velocity=90, pitch=72, start=1.5, end=1.875),   # A4
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),   # C5
    pretty_midi.Note(velocity=90, pitch=79, start=1.5, end=1.875),   # E5
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625), # F4
    pretty_midi.Note(velocity=90, pitch=72, start=2.25, end=2.625), # A4
    pretty_midi.Note(velocity=90, pitch=76, start=2.25, end=2.625), # C5
    pretty_midi.Note(velocity=90, pitch=79, start=2.25, end=2.625), # E5
]
piano.notes.extend(piano_notes)

# Sax: motif on F, start and leave hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.75),   # F4
    pretty_midi.Note(velocity=110, pitch=68, start=1.75, end=2.0),   # A4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.25),   # Bb4
    pretty_midi.Note(velocity=110, pitch=65, start=2.25, end=2.5),   # F4
    pretty_midi.Note(velocity=110, pitch=68, start=2.5, end=2.75),   # A4
    pretty_midi.Note(velocity=110, pitch=69, start=2.75, end=3.0),   # Bb4
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass: walking line in F, roots and fifths with chromatic approaches
# Bb - C - Eb - F
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=30, start=3.0, end=3.375),   # Bb2
    pretty_midi.Note(velocity=80, pitch=32, start=3.375, end=3.75),  # C3
    pretty_midi.Note(velocity=80, pitch=35, start=3.75, end=4.125),  # Eb3
    pretty_midi.Note(velocity=80, pitch=36, start=4.125, end=4.5),   # F3
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, comp on 2 and 4
# Bar 3: Bbmaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),   # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.375),   # D4
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),   # F4
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),   # Ab4
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125), # Bb4
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.125), # D4
    pretty_midi.Note(velocity=90, pitch=71, start=3.75, end=4.125), # F4
    pretty_midi.Note(velocity=90, pitch=74, start=3.75, end=4.125), # Ab4
]
piano.notes.extend(piano_notes)

# Sax: motif continues, tension and release
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),   # Bb4
    pretty_midi.Note(velocity=110, pitch=64, start=3.25, end=3.5),   # Eb4
    pretty_midi.Note(velocity=110, pitch=65, start=3.5, end=3.75),   # F4
    pretty_midi.Note(velocity=110, pitch=60, start=3.75, end=4.0),   # Bb4
    pretty_midi.Note(velocity=110, pitch=64, start=4.0, end=4.25),   # Eb4
    pretty_midi.Note(velocity=110, pitch=65, start=4.25, end=4.5),   # F4
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass: walking line in F, roots and fifths with chromatic approaches
# A - Bb - D - E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=28, start=4.5, end=4.875),   # A2
    pretty_midi.Note(velocity=80, pitch=30, start=4.875, end=5.25),  # Bb2
    pretty_midi.Note(velocity=80, pitch=34, start=5.25, end=5.625),  # D3
    pretty_midi.Note(velocity=80, pitch=36, start=5.625, end=6.0),   # F3
]
bass.notes.extend(bass_notes)

# Piano: open voicings, different chord each bar, comp on 2 and 4
# Bar 4: Amaj7
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=57, start=4.5, end=4.875),   # A4
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.875),   # C#4
    pretty_midi.Note(velocity=90, pitch=68, start=4.5, end=4.875),   # E4
    pretty_midi.Note(velocity=90, pitch=72, start=4.5, end=4.875),   # G4
    pretty_midi.Note(velocity=100, pitch=57, start=5.25, end=5.625), # A4
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.625), # C#4
    pretty_midi.Note(velocity=90, pitch=68, start=5.25, end=5.625), # E4
    pretty_midi.Note(velocity=90, pitch=72, start=5.25, end=5.625), # G4
]
piano.notes.extend(piano_notes)

# Sax: motif resolves on F, final note with release
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=57, start=4.5, end=4.75),   # A4
    pretty_midi.Note(velocity=110, pitch=58, start=4.75, end=5.0),   # Bb4
    pretty_midi.Note(velocity=110, pitch=62, start=5.0, end=5.25),   # D4
    pretty_midi.Note(velocity=110, pitch=65, start=5.25, end=5.5),   # F4
    pretty_midi.Note(velocity=110, pitch=65, start=5.5, end=5.75),   # F4
    pretty_midi.Note(velocity=110, pitch=65, start=5.75, end=6.0),   # F4
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.6875),   # Hihat on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.6875, end=4.875), # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.125), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.125, end=5.5),   # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.125, end=5.3125), # Hihat on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.3125, end=5.5),   # Hihat on &
    pretty_midi.Note(velocity=100, pitch=38, start=5.5, end=5.875),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.5, end=5.875),    # Hihat on 4
]
drums.notes.extend(drum_notes)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("intro_wayne.mid")
