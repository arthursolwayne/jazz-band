
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
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.25),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line: walking, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=46, start=2.25, end=2.625),  # G
    pretty_midi.Note(velocity=80, pitch=47, start=2.625, end=3.0),   # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 2: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=1.5, end=1.875),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.5, end=1.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.5, end=1.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=1.875, end=2.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=1.875, end=2.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: Melody - One short motif, make it sing. Start it, leave it hanging. Come back and finish it.
# F (72), Ab (74), Bb (76), F (72) - a simple, haunting motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=74, start=1.875, end=2.25),
    pretty_midi.Note(velocity=110, pitch=76, start=2.25, end=2.625),
    pretty_midi.Note(velocity=110, pitch=72, start=2.625, end=3.0),
]
sax.notes.extend(sax_notes)

# Bar 3 (3.0 - 4.5s)
# Drums: same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=47, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=3.75, end=4.125),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=4.125, end=4.5),   # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=4.5, end=4.875),  # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),   # Eb
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 3: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=3.0, end=3.375),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.0, end=3.375),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=3.375, end=3.75),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=3.375, end=3.75),  # D
]
piano.notes.extend(piano_notes)

# Sax: Repeat and resolve the motif
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=74, start=3.375, end=3.75),
    pretty_midi.Note(velocity=110, pitch=76, start=3.75, end=4.125),
    pretty_midi.Note(velocity=110, pitch=72, start=4.125, end=4.5),
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),
]
sax.notes.extend(sax_notes)

# Bar 4 (4.5 - 6.0s)
# Drums: same pattern
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=38, start=6.375, end=6.75),  # Out of range
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
    pretty_midi.Note(velocity=90, pitch=42, start=6.0, end=6.375),  # Out of range
    pretty_midi.Note(velocity=90, pitch=42, start=6.375, end=6.75),  # Out of range
    pretty_midi.Note(velocity=90, pitch=42, start=6.75, end=7.125),  # Out of range
    pretty_midi.Note(velocity=90, pitch=42, start=7.125, end=7.5),   # Out of range
]
drums.notes.extend(drum_notes)

# Bass: walking line
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=5.625, end=6.0),   # Ab
    pretty_midi.Note(velocity=80, pitch=48, start=6.0, end=6.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=45, start=6.375, end=6.75),  # F
    pretty_midi.Note(velocity=80, pitch=44, start=6.75, end=7.125),  # Eb
    pretty_midi.Note(velocity=80, pitch=47, start=7.125, end=7.5),   # Ab
]
bass.notes.extend(bass_notes)

# Piano: 7th chords, comp on 2 and 4
piano_notes = [
    # Bar 4: F7 (F, A, C, Eb)
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=90, pitch=76, start=4.5, end=4.875),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=4.5, end=4.875),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.5, end=4.875),  # C
    pretty_midi.Note(velocity=90, pitch=76, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=77, start=4.875, end=5.25),  # Bb
    pretty_midi.Note(velocity=90, pitch=74, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=72, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Sax: Resolve motif with a pause and a final note
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=74, start=4.875, end=5.25),
    pretty_midi.Note(velocity=110, pitch=76, start=5.25, end=5.625),
    pretty_midi.Note(velocity=110, pitch=72, start=5.625, end=6.0),
    pretty_midi.Note(velocity=110, pitch=72, start=6.0, end=6.375),
    pretty_midi.Note(velocity=110, pitch=74, start=6.375, end=6.75),
    pretty_midi.Note(velocity=110, pitch=76, start=6.75, end=7.125),
    pretty_midi.Note(velocity=110, pitch=72, start=7.125, end=7.5),
]
sax.notes.extend(sax_notes)

midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
