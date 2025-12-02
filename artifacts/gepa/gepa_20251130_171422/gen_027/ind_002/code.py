
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=1.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax: short motif, start and leave hanging
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D (root)
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=1.875),  # F (3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=2.0, end=2.125),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # D again
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=1.5, end=1.625),   # D
    pretty_midi.Note(velocity=90, pitch=49, start=1.625, end=1.75),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=1.75, end=1.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=1.875, end=2.0),   # E
    pretty_midi.Note(velocity=90, pitch=53, start=2.0, end=2.125),   # F
    pretty_midi.Note(velocity=90, pitch=51, start=2.125, end=2.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=2.25, end=2.375),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=2.375, end=2.5),   # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=1.5, end=1.625),  # D7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=82, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=86, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=87, start=1.5, end=1.625),
    pretty_midi.Note(velocity=100, pitch=79, start=2.25, end=2.375),  # D7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=82, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=86, start=2.25, end=2.375),
    pretty_midi.Note(velocity=100, pitch=87, start=2.25, end=2.375),
]
piano.notes.extend(piano_notes)

# Drums continue in bar 2
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=2.25, end=2.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=3.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax: resolve the motif, return to the start
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.125),  # D (root)
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.375),  # F (3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=3.5, end=3.625),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),  # D again
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=3.0, end=3.125),   # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.125, end=3.25),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=3.25, end=3.375),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=3.375, end=3.5),   # E
    pretty_midi.Note(velocity=90, pitch=53, start=3.5, end=3.625),   # F
    pretty_midi.Note(velocity=90, pitch=51, start=3.625, end=3.75),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=3.75, end=3.875),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=3.875, end=4.0),   # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=3.0, end=3.125),  # D7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=82, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=86, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=87, start=3.0, end=3.125),
    pretty_midi.Note(velocity=100, pitch=79, start=3.75, end=3.875),  # D7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=82, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=86, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=87, start=3.75, end=3.875),
]
piano.notes.extend(piano_notes)

# Drums continue in bar 3
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=4.5),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
]
drums.notes.extend(drum_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax: variation of the motif, with rest
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=65, start=4.5, end=4.625),  # F (3rd)
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=4.875),  # G (5th)
    pretty_midi.Note(velocity=100, pitch=62, start=5.0, end=5.125),  # D again
]
sax.notes.extend(sax_notes)

# Bass: walking line, chromatic approach
bass_notes = [
    pretty_midi.Note(velocity=90, pitch=50, start=4.5, end=4.625),   # D
    pretty_midi.Note(velocity=90, pitch=49, start=4.625, end=4.75),  # C#
    pretty_midi.Note(velocity=90, pitch=51, start=4.75, end=4.875),  # Eb
    pretty_midi.Note(velocity=90, pitch=52, start=4.875, end=5.0),   # E
    pretty_midi.Note(velocity=90, pitch=53, start=5.0, end=5.125),   # F
    pretty_midi.Note(velocity=90, pitch=51, start=5.125, end=5.25),  # Eb
    pretty_midi.Note(velocity=90, pitch=50, start=5.25, end=5.375),  # D
    pretty_midi.Note(velocity=90, pitch=49, start=5.375, end=5.5),   # C#
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=79, start=4.5, end=4.625),  # D7 (D, F, A, C)
    pretty_midi.Note(velocity=100, pitch=82, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=86, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=87, start=4.5, end=4.625),
    pretty_midi.Note(velocity=100, pitch=79, start=5.25, end=5.375),  # D7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=82, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=86, start=5.25, end=5.375),
    pretty_midi.Note(velocity=100, pitch=87, start=5.25, end=5.375),
]
piano.notes.extend(piano_notes)

# Drums continue in bar 4
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 2
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=6.0),     # Hihat on every 8th
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
