
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
    pretty_midi.Note(velocity=90, pitch=42, start=0.0, end=0.375),
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),
    pretty_midi.Note(velocity=90, pitch=42, start=0.75, end=1.125),
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet enters (1.5 - 3.0s)
# Sax begins with a short motif (Dm7 -> F -> Ab -> Bb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75),  # D (Dm7)
    pretty_midi.Note(velocity=100, pitch=65, start=1.75, end=2.0),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=2.0, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5),  # Bb
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.0, end=2.25),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=2.25, end=2.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2 (1.75 - 2.0)
    pretty_midi.Note(velocity=90, pitch=62, start=1.75, end=2.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=1.75, end=2.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=1.75, end=2.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=1.75, end=2.0),  # F
    # Dm7 on beat 4 (2.25 - 2.5)
    pretty_midi.Note(velocity=90, pitch=62, start=2.25, end=2.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=2.25, end=2.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),  # F
]
piano.notes.extend(piano_notes)

# Bar 3: Sax continues with a variation (Ab -> F -> Bb -> C)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=3.0, end=3.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=3.25, end=3.5),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=3.5, end=3.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=64, start=3.75, end=4.0),  # C
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.5),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=3.75, end=4.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2 (3.25 - 3.5)
    pretty_midi.Note(velocity=90, pitch=62, start=3.25, end=3.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.25, end=3.5),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.25, end=3.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.25, end=3.5),  # F
    # Dm7 on beat 4 (3.75 - 4.0)
    pretty_midi.Note(velocity=90, pitch=62, start=3.75, end=4.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=3.75, end=4.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),  # F
]
piano.notes.extend(piano_notes)

# Bar 4: Sax returns to the opening motif, but with a new twist (Bb -> Ab -> F -> D)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75),  # Bb
    pretty_midi.Note(velocity=100, pitch=60, start=4.75, end=5.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=65, start=5.0, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5),  # D
]
sax.notes.extend(sax_notes)

# Bass: walking line with chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=48, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=5.0, end=5.25),  # E
    pretty_midi.Note(velocity=80, pitch=48, start=5.25, end=5.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Dm7 on beat 2 (4.75 - 5.0)
    pretty_midi.Note(velocity=90, pitch=62, start=4.75, end=5.0),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=4.75, end=5.0),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=4.75, end=5.0),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=4.75, end=5.0),  # F
    # Dm7 on beat 4 (5.25 - 5.5)
    pretty_midi.Note(velocity=90, pitch=62, start=5.25, end=5.5),  # D
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),  # G
    pretty_midi.Note(velocity=90, pitch=65, start=5.25, end=5.5),  # Bb
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),  # F
]
piano.notes.extend(piano_notes)

# Drums continue for the full 6 seconds
drum_notes = [
    # Kick on 1 and 3 of bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=3.0),
    # Snare on 2 and 4 of bar 2 (1.5 - 3.0)
    pretty_midi.Note(velocity=110, pitch=38, start=2.25, end=2.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.125),
    # Hihat on every eighth
    pretty_midi.Note(velocity=90, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=90, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=90, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=90, pitch=42, start=2.625, end=3.0),
    pretty_midi.Note(velocity=90, pitch=42, start=3.0, end=3.375),
    pretty_midi.Note(velocity=90, pitch=42, start=3.375, end=3.75),
    pretty_midi.Note(velocity=90, pitch=42, start=3.75, end=4.125),
    pretty_midi.Note(velocity=90, pitch=42, start=4.125, end=4.5),
    pretty_midi.Note(velocity=90, pitch=42, start=4.5, end=4.875),
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),
    pretty_midi.Note(velocity=90, pitch=42, start=5.25, end=5.625),
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
