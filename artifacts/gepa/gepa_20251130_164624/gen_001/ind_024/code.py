
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

# Bar 2: Full band (1.5 - 3.0s)
# Sax melody
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.875),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=2.25, end=2.625),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=2.625, end=3.0),  # Dm7
]
sax.notes.extend(sax_notes)

# Bass line: walking in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=1.5, end=1.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=1.875, end=2.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=2.25, end=2.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=2.625, end=3.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=44, start=1.875, end=2.25),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=1.875, end=2.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=1.875, end=2.25),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=1.875, end=2.25),  # D
    # Bar 3: Fm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=44, start=2.625, end=3.0),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=2.625, end=3.0),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=2.625, end=3.0),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=2.625, end=3.0),  # D
]
piano.notes.extend(piano_notes)

# Bar 3: Full band (3.0 - 4.5s)
# Sax continues the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.375),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=3.75, end=4.125),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=4.125, end=4.5),  # Dm7
]
sax.notes.extend(sax_notes)

# Bass line: walking in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=3.0, end=3.375),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=3.375, end=3.75),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=3.75, end=4.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=4.125, end=4.5),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 3: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=44, start=3.375, end=3.75),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=3.375, end=3.75),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=3.375, end=3.75),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=3.375, end=3.75),  # D
    # Bar 4: Fm7 on beat 4
    pretty_midi.Note(velocity=100, pitch=44, start=4.125, end=4.5),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.125, end=4.5),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=4.125, end=4.5),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.125, end=4.5),  # D
]
piano.notes.extend(piano_notes)

# Bar 4: Full band (4.5 - 6.0s)
# Sax continues the motif
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.875),  # Dm7
    pretty_midi.Note(velocity=100, pitch=64, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=65, start=5.25, end=5.625),  # Gb
    pretty_midi.Note(velocity=100, pitch=62, start=5.625, end=6.0),  # Dm7
]
sax.notes.extend(sax_notes)

# Bass line: walking in Fm
bass_notes = [
    pretty_midi.Note(velocity=100, pitch=44, start=4.5, end=4.875),  # F
    pretty_midi.Note(velocity=100, pitch=45, start=4.875, end=5.25),  # Gb
    pretty_midi.Note(velocity=100, pitch=42, start=5.25, end=5.625),  # Eb
    pretty_midi.Note(velocity=100, pitch=41, start=5.625, end=6.0),  # D
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 4: Fm7 on beat 2
    pretty_midi.Note(velocity=100, pitch=44, start=4.875, end=5.25),  # F
    pretty_midi.Note(velocity=100, pitch=47, start=4.875, end=5.25),  # Ab
    pretty_midi.Note(velocity=100, pitch=50, start=4.875, end=5.25),  # C
    pretty_midi.Note(velocity=100, pitch=53, start=4.875, end=5.25),  # D
]
piano.notes.extend(piano_notes)

# Drums: Bar 3 and 4
drum_notes = [
    # Bar 3: Kick on 1 and 3
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
    pretty_midi.Note(velocity=100, pitch=42, start=5.625, end=6.0),
]
drums.notes.extend(drum_notes)

midi.instruments.extend([sax, bass, piano, drums])

midi.write("dante_intro.mid")
