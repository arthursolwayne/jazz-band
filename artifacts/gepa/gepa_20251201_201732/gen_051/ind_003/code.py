
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
    pretty_midi.Note(velocity=80, pitch=42, start=1.3125, end=1.5)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Saxophone: short motif, one phrase, leave it hanging
sax_notes = [
    # Fm7 (F, Ab, C, Eb) - start with a chromatic approach to F
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.625, end=1.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # G
]

# Bass: walking line, roots and fifths with chromatic approach
bass_notes = [
    # F -> C -> Ab -> Eb -> F
    pretty_midi.Note(velocity=80, pitch=38, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.625, end=1.75),  # C
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=38, start=1.875, end=2.0),  # F
]

# Piano: open voicing, Fm7 -> Ab7 -> Bb7 -> Eb7
piano_notes = [
    # Fm7 (F, Ab, C, Eb)
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=67, start=1.5, end=1.75),
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),
    # Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0),
]

# Bar 3: Full quartet (3.0 - 4.5s)
# Saxophone: continuation of motif, slightly altered
sax_notes_continuation = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.5),  # Eb
]

# Bass: walking line, Ab -> Eb -> Bb -> F
bass_notes_continuation = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.125),  # Ab
    pretty_midi.Note(velocity=80, pitch=38, start=3.125, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=3.25, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.5),  # Ab
]

# Piano: open voicings, Ab7 -> Bb7 -> Eb7 -> Fm7
piano_notes_continuation = [
    # Ab7 (Ab, C, Eb, G)
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25),
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.25),
    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),
]

# Bar 4: Full quartet (4.5 - 6.0s)
# Saxophone: final phrase, resolution avoided
sax_notes_final = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=67, start=4.625, end=4.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.0),  # F
]

# Bass: walking line, Eb -> Bb -> F -> Ab
bass_notes_final = [
    pretty_midi.Note(velocity=80, pitch=38, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=41, start=4.625, end=4.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=38, start=4.875, end=5.0),  # F
]

# Piano: open voicing, Eb7 -> Bb7 -> F7 -> Ab7
piano_notes_final = [
    # Eb7 (Eb, G, Bb, D)
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75),
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),
    # Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0),
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),
]

# Add all notes to instruments
sax.notes.extend(sax_notes)
sax.notes.extend(sax_notes_continuation)
sax.notes.extend(sax_notes_final)

bass.notes.extend(bass_notes)
bass.notes.extend(bass_notes_continuation)
bass.notes.extend(bass_notes_final)

piano.notes.extend(piano_notes)
piano.notes.extend(piano_notes_continuation)
piano.notes.extend(piano_notes_final)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
