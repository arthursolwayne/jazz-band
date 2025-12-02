
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
# Sax motif: D (D4) -> F# (F#4) -> B (B4) -> D (D5) on beat 1
# Then leave it hanging on the last beat
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),   # D5
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.875),   # D3
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25),   # Eb3
    pretty_midi.Note(velocity=80, pitch=45, start=2.25, end=2.625),   # E3
    pretty_midi.Note(velocity=80, pitch=46, start=2.625, end=3.0),    # F3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 - 7th chord on beat 2 (D7)
    pretty_midi.Note(velocity=90, pitch=62, start=1.875, end=2.25),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=1.875, end=2.25),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # C#5
    # Bar 3 - 7th chord on beat 4 (B7)
    pretty_midi.Note(velocity=90, pitch=69, start=2.625, end=3.0),   # B4
    pretty_midi.Note(velocity=90, pitch=74, start=2.625, end=3.0),   # D5
    pretty_midi.Note(velocity=90, pitch=77, start=2.625, end=3.0),   # F#5
    pretty_midi.Note(velocity=90, pitch=81, start=2.625, end=3.0),   # A5
]
piano.notes.extend(piano_notes)

# Bar 3: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.8125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.0),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.6875, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.0625, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=2.4375, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=2.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=2.8125, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (3.0 - 4.5s)
# Sax: Repeat the motif, but finish it
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D4
    pretty_midi.Note(velocity=100, pitch=66, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),  # B4
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),   # D5
]
sax.notes.extend(sax_notes)

# Bass: Walking line in D, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=46, start=3.0, end=3.375),   # F3
    pretty_midi.Note(velocity=80, pitch=47, start=3.375, end=3.75),   # F#3
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.125),   # G3
    pretty_midi.Note(velocity=80, pitch=49, start=4.125, end=4.5),    # G#3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 - 7th chord on beat 2 (D7)
    pretty_midi.Note(velocity=90, pitch=62, start=3.375, end=3.75),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # F#4
    pretty_midi.Note(velocity=90, pitch=71, start=3.375, end=3.75),  # A4
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # C#5
    # Bar 4 - 7th chord on beat 4 (B7)
    pretty_midi.Note(velocity=90, pitch=69, start=4.125, end=4.5),   # B4
    pretty_midi.Note(velocity=90, pitch=74, start=4.125, end=4.5),   # D5
    pretty_midi.Note(velocity=90, pitch=77, start=4.125, end=4.5),   # F#5
    pretty_midi.Note(velocity=90, pitch=81, start=4.125, end=4.5),   # A5
]
piano.notes.extend(piano_notes)

# Bar 4: Drums
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.3125),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.5),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.625),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.1875),
    pretty_midi.Note(velocity=80, pitch=42, start=3.1875, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5625),
    pretty_midi.Note(velocity=80, pitch=42, start=3.5625, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=3.9375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.9375, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.3125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.3125, end=4.5),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
