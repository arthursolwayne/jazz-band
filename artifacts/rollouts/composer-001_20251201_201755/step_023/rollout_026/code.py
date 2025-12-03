
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
# Bass: Walking line in F (F2, Bb2, C3, D3, F3, Ab2, Bb2, C3)
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),  # F2
    pretty_midi.Note(velocity=90, pitch=70, start=1.875, end=2.25),  # Bb2
    pretty_midi.Note(velocity=90, pitch=81, start=2.25, end=2.625),  # C3
    pretty_midi.Note(velocity=90, pitch=83, start=2.625, end=3.0),  # D3
]
bass.notes.extend(bass_notes)

# Piano: Open voicings, different chord each bar, resolve on the last
piano_notes = [
    # Bar 2: Fmaj7 (F, A, C, E)
    pretty_midi.Note(velocity=100, pitch=77, start=1.5, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=3.0),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=1.5, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=1.5, end=3.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif (F, G, Ab, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=79, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=80, start=2.625, end=3.0),  # Bb
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: F, G, Ab, A
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=78, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=3.75, end=4.125),  # Ab
    pretty_midi.Note(velocity=90, pitch=80, start=4.125, end=4.5),  # A
]
bass.notes.extend(bass_notes)

# Piano: Gm7 (G, Bb, D, F)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=78, start=3.0, end=4.5),  # G
    pretty_midi.Note(velocity=100, pitch=80, start=3.0, end=4.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=4.5),  # D
    pretty_midi.Note(velocity=100, pitch=77, start=3.0, end=4.5),  # F
]
piano.notes.extend(piano_notes)

# Sax: Motif repetition with variation (G, Ab, A, Bb)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=78, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=110, pitch=79, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=80, start=3.75, end=4.125),  # A
    pretty_midi.Note(velocity=110, pitch=81, start=4.125, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Same pattern, shifted
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.0),
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

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: F, G, Ab, A
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=78, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=90, pitch=79, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=90, pitch=80, start=5.625, end=6.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: Fmaj7 (F, A, C, E)
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=77, start=4.5, end=6.0),  # F
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=6.0),  # A
    pretty_midi.Note(velocity=100, pitch=81, start=4.5, end=6.0),  # C
    pretty_midi.Note(velocity=100, pitch=84, start=4.5, end=6.0),  # E
]
piano.notes.extend(piano_notes)

# Sax: Motif variation (F, G, Ab, Bb) with a slight delay on the last note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=77, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=78, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=79, start=5.25, end=5.625),  # Ab
    pretty_midi.Note(velocity=110, pitch=80, start=5.625, end=6.0),  # Bb
]
sax.notes.extend(sax_notes)

# Drums: Same pattern, shifted
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.375),
    pretty_midi.Note(velocity=110, pitch=38, start=6.25, end=6.5),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.6875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.6875, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.0625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.0625, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.4375),
    pretty_midi.Note(velocity=80, pitch=42, start=5.4375, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=5.8125),
    pretty_midi.Note(velocity=80, pitch=42, start=5.8125, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
# midi.write disabled
