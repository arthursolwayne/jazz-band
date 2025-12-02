
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),   # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=36, start=0.75, end=1.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=1.125, end=1.5),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=1.75, end=2.0),   # F#
    pretty_midi.Note(velocity=80, pitch=64, start=2.0, end=2.25),   # F
    pretty_midi.Note(velocity=80, pitch=63, start=2.25, end=2.5),   # E
    pretty_midi.Note(velocity=80, pitch=64, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=2.75, end=3.0),   # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),   # F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.75),
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),   # F7 again on beat 4
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.625),   # Hihat on 1
    pretty_midi.Note(velocity=95, pitch=38, start=1.875, end=2.0),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=1.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.375),  # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=2.625, end=2.75),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=2.75),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: Melody starts on beat 2 of bar 2
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=1.875, end=2.25),  # A (beat 2)
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.625), # G (beat 3)
    pretty_midi.Note(velocity=110, pitch=69, start=2.625, end=3.0),  # A (beat 4) — leaves it hanging
]
sax.notes.extend(sax_notes)

# Bar 3: (3.0 - 4.5s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=3.25, end=3.5),   # F#
    pretty_midi.Note(velocity=80, pitch=64, start=3.5, end=3.75),   # F
    pretty_midi.Note(velocity=80, pitch=63, start=3.75, end=4.0),   # E
    pretty_midi.Note(velocity=80, pitch=64, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=4.25, end=4.5),   # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),   # F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),   # F7 again on beat 4
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.125),   # Hihat on 1
    pretty_midi.Note(velocity=95, pitch=38, start=3.375, end=3.5),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.4375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=3.875),  # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=4.125, end=4.25),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.25),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: Melody continues on beat 2 of bar 3
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # G (beat 2)
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125), # F (beat 3)
    pretty_midi.Note(velocity=110, pitch=67, start=4.125, end=4.5),  # G (beat 4) — still unresolved
]
sax.notes.extend(sax_notes)

# Bar 4: (4.5 - 6.0s)
# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=4.75, end=5.0),   # F#
    pretty_midi.Note(velocity=80, pitch=64, start=5.0, end=5.25),   # F
    pretty_midi.Note(velocity=80, pitch=63, start=5.25, end=5.5),   # E
    pretty_midi.Note(velocity=80, pitch=64, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=80, pitch=65, start=5.75, end=6.0),   # F#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),   # F7 (F, A, C, E♭)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),   # F7 again on beat 4
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.625),   # Hihat on 1
    pretty_midi.Note(velocity=95, pitch=38, start=4.875, end=5.0),   # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=4.9375), # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625), # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.375),  # Hihat on 3
    pretty_midi.Note(velocity=95, pitch=38, start=5.625, end=5.75),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=5.75),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Sax: Melody resolves on beat 2 of bar 4
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=69, start=4.875, end=5.25),  # A (beat 2)
    pretty_midi.Note(velocity=100, pitch=67, start=5.25, end=5.625), # G (beat 3)
    pretty_midi.Note(velocity=110, pitch=69, start=5.625, end=6.0),  # A (beat 4) — resolves with a lingering note
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
