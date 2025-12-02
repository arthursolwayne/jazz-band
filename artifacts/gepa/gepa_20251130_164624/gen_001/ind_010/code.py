
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
    pretty_midi.Note(velocity=110, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Fm7 (F, Ab, Bb, D) -> Bb, F, Ab, D -> F, Ab, Bb, D (motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0), # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5), # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=43, start=1.5, end=1.75), # F
    pretty_midi.Note(velocity=80, pitch=45, start=1.75, end=2.0), # G
    pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.25), # Ab
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.5), # Bb
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 (F7 on 2, F7 on 4)
piano_notes = [
    # Bar 2 (1.5 - 2.0s): F7 on 2
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0), # F
    pretty_midi.Note(velocity=100, pitch=68, start=1.75, end=2.0), # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=1.75, end=2.0), # C
    # Bar 3 (2.5 - 3.0s): F7 on 4
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=2.875), # F
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=2.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.625, end=2.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=2.625, end=2.875), # C
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Repeat motif starting on Ab
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25), # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5), # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.75), # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0), # Ab
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.25), # Bb
    pretty_midi.Note(velocity=80, pitch=44, start=3.25, end=3.5), # Ab
    pretty_midi.Note(velocity=80, pitch=43, start=3.5, end=3.75), # F
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.0), # G
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 (F7 on 2, F7 on 4)
piano_notes = [
    # Bar 3 (3.0 - 3.5s): F7 on 2
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5), # F
    pretty_midi.Note(velocity=100, pitch=68, start=3.25, end=3.5), # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.25, end=3.5), # C
    # Bar 4 (4.0 - 4.5s): F7 on 4
    pretty_midi.Note(velocity=100, pitch=65, start=4.125, end=4.375), # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.375), # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.125, end=4.375), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.125, end=4.375), # C
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish motif, descending
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.75), # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0), # G
    pretty_midi.Note(velocity=100, pitch=60, start=5.0, end=5.25), # F
    pretty_midi.Note(velocity=100, pitch=58, start=5.25, end=5.5), # Eb
]
sax.notes.extend(sax_notes)

# Bass: Walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.75), # Ab
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=5.0), # Bb
    pretty_midi.Note(velocity=80, pitch=40, start=5.0, end=5.25), # Db
    pretty_midi.Note(velocity=80, pitch=41, start=5.25, end=5.5), # D
]
bass.notes.extend(bass_notes)

# Piano: Comp on 2 and 4 (F7 on 2, F7 on 4)
piano_notes = [
    # Bar 4 (4.5 - 5.0s): F7 on 2
    pretty_midi.Note(velocity=100, pitch=65, start=4.75, end=5.0), # F
    pretty_midi.Note(velocity=100, pitch=68, start=4.75, end=5.0), # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.75, end=5.0), # C
    # Bar 4 (5.5 - 6.0s): F7 on 4
    pretty_midi.Note(velocity=100, pitch=65, start=5.625, end=5.875), # F
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=5.875), # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.625, end=5.875), # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.625, end=5.875), # C
]
piano.notes.extend(piano_notes)

# Drums: Continue for bar 2-4
# Bar 2 (1.5 - 3.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75), # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 3 (3.0 - 4.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25), # Snare on 4
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

# Bar 4 (4.5 - 6.0s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875), # Kick on 1
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0), # Kick on 3
    pretty_midi.Note(velocity=110, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=100, pitch=38, start=6.0, end=6.375), # Snare on 4 (off the end)
    # Hihat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Write the MIDI file
midi.write("dante_intro.mid")
