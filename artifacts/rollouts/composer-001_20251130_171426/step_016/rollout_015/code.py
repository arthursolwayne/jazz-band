
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
    pretty_midi.Note(velocity=100, pitch=42, start=2.625, end=3.0),
]
drums.notes.extend(drum_notes)

# Bar 2: Full quartet (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # E
    pretty_midi.Note(velocity=100, pitch=60, start=2.25, end=2.625),  # C
    pretty_midi.Note(velocity=100, pitch=65, start=2.625, end=3.0),   # F#
]
sax.notes.extend(sax_notes)

# Bass line (walking)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=1.875),  # D
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),  # Eb
    pretty_midi.Note(velocity=100, pitch=45, start=2.25, end=2.625),  # E
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),   # G
]
bass.notes.extend(bass_notes)

# Piano (comping on 2 and 4)
piano_notes = [
    # Bar 2, beat 2 (7th chord on E7)
    pretty_midi.Note(velocity=100, pitch=49, start=1.875, end=2.25),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=1.875, end=2.25),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # C
    # Bar 2, beat 4 (7th chord on G7)
    pretty_midi.Note(velocity=100, pitch=55, start=2.625, end=3.0),   # B
    pretty_midi.Note(velocity=100, pitch=57, start=2.625, end=3.0),   # D
    pretty_midi.Note(velocity=100, pitch=56, start=2.625, end=3.0),   # C
    pretty_midi.Note(velocity=100, pitch=59, start=2.625, end=3.0),   # F
]
piano.notes.extend(piano_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=3.375, end=3.75),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=3.75, end=4.125),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=4.125, end=4.5),   # E
]
sax.notes.extend(sax_notes)

# Bass line (walking)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=49, start=3.0, end=3.375),  # G
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=52, start=3.75, end=4.125),  # B
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),   # C
]
bass.notes.extend(bass_notes)

# Piano (comping on 2 and 4)
piano_notes = [
    # Bar 3, beat 2 (7th chord on E7)
    pretty_midi.Note(velocity=100, pitch=49, start=3.375, end=3.75),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=3.375, end=3.75),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # C
    # Bar 3, beat 4 (7th chord on G7)
    pretty_midi.Note(velocity=100, pitch=55, start=4.125, end=4.5),   # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.125, end=4.5),   # D
    pretty_midi.Note(velocity=100, pitch=56, start=4.125, end=4.5),   # C
    pretty_midi.Note(velocity=100, pitch=59, start=4.125, end=4.5),   # F
]
piano.notes.extend(piano_notes)

# Bar 4: Full quartet (4.5 - 6.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # D
    pretty_midi.Note(velocity=100, pitch=65, start=4.875, end=5.25),  # F#
    pretty_midi.Note(velocity=100, pitch=60, start=5.25, end=5.625),  # C
    pretty_midi.Note(velocity=100, pitch=64, start=5.625, end=6.0),   # E
]
sax.notes.extend(sax_notes)

# Bass line (walking)
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=55, start=4.5, end=4.875),  # B
    pretty_midi.Note(velocity=100, pitch=57, start=4.875, end=5.25),  # D
    pretty_midi.Note(velocity=100, pitch=59, start=5.25, end=5.625),  # F
    pretty_midi.Note(velocity=100, pitch=60, start=5.625, end=6.0),   # G
]
bass.notes.extend(bass_notes)

# Piano (comping on 2 and 4)
piano_notes = [
    # Bar 4, beat 2 (7th chord on E7)
    pretty_midi.Note(velocity=100, pitch=49, start=4.875, end=5.25),  # G
    pretty_midi.Note(velocity=100, pitch=52, start=4.875, end=5.25),  # B
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # A
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # C
    # Bar 4, beat 4 (7th chord on G7)
    pretty_midi.Note(velocity=100, pitch=55, start=5.625, end=6.0),   # B
    pretty_midi.Note(velocity=100, pitch=57, start=5.625, end=6.0),   # D
    pretty_midi.Note(velocity=100, pitch=56, start=5.625, end=6.0),   # C
    pretty_midi.Note(velocity=100, pitch=59, start=5.625, end=6.0),   # F
]
piano.notes.extend(piano_notes)

# Drums: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 2
    pretty_midi.Note(velocity=100, pitch=36, start=1.5, end=1.875),   # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=1.875, end=2.0),   # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=1.5, end=2.25),    # Hihat
    # Bar 3
    pretty_midi.Note(velocity=100, pitch=36, start=3.0, end=3.375),   # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=3.375, end=3.5),   # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=3.0, end=3.75),    # Hihat
    # Bar 4
    pretty_midi.Note(velocity=100, pitch=36, start=4.5, end=4.875),   # Kick
    pretty_midi.Note(velocity=100, pitch=38, start=4.875, end=5.0),   # Snare
    pretty_midi.Note(velocity=100, pitch=42, start=4.5, end=5.25),    # Hihat
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_russo_intro.mid")
