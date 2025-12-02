
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
    pretty_midi.Note(velocity=90, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=0.375, end=0.75), # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=1.125, end=1.5),  # Hihat on 4
    pretty_midi.Note(velocity=80, pitch=42, start=0.0, end=1.5)     # Hihat on every 8th
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: Motif with space and unique durations
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.625),  # Fm7 (F, Ab, Bb, Db) - F
    pretty_midi.Note(velocity=100, pitch=69, start=1.625, end=1.75), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=1.875), # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=1.875, end=2.0),  # Db
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.125),  # F (reprise)
    pretty_midi.Note(velocity=100, pitch=69, start=2.125, end=2.25), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=2.25, end=2.5),   # Bb (hold)
    pretty_midi.Note(velocity=100, pitch=70, start=2.5, end=2.75),   # Db
    pretty_midi.Note(velocity=100, pitch=64, start=2.75, end=3.0)    # F (end on 4)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=1.5, end=1.625),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=1.75, end=1.875), # D
    pretty_midi.Note(velocity=80, pitch=41, start=1.875, end=2.0),  # Db
    pretty_midi.Note(velocity=80, pitch=44, start=2.0, end=2.125),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=2.125, end=2.25), # G
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.5),   # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=2.5, end=2.75),   # F
    pretty_midi.Note(velocity=80, pitch=43, start=2.75, end=3.0),   # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=2.0),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=2.0),
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=2.0),

    pretty_midi.Note(velocity=90, pitch=64, start=2.5, end=3.0),   # F7
    pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=60, start=2.5, end=3.0),
    pretty_midi.Note(velocity=90, pitch=62, start=2.5, end=3.0)
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: Motif variation
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=69, start=3.0, end=3.125),  # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=3.125, end=3.25), # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=3.25, end=3.375), # Db
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),  # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.75),   # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=4.0, end=4.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=4.25, end=4.5),   # Ab
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=3.0, end=3.125),  # Db
    pretty_midi.Note(velocity=80, pitch=42, start=3.125, end=3.25), # D
    pretty_midi.Note(velocity=80, pitch=43, start=3.25, end=3.375), # Eb
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=3.5, end=3.75),   # G
    pretty_midi.Note(velocity=80, pitch=46, start=3.75, end=4.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=4.0, end=4.25),   # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.25, end=4.5),   # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.5),   # F7
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.5),
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.5),

    pretty_midi.Note(velocity=90, pitch=64, start=4.0, end=4.5),   # F7
    pretty_midi.Note(velocity=90, pitch=69, start=4.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=60, start=4.0, end=4.5),
    pretty_midi.Note(velocity=90, pitch=62, start=4.0, end=4.5)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=3.375, end=3.75), # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=3.75, end=4.125), # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=4.125, end=4.5),  # Hihat on 4
    pretty_midi.Note(velocity=80, pitch=42, start=3.0, end=4.5)     # Hihat on every 8th
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: Motif variation with a question at the end
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=100, pitch=69, start=4.625, end=4.75), # Ab
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875), # Bb
    pretty_midi.Note(velocity=100, pitch=70, start=4.875, end=5.0),  # Db
    pretty_midi.Note(velocity=100, pitch=67, start=5.0, end=5.25),   # Bb
    pretty_midi.Note(velocity=100, pitch=69, start=5.25, end=5.5),   # Ab
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=100, pitch=67, start=5.75, end=6.0)    # Bb (ends on a question)
]
sax.notes.extend(sax_notes)

# Bass: Walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=44, start=4.5, end=4.625),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=4.625, end=4.75), # Eb
    pretty_midi.Note(velocity=80, pitch=42, start=4.75, end=4.875), # D
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.0),  # Db
    pretty_midi.Note(velocity=80, pitch=44, start=5.0, end=5.125),  # F
    pretty_midi.Note(velocity=80, pitch=45, start=5.125, end=5.25), # G
    pretty_midi.Note(velocity=80, pitch=46, start=5.25, end=5.5),   # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=5.5, end=5.75),   # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.75, end=6.0),   # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=5.0),   # F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=5.0),
    pretty_midi.Note(velocity=90, pitch=62, start=4.5, end=5.0),

    pretty_midi.Note(velocity=90, pitch=64, start=5.5, end=6.0),   # F7
    pretty_midi.Note(velocity=90, pitch=69, start=5.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=60, start=5.5, end=6.0),
    pretty_midi.Note(velocity=90, pitch=62, start=5.5, end=6.0)
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    pretty_midi.Note(velocity=90, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=80, pitch=42, start=4.875, end=5.25), # Hihat on 2
    pretty_midi.Note(velocity=90, pitch=38, start=5.25, end=5.625), # Snare on 3
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),  # Hihat on 4
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=6.0)     # Hihat on every 8th
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("jazz_intro.mid")
