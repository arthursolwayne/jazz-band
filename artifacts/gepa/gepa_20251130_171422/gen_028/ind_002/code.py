
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Only drums here. No piano, bass, or sax until bar 2.
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.375),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=0.375, end=0.75),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=0.75, end=1.125), # Snare on 3
    pretty_midi.Note(velocity=90, pitch=42, start=1.125, end=1.5),   # Hihat on 4
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=1.5, end=1.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=1.75, end=2.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=2.0, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=2.25, end=2.5),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=2.5, end=2.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=2.75, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=1.5, end=1.75),  # Bb7 (Dm7)
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.75),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.75),   # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=1.5, end=1.75),   # D
    pretty_midi.Note(velocity=100, pitch=70, start=2.25, end=2.5),  # Bb7
    pretty_midi.Note(velocity=90, pitch=67, start=2.25, end=2.5),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=2.25, end=2.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=2.25, end=2.5),   # D
]
piano.notes.extend(piano_notes)

# Sax: Melody (sparse, expressive)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.75),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=2.0, end=2.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=2.5, end=2.75),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=3.0, end=3.25),  # D
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=3.0, end=3.25),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=3.25, end=3.5),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=3.5, end=3.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=3.75, end=4.0),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=4.0, end=4.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=4.25, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=3.0, end=3.25),  # Bb7 (Dm7)
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.25),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.25),   # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=3.0, end=3.25),   # D
    pretty_midi.Note(velocity=100, pitch=70, start=3.75, end=4.0),  # Bb7
    pretty_midi.Note(velocity=90, pitch=67, start=3.75, end=4.0),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=3.75, end=4.0),   # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=3.75, end=4.0),   # D
]
piano.notes.extend(piano_notes)

# Sax: Melody (sparse, expressive)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=65, start=3.0, end=3.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=3.5, end=3.75),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=4.0, end=4.25),  # D
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # E
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line, chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=50, start=4.5, end=4.75),  # D
    pretty_midi.Note(velocity=80, pitch=49, start=4.75, end=5.0),  # C
    pretty_midi.Note(velocity=80, pitch=51, start=5.0, end=5.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=52, start=5.25, end=5.5),  # F
    pretty_midi.Note(velocity=80, pitch=51, start=5.5, end=5.75),  # Eb
    pretty_midi.Note(velocity=80, pitch=50, start=5.75, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp
piano_notes = [
    pretty_midi.Note(velocity=100, pitch=70, start=4.5, end=4.75),  # Bb7 (Dm7)
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.75),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=4.5, end=4.75),   # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=4.5, end=4.75),   # D
    pretty_midi.Note(velocity=100, pitch=70, start=5.25, end=5.5),  # Bb7
    pretty_midi.Note(velocity=90, pitch=67, start=5.25, end=5.5),   # F
    pretty_midi.Note(velocity=90, pitch=64, start=5.25, end=5.5),   # Ab
    pretty_midi.Note(velocity=90, pitch=60, start=5.25, end=5.5),   # D
]
piano.notes.extend(piano_notes)

# Sax: Melody (sparse, expressive)
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.75),  # E
    pretty_midi.Note(velocity=110, pitch=65, start=5.0, end=5.25),  # G
    pretty_midi.Note(velocity=110, pitch=62, start=5.5, end=5.75),  # E
    pretty_midi.Note(velocity=110, pitch=60, start=6.0, end=6.25),  # D
]
sax.notes.extend(sax_notes)

# Drums: kick=36, snare=38, hihat=42
drum_notes = [
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),  # Kick on 1
    pretty_midi.Note(velocity=90, pitch=42, start=4.875, end=5.25),  # Hihat on 2
    pretty_midi.Note(velocity=100, pitch=38, start=5.25, end=5.625), # Snare on 3
    pretty_midi.Note(velocity=90, pitch=42, start=5.625, end=6.0),   # Hihat on 4
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
