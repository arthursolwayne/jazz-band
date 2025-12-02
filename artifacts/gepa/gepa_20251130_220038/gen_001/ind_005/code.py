
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

# Marcus on bass (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=41, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=80, pitch=40, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=80, pitch=39, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=80, pitch=43, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 2, beat 2 (Fm7)
    pretty_midi.Note(velocity=90, pitch=41, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=90, pitch=44, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=1.875, end=2.25),  # D
    # Bar 2, beat 4 (Fm7)
    pretty_midi.Note(velocity=90, pitch=41, start=2.625, end=3.0),   # F
    pretty_midi.Note(velocity=90, pitch=46, start=2.625, end=3.0),   # A
    pretty_midi.Note(velocity=90, pitch=44, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=90, pitch=48, start=2.625, end=3.0),   # D
]
piano.notes.extend(piano_notes)

# Dante on sax (melody, one short motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),   # F
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)

# Marcus on bass (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.375),  # Ab
    pretty_midi.Note(velocity=80, pitch=44, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=80, pitch=42, start=3.75, end=4.125),  # E
    pretty_midi.Note(velocity=80, pitch=41, start=4.125, end=4.5),   # F
]
bass.notes.extend(bass_notes)

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 3, beat 2 (Fm7)
    pretty_midi.Note(velocity=90, pitch=41, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=90, pitch=44, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=3.375, end=3.75),  # D
    # Bar 3, beat 4 (Fm7)
    pretty_midi.Note(velocity=90, pitch=41, start=4.125, end=4.5),   # F
    pretty_midi.Note(velocity=90, pitch=46, start=4.125, end=4.5),   # A
    pretty_midi.Note(velocity=90, pitch=44, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=90, pitch=48, start=4.125, end=4.5),   # D
]
piano.notes.extend(piano_notes)

# Dante on sax (melody, one short motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),   # F
]
sax.notes.extend(sax_notes)

# Bar 4: Full quartet (4.5 - 6.0s)

# Marcus on bass (walking line, chromatic approaches)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=42, start=4.5, end=4.875),  # E
    pretty_midi.Note(velocity=80, pitch=41, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=5.25, end=5.625),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=5.625, end=6.0),   # Ab
]
bass.notes.extend(bass_notes)

# Diane on piano (7th chords, comp on 2 and 4)
piano_notes = [
    # Bar 4, beat 2 (Fm7)
    pretty_midi.Note(velocity=90, pitch=41, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=90, pitch=46, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=90, pitch=44, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=90, pitch=48, start=4.875, end=5.25),  # D
    # Bar 4, beat 4 (Fm7)
    pretty_midi.Note(velocity=90, pitch=41, start=5.625, end=6.0),   # F
    pretty_midi.Note(velocity=90, pitch=46, start=5.625, end=6.0),   # A
    pretty_midi.Note(velocity=90, pitch=44, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=90, pitch=48, start=5.625, end=6.0),   # D
]
piano.notes.extend(piano_notes)

# Dante on sax (melody, one short motif)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # D
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),   # F
]
sax.notes.extend(sax_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),
    pretty_midi.Note(velocity=110, pitch=38, start=1.875, end=2.25),
    pretty_midi.Note(velocity=100, pitch=36, start=2.625, end=2.875),
    pretty_midi.Note(velocity=110, pitch=38, start=3.0, end=3.375),
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),
    pretty_midi.Note(velocity=110, pitch=38, start=3.375, end=3.75),
    pretty_midi.Note(velocity=100, pitch=36, start=4.125, end=4.375),
    pretty_midi.Note(velocity=110, pitch=38, start=4.5, end=4.875),
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),
    pretty_midi.Note(velocity=110, pitch=38, start=4.875, end=5.25),
    pretty_midi.Note(velocity=100, pitch=36, start=5.625, end=5.875),
    pretty_midi.Note(velocity=110, pitch=38, start=6.0, end=6.25),
    # Hi-hats
    pretty_midi.Note(velocity=80, pitch=42, start=1.5, end=1.875),
    pretty_midi.Note(velocity=80, pitch=42, start=1.875, end=2.25),
    pretty_midi.Note(velocity=80, pitch=42, start=2.25, end=2.625),
    pretty_midi.Note(velocity=80, pitch=42, start=2.625, end=3.0),
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

# Save the MIDI file
midi.write("4_bar_jazz_intro.mid")
