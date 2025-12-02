
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums only
drum_notes = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=36, start=1.125, end=1.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=0.875),
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=100, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=100, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=100, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0)
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: walking line with chromatic approach
bass_notes = [
    # Dm7 chord: D, F, A, C
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.625, end=1.75),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=1.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.875, end=2.0),  # C
    pretty_midi.Note(velocity=100, pitch=61, start=2.0, end=2.125),  # Eb (chromatic)
    pretty_midi.Note(velocity=100, pitch=62, start=2.125, end=2.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=2.25, end=2.375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),  # C
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on 2
    pretty_midi.Note(velocity=100, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=1.75, end=2.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=1.75, end=2.0),  # C
    # Dm7 on 4
    pretty_midi.Note(velocity=100, pitch=62, start=2.375, end=2.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=2.375, end=2.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=2.375, end=2.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=2.375, end=2.5),  # C
]
piano.notes.extend(piano_notes)

# Sax: Whispering motif
sax_notes = [
    # First note: D (62), quarter note, slow
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),
    # Second note: F (60), eighth note, slightly higher
    pretty_midi.Note(velocity=100, pitch=60, start=1.875, end=2.0),
    # Third note: A (64), eighth note, with tension
    pretty_midi.Note(velocity=100, pitch=64, start=2.0, end=2.125),
    # Fourth note: C (67), quarter note, resolution
    pretty_midi.Note(velocity=100, pitch=67, start=2.125, end=2.5)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: walking line with chromatic approach
bass_notes_2 = [
    pretty_midi.Note(velocity=100, pitch=67, start=3.0, end=3.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=3.125, end=3.25),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.375, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=3.5, end=3.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=3.625, end=3.75),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=3.875),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),  # C
]
bass.notes.extend(bass_notes_2)

# Piano: 7th chords on 2 and 4
piano_notes_2 = [
    # Dm7 on 2
    pretty_midi.Note(velocity=100, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.25, end=3.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.25, end=3.5),  # C
    # Dm7 on 4
    pretty_midi.Note(velocity=100, pitch=62, start=3.875, end=4.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=3.875, end=4.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=3.875, end=4.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=3.875, end=4.0),  # C
]
piano.notes.extend(piano_notes_2)

# Sax: Second motif, build and cry
sax_notes_2 = [
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=67, start=3.375, end=3.5),
    pretty_midi.Note(velocity=100, pitch=69, start=3.5, end=3.625),
    pretty_midi.Note(velocity=100, pitch=67, start=3.625, end=4.0)
]
sax.notes.extend(sax_notes_2)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: walking line with chromatic approach
bass_notes_3 = [
    pretty_midi.Note(velocity=100, pitch=67, start=4.5, end=4.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.625, end=4.75),  # A
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.875, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=61, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=62, start=5.125, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=5.25, end=5.375),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5),  # C
]
bass.notes.extend(bass_notes_3)

# Piano: 7th chords on 2 and 4
piano_notes_3 = [
    # Dm7 on 2
    pretty_midi.Note(velocity=100, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=4.75, end=5.0),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=4.75, end=5.0),  # C
    # Dm7 on 4
    pretty_midi.Note(velocity=100, pitch=62, start=5.375, end=5.5),  # D
    pretty_midi.Note(velocity=100, pitch=60, start=5.375, end=5.5),  # F
    pretty_midi.Note(velocity=100, pitch=64, start=5.375, end=5.5),  # A
    pretty_midi.Note(velocity=100, pitch=67, start=5.375, end=5.5),  # C
]
piano.notes.extend(piano_notes_3)

# Sax: Final phrase, emotional release
sax_notes_3 = [
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=69, start=4.875, end=5.125),
    pretty_midi.Note(velocity=100, pitch=67, start=5.125, end=5.5),
    pretty_midi.Note(velocity=100, pitch=64, start=5.5, end=6.0)
]
sax.notes.extend(sax_notes_3)

# Drums: continue the pattern
drum_notes_2 = [
    # Kick on 1 and 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.5),
    # Snare on 2 and 4
    pretty_midi.Note(velocity=100, pitch=38, start=3.75, end=3.875),
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),
    # Hi-hat on every eighth
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=100, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0)
]
drums.notes.extend(drum_notes_2)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_4bar_intro.mid")
