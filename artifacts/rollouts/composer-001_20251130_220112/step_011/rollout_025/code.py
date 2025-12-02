
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
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)

# Bass line - walking line in Fm
bass_notes = [
    # Fm7: F, Ab, Bb, D
    # Walking line: F -> Gb -> Ab -> A
    pretty_midi.Note(velocity=80, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=80, pitch=68, start=2.25, end=2.625),  # Ab
    pretty_midi.Note(velocity=80, pitch=70, start=2.625, end=3.0),  # A
]
bass.notes.extend(bass_notes)

# Piano - comp on 2 and 4 with 7th chords
piano_notes = [
    # Fm7: F, Ab, Bb, D
    pretty_midi.Note(velocity=100, pitch=71, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=68, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=64, start=1.5, end=1.875),
    # Fm7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=68, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=70, start=2.625, end=3.0),
    pretty_midi.Note(velocity=100, pitch=64, start=2.625, end=3.0),
]
piano.notes.extend(piano_notes)

# Saxophone - motif
# Fm scale: F, Gb, Ab, A, Bb, B, Db
# Motif: F -> Ab -> Bb -> F (hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=2.25, end=2.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=2.625, end=3.0),  # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Bass line - walking line in Fm
bass_notes = [
    # Fm7: F, Ab, Bb, D
    # Walking line: B -> C -> D -> Eb
    pretty_midi.Note(velocity=80, pitch=70, start=3.0, end=3.375),  # Bb
    pretty_midi.Note(velocity=80, pitch=69, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=80, pitch=72, start=4.125, end=4.5),  # Db
]
bass.notes.extend(bass_notes)

# Piano - comp on 2 and 4 with 7th chords
piano_notes = [
    # Fm7: F, Ab, Bb, D
    pretty_midi.Note(velocity=100, pitch=71, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=68, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.375),
    pretty_midi.Note(velocity=100, pitch=64, start=3.0, end=3.375),
    # Fm7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=68, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=70, start=4.125, end=4.5),
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),
]
piano.notes.extend(piano_notes)

# Saxophone - motif
# Fm scale: F, Gb, Ab, A, Bb, B, Db
# Motif: F -> Ab -> Bb -> F (hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=3.75, end=4.125),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=4.125, end=4.5),  # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Bass line - walking line in Fm
bass_notes = [
    # Fm7: F, Ab, Bb, D
    # Walking line: Eb -> F -> Gb -> Ab
    pretty_midi.Note(velocity=80, pitch=72, start=4.5, end=4.875),  # Db
    pretty_midi.Note(velocity=80, pitch=71, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.625),  # Gb
    pretty_midi.Note(velocity=80, pitch=68, start=5.625, end=6.0),  # Ab
]
bass.notes.extend(bass_notes)

# Piano - comp on 2 and 4 with 7th chords
piano_notes = [
    # Fm7: F, Ab, Bb, D
    pretty_midi.Note(velocity=100, pitch=71, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=68, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.875),
    pretty_midi.Note(velocity=100, pitch=64, start=4.5, end=4.875),
    # Fm7 again on beat 4
    pretty_midi.Note(velocity=100, pitch=71, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=68, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=70, start=5.625, end=6.0),
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),
]
piano.notes.extend(piano_notes)

# Saxophone - motif
# Fm scale: F, Gb, Ab, A, Bb, B, Db
# Motif: F -> Ab -> Bb -> F (hanging)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=71, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=110, pitch=68, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=110, pitch=70, start=5.25, end=5.625),  # Bb
    pretty_midi.Note(velocity=110, pitch=71, start=5.625, end=6.0),  # F
]
sax.notes.extend(sax_notes)

# Drums for bar 3-4
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
    pretty_midi.Note(velocity=80, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=80, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
