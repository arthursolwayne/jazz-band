
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
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=80, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Start the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.75),  # Fm7 - F
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # Ab - chromatic approach
    pretty_midi.Note(velocity=100, pitch=66, start=2.0, end=2.25),  # G - half-step above
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.5),  # F - return
    pretty_midi.Note(velocity=100, pitch=67, start=2.5, end=2.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=2.75, end=3.0),  # Bb - tension
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=2.5, end=2.75),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=2.75, end=3.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2 (1.5 - 2.0s) - F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=1.75, end=2.0),  # F
    # Bar 3 (2.5 - 3.0s) - Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=73, start=2.75, end=3.0),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=2.75, end=3.0),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=2.75, end=3.0),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=2.75, end=3.0),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Continue the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=3.5, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=3.0, end=3.25),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=3.5, end=3.75),  # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.0, end=4.25),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=4.25, end=4.5),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3 (3.0 - 3.5s) - F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=3.25, end=3.5),  # F
    # Bar 4 (4.0 - 4.5s) - Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=73, start=4.25, end=4.5),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=4.25, end=4.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=4.25, end=4.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=4.25, end=4.5),  # Bb
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Finish the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=66, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=100, pitch=60, start=5.75, end=6.0),  # D
]
sax.notes.extend(sax_notes)

# Bass: Walking line in Fm
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.75),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=80, pitch=45, start=5.0, end=5.25),  # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=46, start=5.5, end=5.75),  # G
    pretty_midi.Note(velocity=80, pitch=48, start=5.75, end=6.0),  # Bb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4 (4.5 - 5.0s) - F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=90, pitch=69, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=90, pitch=64, start=4.75, end=5.0),  # F
    # Bar 4 (5.0 - 5.5s) - Bb7 (Bb, D, F, Ab)
    pretty_midi.Note(velocity=90, pitch=73, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=69, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # Ab
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.5),  # Bb
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3
drum_notes = [
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
