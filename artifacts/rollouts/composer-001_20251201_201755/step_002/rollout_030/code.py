
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
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=1.5, end=1.875),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Marcus: Walking bass line in Fm (F, Ab, D, Eb)
# Diane: Fm7 -> Bbm7 -> Eb7 -> Am7 (open voicings, resolve on the last)
# You: Sax motif - short, singable, leaves a question
# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Marcus (Bass)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=67, start=1.875, end=2.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=69, start=2.25, end=2.625),  # D2
    pretty_midi.Note(velocity=90, pitch=70, start=2.625, end=3.0),  # Eb2
]
bass.notes.extend(bass_notes)

# Diane (Piano)
piano_notes = [
    # Fm7 (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=69, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=60, start=1.5, end=1.875),

    # Bbm7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=72, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=69, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=71, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.25),

    # Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=74, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=72, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=69, start=2.25, end=2.625),

    # Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=77, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=72, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=74, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Little Ray (Drums) - Bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=2.25, end=2.625),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=2.625, end=3.0),  # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),  # Hihat on 4
]
drums.notes.extend(drum_notes)

# Dante (Sax) - Bar 2
# Motif: F, Ab, Bb, F (sings, leaves a question)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Marcus: Walking bass line in Fm (F, Ab, D, Eb)
# Diane: Fm7 -> Bbm7 -> Eb7 -> Am7 (open voicings, resolve on the last)
# You: Sax motif - continuation of the theme, but with variation
# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Marcus (Bass)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F2
    pretty_midi.Note(velocity=90, pitch=67, start=3.375, end=3.75),  # Ab2
    pretty_midi.Note(velocity=90, pitch=69, start=3.75, end=4.125),  # D2
    pretty_midi.Note(velocity=90, pitch=70, start=4.125, end=4.5),   # Eb2
]
bass.notes.extend(bass_notes)

# Diane (Piano)
piano_notes = [
    # Fm7 (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.375),

    # Bbm7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=72, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=69, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=71, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.75),

    # Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=74, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=72, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=69, start=3.75, end=4.125),

    # Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=77, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=74, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Little Ray (Drums) - Bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.75),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=3.75, end=4.125),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=4.125, end=4.5),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Dante (Sax) - Bar 3
# Motif: F, Ab, Bb, F (sings, leaves a question)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),   # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Marcus: Walking bass line in Fm (F, Ab, D, Eb)
# Diane: Fm7 -> Bbm7 -> Eb7 -> Am7 (open voicings, resolve on the last)
# You: Sax motif - continuation of the theme, but with variation
# Little Ray: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Marcus (Bass)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F2
    pretty_midi.Note(velocity=90, pitch=67, start=4.875, end=5.25),  # Ab2
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.625),  # D2
    pretty_midi.Note(velocity=90, pitch=70, start=5.625, end=6.0),   # Eb2
]
bass.notes.extend(bass_notes)

# Diane (Piano)
piano_notes = [
    # Fm7 (F, Ab, D, C)
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=60, start=4.5, end=4.875),

    # Bbm7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=72, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=71, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=67, start=4.875, end=5.25),

    # Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=74, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=72, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.625),

    # Am7 (A, C, E, G)
    pretty_midi.Note(velocity=100, pitch=77, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=74, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Little Ray (Drums) - Bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),  # Hihat on 1
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),  # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=36, start=5.25, end=5.625),  # Kick on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),  # Hihat on 3
    pretty_midi.Note(velocity=100, pitch=38, start=5.625, end=6.0),   # Snare on 4
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Dante (Sax) - Bar 4
# Motif: F, Ab, Bb, F (sings, leaves a question)
# This time, leave the last note hanging
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=67, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=72, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),   # F (hanging note)
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write('jazz_intro.mid')
