
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=120)

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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif - C4 (C), E4 (E), D4 (D), B3 (B)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=1.5, end=1.75),  # C4
    pretty_midi.Note(velocity=110, pitch=64, start=1.75, end=2.0),  # E4
    pretty_midi.Note(velocity=110, pitch=62, start=2.0, end=2.25),  # D4
    pretty_midi.Note(velocity=110, pitch=61, start=2.25, end=2.5),  # B3
]
sax.notes.extend(sax_notes)

# Bass: Walking line in C minor - C3, D3, Eb3, F3, G3, Ab3, A3, Bb3
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=48, start=1.5, end=1.75),  # C3
    pretty_midi.Note(velocity=90, pitch=50, start=1.75, end=2.0),  # D3
    pretty_midi.Note(velocity=90, pitch=51, start=2.0, end=2.25),  # Eb3
    pretty_midi.Note(velocity=90, pitch=53, start=2.25, end=2.5),  # F3
    pretty_midi.Note(velocity=90, pitch=55, start=2.5, end=2.75),  # G3
    pretty_midi.Note(velocity=90, pitch=56, start=2.75, end=3.0),  # Ab3
    pretty_midi.Note(velocity=90, pitch=57, start=3.0, end=3.25),  # A3
    pretty_midi.Note(velocity=90, pitch=58, start=3.25, end=3.5),  # Bb3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 (C, E, B, D) on beat 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),
    # D7 (D, F#, C#, E) on beat 4 (2.75 - 3.0)
    pretty_midi.Note(velocity=100, pitch=62, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=67, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=71, start=2.75, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0),
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif but with variation (C4, D4, E4, B3)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),  # C4
    pretty_midi.Note(velocity=110, pitch=62, start=3.25, end=3.5),  # D4
    pretty_midi.Note(velocity=110, pitch=64, start=3.5, end=3.75),  # E4
    pretty_midi.Note(velocity=110, pitch=61, start=3.75, end=4.0),  # B3
]
sax.notes.extend(sax_notes)

# Bass: Walking line in C minor - Bb3, B3, C3, D3, Eb3, F3, G3, Ab3
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=58, start=3.0, end=3.25),  # Bb3
    pretty_midi.Note(velocity=90, pitch=59, start=3.25, end=3.5),  # B3
    pretty_midi.Note(velocity=90, pitch=48, start=3.5, end=3.75),  # C3
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=4.0),  # D3
    pretty_midi.Note(velocity=90, pitch=51, start=4.0, end=4.25),  # Eb3
    pretty_midi.Note(velocity=90, pitch=53, start=4.25, end=4.5),  # F3
    pretty_midi.Note(velocity=90, pitch=55, start=4.5, end=4.75),  # G3
    pretty_midi.Note(velocity=90, pitch=56, start=4.75, end=5.0),  # Ab3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 (C, E, B, D) on beat 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    # D7 (D, F#, C#, E) on beat 4 (4.25 - 4.5)
    pretty_midi.Note(velocity=100, pitch=62, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=67, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=71, start=4.25, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.25, end=4.5),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Repeat motif with resolution (C4, B3, C4, B3) to create a question
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=60, start=4.5, end=4.75),  # C4
    pretty_midi.Note(velocity=110, pitch=61, start=4.75, end=5.0),  # B3
    pretty_midi.Note(velocity=110, pitch=60, start=5.0, end=5.25),  # C4
    pretty_midi.Note(velocity=110, pitch=61, start=5.25, end=5.5),  # B3
]
sax.notes.extend(sax_notes)

# Bass: Walking line in C minor - B3, C3, D3, Eb3, F3, G3, Ab3, A3
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=59, start=4.5, end=4.75),  # B3
    pretty_midi.Note(velocity=90, pitch=48, start=4.75, end=5.0),  # C3
    pretty_midi.Note(velocity=90, pitch=50, start=5.0, end=5.25),  # D3
    pretty_midi.Note(velocity=90, pitch=51, start=5.25, end=5.5),  # Eb3
    pretty_midi.Note(velocity=90, pitch=53, start=5.5, end=5.75),  # F3
    pretty_midi.Note(velocity=90, pitch=55, start=5.75, end=6.0),  # G3
    pretty_midi.Note(velocity=90, pitch=56, start=6.0, end=6.25),  # Ab3
    pretty_midi.Note(velocity=90, pitch=57, start=6.25, end=6.5),  # A3
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # C7 (C, E, B, D) on beat 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),
    # D7 (D, F#, C#, E) on beat 4 (5.75 - 6.0)
    pretty_midi.Note(velocity=100, pitch=62, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=71, start=5.75, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.75, end=6.0),
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=80, pitch=42, start=6.0, end=6.375),
    pretty_midi.Note(velocity=80, pitch=42, start=6.375, end=6.75),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
